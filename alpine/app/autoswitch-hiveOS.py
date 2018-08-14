#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# based on walmins' version 0.4 contributions
# version 0.68 by dimos.kokkonos & antonis.kokkonos
# python3
# last modification: 2018-08-14
# source https://forum.hiveos.farm/discussion/192/hive-api
import requests
import json
import hmac
import hashlib
import urllib
import pycurl
import base64
import io
import datetime
import time
from VARS import *
import logging
import operator
from termcolor import colored
import termcolor

greaterProfit = GREATER_PROFIT
debug = DEBUG
sleepTime = SLEEP_TIME

def minerHiveOS(params):
	params["public_key"] = PUBLIC_KEY
	post_data = urllib.parse.urlencode(params)
	HMAC = hmac.new(SECRET_KEY.encode(), post_data.encode(), hashlib.sha256).hexdigest()
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, URL)
	curl.setopt(pycurl.HTTPHEADER, ['HMAC: ' + str(HMAC)])
	curl.setopt(pycurl.POST, True)
	curl.setopt(pycurl.POSTFIELDS, post_data)
	curl.setopt(pycurl.CONNECTTIMEOUT, 10)
	curl.setopt(pycurl.TIMEOUT, 5)
	buf = io.BytesIO()
	curl.setopt(pycurl.WRITEFUNCTION, buf.write)
	try:
		curl.perform()
		response = buf.getvalue()

		# Uncomment to debug raw JSON response
		# self.__log("< " + response)
		http_code = curl.getinfo(pycurl.HTTP_CODE)
		curl.close()
		result = json.loads(response)
		return result
	except pycurl.error:
		# ret = e.args[0]
		# print ("error-- ",ret)
		return False

# Monitor stats for all the rigs
def getCurrentStats():
	logging.info(colored("*** Get-Current-Stats ***", 'cyan'))
	currentStats = {}
	params = {
		'method': 'getCurrentStats'
	}
	currentStats['rigID'] = str(RIG_ID)
	stats = minerHiveOS(params)
	if stats:
		currentStats['algo'] = list(stats['result']['summary']['algo'].keys())[0]
		currentStats['miner'] = stats['result']['rigs'][currentStats['rigID']]['miner']
		currentStats['walletID'] = stats['result']['rigs'][currentStats['rigID']]['id_wal']
		currentStats['walletName'] =  stats['result']['rigs'][currentStats['rigID']]['wallet_name']
		return currentStats
	else:
		return False

# Sets parameters for rigs
def multiRocket(rig_ids_str, miner, id_wal):
	"""
	@param rig_ids_str coma separated string with rig ids "1,2,3,4"
	@param miner Miner to set. Leave it null if you do not want to change. "claymore", "claymore-z", "ewbf", ...
	@param miner2 Second miner to set. Leave it null if you do not want to change. "0" - if you want to unset it.
	@param id_wal ID of wallet. Leave it null if you do not want to change.
	@param id_oc ID of OC profile. Leave it null if you do not want to change.
	@return bool|mixed
	"""

	params = {
		'method': 'multiRocket',
		'rig_ids_str': rig_ids_str,
		'miner': miner,
		'id_wal': id_wal,
	}

	result = minerHiveOS(params)
	if 'error' in result:
		return False

	return result

def getProfitCoin():
	logging.info(colored("*** Get-Most-Profitable-Coin ***", 'cyan'))
	profitability = {}
	url_opener = urllib.request.build_opener()
	url_opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
	try:
	    response = url_opener.open(SRC['whattomine']['url'])
	    string = response.read().decode('utf-8')
	    json_obj = json.loads(string)
	except:
	    json_obj = {'coins': {}}
	    print ("error")
	flag=0
	for coin_set in json_obj['coins'].items():
		coin = coin_set[1]

		if coin['algorithm'] in profitability:
			if profitability.get(coin['tag']) < coin['profitability']:
				profitability[coin['tag']] = coin['profitability']
		else:
			profitability[coin['tag']] = coin['profitability']

		if coin['tag'] ==  "NICEHASH":
			if flag==0:
				NicehashProfit = coin['profitability']
				NicehashAlgo = coin['algorithm']
				flag=1
				str = NicehashAlgo +' '
				coin['tag'] = str
			profitability[coin['tag']] = NicehashProfit

		if coin['tag'] in wallets.keys():
			tag=0
		else:
			del profitability [coin['tag']]

	if debug == True:
		print (profitability)
	return profitability

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
	logging.info(colored("Start autoswitch-HiveOS", 'white', attrs=['bold']))
	while True:
		try:
			CurrentStats = getCurrentStats()
			logging.info(colored("======== My-Stats =======", 'white', attrs=['bold']))
			logging.info(colored("RIG-ID      : %s", 'white'), CurrentStats['rigID'])
			logging.info(colored("Wallet-ID   : %s", 'white'), CurrentStats['walletID'])
			logging.info(colored("Wallet-Name : %s", 'yellow'), CurrentStats['walletName'])
			logging.info(colored("Miner       : %s", 'white'), CurrentStats['miner'])
			logging.info(colored("Algo        : %s", 'white'), CurrentStats['algo'])
			ProfitCoin = getProfitCoin()
			for coins in wallets.items():
				if CurrentStats['walletID'] == coins[1]['id_wal']:
					CurrentStats['wtmAlgo'] = coins[0]
					if CurrentStats['wtmAlgo'] in ProfitCoin.keys():
						CurrentStats['profit'] = ProfitCoin[CurrentStats['wtmAlgo']]
					else:
						CurrentStats['profit'] = 0
			if 'wtmAlgo' in CurrentStats:
				if debug == True:
					print (CurrentStats)
				currentProfit = (ProfitCoin[list(ProfitCoin.keys())[0]])
				logging.info(colored("Whattomine.com-Profit : %s%% (%s)", 'white'), currentProfit, list(ProfitCoin.keys())[0])
				logging.info(colored("Current-Coin-Profit   : %s%% \n", 'white'), CurrentStats['profit'])
				if currentProfit > (CurrentStats['profit'] + greaterProfit) and CurrentStats['wtmAlgo'] != list(ProfitCoin.keys())[0]:
					logging.info(colored("Set-to-RIG: %s -> Wallet-ID: %s, Wallet-Name: %s,  Miner: %s, Algo: %s \n", 'green'),  CurrentStats['rigID'],  wallets[list(ProfitCoin.keys())[0]]['id_wal'], wallets[list(ProfitCoin.keys())[0]]['wallet_name'], wallets[list(ProfitCoin.keys())[0]]['miner'], 
wallets[list(ProfitCoin.keys())[0]]['algo'])
					if wallets[list(ProfitCoin.keys())[0]]['id_wal']:
						multiRocket(CurrentStats['rigID'], wallets[list(ProfitCoin.keys())[0]]['miner'], wallets[list(ProfitCoin.keys())[0]]['id_wal'],)

		except KeyboardInterrupt:
			print ("Keyboard Interrupted! bye!")
		time.sleep(sleepTime)

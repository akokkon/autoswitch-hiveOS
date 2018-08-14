SECRET_KEY = 'INSERT_YOUR_SECRET_API_KEY'
PUBLIC_KEY = 'INSERT_YOUR_PUBLIC_API_KEY'
RIG_ID = 'INSERT_RIG_ID'
#
# Define the profit percentage for autoswitching
GREATER_PROFIT = 10
#
# Default value is 'False'. Insert 'True' to see the list of minable coins
DEBUG = False
#
# Time in seconds for the next autoswitching check
SLEEP_TIME = 240
#
# Check your best server
URL = "https://the.hiveos.farm/worker/eypiay.php"

"""
You need to pass it some parameters about your setup, and then parse it according to what you're looking for..
Select your cards and input power cost, click calculate, then copy the link and add ".json" after "coins" and you will get output based on what you fed into it.
https://www.reddit.com/r/gpumining/comments/7wwveu/how_to_read_whattomine_json/?st=jgt4s3wm&sh=7285ed6b
https://whattomine.com/
"""
SRC = {
    'whattomine': {
    			'url': "https://whattomine.com/coins.json?utf8=%E2%9C%93&&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=0&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=1.18&adapt_q_1070=7.93&adapt_q_1070Ti=0&adapt_q_1080=0&adapt_q_1080Ti=0&eth=true&factor[eth_hr]=247.0&factor[eth_p]=972.0&zh=true&factor[zh_hr]=320.0&factor[zh_p]=1060.0&factor[phi_hr]=45.0&factor[phi_p]=390.0&factor[cnh_hr]=2850.0&factor[cnh_p]=330.0&factor[cn7_hr]=2580.0&factor[cn7_p]=330.0&eq=true&factor[eq_hr]=3650.0&factor[eq_p]=1080.0&lre=true&factor[lrev2_hr]=285000.0&factor[lrev2_p]=1070.0&ns=true&factor[ns_hr]=7930.0&factor[ns_p]=1030.0&factor[tt10_hr]=27.0&factor[tt10_p]=450.0&x16r=true&factor[x16r_hr]=75.0&factor[x16r_p]=930.0&factor[l2z_hr]=1.35&factor[l2z_p]=360.0&factor[phi2_hr]=0.0&factor[phi2_p]=0.0&factor[xn_hr]=4.8&factor[xn_p]=360.0&factor[cost]=0.135&sort=Profit&volume=0&revenue=current&factor[exchanges][]=&factor[exchanges][]=binance&factor[exchanges][]=bitfinex&factor[exchanges][]=bittrex&factor[exchanges][]=cryptobridge&factor[exchanges][]=cryptopia&factor[exchanges][]=hitbtc&factor[exchanges][]=poloniex&factor[exchanges][]=yobit&dataset=Main&commit=Calculate",
                'sort_key': "profitability"
                }
        }

#id_wallet -> start script with the one which you want and see the logs of this script

"""
Because the 'coin-tag' NICEHASH is used for several different algos (e.g. ethash, equihash, neoscrypt ...) we use as 'coin-tag' 
and as 'algo' the name of algorithm followed by a space (e.g. 'ethash ', 'equihash ', 'neoscrypt ') 
"""
wallets = {
	'BCI': {
			'hive_name': 'BCI',
			'algo': 'equihash',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'BCI -bci.suprnova.cc'
			},
	'BTCP': {
			'hive_name': 'BTCP',
			'algo': 'equihash',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'BTCP - stratum://btcp.suprnova.cc'
			},
	'BTCZ': {
			'hive_name': 'BTCZ',
			'algo': 'zhash',
			'miner': 'ewbf',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'BTCZ - mine-btcz-euro.equipool.1ds.us'
			},
	'BTG': {
			'hive_name': 'BTG',
			'algo': 'zhash',
			'miner': 'ewbf',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'BTG - btg.suprnova.cc'
			},
	'CMM': {
			'hive_name': 'CMM',
			'algo': 'equihash',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'CMM - mine.vpool.io'
			},
	'CRC': {
			'hive_name': 'CRC',
			'algo': 'neoscrypt',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'CRC->BTC - stratum+tcp://neoscrypt.mine.zergpool.com'
			},
	'DIN': {
			'hive_name': 'DIN',
			'algo': 'neoscrypt',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'DIN - stratum+tcp://neoscrypt.mine.zergpool.com'
			},
	'ETH': {
			'hive_name': 'ETH',
			'algo': 'ethash',
			'miner': 'ethminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'ETH - eth-eu.dwarfpool.com'
			},
	'ETC': {
			'hive_name': 'ETC',
			'algo': 'ethash',
			'miner': 'ethminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'ETC - eu1-etc.ethermine.org'
			},
	'HUSH': {
			'hive_name': 'HUSH',
			'algo': 'equihash',
			'miner': 'dstm',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'HUSH - hush.suprnova.cc'
			},
	'KMD': {
			'hive_name': 'KMD',
			'algo': 'equihash',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'KMD - kmd.suprnova.cc:6250'
			},
	'MONA': {
			'hive_name': 'MONA',
			'algo': 'lyra2REv2',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'MONA - stratum+tcp://lyra2v2.mine.zergpool.com'
			},
	'Equihash ': {
			'hive_name': 'Nicehash-Equihash',
			'algo': 'Equihash ',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'Nicehash-Equihash'
			},
	'Ethash ': {
			'hive_name': 'Nicehash-Ethash',
			'algo': 'Ethash ',
			'miner': 'ethminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'Nicehash-Ethash'
			},
	'Lyra2REv2 ': {
			'hive_name': 'Nicehash-Lyra2rev2',
			'algo': 'Lyra2REv2 ',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'Nicehash-Lyra2rev2'
			},
	'Neoscrypt ': {
			'hive_name': 'Nicehash-Neoscrypt',
			'algo': 'Neoscrypt ',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'Nicehash-Neoscrypt'
			},
	'X16R ': {
			'hive_name': 'Nicehash-X16R',
			'algo': 'X16r ',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'Nicehash-X16R'
			},
	'RVN': {
			'hive_name': 'RVN',
			'algo': 'x16r',
			'miner': 'ccminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'RVN - stratum+tcp://us.ravenminer.com'
			},
	'ZCL': {
			'hive_name': 'ZCL',
			'algo': 'equihash',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'ZCL - zcl.suprnova.cc'
			},
	'ZEC': {
            'hive_name': 'ZEC',
            'algo': 'equihash',
            'miner': 'bminer',
            'id_wal': INSERT_WALLET_ID,
            'wallet_name': 'ZEC - zec-eu.suprnova.cc'
            },
	'ZEN': {
			'hive_name': 'ZEN',
			'algo': 'equihash',
			'miner': 'bminer',
			'id_wal': INSERT_WALLET_ID,
			'wallet_name': 'ZEN - zen.suprnova.cc'
			}
	}

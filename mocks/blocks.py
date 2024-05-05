from mocks import wallets

COIN = 1000000
MY_WALLET = wallets.get()["my_wallet"]
FRIEND_WALLET = wallets.get()["friend_wallet"]

BLOCKS = [
    # Genesis block
    {
        "hash": "00000244a5bae572247ca9f5b9149fc3980fa90a7a70cd35030a29d81ebc88ea",
        "version": 1,
        "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
        "timestamp": 1231006505000,
        "difficulty": 22,
        "nonce": 2620954,
        "blocksize": 441,
        "txs": [
            {
                "hash": "892d3a0a01ab1a1c3d67e1592e5bd11df687e26098dda08478e6a58e0f6b337a", 
                "vin": [
                    {"prevout": "COINBASE"}
                ],
                "vout": [
                    {
                        "value": 50 * COIN,
                        "script_pub_key": MY_WALLET["public_address"]
                    }
                ]
            },
        ]
    },
    # Block #2 - new Coinbase and give 20 BTC to friend
    {
        "hash": "000001a20dacb2ede72eb4b35dea74b83fd4bc0b23849b789fee19c7eac2f1b9",
        "version": 1,
        "previous_hash": "00000244a5bae572247ca9f5b9149fc3980fa90a7a70cd35030a29d81ebc88ea",
        "timestamp": 1520947111852,
        "difficulty": 22,
        "nonce": 210212,
        "blocksize": 225,
        "txs": [
            {
                "hash": "892d3a0a01ab1a1c3d67e1592e5bd11df687e26098dda08478e6a58e0f6b337a",
                "vin": [
                    {"prevout": "COINBASE"}
                ],
                "vout": [
                    {
                        "value": 50 * COIN,
                        "script_pub_key": MY_WALLET["public_address"]
                    }
                ]
            },
            {
                "hash": "522f5e10a101de1b8e2b2289b2f5801daf007221f01a7256a3c961c9d26412fc",
                "vin": [
                    {
                        "prevout": "892d3a0a01ab1a1c3d67e1592e5bd11df687e26098dda08478e6a58e0f6b337a",
                        "n": 0,
                        "script_sig": MY_WALLET["public_key"] + " 9e4a280fc9a65e4791470150991a61f7baa83ac86998151f842696b5a5363bcd144bcceb069fc45a43e73c2583ba816d136c896e4301b0d86c6acb59cdffaaad"
                    }
                ],
                "vout": [
                    {
                        "value": 6 * COIN,
                        "script_pub_key": FRIEND_WALLET["public_address"],
                    },
                    {
                        "value": 44 * COIN,
                        "script_pub_key": MY_WALLET["public_address"]
                    }
                ]
            },
        ]
    },
    # Block #3 - new Coinbase and get 5 BTC from friend
    {
        "hash": "00000369dd0974cb0a472a961247607c196e6353c3ea04746b9bde3272b7de6a",
        "previous_hash": "000001a20dacb2ede72eb4b35dea74b83fd4bc0b23849b789fee19c7eac2f1b9",
        "version": 1,
        "timestamp": 1520948119344,
        "difficulty": 22,
        "nonce": 6317304,
        "txs": [
            {
                "hash": "892d3a0a01ab1a1c3d67e1592e5bd11df687e26098dda08478e6a58e0f6b337a",
                "vin": [ 
                    {"prevout": "COINBASE"}
                ],
                "vout": [ 
                    {
                        "value": 50 * COIN,
                        "script_pub_key": MY_WALLET["public_address"]
                    }
                ]
            },
            {
                "hash": "",
                "vin": [
                    {
                        "prevout": "522f5e10a101de1b8e2b2289b2f5801daf007221f01a7256a3c961c9d26412fc",
                        "n": 1,
                        "script_sig": FRIEND_WALLET["public_key"] + " b82384b58e01c6fa43a055436c7031e03025ee20f821cede2b6d4062053a83879ca3b37d9f3f2ef1b53b954b287f399eaba460e52ca9437855d637f427709238"
                    },
                ],
                "vout": [
                    {
                        "value": 10 * COIN,
                        "script_pub_key": MY_WALLET["public_address"]
                    },
                    {
                        "value": 10 * COIN,
                        "script_pub_key": FRIEND_WALLET["public_address"]
                    }
                ]
            }
        ]
    }
]

def get():    
    return BLOCKS

# "txs": [
#     {
#         "hash": SHA256(vin, vout serialized + block has), 
#         # where is money coming from?
#         "vin": [
#             # input 1 - 5 BTC
#             # input 2 - 5 BTC
#         ],
#         # where is money going to?
#         "vout": [
#             # output 1 - 5 BTC to friend
#             # output 2 - 5 BTC to self
#             {
#                 value: 6 * 1000000,
#                 scriptPubKey: `address of recipient | public key hash`
#             }
#         ]
#     },
# ]

import ecdsa
import hashlib
import utils

COIN = 1000000

# sign a transaction input with private key
def unlock_transaction(txid, private_key_hex: str):
    try:
        private_key_bytes = bytes.fromhex(private_key_hex)

        # Hash transaction ID
        hash = utils.hash(txid)
        # Initialize signing keys
        keys = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
        # Sign txid hash with signing keys
        signature = keys.sign(hash)
        # Return in hexadecimal format
        return signature.hex()
    except Exception as e:
        print('unlock_transaction error', e)
        return None

# # verify that signature is owner of address and matches transaction
# def verify_unlock(txid, address, public_key, signature):
#     try:
#         # First, validate that address is derived from public key
#         is_address = utils.get_address(public_key) == address
#         if not is_address:
#             print('verify_unlock', utils.get_address(public_key).decode('utf-8'), address)
#             return False
        
#         # Hash transaction ID
#         hash = utils.hash(txid)
        
#         # Initialize verification keys
#         keys = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
        
#         # Verify if the signature matches the public key and transaction hash
#         is_valid = keys.verify(signature, hash)
#         return is_valid
#     except Exception as e:
#         print('verify_unlock error', e)
#         return False

# verify that signature is owner of address and matches transaction
def verify_unlock(txid, address, public_key, signature):
    try:
        # First, get the address form the given public key
        obtained_address = utils.get_address(public_key)

        # Validate that address is derived from public key
        if obtained_address != address:
            return False
        
        # Hash transaction ID
        hash = utils.hash(txid)

        # Initialize verification keys
        keys = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)

        # Verify if the signature matches the public key and transaction hash
        is_valid = keys.verify(bytes.fromhex(signature), hash)
        return is_valid
    except Exception as e:
        return False

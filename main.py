import utils
import verify_signature
from mocks import blocks
from mocks import wallets

import hashlib
import base58
from ripemd import ripemd160


if __name__ == "__main__":
    wallets = wallets.get()
    blocks = blocks.get()

    block = 1
    prevout = blocks[block]["txs"][1]["vin"][0]["prevout"]

    # print("> Signing trx...")

    # private_key_hex = wallets["friend_wallet"]["private_key_hex"]
    # public_key = wallets["friend_wallet"]["public_key"]

    # print("> txid (prevout) to be verify", prevout)
    # print("> public_key", public_key)
    # print("> signature", verify_signature.unlock_transaction(prevout, private_key_hex))
    
    print("> Verifying trx...")

    address = wallets["my_wallet"]["public_address"]
    script_sig = blocks[block]["txs"][1]["vin"][0]["script_sig"]
    public_key = script_sig.split()[0]
    signature = script_sig.split()[1]

    print("> txid (prevout) to be verify", prevout)
    print("> public_key", public_key)
    print("> signature", signature)
    print("> Valid?", verify_signature.verify_unlock(prevout, address, public_key, signature))

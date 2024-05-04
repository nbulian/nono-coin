# Function that creates full Bitcoin wallets

import secrets
import ecdsa
import hashlib
import base58
import utils
from ripemd import ripemd160

def create_private_key_wif(private_key):
    # Step 1: Concatenate '80' with the private key and convert it to bytes
    step1 = bytes.fromhex("80" + private_key)
    
    # Step 2: Calculate the SHA-256 hash
    step2 = hashlib.sha256(step1).digest()
    
    # Step 3: Calculate the SHA-256 hash of the resulting hash
    step3 = hashlib.sha256(step2).digest()
    
    # Get the first 4 bytes (8 hexadecimal characters) of the resulting hash
    checksum = step3[:4].hex()
    
    # Step 4: Concatenate step1 with the checksum
    step4 = step1.hex() + checksum
    
    # Encode in base58
    privateKeyWIF = base58.b58encode(bytes.fromhex(step4)).decode()
    
    return privateKeyWIF

def create_public_address(public_key_hash):
    
    print("Creating address...")

    # Step 1: Concatenate '04' with publicKeyHash and convert it to bytes
    step1 = bytes.fromhex("04" + public_key_hash)
    
    # Step 2: Calculate the SHA-256 hash
    step2 = hashlib.sha256(step1).digest()
    print('SHA-256 hash of 1:', step2.hex().upper())

    # Step 3: Calculate the SHA-256 hash of the resulting hash
    h = ripemd160.new(step2)
    step3 = h.digest()
    print('RIPEMD-160 Hash of 2:', step3.hex().upper())
    
    # Step 4: Adding network bytes
    step4 = bytes.fromhex("00" + step3.hex())
    print('Adding network bytes:', step4.hex().upper())
    
    # Step 5: Calculate the SHA-256 hash
    step5 = hashlib.sha256(step4).digest()
    print('SHA-256 hash of 4:', step5.hex().upper())

    # Step 6: Calculate the SHA-256 hash
    step6 = hashlib.sha256(step5).digest()
    print('SHA-256 hash of 5:', step6.hex().upper())

    # Step 7: Get the first 4 bytes (8 hexadecimal characters) of the resulting hash
    step7 = step6[:4].hex()
    print('First four bytes of 6 -checksum-:', step7.upper())

    # Step 8: Concatenate step1 with the checksum
    step8 = step4.hex() + step7
    print('Adding 7 at the end of 4')
    
    # Base58 encoding of 8 (Address)
    address = base58.b58encode(bytes.fromhex(step8)).decode()
    
    return address

def make_wallet():
    max_hex = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140"
    max_bytes = bytes.fromhex(max_hex)
    is_invalid = True
    
    while is_invalid:
        # 32 byte random number
        private_key = secrets.token_bytes(32) 
        
        # convert to hexadecimal
        private_key_hex = private_key.hex()

        print('> Private ECDSA key created:', private_key_hex)
        
        # Compare the generated private key with the maximum
        if max_bytes > private_key:
            is_invalid = False

    # generate public key from private
    private_key_instance = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    public_key_hex = private_key_instance.verifying_key.to_string().hex()
    print('> Public ECDSA key created:', public_key_hex)
    
    # generate public key hash
    public_key_hash_bytes = utils.hash(public_key_hex)
    public_key_hash_hex = public_key_hash_bytes.hex()
    print('> Public key RIPEMD-160 created:', public_key_hash_hex)
    
    # generate public address
    public_address = create_public_address(public_key_hex)
    print('> Public address:', public_address)
    print('> Check address: ', f'https://www.blockchain.com/explorer/addresses/btc/{public_address}')
    
    # generate private key WIF (wallet import format)
    private_key_wif = create_private_key_wif(private_key_hex)
    print('> Private key WIF (wallet import format) created:', private_key_wif)
    
    wallet = {
        "private_key_hex": private_key_hex,
        "private_key_wif": private_key_wif,
        "public_key": public_key_hex,
        "public_key_hash": public_key_hash_hex,
        "public_address": public_address,
    }

    return wallet

print("# Creating Bitcoin Wallet Keys & Address...")

make_wallet()

print("* Only use this site for testing purposes. Do not use for live wallets")

"""
Script Name: utils.py
Author: Nahuel Bulian
Description: 
    Description: This module contains utility functions that are commonly used across the project. It includes functions for data processing, file handling, and other miscellaneous tasks.
Usage:
    Import this module into your Python scripts using 'import utils' to access the utility functions.
Dependencies:
    - None
Compatibility:
    - Python 3.x
"""

import hashlib
import base58
from ripemd import ripemd160

# hash with both SHA-256 and RIPEMD-160 algorithms
def hash(msg):
    # Hash with SHA-256 algorithm
    hash_sha256 = hashlib.sha256(bytes.fromhex(msg)).digest()

    # Get RIPEMD-160 hash as bytes
    h = ripemd160.new(hash_sha256)
    ripemd_hash = h.digest()

    return ripemd_hash

def get_address(public_key):
    # Compute the hash160 digest of the public key
    hash160_digest = hash(public_key)
    
    # Set the version bytes for the Bitcoin mainnet addresses
    version = b'\x00'
    
    # Calculate the checksum by double hashing the version concatenated with the hash160 digest
    checksum = hashlib.sha256(hashlib.sha256(version + hash160_digest).digest()).digest()[:4]
    
    # Concatenate the version, hash160 digest, and checksum to form the address bytes
    address_bytes = version + hash160_digest + checksum
    
    # Encode the address bytes using Base58 encoding
    address = base58.b58encode(address_bytes).decode('utf-8')
    
    return address

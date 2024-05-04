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

# get a base58 encoded BTC address given a user's public key
def get_address(public_key):
    # Obtain public key hash
    public_key_hash = hash(public_key)
    
    # Encode public key hash in base58
    address = base58.b58encode(public_key_hash)
    
    return address

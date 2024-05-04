# Nono Coin

This code have been written base on the Udemy course [Breaking Down Bitcoin](https://www.udemy.com/course/breaking-down-bitcoin/)

The instructor approach was "Learn how to build Bitcoin from scratch, in JavaScript!" but I decided to add a bit more of fun doing it with Python. Let's see how it goes!

URL: https://www.udemy.com/course/breaking-down-bitcoin/

Course creator by [Tom Goldenberg](https://www.udemy.com/course/breaking-down-bitcoin/?couponCode=ST2MT43024#instructor-1)

## Table of Contents

- [Nono Coin](#nono-coin)
  - [Table of Contents](#table-of-contents)
  - [Bitcoin Transaction Anatomy](#bitcoin-transaction-anatomy)
    - [Example Bitcoin Transaction](#example-bitcoin-transaction)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Creator](#creator)
  - [Repository](#repository)

## Bitcoin Transaction Anatomy
- **Version (`version`)**: The version of the transaction. This is useful for future updates to the Bitcoin protocol.
  
- **Inputs (`vin`)**: The inputs of a transaction are references to outputs of previous transactions being spent. Each input contains information indicating which previous output is being spent and a digital signature proving that the owner of the previous output has authorized the transfer. The "COINBASE" input in the genesis transaction is an exception, as it is the first transaction and has no inputs. In this case, new coins are generated and awarded to the miner.
  
- **Outputs (`vout`)**: The outputs of a transaction are the Bitcoin addresses to which funds are being sent and the amount of bitcoins being sent. Each output also includes a locking script (`script_pub_key`), which is a script that defines the conditions under which the bitcoins can be spent in the future.
  
- **Value (`value`)**: The amount of bitcoins being transferred in the transaction.
  
- **Previous Block (`previous_hash`)**: The hash of the previous block in the blockchain. This establishes the chronological sequence of blocks and ensures the integrity of the chain.
  
- **Timestamp (`timestamp`)**: The timestamp at which the transaction was created.
  
- **Difficulty and Nonce (`difficulty`, `nonce`)**: These are values used in the mining process to find a valid hash that meets the target difficulty set by the Bitcoin network. The nonce is an arbitrary number that is iteratively changed until a valid hash is found.
  
- **Block Size (`blocksize`)**: The size of the block in bytes.

### Example Bitcoin Transaction

```json
{
    "hash": "92a4b682ec5425f6208702f2278b8eb368d89e9d4c7a4d5c2366ef43f4b1fb12",  // Transaction hash
    "version": 1,  // Transaction version
    "locktime": 0,  // Transaction lock time
    
    "vin": [  // Transaction inputs
        {
            "txid": "f3f55fb31b0d10d6d1d94ff24d1936bb883f66d4a7e3366e56275a761cb12e63",  // Previous transaction ID
            "vout": 0,  // Previous output index
            "scriptSig": "47304402207a0a33d42f06fd16af245038c50f9565794b8f26866b9e1b9daa624556a636020220123b8f8a3ea12b46d9ff178d1841aa12755c18aa5a5205f36d9c865dbb16c2ab012102c97d2e1de56ad6a0bcb9c1676f8b1ccae4474f2a2dcce602c5864b550a7cfeab",  // Script signature
            "sequence": 4294967295  // Sequence number
        }
    ],
    "vout": [  // Transaction outputs
        {
            "value": 0.01000000,  // Bitcoin amount (BTC)
            "scriptPubKey": "76a91401b5f8e935da1a58a6cda4a5b6bf3efabbdcb16a88ac"  // Script public key
        },
        {
            "value": 0.05000000,  // Bitcoin amount (BTC)
            "scriptPubKey": "76a914c6a8d9cfb0cc78241e646ff671d0beada631a46088ac"  // Script public key
        }
    ]
}
```

## Installation

Installation instructions are currently being determined and will be updated soon. Please check back later for updates.


```bash
# Installation command
$ pip install -r requirements.txt
```

## Usage

Usage instructions are currently being determined and will be updated soon. Please check back later for updates.

```bash
# Example usage command
$ 
```

## Contributing

If you would like to contribute to the project, please follow these guidelines:

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Test your changes
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature`)
7. Create a new Pull Request

## License

This project is licensed under the [MIT License](LICENSE.md).

## Creator

[Nahuel Bulian](https://github.com/nbulian)

## Repository

[Link to Repository](https://github.com/nbulian/nono-coin)

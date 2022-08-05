# source:
# https://www.freecodecamp.org/news/how-to-create-an-ethereum-wallet-address-from-a-private-key-ae72b0eee27b/

import codecs
# pip3 install ecdsa
import ecdsa
# pip3 install pycryptodome
from Crypto.Hash import keccak

# A private key is a 64 hex digits string = 256 bits of data
private_key_bytes = codecs.decode("8888888888888888888888888888888888888888888888888888888888888888", "hex")

# Obtain the public key using secp256k1 algorithm
key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
key_bytes = key.to_string()
public_key = codecs.encode(key_bytes, "hex")
print(public_key)

# Generate a keccak hash
public_key_bytes = codecs.decode(public_key, "hex")
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_key_bytes)
keccak_digest = keccak_hash.hexdigest()
print(keccak_digest)

# The address is the rightmost 20 bytes = 40 last hex digits
wallet_len = 40
wallet = "0x" + keccak_digest[-wallet_len:]
print(wallet)

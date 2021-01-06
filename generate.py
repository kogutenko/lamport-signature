import sys
import os
from hashlib import sha256

if len(sys.argv) != 2:
    print("Lamport public and private key generator\n")
    print("Usage: generate.py [key_title]\n")
    print("Produces two files with names [key_title].public and [key_title].private. Files will be overwritten!\n")
    sys.exit()


# Generating cryptographically secure 256-bit numbers and its hashes

private_list = [(os.urandom(32), os.urandom(32)) for i in range(256)]

public_list  = [(sha256(x).hexdigest(), sha256(y).hexdigest()) for (x, y) in private_list]


# Writing to file

file_name = sys.argv[1]

# Private key

private_file = open(file_name + ".private", "wb")

for (x, y) in private_list:
    private_file.write(x.hex().encode() + b" " + y.hex().encode() + b"\n")

private_file.close()

# Public key

private_file = open(file_name + ".public", "wb")

for (x, y) in public_list:
    private_file.write(x.encode() + b" " + y.encode() + b"\n")

private_file.close()

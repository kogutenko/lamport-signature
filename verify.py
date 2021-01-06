import sys
from hashlib import sha256
from binascii import unhexlify

if len(sys.argv) != 3:
    
    print("Lamport sign verifier\n")
    print("Usage: verify.py [document_name] [public_key]\n")
    print("Notice: public key file should be provided without '.public' extension\n")
    
    sys.exit()


# Reading input files

# Document

document_name = sys.argv[1]

with open(document_name, "rb") as content_file:
    document_file = content_file.read()

# Public key

key_name = sys.argv[2]

with open(key_name + ".public", "r") as content_file:
    public_file = content_file.read()

# Sign

with open(document_name + ".sign", "r") as content_file:
    sign_file = content_file.read()


# Converting public keys file to a list form

public_file = public_file.split("\n")

public_list = [public_file[i].split(" ") for i in range(256)]


# Converting sign to a list form

sign_list = sign_file.split("\n")


# Calculating document hash

document_hash = sha256(document_file).digest()


# Validating sign

index = 0

# Extracting only needed private keys

for byte in document_hash:
    
    bit = 0x80
    
    while bit:
        
        if (bit & byte == 0 and public_list[index][0] != sha256(unhexlify(sign_list[index])).hexdigest()) or \
           (bit & byte == 1 and public_list[index][1] != sha256(unhexlify(sign_list[index])).hexdigest()):
            print("Error: not genuine sign")
            sys.exit()
        
        bit >>= 1
        index += 1

print("Success: sign is genuine")

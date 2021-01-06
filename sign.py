import sys
from hashlib import sha256

if len(sys.argv) != 3:
    
    print("Lamport sign generator\n")
    print("Usage: sign.py [document_name] [key_name]\n")
    print("Notice: private key file should be provided without '.private' extension\n")
    print("Produces one file with name [document_name].sign")
    
    sys.exit()


# Reading input files

# Document

document_name = sys.argv[1]

with open(document_name, "rb") as content_file:
    document_file = content_file.read()

# Private key

key_name = sys.argv[2]

with open(key_name + ".private", "r") as content_file:
    private_file = content_file.read()


# Converting private keys file to list form

private_file = private_file.split("\n")

private_list = [private_file[i].split(" ") for i in range(256)]


# Calculating document hash

document_hash = sha256(document_file).digest()


# Exporting sign

sign_list = []

index = 0

# Extracting only needed private keys

for byte in document_hash:
    
    bit = 0x80
    
    while bit:
        
        if bit & byte:
            sign_list.append(private_list[index][1])
        else:
            sign_list.append(private_list[index][0])
        
        bit >>= 1
        index += 1

# Writing to file

sign_file = open(document_name + ".sign", "w")

for sign in sign_list:
    sign_file.write(sign + "\n")

sign_file.close()

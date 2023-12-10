import re

def valid_ethereum_address(address):
    if not re.match(r"^(0x)?[0-9a-fA-F]{40}$", address):#checking the basic format
        return False
    if re.match(r"^(0x)?[0-9A-Fa-f]{40}$", address) or re.match(r"^(0x)?[0-9a-fA-F]{40}$", address):#checking that each letter has correct caps 
        return True
    return False
address_tocheck = input("Enter your Ethereum address")
print(valid_ethereum_address(address_tocheck))
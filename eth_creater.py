from eth_account import Account
import json

addresses = []

for _ in range(0, 20):
    acct = Account.create()
    address = acct.address
    private_key = acct._private_key.hex()
    addresses.append({
        address: private_key,
    })

with open('eth_addresses.json', 'w') as f:
    json.dump(addresses, f, indent=4)

with open('eth_addresses.json', 'r') as f:
    addresses = json.load(f)

with open('eth_addresses.json', 'r') as json_file:
    data = json.load(json_file)

with open('output.txt', 'w') as txt_file:
    for entry in data:
        address, private_key = list(entry.items())[0]
        txt_file.write(f"{address}:{private_key}\n")

print("Conversion completed. Check 'output.txt' for the result.")

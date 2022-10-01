from pprint import pprint
from data import WalletInfo
from urls import wallet_info

i = wallet_info("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

wi = WalletInfo(**i)
t = wi.transactions[0]

print(t.hash)
inputs = sum(i["prev_out"]["value"] for i in t.inputs)
print(inputs)

outputs = sum(o["value"] for o in t.out)
print(outputs)


print(inputs - outputs)
print(t.fee)

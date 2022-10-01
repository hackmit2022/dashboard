from pprint import pprint
from data import WalletInfo
from urls import wallet_info

from urls import get_difficulty
from data import Difficulty

i = wallet_info("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

d = Difficulty(**get_difficulty())

wi = WalletInfo(**i)
t = wi.transactions[10]

print(t.time)
# pprint(i["txs"])

# print(list(zip(*d.values)))
day, close_diff = min(d.values, key=lambda d: abs(d[0] - t.time))
print(close_diff)

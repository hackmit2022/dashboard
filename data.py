from pydantic import BaseModel, Field
from datetime import datetime
from urls import wallet_info, get_difficulty

import pytz


class Difficulty(BaseModel):
    @classmethod
    def from_source(cls):
        return cls(**get_difficulty())

    def __init__(self, *, values: list[dict[str, int]], **data):
        values = [
            (datetime.fromtimestamp(dic["x"], tz=pytz.utc), dic["y"]) for dic in values
        ]
        super().__init__(values=values, **data)

    values: list[tuple[datetime, int]]


class Transaction(BaseModel):
    hash: str
    time: datetime
    inputs: list[dict]
    out: list[dict]

    @property
    def fee(self):
        inputs = sum(i["prev_out"]["value"] for i in self.inputs)
        outputs = sum(o["value"] for o in self.out)
        return inputs - outputs


class WalletInfo(BaseModel):
    @classmethod
    def from_hash(cls, hash: str):
        return cls(**wallet_info(hash))

    transactions: list[Transaction] = Field(..., alias="txs")
    total_sent: int
    total_received: int
    final_balance: int


def close_diff(transaction: Transaction, diff: Difficulty):
    day, close_diff = min(diff.values, key=lambda d: abs(d[0] - transaction.time))
    return close_diff

import requests

difficulty = (
    "https://api.blockchain.info/charts/difficulty?timespan=10years&format=json"
)
wallet = "https://blockchain.info/rawaddr/{wallet_address}"


def get_difficulty():
    """Get the difficulty of the Bitcoin network."""
    return requests.get(difficulty).json()


def wallet_info(wallet_address):
    """Get the wallet information."""
    return requests.get(wallet.format(wallet_address=wallet_address)).json()

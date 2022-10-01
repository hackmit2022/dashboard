from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from data import close_diff
from data import Difficulty

from data import WalletInfo

app = Dash(__name__)


diff = Difficulty.from_source()

app.layout = html.Div(
    [
        dcc.Input(
            id="wallet-hash", placeholder="wallet address", type="text", debounce=True
        ),
        html.H4("Interactive color selection with simple Dash example"),
        html.P("Select color:"),
        html.P("bruh", id="main-content"),
    ]
)


@app.callback(Output("main-content", "children"), Input("wallet-hash", "value"))
def update_wallet_display(hash):
    print("hash", hash)

    wi = WalletInfo.from_hash(hash)

    print(wi.transactions[20].time)

    [html.P(hash)]

    return [html.P(f"{t.fee} - {close_diff(t, diff)}") for t in wi.transactions]


app.run_server(debug=True)

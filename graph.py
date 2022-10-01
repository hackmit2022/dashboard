from dash import Dash, dcc, html, Input, Output
from data import close_diff, Difficulty, WalletInfo
from C02_per_block import calculate_CO2_per_block

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

    [html.P(hash)]

    return [
        html.P(
            f"{ti[0].time} - {ti[0].fee} - {ti[1]} - {calculate_CO2_per_block(ti[1]):.9}"
        )
        for ti in ((t, close_diff(t, diff)) for t in wi.transactions)
    ]


app.run_server(debug=True)

from dash import Dash, dcc, html, Input, Output, dash_table
from data import close_diff, Difficulty, WalletInfo
from C02_per_block import calculate_CO2_per_block

app = Dash(__name__)


diff = Difficulty.from_source()

app.layout = html.Div(
    [
        html.H4("What's your impact?", id="impact"),
        html.Div(
            dcc.Input(
                id="wallet-hash",
                placeholder="wallet address",
                type="text",
                debounce=True,
            ),
            id="input-container",
        ),
        html.Div("", id="transaction-container"),
    ]
)


@app.callback(
    Output("transaction-container", "children"), Input("wallet-hash", "value")
)
def update_wallet_display(hash):
    print("hash", hash)

    wi = WalletInfo.from_hash(hash)

    return [
        dash_table.DataTable(
            data=[
                {
                    "date": t.time.strftime("%Y-%m-%d"),
                    "fee (sat)": t.fee,
                    "CO2 (kg)": f"{calculate_CO2_per_block(diff):.8}",
                }
                for t, diff in ((t, close_diff(t, diff)) for t in wi.transactions)
            ],
        )
    ]


app.run_server(debug=True)

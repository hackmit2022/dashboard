from dash import Dash, dcc, html, Input, Output, dash_table
from data import close_diff, Difficulty, WalletInfo
from C02_per_block import calculate_CO2_per_block, calculate_energy_per_block

app = Dash(__name__)


diff = Difficulty.from_source()

app.layout = html.Div(
    [
        html.H1("What's your impact?", id="impact"),
        html.Div(
            dcc.Input(
                id="wallet-hash",
                placeholder="wallet address",
                type="text",
                debounce=True,
            ),
            id="input-container",
        ),
        html.Div(
            [
                html.Div("", id="transaction-container"),
                html.Div("", id="totals-container"),
            ],
            id="info-container",
        ),
    ]
)


@app.callback(
    Output("transaction-container", "children"),
    Output("totals-container", "children"),
    Input("wallet-hash", "value"),
)
def update_wallet_display(hash):
    print("hash", hash)

    wi = WalletInfo.from_hash(hash)

    transaction_data = [
        (t, diff, calculate_energy_per_block(diff), calculate_CO2_per_block(diff))
        for t, diff in ((t, close_diff(t, diff)) for t in wi.transactions)
    ]

    totals = {
        "fees": sum(t.fee for t, _, _, _ in transaction_data),
        "CO2": sum(co2 for _, _, _, co2 in transaction_data),
        "energy": sum(energy for _, _, energy, _ in transaction_data),
    }

    return [
        [
            html.H3("Transactions:"),
            dash_table.DataTable(
                data=[
                    {
                        "date": t.time.strftime("%Y-%m-%d"),
                        "fee (sat)": t.fee,
                        "CO2 (kg)": f"{co2:.8}",
                        "energy (kWh)": f"{energy:.8}",
                    }
                    for t, diff, energy, co2 in transaction_data
                ],
            ),
        ],
        [
            html.H2("Your totals"),
            html.P(
                f"Total fees: {totals['fees']/1e8} BTC = {totals['fees']/1e8 * 19158.40:.2f} USD"
            ),
            html.P("Total CO2: {:.2f} kg".format(totals["CO2"])),
            html.P("Total Energy: {:.0f} kWh".format(totals["energy"])),
        ],
    ]


app.run_server(debug=True)

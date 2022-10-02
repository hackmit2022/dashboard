def calculate_energy_per_block(difficulty):

    hashes_per_block = 4.3e9 * difficulty
    max_hashes_per_joule = 11100 * 1000000
    joules_per_block = hashes_per_block / max_hashes_per_joule
    kwh_per_block = joules_per_block / 3.6e6
    kwh_per_transaction = kwh_per_block / 1800
    return kwh_per_transaction


def calculate_CO2_per_block(difficulty):
    kwh = calculate_energy_per_block(difficulty)
    kg_CO2_per_kwh = 0.82 * 0.45
    CO_2_per_block = kwh * kg_CO2_per_kwh

    return CO_2_per_block

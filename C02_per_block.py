def calculate_CO2_per_block(difficulty):

    hashes_per_block = 4.3e9 * difficulty
    max_hashes_per_joule = 11100 * 1000000
    joules_per_block = hashes_per_block / max_hashes_per_joule
    kwh = joules_per_block * 3.6e6
    pounds_CO2_per_kwh = .82
    CO_2_per_block = kwh * pounds_CO2_per_kwh

    return CO_2_per_block

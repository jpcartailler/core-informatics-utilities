# Freezer E configuration

# Freezer name and barcode
freezer = 'FE'
barcode_freezer = 'FRZ4'

# 2 Shelves (top 2)
# 5 racks
# 7 drawers
# 4 boxes

containers_config = {
    'c1': {
        'name_prefix': 'S',
        'name_starting_index': 1,
        'barcode_prefix': 'SHF',
        'barcode_starting_index': 16,
        'number_to_create': 5
    }
}

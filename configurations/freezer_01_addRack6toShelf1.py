# Freezer 1 configuration
# add a 6th rack to the existing Shelf 1 (SHF10) of Freezer 1 (FRZ1)
# the output will need to be dissected a bit

# Freezer name and barcode
freezer = 'F1'
barcode_freezer = 'FRZ1'

# 2 Shelves (top 2)
# 5 racks
# 7 drawers
# 4 boxes

containers_config = {
    'c1': {
        'name_prefix': 'S',
        'name_starting_index': 1,
        'barcode_prefix': 'SHF',
        'barcode_starting_index': 10,
        'number_to_create': 1
    },
    'c2': {
        'name_prefix': 'R',
        'name_starting_index': 6,
        'barcode_prefix': 'RCK',
        'barcode_starting_index': 71,
        'number_to_create': 1
    },
    'c3': {
        'name_prefix': 'D',
        'name_starting_index': 1,
        'barcode_prefix': 'DRW',
        'barcode_starting_index': 500,
        'number_to_create': 7
    },
    'c4': {
        'name_prefix': 'FB',
        'name_starting_index': 1,
        'barcode_prefix': 'FB',
        'barcode_starting_index': 1321,
        'number_to_create': 4
    }
}

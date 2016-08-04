# Freezer 1 configuration

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
        'barcode_starting_index': 13,
        'number_to_create': 2
    },
    'c2': {
        'name_prefix': 'R',
        'name_starting_index': 1,
        'barcode_prefix': 'RCK',
        'barcode_starting_index': 56,
        'number_to_create': 5
    },
    'c3': {
        'name_prefix': 'D',
        'name_starting_index': 1,
        'barcode_prefix': 'DRW',
        'barcode_starting_index': 430,
        'number_to_create': 7
    },
    'c4': {
        'name_prefix': 'FB',
        'name_starting_index': 1,
        'barcode_prefix': 'FB',
        'barcode_starting_index': 841,
        'number_to_create': 4
    }
}


# 1 shelf
# 4 bins
# 10 boxes

containers_config = {
    'c1': {
        'name_prefix': 'S',
        'name_starting_index': 3,
        'barcode_prefix': 'SHF',
        'barcode_starting_index': 12,
        'number_to_create': 1
    },
    'c2': {
        'name_prefix': 'B',
        'name_starting_index': 1,
        'barcode_prefix': 'BIN',
        'barcode_starting_index': 1,
        'number_to_create': 4
    },
    'c3': {
        'name_prefix': 'FB',
        'name_starting_index': 1,
        'barcode_prefix': 'FB',
        'barcode_starting_index': 841,
        'number_to_create': 10
    }
}
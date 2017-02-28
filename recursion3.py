#!/usr/bin/python

"""
Freezer Configuration Builder for Core Informatics LIMS

See README.md for usage documentation.

"""

import pprint


def create_freezer_records(freezer, configuration, counter=1, location=None, data=None, barcode_index=None):
    """
    Create all named records for locations based on freezer configuration.

    :param freezer: (string) Freezer name (eg. F1)
    :param configuration: (dictionary) Freezer configuration input
    :param counter: (integer) Internal counter
    :param location: (string) Record name assembly (e.g. F1-R3-D4-...)
    :param data: (list) Array of stored locations
    :return: (list) Array of stored locations
    """

    # Create dictionary lookup key from current level
    key = "c" + str(counter)

    # First pass
    if location is None:
        location = ''

    # First pass
    if data is None:
        data = []

    # First pass
    #if barcode_index is None:
    #    barcode_index = configuration[key]['barcode_starting_index']
    #print "barcode_index: " + str(barcode_index)
    print "+"*60
    if (counter > 1):
        parent_count = counter - 1
        parent_key = "c" + str(parent_count)

        if barcode_index is None:
            barcode_index = configuration[parent_key]['barcode_starting_index']
            print "top/first:" + str(barcode_index)
        else:
            barcode_index=barcode_index
            print "top/not first:" + str(barcode_index)

        parent_barcode = configuration[parent_key]['barcode_prefix'] + str(barcode_index)

        barcode_index += 1

    else:
        parent_barcode = ''
    temp3 = location

    counter += 1 # increment to next level

    for i in range(0, configuration[key]['number_to_create']):

        name_index_incr = configuration[key]['name_index'] + i

        #location = location + str(configuration[key]['attr1'])
        location = temp3 + str(configuration[key]['name_prefix']) + str(name_index_incr)
        #print "counter: " + str(counter)
        print "i(" + str(i) + "). counter(" + str(counter) + ").  /  " + str(location) + " / " + parent_barcode
        # Parent barcode, only valid for second iteration since the first *is* the root
        # and has no parent. Hence, at level 2, we can back up and look at the previous level's
        # data. The freezer (root) bacode information will look like:
        # 'barcode_prefix': 'FRZ',
        # 'barcode_starting_index': 1,

        #print "parent_barcode: " + str(parent_barcode)

        print "-" * 40
        # write data to list
        data.append([key, location, parent_barcode])

        if(counter > len(configuration)):
            # save new record
            barcode = ''
            #parent_barcode = ''
            #data.append([key, location, parent_barcode])
            location=''
        else:
            #barcode_index += 1

            location = location + "-"
            create_freezer_records(freezer, configuration, counter, location, data, barcode_index)


    return data


def create_excel_spreadsheets(data, configuration):
    """
    Generate Excel spreadsheets using the configuration data and freezer data

    :param data: output from the create_freezer_records function
    :param configuration: freezer configuration input in the form of a dictionary
    :return: files written to disk in .xlsx format
    """

    # Create dictionary and preformat it
    sheets = {}
    for key in configuration:
        sheets[key] = []    # setup list for specific level

    #pprint.pprint(sheets)
    for d in data:

        for key in sheets:
            #print "key in sheets: " + str(key) + ". " + str(d[0])

            if (d[0] == key):
                #print d[1]
                sheets[key].append(d)


    return sheets



configuration = {
    'c1': {
        'name_prefix': 'F',
        'name_index': 1,
        'barcode_prefix': 'FRZ',
        'barcode_starting_index': 1,
        'number_to_create': 1
    },
    'c2': {
        'name_prefix' : 'S',
        'name_index' : 1,
        'barcode_prefix': 'SHF',
        'barcode_starting_index':10,
        'number_to_create' : 2
    },
    'c3': {
        'name_prefix' : 'R',
        'name_index' : 1,
        'barcode_prefix': 'RCK',
        'barcode_starting_index': 46,
        'number_to_create' : 5
    },
    'c4': {
        'name_prefix' : 'D',
        'name_index' : 1,
        'barcode_prefix': 'DRW',
        'barcode_starting_index': 255,
        'number_to_create' : 7
    },
    'c5': {
        'name_prefix' : 'B',
        'name_index' : 1,
        'barcode_prefix': 'FB',
        'barcode_starting_index': 421,
        'number_to_create' : 4
    }
}

configuration = {
    'c1': {
        'name_prefix': 'F',
        'name_index': 1,
        'barcode_prefix': 'FRZ',
        'barcode_starting_index': 1,
        'number_to_create': 1
    },
    'c2': {
        'name_prefix': 'S',
        'name_index': 1,
        'barcode_prefix': 'SHF',
        'barcode_starting_index': 10,
        'number_to_create': 2
    },
    'c3': {
        'name_prefix': 'R',
        'name_index': 1,
        'barcode_prefix': 'RCK',
        'barcode_starting_index': 46,
        'number_to_create': 5
    }
}


# Create freezer records
data = create_freezer_records('F1', configuration)

# Create spreadsheets
sheets = create_excel_spreadsheets(data, configuration)

# Testing
# print ""
print "+" * 60
#pprint.pprint(sheets)
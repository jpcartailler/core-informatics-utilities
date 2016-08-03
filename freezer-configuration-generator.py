#!/usr/bin/python

'''
Freezer configuration builder

Developed for use with Core Informatics LIMS location configuration

See README.md for documentation.

'''

import xlsxwriter

# CONFIGURATION START ----------------------------------

# Freezer name and barcode
freezer = 'F2'
barcode_freezer = 'FRZ2'

# Prefix and 'Starting index' needs to be looked up in C.I. LIMS via the
# Admin > Location > ENTITY_TYPE > List All. From there, find the
# appropriate values

# What containers should be built?
containers_to_use = ['c1', 'c2', 'c3', 'c4']

# Configuration of containers to build
containers_config = {
    'c1': {
        'name_prefix': 'S',
        'name_starting_index': 1,
        'barcode_prefix': 'SHF',
        'barcode_starting_index': 4,
        'number_to_create': 3
    },
    'c2': {
        'name_prefix': 'R',
        'name_starting_index': 1,
        'barcode_prefix': 'RCK',
        'barcode_starting_index': 31,
        'number_to_create': 5
    },
    'c3': {
        'name_prefix': 'D',
        'name_starting_index': 1,
        'barcode_prefix': 'DRW',
        'barcode_starting_index': 255,
        'number_to_create': 7
    },
    'c4': {
        'name_prefix': 'B',
        'name_starting_index': 1,
        'barcode_prefix': 'FB',
        'barcode_starting_index': 421,
        'number_to_create': 4
    }
}

# CONFIGURATION END ------------------------------------

# FUNCTIONS --------------------------------------------

def writeExcel(filename, data):

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'BARCODE')
    worksheet.write(0, 1, 'NAME')
    worksheet.write(0, 2, 'LOCATION BARCODE')
    worksheet_row = 1

    for d in data:
        barcode = d[0]
        name = d[1]
        barcode_location = d[2]

        worksheet.write(worksheet_row, 0, barcode)
        worksheet.write(worksheet_row, 1, name)
        worksheet.write(worksheet_row, 2, barcode_location)

        worksheet_row += 1

    workbook.close()



# CODE # FUNCTIONS --------------------------------------------
# print containers_to_use
# ranges = [ range(x) for x in containers_to_use ]
# for i in itertools.product(*ranges):
#     print i



# for key, value in sorted(containers_config.items()):
#
#     print '-' * 20
#     print 'Processing container ' + key
#
#     # Get individual container data
#     for key2, value2 in value.items():
#         print key2, value2

c1_exceldata = []
c2_exceldata = []
c3_exceldata = []
c4_exceldata = []
c1_exceldata
# Loop through each container

##################
# Go to c1 level
c1_index = containers_config['c1']['name_starting_index'] # reset shelf index foreach rack

for i in range(0, containers_config['c1']['number_to_create']):

    # set up values
    barcode = ''
    name = freezer + containers_config['c1']['name_prefix'] + str(c1_index)
    barcode_location = barcode_freezer

    # add data to list
    c1_exceldata.append([barcode, name, barcode_location])


    ##################
    # Go to c2 level
    if('c2' in containers_to_use):

        c2_index = containers_config['c2']['name_starting_index'] # reset shelf index foreach rack

        for i in range(0, containers_config['c2']['number_to_create']):

            # set up values
            barcode = ''
            name = freezer + containers_config['c1']['name_prefix'] + str(c1_index) + containers_config['c2']['name_prefix'] + str(c2_index)
            barcode_location = containers_config['c1']['barcode_prefix'] + str(containers_config['c1']['barcode_starting_index'])

            # add data to list
            c2_exceldata.append([barcode, name, barcode_location])


            ##################
            # Go to c3 level
            if('c3' in containers_to_use):
                c3_index = containers_config['c3']['name_starting_index'] # reset shelf index foreach rack

                for i in range(0, containers_config['c3']['number_to_create']):

                    # set up values
                    barcode = ''
                    name = freezer + containers_config['c1']['name_prefix'] + str(c1_index) + containers_config['c2']['name_prefix'] + str(c2_index) + containers_config['c3']['name_prefix'] + str(c3_index)
                    barcode_location = containers_config['c2']['barcode_prefix'] + str(containers_config['c2']['barcode_starting_index'])

                    # add data to list
                    c3_exceldata.append([barcode, name, barcode_location])

                    ##################
                    # Go to c4 level
                    if('c4' in containers_to_use):

                        c4_index = containers_config['c4']['name_starting_index'] # reset shelf index foreach rack

                        for i in range(0, containers_config['c4']['number_to_create']):

                            # set up values
                            barcode = ''
                            name = freezer + containers_config['c1']['name_prefix'] + str(c1_index) + containers_config['c2']['name_prefix'] + str(c2_index) + containers_config['c3']['name_prefix'] + str(c3_index) + containers_config['c4']['name_prefix'] + str(c4_index)
                            barcode_location = containers_config['c3']['barcode_prefix'] + str(containers_config['c3']['barcode_starting_index'])

                            # add data to list
                            c4_exceldata.append([barcode, name, barcode_location])

                            # increment to next container
                            c4_index += 1

                    # increment to next container
                    c3_index += 1
                    containers_config['c3']['barcode_starting_index']  += 1

            # increment to next container
            c2_index += 1
            containers_config['c2']['barcode_starting_index']  += 1


    # increment to next container
    c1_index += 1
    containers_config['c1']['barcode_starting_index']  += 1

print "-" * 80
dict = {}
dict['c1'] = c1_exceldata
dict['c2'] = c2_exceldata
dict['c3'] = c3_exceldata
dict['c4'] = c4_exceldata

for c in containers_to_use:
    filename = c + '_exceldata.xlsx'
    array_name = str(c) + '_exceldata'
    #writeExcel('c1_exceldata.xlsx', c1_exceldata)
    writeExcel(filename, dict[c])
    print "Saved " + str(len(dict[c])) + " records to " + filename

print "-" * 80

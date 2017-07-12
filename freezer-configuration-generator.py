#!/usr/bin/python

'''
Freezer configuration builder

Developed for use with Core Informatics LIMS location configuration

See README.md for documentation.

'''

import xlsxwriter
import yaml
import os


# ----------------------------------------------------------------------------------------------------------------------
# CONFIGURATION START
#
yaml_file = ''

try:
    containers_config = yaml.load(file(yaml_file, 'r'))
except yaml.YAMLError, exc:
    print "Error in YAML configuration file:", exc


output_dir = os.path.splitext(os.path.basename(yaml_file))[0]


# ----------------------------------------------------------------------------------------------------------------------
# INITIALIZATION START
#
c1_exceldata = []
c2_exceldata = []
c3_exceldata = []
c4_exceldata = []

# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS START
#
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



# ----------------------------------------------------------------------------------------------------------------------
# BUILD CONFIGURATION
#
freezer = containers_config['freezer']
barcode_freezer = containers_config['barcode_freezer']
name_delimiter = containers_config['name_delimiter']
containers_to_use = containers_config['containers_to_use']


# Go to c1 level
c1_index = containers_config['c1']['name_starting_index'] # reset shelf index foreach rack

for i in range(0, containers_config['c1']['number_to_create']):

    # set up values
    barcode = ''
    name = freezer + name_delimiter + containers_config['c1']['name_prefix'] + str(c1_index)
    c1_parent_name = name
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
            name = c1_parent_name + name_delimiter + containers_config['c2']['name_prefix'] + str(c2_index)
            c2_parent_name = name
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
                    name = c2_parent_name + name_delimiter + containers_config['c3']['name_prefix'] + str(c3_index)
                    c3_parent_name = name
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
                            name = c3_parent_name + name_delimiter + containers_config['c4']['name_prefix'] + str(c4_index)
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

# ----------------------------------------------------------------------------------------------------------------------
# WRITE EXCEL FILES
#
print "-" * 80
dict = {}
dict['c1'] = c1_exceldata
dict['c2'] = c2_exceldata
dict['c3'] = c3_exceldata
dict['c4'] = c4_exceldata

for c in containers_to_use:

    dirPath = os.path.dirname(os.path.realpath(__file__))

    filename = dirPath + '/output/' + output_dir + '/' + c + '_exceldata.xlsx'

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "w") as f:

        array_name = str(c) + '_exceldata'
        writeExcel(filename, dict[c])
        print "Saved " + str(len(dict[c])) + " records to " + filename

print "-" * 80

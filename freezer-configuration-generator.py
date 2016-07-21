#!/usr/bin/python

'''
Freezer configuration builder

Developed for use with Core Informatics LIMS location configuration

This script assumes the following organization:
  freezer > shelf > rack > drawer > box

Output (for each level) will need to be 3 columns. Headers are
 - BARCODE
 - NAME
 - LOCATION BARCODE
The values for BARCODE are blank. The LOCATION BARCODE is the PARENT
barcode. For example, if entering a SHELF, then the LOCATION BARCODE would be
the parent FREEZER barcode.

'''

import csv

# Freezer configuration via LIMS must first occur
freezer = 'F2'
barcode_freezer = 'FRZ2'

# Prefix and 'Starting index' needs to be looked up via the
# Admin > Location > ENTITY_TYPE > List All. From there, find the
# appropriate values

shelf_prefix = 'S'
shelf_starting_index = 1
barcode_shelf_prefix = 'SHF'
barcode_shelf_starting_index = 4
num_shelf_created = 0

rack_prefix = 'R'
rack_starting_index = 1
barcode_rack_prefix = 'RCK'
barcode_rack_starting_index = 16
num_rack_created = 0

drawer_prefix = 'D'
drawer_starting_index = 1
barcode_drawer_prefix = 'DRW'
barcode_drawer_starting_index = 150
num_drawer_created = 0

box_prefix = 'B'
box_starting_index = 1
barcode_box_prefix = 'FB'
barcode_box_starting_index = 421
num_box_created = 0

# number of entities, per parent (freezer is top level)
num_shelf   = 3
num_rack    = 5
num_drawer  = 7
num_box     = 4

# ---------------------------------------------------------------------------------------------------------------------
# SHELF Loop
# Output example: "", "F2S1", "FRZ2"
ofile  = open('shelf.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

writer.writerow( ('BARCODE','NAME','LOCATION BARCODE') )

shelf_index = shelf_starting_index # reset shelf index foreach rack

for i in range (0, num_shelf):

    barcode = ''
    name = freezer + shelf_prefix + str(shelf_index)
    barcode_location = barcode_freezer

    writer.writerow( (barcode, name, barcode_location) )

    shelf_index += 1   # increment to next shelf

    num_shelf_created += 1

ofile.close()

# ---------------------------------------------------------------------------------------------------------------------
# RACK LOOP
# Output example: "", "F2S1R1", "SHF4"
ofile  = open('rack.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

writer.writerow( ('BARCODE','NAME','LOCATION BARCODE') )

shelf_index = shelf_starting_index # reset shelf index foreach rack

for i in range (0, num_shelf):

    rack_index = rack_starting_index # reset rack index

    for j in range (0, num_rack):

        barcode = ''
        name = freezer + shelf_prefix + str(shelf_index) + rack_prefix + str(rack_index)
        barcode_location = barcode_shelf_prefix + str(barcode_shelf_starting_index)

        writer.writerow( (barcode, name, barcode_location) )

        rack_index += 1   # increment to next shelf

        num_rack_created += 1

    shelf_index += 1   # increment to next shelf
    barcode_shelf_starting_index += 1   # increment to next shelf

ofile.close()


# ---------------------------------------------------------------------------------------------------------------------
# DRAWER LOOP
# Output example: "", "F2S7R16D1", "RCK31"
ofile  = open('drawer.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

writer.writerow( ('BARCODE','NAME','LOCATION BARCODE') )

shelf_index = shelf_starting_index # reset shelf index foreach rack

for i in range (0, num_shelf):

    rack_index = rack_starting_index # reset rack index

    for j in range (0, num_rack):

        drawer_index = drawer_starting_index # reset rack index

        for k in range (0, num_drawer):

            barcode = ''
            name = freezer + shelf_prefix + str(shelf_index) + rack_prefix + str(rack_index) + drawer_prefix + str(drawer_index)
            barcode_location = barcode_rack_prefix + str(barcode_rack_starting_index)

            writer.writerow( (barcode, name, barcode_location) )

            drawer_index += 1   # increment to next shelf

            num_drawer_created += 1


        rack_index += 1   # increment to next shelf
        barcode_rack_starting_index += 1   # increment to next shelf

    shelf_index += 1   # increment to next shelf
    barcode_shelf_starting_index += 1   # increment to next shelf

ofile.close()

# ---------------------------------------------------------------------------------------------------------------------
# BOX LOOP
# Output example: "", "F2S1R1D1B1", "DRW_"
ofile  = open('box.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

writer.writerow( ('BARCODE','NAME','LOCATION BARCODE') )

shelf_index = shelf_starting_index
rack_index = rack_starting_index
drawer_index = drawer_starting_index
box_index = box_starting_index

shelf_index = shelf_starting_index # reset shelf index foreach rack

for i in range (0, num_shelf):

    rack_index = rack_starting_index # reset rack index

    for j in range (0, num_rack):

        drawer_index = drawer_starting_index # reset rack index

        for k in range (0, num_drawer):

            box_index = box_starting_index # reset rack index

            for l in range (0, num_box):

                barcode = ''
                name = freezer + shelf_prefix + str(shelf_index) + rack_prefix + str(rack_index) + drawer_prefix + str(drawer_index) + box_prefix + str(box_index)
                barcode_location = barcode_drawer_prefix + str(barcode_drawer_starting_index)

                writer.writerow( (barcode, name, barcode_location) )

                box_index += 1   # increment to next shelf

                num_box_created += 1

            drawer_index += 1   # increment to next shelf
            barcode_drawer_starting_index += 1   # increment to next shelf

        rack_index += 1   # increment to next shelf
        barcode_rack_starting_index += 1   # increment to next shelf

    shelf_index += 1   # increment to next shelf
    barcode_shelf_starting_index += 1   # increment to next shelf

ofile.close()

print "OUTPUT:"
print 'Number of shelves created: ' + str(num_shelf_created)
print 'Number of racks created: ' + str(num_rack_created)
print 'Number of drawers created: ' + str(num_drawer_created)
print 'Number of boxes created: ' + str(num_box_created)
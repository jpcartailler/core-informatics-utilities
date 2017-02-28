import pprint

def createFreezer(freezer, configuration, counter=1, location=None, data=None):

    # Create dictionary lookup key from current level
    key = "c" + str(counter)

    # Fist pass - Prepend name with freezer option
    if location is None:
        location = freezer + "-"

    # First pass - Create data dictionary, to hold level-specific list records
    if data is None:
        data = {}
        for key in configuration:
            print "key:" +key
            data[key] = None





    temp3 = location

    counter += 1 # increment to next level

    data_record = []

    for i in range(0, configuration[key]['number_to_create']):

        name_index_incr = configuration[key]['name_index'] + i

        #location = location + str(configuration[key]['attr1'])
        location = temp3 + str(configuration[key]['name_prefix']) + str(name_index_incr)

        # if we have reached the last leaf of the tree, now is the time
        # to save the data and go to the next one
        parent_barcode = ''

        #pprint.pprint(data[key])
        # Get old record
        old_data_record = data[key]
        # New record - add to old
        data_record.append([key, location, parent_barcode])


        data[key]=data_record

        if(counter > len(configuration)):
            # save new record
            barcode = ''
            #parent_barcode = ''
            #data.append([key, location, parent_barcode])
            location=''
        else:
            location = location + "-"
            createFreezer(freezer, configuration, counter, location, data)



    return data



configuration = {
    'c1': {
        'name_prefix' : 'S',
        'name_index' : 1,
        'number_to_create' : 3
    },
    'c2': {
        'name_prefix' : 'R',
        'name_index' : 1,
        'number_to_create' : 2
    },
    'c3': {
        'name_prefix' : 'D',
        'name_index' : 1,
        'number_to_create' : 4
    },
    'c4': {
        'name_prefix' : 'B',
        'name_index' : 1,
        'number_to_create' : 5
    }
}




data = createFreezer('F1', configuration)
print "+" * 20
pprint.pprint(data)
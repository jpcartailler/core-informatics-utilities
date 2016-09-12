# Core Informatics Utilities

## Freezer configuration
A utility for generating configuration data in the form of Excel files is available as a Python (2.7+) script:

`freezer-configuration-generator.py`

The script makes no assumptions about the freezer layout. Any of the following are possible:

> FREEZER > SHELF > RACK > DRAWER > BOX

> FREEZER > SHELF > BIN > BOX

In the first example, one might want to configure 1 freezer, which contains 3 shelves. Each shelf would contain 5 racks, each rack 7 drawers and each drawer 4 boxes.

| | Freezer | Shelf | Rack | Drawer | Box |
| :---: | :---: | :---: | :---: | :---: | :---: |
| # of containers per parent | 1 | 3 | 5 | 7 | 4 |
| Expected container totals | 1 | 3 | 15 |105 | 420 |

The script abstracts out each level into a "container", creating a tree described as c1 > c2 > c3 > c4 where c1 is the parent of c2, etc...
### Input
Currently, the input is setup within the script, but this could eventually be factored out into a config/input file. For the example above, the following configuration would work:

Pick a delimiter - when creating the location names, include a delimiter if desired. For example, F2S3R1D1B4 vs F2-S3-R1-D1-B4:
```python
name_delimiter = '-'
```

If, instead of the concatenated names, all that is needed is the current level name, then set the following to True. i.e. instead of "F2-S3-R1-D1-B4" get only "B4".

```python
name_short = True # True for short names, False for long concatenated names
```

Set up the freezer:
```python
freezer = 'F2'
barcode_freezer = 'FRZ2'
```

Set what containers to parse through:
```python
containers_to_use = ['c1', 'c2', 'c3', 'c4']
```

Lastly, populate the following dictionary in a way that best reflects your environment. Here are definitions of the configuration options:

* **name_prefix** - the human-readable prefix for this level. Example: 'S' for Shelf
* **name_starting_index** - the human-readable container-integer for this level. Example: '1' would be added to 'S' to create 'S1' (Shelf #1).
* **barcode_prefix** - the LIMS-specific barcode for the container type. Example 'SHF' for Shelf.
* **barcode_starting_index** - the LIMS-specific and next-available barcode integer for the container in question. Example: '374' should be added to 'SHF' to create 'SHF374' (LIMS unique barcode identifier for that shelf container)
```python
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
```

### Output
Output (for each level) will need to be 3 columns. Headers are
 - BARCODE
 - NAME
 - LOCATION BARCODE

The values for BARCODE should remain blank, but are there as placeholders for LIMS-generated barcodes. The LOCATION BARCODE is the *parent* entity's barcode. For example, if entering a SHELF, then the LOCATION BARCODE would be
the parent FREEZER barcode.

Example Excel output:

| BARCODE | NAME | LOCATION BARCODE |
| --- | :---: | :---: |
|  | F2S1 | FRZ2 |
|  | F2S2 | FRZ2 |
|  | F2S3 | FRZ2 |

The script will output an individual spreadsheet for *each* level processed. The example above (C1 > C2 > C3 > C4) would generate c1_exceldata.xlsx, c2_exceldata.xlsx, c3_exceldata.xlsx, and c4_exceldata.xlsx.

### Dependencies
The [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) module is required and can easily be installed with
`pip install xlsxwriter`.

# Core Informatics Utilities

## Freezer configuration
A utility for generating configuration data in the form of Excel files is available as a Python (2.7+) script:

`freezer-configuration-generator.py`

Currently, the script assumes the following organization of a FREEZER:

> FREEZER > SHELF > RACK > DRAWER > BOX

Example freezer setup:

| | Freezer | Shelf | Rack | Drawer | Box |
| :---: | :---: | :---: | :---: | :---: | :---: |
| # of containers per parent | 1 | 3 | 5 | 7 | 4 |
| Expect container totals | 1 | 3 | 15 |105 | 420 |


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

## Dependencies
The [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) module is required and can easily be installed with
`pip install xlsxwriter`.

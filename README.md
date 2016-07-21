# Core Informatics Utilities

## Freezer configuration
A utility for generating configuration data in the form of CSV files is available as a Python (2.7+) script:

`freezer-configuration-generator.py`

Currently, the script assumes the following organization of a FREEZER:

> FREEZER > SHELF > RACK > DRAWER > BOX

Output (for each level) will need to be 3 columns. Headers are
 - BARCODE
 - NAME
 - LOCATION BARCODE

The values for BARCODE should remain blank, but are there as placeholders for LIMS-generated barcodes. The LOCATION BARCODE is the *parent* entity's barcode. For example, if entering a SHELF, then the LOCATION BARCODE would be
the parent FREEZER barcode.

Example CSV output:

| BARCODE | NAME | LOCATION BARCODE |
| --- | :---: | :---: |
|  | F2S1 | FRZ2 |
|  | F2S2 | FRZ2 |
|  | F2S3 | FRZ2 |

## Dependencies
The "csv" module is required and comes installed with Python.

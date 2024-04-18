# Noptis Fixer
Fixes errors in the Noptis xml schema (xsd) and generates python code.

## TL;DR;
The fixed schema can be found in static/fixed

A generated python lib from the noptis schema can be found in static/noptis

## Setup
```commandline
pip install -r requirements.txt
```

### Optional
```commandline
sudo apt install yapf
pip install pre-commit
```

## Usage
TL;DR;
```commandline
python noptis_fixer.py
```

By default, it saves schemas and libraries to temp/.

For more information use:
```commandline
python noptis_fixer.py --help
```

### Generate correct xml schema (xsd)
The original schema contains a few errors:
- Uses windows path
- Uses multiple imports (only one allowed in xsd)
- Missing include (because of the incorrect import)

To generate a corrected schema you can use:

```python
import fix_file_errors
fix_file_errors.apply_fixes(
    schema_root_path='path/to/original/files',
    fix_path='where/fixed/files/end/up')
```

Where ```schema_root_path``` is the path to the unzipped folder from noptis webpage.
and ```fix_path``` is the folder to which you wish to write the fixed schema to.

Examples:

```python
import pathlib
import fix_file_errors
fix_file_errors.apply_fixes(
    schema_root_path=pathlib.Path('Downloads/roi/'),
    fix_path=pathlib.Path('fixed/'))
```

### Generate python lib from the schema
To take things even further you could generate python code from the xml schema.

```python
import fix_file_errors
fix_file_errors.generate_library(fixed_files_path='fixed/')
```

Where ```fixed_files_path``` is the path to the folder where the corrected schema files are.
The code generation will not work with the original schema files.

### Bonus: Validate xml file

```python
import pathlib
import fix_file_errors
schema = fix_file_errors.schema_collection(pathlib.Path('fixed/'))
schema.roi_from_pub_trans.validate(pathlib.Path('test/samples/deviation_case_update_event.xml'))
```

## Development
Set up the development environment with the following script:

    ./dev_environment_setup.sh

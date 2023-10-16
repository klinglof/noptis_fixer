import pathlib
import tempfile

import pytest

import download
import fix_file_errors


@pytest.fixture(scope='session')
def temp_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture(scope='session')
def xml_folder():
    return pathlib.Path('samples')


@pytest.fixture(scope='session')
def fixed_files(temp_directory):
    schema_path = pathlib.Path(temp_directory, 'raw')
    download.schema(schema_path)
    fix_path = pathlib.Path('temp', 'fixed')
    fix_file_errors.apply_fixes(schema_path, fix_path)
    yield fix_file_errors.schema_collection(fix_path)


@pytest.fixture(scope='session')
def build_library(temp_directory):
    fix_file_errors.generate_library(pathlib.Path('temp', 'fixed'),
                                     'temp.noptis')


@pytest.fixture(scope='session')
def noptis(build_library):
    import temp.noptis.roi_from_pub_trans
    return temp.noptis.roi_from_pub_trans


@pytest.fixture(scope='session')
def pt_shared(build_library):
    import temp.noptis.ptshared.pt_shared_types
    return temp.noptis.ptshared.pt_shared_types

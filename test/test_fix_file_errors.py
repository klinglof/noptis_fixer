import pathlib
import tempfile

import pytest

import fix_file_errors


@pytest.fixture
def temp_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def xml_folder():
    return pathlib.Path('samples')


@pytest.fixture
def fixed_files(temp_directory):
    schema_path = pathlib.Path('raw')
    fix_path = pathlib.Path(temp_directory)
    fix_file_errors.apply_fixes(schema_path, fix_path)
    yield fix_file_errors.schema_collection(fix_path)


def test_deviation_case_update_event(fixed_files, xml_folder):
    fixed_files.roi_from_pub_trans.validate(
        pathlib.Path(xml_folder, 'deviation_case_update_event.xml'))
    assert fixed_files.roi_from_pub_trans.is_valid(
        pathlib.Path(xml_folder, 'deviation_case_update_event.xml'))


def test_deviation_case_create_event(fixed_files, xml_folder):
    fixed_files.roi_from_pub_trans.validate(
        pathlib.Path(xml_folder, 'deviation_case_create_event.xml'),
        schema_path='//DeviationCaseCreateEvent')
    assert fixed_files.roi_from_pub_trans.is_valid(
        pathlib.Path(xml_folder, 'deviation_case_create_event.xml'),
        schema_path='//DeviationCaseCreateEvent')


def test_publish_decision_event(fixed_files, xml_folder):
    fixed_files.roi_from_pub_trans.validate(
        pathlib.Path(xml_folder, 'publish_decision_event.xml'))
    assert fixed_files.roi_from_pub_trans.is_valid(
        pathlib.Path(xml_folder, 'publish_decision_event.xml'))


def test_deviation_message_version_event(fixed_files, xml_folder):
    fixed_files.roi_from_pub_trans.validate(
        pathlib.Path(xml_folder, 'deviation_message_version_event.xml'))
    assert fixed_files.roi_from_pub_trans.is_valid(
        pathlib.Path(xml_folder, 'deviation_message_version_event.xml'))

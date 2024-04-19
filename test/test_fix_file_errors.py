import pathlib

import fix_file_errors


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


def test_update_incorrect_version():
    result = fix_file_errors.fix_incorrect_schema_version(
        '<xs:schema xmlns:ROI="http://www.pubtrans.com/ROI/3.0" '
        'xmlns:PT="http://www.pubtrans.com/PT/1.0" '
        'xmlns:xs="http://www.w3.org/2001/XMLSchema" '
        'targetNamespace="http://www.pubtrans.com/ROI/3.0" '
        'elementFormDefault="unqualified" '
        'attributeFormDefault="unqualified" version="3.0.8"> '
        '<xs:annotation> <xs:documentation> Version 3.0.9')
    assert result == ('<xs:schema xmlns:ROI="http://www.pubtrans.com/ROI/3.0" '
                      'xmlns:PT="http://www.pubtrans.com/PT/1.0" '
                      'xmlns:xs="http://www.w3.org/2001/XMLSchema" '
                      'targetNamespace="http://www.pubtrans.com/ROI/3.0" '
                      'elementFormDefault="unqualified" '
                      'attributeFormDefault="unqualified" version="3.0.9"> '
                      '<xs:annotation> <xs:documentation> Version 3.0.9')

"""Tests specific examples records for certain data formats to make sure
they validate against the appropriate schema"""
from typing import List
import json
import os

from jsonschema import Draft7Validator, RefResolver

_base_dir = os.path.dirname(__file__)
_schema_path = os.path.join(_base_dir, "..", "schemas")
_format_path = os.path.join(_base_dir, "..", "formats")


def make_validator(format_name: str) -> Draft7Validator:
    """Prepare a validator for a certain format specification

    Args:
        format_name: Name of the data format
    Returns:
        Validator ready to use on certain records
    """

    # Load in the schema
    with open(os.path.join(_format_path, f'{format_name}.json')) as fp:
        schema = json.load(fp)

    # Make the validator
    validator = Draft7Validator(schema, resolver=RefResolver(f'file:///{_schema_path}/', schema))
    return validator


def run_validator(paths: List, validator: Draft7Validator):
    """Test a list of records using a certain validator

    Args:
        paths: List of paths to records for testing
        validator: JSON validator object
    """

    for path in paths:
        with open(path) as fp:
            record = json.load(fp)
        validator.validate(record)


def test_test_record():
    # Get the list of compounds to use
    tests = [os.path.join(_base_dir, 'data', f) for f in ['test_schema.json']]
    validator = make_validator("testRecord")

    run_validator(tests, validator)

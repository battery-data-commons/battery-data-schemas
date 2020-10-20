from jsonschema import Draft7Validator, RefResolver
import json
import glob
import os

# Find all the schemas
schema_path = os.path.abspath('schemas')

# Get a list of the schemas and formats assembled from schemas
schemas = glob.glob(f'{schema_path}/**/*.json', recursive=True)
formats = glob.glob(f'formats/*.json')

# Loop through to make sure they are all valid
for schema in schemas + formats:
    print('Checking {}...'.format(os.path.relpath(schema, '.')), end="")

    # Load in the schema
    with open(schema) as fp:
        schema = json.load(fp)

    # Pull in the references
    validator = Draft7Validator(Draft7Validator.META_SCHEMA,
                                resolver=RefResolver(f'file:///{schema_path}/', schema))
    validator.validate(schema)
    print('OK')

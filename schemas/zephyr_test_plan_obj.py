from flasgger import Schema, fields
from marshmallow import validate
from helpers.schema_validation import Env


class TestSchema(Schema):
    test_plan_key = fields.Str()
    test_type = fields.Str(validate=validate.OneOf(choices={'', 'AUTOMATED', 'automated', 'MANUAL', 'manual'},
                                                   error="value '{input}' is wrong. Should be one of: '{choices}'"))
    test_case_params = fields.Str()


class TestsReportSchema(Schema):
    test_details = fields.Nested(TestSchema(many=True))
    should_add_unexecuted_cases = fields.Bool(default=False, missing=False)
    zephyr_env = fields.Str(required=False, default='prod', validate=Env(exclude=['invalid_env']))


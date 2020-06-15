import operator
from collections import namedtuple
from marshmallow import ValidationError
from marshmallow.validate import Validator


class ErrorTemplates:
    VALID_CHOICES = "Valid choices: {}"
    GREATER_THAN_ZERO = "Should be greater than 0"
    STRING_EQUALS_BOOL = "Should be one of [True, False]"
    INVALID_LENGTH = "error: {item_name} length {cmp} {required}"


class Env(Validator):
    """Validate if env is valid.

    :param list exclude: environments to be excluded from validation.
    """

    def __init__(self, exclude=None):
        self.exclude = exclude

    def __call__(self, value):
        expected_envs = ['dev', 'staging', 'uat', 'prod']
        value = value.lower()
        if value not in expected_envs:
            raise ValidationError(ErrorTemplates.VALID_CHOICES.format(expected_envs))
        return value

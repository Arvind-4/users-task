import os
from django.core.exceptions import ImproperlyConfigured

truthy = ["true", "True", "1", "yes", "y", "on"]


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError as e:
        error_msg = f"Set the {env_variable} environment variable"
        raise ImproperlyConfigured(error_msg) from e


def get_int_env_value(env_variable):
    try:
        return int(get_env_value(env_variable))
    except ValueError as e:
        error_msg = f"Value set for {env_variable} is not integer"
        raise ImproperlyConfigured(error_msg) from e


def get_boolean_env_value(env_variable):
    try:
        return os.environ[env_variable] in truthy
    except KeyError as e:
        error_msg = f"Set the {env_variable} environment variable"
        raise ImproperlyConfigured(error_msg) from e


def get_array_env(env_variable, allowed_values=None):
    env_array = [
        env_item.strip()
        for env_item in get_env_value(env_variable).split(",")
        if env_item.strip()
    ]

    if allowed_values is not None:
        env_array = [env_item for env_item in env_array if env_item in allowed_values]

    return env_array

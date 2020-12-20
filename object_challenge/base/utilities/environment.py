import os

__all__ = ('get_env_var', 'get_env_list')

_PREFIX = 'APP_'


def get_env_var(name, default=None, prefixed=False):
    """ Returns the value of the environment variable with th given name

    :param name: name of environment variable
    :param prefixed whether to add project name prefix to env var or not
    :param default: default value if the environment variable was not set
    :return: value of the given environment variable
    """
    key = f'{_PREFIX if prefixed else ""}{name}'
    return os.environ.get(key, default)


def get_env_list(name, default=None, prefixed=False):
    values = get_env_var(name, default, prefixed)

    if values is None:
        return list()

    if type(values) == list:
        return values

    return [value.strip() for value in values.split(',') if value.strip()]

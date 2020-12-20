import multiprocessing

from object_challenge.base import utilities

HOST = utilities.get_env_var("HOST", "0.0.0.0", True)
PORT = utilities.get_env_var("PORT", "5000", True)

# Gunicorn config
bind = ''.join([HOST, ':', PORT])
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()

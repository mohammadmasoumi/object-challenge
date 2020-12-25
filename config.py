import multiprocessing
import os

HOST = os.environ.get("APP_HOST", "0.0.0.0")
PORT = os.environ.get("APP_PORT", "5000")

# Gunicorn config
bind = ''.join([HOST, ':', PORT])
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()

"""
celery -A celery_app worker -l info
"""

import time
import random
import celery

from celery.utils.log import get_task_logger
from celery_app import app

logger = get_task_logger(__name__)


@app.task(name='tasks.add')
def add(x, y):
    time.sleep(20)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task(ignore_result=True)
def xsum(numbers):
    return sum(numbers)

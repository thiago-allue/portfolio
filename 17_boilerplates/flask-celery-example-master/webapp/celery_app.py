"""
celery -A celery_app worker -l info
"""
import celery


app = celery.Celery(
    name='capp',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['tasks']
)

app.conf.update(
    result_expires=3600,
    enable_utc=True,
    timezone='Europe/London',
)


if __name__ == '__main__':
    app.start()

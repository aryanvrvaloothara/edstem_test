import webbrowser
from time import sleep

from celery import shared_task


@shared_task
def open_tab(urls):
    for url in urls:
        webbrowser.open(url)
        sleep(5)
    return None

from apscheduler.schedulers.blocking import BlockingScheduler
import requests


def job():
    response = requests.get("https://baidu.com", params={}, headers={})
    print(response.content)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', seconds=5*60, kwargs={})
    scheduler.start()

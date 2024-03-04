import schedule 
from schedule import every, repeat
from datetime import time, timedelta, datetime
from time import sleep


def job():
    print("Kinda sus, ngl")

schedule.every().second.do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().minute.at(":40").do(job)
schedule.every().hour.until(time(11, 33, 42)).do(job)
schedule.every().hour.until(timedelta(hours=8)).do(job)

j = schedule.every(1).to(5).seconds.do(job)

counter = 1

while True:
    schedule.run_pending()
    sleep(1)
    counter += 1
    if counter >= 10:
        schedule.cancel_job(j)


# ==============================================
# Decorators

@repeat(every(5).seconds, message="Everyone")
@repeat(every(2).seconds, message="He")
def job2(message):
    print(f"{message} is definetely sus")

# or 
schedule.every().second.do(job2, message="She")

while True:
    schedule.run_pending()
    sleep(1)

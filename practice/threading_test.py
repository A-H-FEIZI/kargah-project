import threading
import time

def task(name, seconds):
    print(f"{name} شروع شد")
    time.sleep(seconds)
    print(f"{name} بعد از {seconds} ثانیه تموم شد")

t1 = threading.Thread(target=task, args=("کار الف", 2))
t2 = threading.Thread(target=task, args=("کار ب", 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("هر دو تموم شدن")
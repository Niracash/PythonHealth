import shutil
import psutil
import os
import datetime
import time

# print(psutil.cpu_percent(60))
# checking if disk space is more than 20% free
def check_disk_usage(disk):
        global free
        du = shutil.disk_usage(disk)
        free = du.free / du.total * 100
        return free > 20
# check if cpu usage is less than 75%
def check_cpu_usage():
        # check cpu usage percent every 1 min
        global usage
        usage = psutil.cpu_percent(60)
        return usage < 75
while True:
    time.sleep(30)
    if not check_disk_usage("/"):
        print(free)
        print("Disk usage is low!")
        # Create file if not exists, write errors in text file with timestamp
        with open("DiskLog.txt", "a") as file:
            timespam = os.path.getmtime("DiskLog.txt")
            date = datetime.datetime.fromtimestamp(timespam)
            file.write("Disk error! Disk usage: {}, Time: {} \n".format(free, date))

    elif not check_cpu_usage():
        print(usage)
        print("CPU usage is high!")
        # Create file if not exists, write errors in text file with timestamp
        with open("CPULog.txt", "a") as file:
            timespam = os.path.getmtime("CPULog.txt")
            date = datetime.datetime.fromtimestamp(timespam)
            file.write("CPU error! CPU Usage: {}, Time: {} \n".format(usage, date))
            
    else:
        print(usage)
        print("Everything is ok!")
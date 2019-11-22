#!/usr/bin/env python3

from crontab import CronTab
import time

cron = CronTab(user = 'siddhant')

time_user = input("Enter time in format(HH:MM): ")
time_snap = time.strptime(time_user, "%H:%M")
hour = time_snap.tm_hour
min = time_snap.tm_min

droplet_id = int(input("Enter the droplet id:"))

print("Setting up the cron job")

job = cron.new(command = '/home/siddhant/magehost/Task_1/snap.py {0}'.format(droplet_id))
job.hour.on(hour)
job.minute.on(min)

for item in cron:
	print(item)

cron.write()


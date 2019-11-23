# magehost

Tasks for magehost

Task 1: DigitalOcean API
1. Study the DigitalOcean API
2. Analyse how snapshots are taken
3. Create a script that takes input as the time of the day to perform snapshot of the droplet. And this script takes a snapshot daily for last 7 days. Deletes any backups older than 7 days.

Task 2: AWS Lightsail API
1. Study the AWS Lightsail API
2. Create a script that takes hostname and lightsail configuration as input and spins up a new lightsail instance with Ubuntu OS, assigns a static IP address, adds a tag 'MageHost' to this instance and takes its snapshot just after creation.

Task submission - 
Task 1 -

1. Change the API token in snap.py
2. Use cron.py to run the script.

Task 2 -
1. Run lightsail.py
2. To change region or blueprintid, edit lightsail.py and enter the values

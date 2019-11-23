#!/usr/bin/env python3

import logging
import boto3
import requests
from botocore.exceptions import ClientError

def create_lightsail_instance(instancenames,availabilityzone,blueprintid,bundleid,tag):

	client = boto3.client('lightsail')
	try:
		response = client.create_instances(instanceNames=instancenames,
				availabilityZone=availabilityzone,
				blueprintId=blueprintid,
				bundleid,
				tags=tag)
	except ClientError as e:
		logging.error(e)
		return None
	return response['operations'][0]

def allocate_static_ip(staticip):
        client = boto3.client('lightsail')
        try:
                response = client.allocate_static_ip(staticIpName=staticip)
        except ClientError as e:
                logging.error(e)
                return None
        return response['operations'][0]


def attach_static_ip(staticip,instancename):
	client = boto3.client('lightsail')
	try:
		response = client.attach_static_ip(staticIpName=staticip,
						instanceName=instancename)
	except ClientError as e:
		logging.error(e)
		return None
	return response['operations'][0]

def create_instance_snapshot(snapshotname,instancename):
	client = boto3.client('lightsail')
	try:
		response = client.create_instance_snapshot(instanceSnapshotName=snapshotname,instanceName=instancename)
	except ClientError as e:
		logging.error(e)
		return None
	return response['operations'][0]

def main():
	instanceNames = []
	instance = input("Enter the name of the instance:")
	instancenames.append(instance)
	availabilityzone = 'ap-south-1a'
	blueprintid = 'ubuntu'
	bundleid = 'micro_1_0'
	tags = []
	tag = {'key':'Name','value':'MageHost'}
	tags.append(tag)
	
	logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s: %(asctime)s: %(message)s')
	
	instance_info = create_lightsail_instance(instancenames,availabilityzone,blueprintid,bundleid,tags)

	if instance_info is not None:
		logging.info(f'Launched Instance: {instance_info["id"]}')
	
	sleep(10)

	staticip = input("Enter the static ip")
	print("Allocating static ip")
	static_info =  allocate_static_ip(staticip)
	if static_info is not None:
		logging.info(f'Status: {static_info["status"]}')

	sleep(5)
	print(f'Attaching static ip to instance {instance}')
	attach_static_ip(staticip,instance)
	sleep(10)
	snapshotname = f' snap {instance} {time.time.now()}'
	print("Creating snapshot")
	snapshot_info = create_instance_snapshot(snapshotname,instancename)

if __name__ == '__main__':
	main()

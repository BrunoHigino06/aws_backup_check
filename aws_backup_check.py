from time import process_time_ns
import boto3
import json

def aws_backup_check():
    client = boto3.client('backup', region_name='sa-east-1')
    response = client.list_backup_jobs(
        MaxResults=1
    )

    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

    database = json.loads(json_response)

    BackupJobId = database['BackupJobs']['BackupJobId']
    
    if BackupJobId in database['BackupJobs']:
        print("Key exist in JSON data")
    else:
        print("Key doesn't exist in JSON data")
        print(database)




aws_backup_check()
import boto3
import json

def aws_backup_check():
    client = boto3.client('backup', region_name='sa-east-1')
    response = client.list_backup_jobs(
        MaxResults=1
    )

    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)
    if json_response is None:
        print("Any backup funded in account: "+json_response['BackupJobs']['AccountId'])
    else:
        print("backup funded in account: "+json_response['BackupJobs']['AccountId'])


aws_backup_check()
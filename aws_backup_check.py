import boto3
import json

def aws_backup_check():
    client = boto3.client('backup', region_name='sa-east-1')
    response = client.list_backup_jobs(
        MaxResults=1
    )

    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

    database = json.loads(json_response)

    for jobId in database['BackupJobs']:
               
        if jobId['BackupJobId']:
            print('exist')
    print('No ID')




aws_backup_check()
import boto3
import json

def aws_backup_check():
    client = boto3.client('backup', region_name='us-east-1')
    response = client.list_backup_jobs(
        MaxResults=1
    )

    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

    f = json.loads(json_response)

    finder = f['BackupJobs']

    if finder is None:
        print("Any backup funded in account: "+json_response['BackupJobs']['AccountId'])
        print(f)
    else:
        print("backup funded in account: ")
        print(f)


aws_backup_check()
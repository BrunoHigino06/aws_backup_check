import boto3
import json

def aws_backup_check():
    client = boto3.client('backup', region_name='sa-east-1')
    response = client.list_backup_jobs(
        MaxResults=1
    )

    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

    database = json.loads(json_response)
    print(database)

    test = True if "BackupJobId" in database["BackupJobs"][0]["BackupJobId"] else False

    print(test)


    



aws_backup_check()
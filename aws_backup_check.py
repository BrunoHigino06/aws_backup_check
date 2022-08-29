import boto3
import json

def aws_backup_check():
    client = boto3.client('backup', region_name='us-east-1')
    response = client.list_backup_jobs(
        MaxResults=1
    )

    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

    database = json.loads(json_response)
    print(database)

    try:
        test = True if "BackupJobId" in database["BackupJobs"][0] else False
        print(test)
    except:
        print('No founded')


    



aws_backup_check()
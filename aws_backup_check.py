import boto3
import json

def aws_backup_check(accountid):
    regions = ["us-east-1", "sa-east-1"]

    for region in regions:

        client = boto3.client('backup', region_name=region)
        response = client.list_backup_jobs(
            MaxResults=1
        )

        json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

        database = json.loads(json_response)
        try:
            test = True if "BackupJobId" in database["BackupJobs"][0] else False
        except:
            print('No backup job found in the region: '+region+' in the account: '+accountid)
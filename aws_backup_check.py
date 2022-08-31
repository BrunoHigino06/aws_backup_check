import boto3
import json

def aws_backup_check(accountid, KEY_ID, ACCESS_KEY, TOKEN):

    regions = ["us-east-1", "sa-east-1"]

    for region in regions:

        organizations = boto3.client('organizations', region_name=region, aws_access_key_id=KEY_ID, aws_secret_access_key=ACCESS_KEY, aws_session_token=TOKEN)
        org_response = organizations.describe_account(
        AccountId=accountid
        )

        org_json = json.dumps(org_response, indent=4, sort_keys=True, default=str)

        org_database = json.loads(org_json)

        accountname = org_database['Account'][0]['Name']

        backup = boto3.client('backup', region_name=region, aws_access_key_id=KEY_ID, aws_secret_access_key=ACCESS_KEY, aws_session_token=TOKEN)
        response = backup.list_backup_jobs(
            MaxResults=1
        )

        json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

        database = json.loads(json_response)
        try:
            test = True if "BackupJobId" in database["BackupJobs"][0] else False
        except:
            print(accountid+','+accountname+','+region+'Não')
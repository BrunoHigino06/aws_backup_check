import boto3
import json

def aws_backup_check(accountid, KEY_ID, ACCESS_KEY, TOKEN):

    regions = ["us-east-1", "sa-east-1"]

    for region in regions:

        backup = boto3.client('backup', region_name=region, aws_access_key_id=KEY_ID, aws_secret_access_key=ACCESS_KEY, aws_session_token=TOKEN)
        response = backup.list_backup_jobs(
            MaxResults=1
        )

        json_response = json.dumps(response, indent=4, sort_keys=True, default=str)

        database = json.loads(json_response)
        try:
            test = True if "BackupJobId" in database["BackupJobs"][0] else False
        except:
            print(accountid+',,'+region+',Não')
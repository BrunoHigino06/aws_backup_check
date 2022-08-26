import boto3

def aws_backup_check():
    client = boto3.client('backup')
    response = client.list_backup_jobs(
        MaxResults=1
    )
    print("Teste response: "+response)


aws_backup_check()
import boto3, logging
from aws_backup_check import aws_backup_check

def sts_session(accountid):

    role_list = ["AWSCloudFormationStackSetExecutionRole","AWSControlTowerExecution","stacksets-exec-46288c5824f5abf8b0d0317def1b12e5"]
    
    for role in role_list:

        role_arn = "arn:aws:iam::"+accountid+":role/"+role

        try:
            sts_client = boto3.client('sts')
            sts_session = sts_client.assume_role(RoleArn=role_arn, RoleSessionName='aws_cli_'+accountid)
            KEY_ID = sts_session['Credentials']['AccessKeyId']
            ACCESS_KEY = sts_session['Credentials']['SecretAccessKey']
            TOKEN = sts_session['Credentials']['SessionToken']
            aws_backup_check(accountid, KEY_ID, ACCESS_KEY, TOKEN)
            logging.info(f'Credenciais temporárias recebidas para {accountid} com a role {role}')
            return KEY_ID, ACCESS_KEY, TOKEN

        except Exception as e:
            logging.info(f'Erro ao acessar {accountid} com a role {role}')
            pass
import boto3, json

def get_accountname(accountid):
    organizations = boto3.client('organizations')
    org_response = organizations.describe_account(
            AccountId=accountid
    )

    org_json = json.dumps(org_response, indent=4, sort_keys=True, default=str)

    org_database = json.loads(org_json)

    accountname = org_database['Account'][0]['Name']
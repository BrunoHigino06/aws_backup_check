from sts_session import sts_session
from aws_backup_check import aws_backup_check

def generate_report():
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())
            aws_backup_check(id, sts_session.KEY_ID, sts_session.ACCESS_KEY, sts_session.TOKEN)

generate_report()
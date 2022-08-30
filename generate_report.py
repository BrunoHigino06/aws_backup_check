from sts_session import sts_session
from aws_backup_check import aws_backup_check

def generate_report():
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())
            aws_backup_check(id, sts_session.key, sts_session.access, sts_session.token)

generate_report()
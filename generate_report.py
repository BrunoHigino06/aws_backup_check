import os
from sts_session import sts_session
from aws_backup_check import aws_backup_check

def generate_report():
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())
            aws_backup_check(id, os.environ["KEY_ID"], os.environ["ACCESS_KEY"], os.environ["TOKEN"])

generate_report()
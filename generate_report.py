import os
from sts_session import sts_session
from aws_backup_check import aws_backup_check

def generate_report():
    print('AccountId,Region,Backup?')
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())

generate_report()
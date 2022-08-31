import os
from sts_session import sts_session

def generate_report():
    print('AccountId,Account Name,Region,Backup?')
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())

generate_report()
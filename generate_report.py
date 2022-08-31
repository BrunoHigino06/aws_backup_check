import os
from sts_session import sts_session

def generate_report():
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())

generate_report()
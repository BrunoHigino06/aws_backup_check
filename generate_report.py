import sts_session
import aws_backup_check

def generate_report():
    with open("accounts.txt") as f:
        for id in f:
            sts_session.sts_session(id.strip())
            aws_backup_check.aws_backup_check(id, sts_session.sts_session.KEY_ID, sts_session.sts_session.ACCESS_KEY, sts_session.sts_session.TOKEN)

generate_report()
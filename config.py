
def find_sensitive_port(logs):
    sensitive_port = [log for log in logs if log[3] in ["22", "23", "3389"]]
    return sensitive_port
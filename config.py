
def find_sensitive_port(logs):
    sensitive_port = [log[1] for log in logs if log[3] in ["22", "23", "3389"]]
    return sensitive_port
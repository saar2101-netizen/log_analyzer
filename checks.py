
def find_external_ip(logs):
    external_ip = [log[1] for log in logs if not log[1].startswith("10.") and not log[1].startswith("192.168")]
    return external_ip

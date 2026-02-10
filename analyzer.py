import checks
import config
import csv

def check_size(logs):
    large_size = [log[1] for log in logs if int(log[-1]) > 5000]
    return large_size


def logs_tags(logs):
    tags_log = [log + ["LARGE"] if int(log[-1]) > 5000 else log + ["NORMAL"] for log in logs]
    return tags_log


def count_requests(logs):
    requests = dict()
    for log in logs:
        s_ip = log[1]
        if s_ip in requests:
            requests[s_ip] += 1
        else:
            requests[s_ip] = 1
    return requests


def port_protocol(logs):
    port_and_protocol = dict()
    for log in logs:
        port = log[3]
        protocol = log[4]
        port_and_protocol[port] = protocol
    return port_and_protocol


def find_suspicions(logs):
    EXTERNAL = checks.find_external_ip(logs)
    SENSITIVE = config.find_sensitive_port(logs)
    LARGE = check_size(logs)
    NIGHT = checks.night_activity(logs)
    s_dict = dict()
    for log in logs:
        lst_suspicions = []
        s_ip = log[1]
        if s_ip in EXTERNAL:
            lst_suspicions.append("EXTERNAL_IP")
        if s_ip in SENSITIVE:
            lst_suspicions.append("SENSITIVE_PORT")
        if s_ip in LARGE:
            lst_suspicions.append("LARGE_PACKET")
        if s_ip in NIGHT:
            lst_suspicions.append("NIGHT_ACTIVITY")
        if lst_suspicions:
            s_dict[s_ip] = lst_suspicions
    return s_dict

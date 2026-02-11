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


import datetime


def find_suspicions(logs):
    s_dict = dict()

    start_time = datetime.time(0, 0, 0)
    end_time = datetime.time(6, 0, 0)
    sensitive_ports = ["22", "23", "3389"]

    for log in logs:
        timestamp_str = log[0]
        s_ip = log[1]
        dst_port = log[3]
        size = int(log[5])

        lst_suspicions = []

        if not s_ip.startswith("10.") and not s_ip.startswith("192.168."):
            lst_suspicions.append("EXTERNAL_IP")

        if dst_port in sensitive_ports:
            lst_suspicions.append("SENSITIVE_PORT")

        if size > 5000:
            lst_suspicions.append("LARGE_PACKET")

        try:
            log_time = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").time()
            if start_time <= log_time <= end_time:
                lst_suspicions.append("NIGHT_ACTIVITY")
        except ValueError:
            pass

        if lst_suspicions:
            if s_ip not in s_dict:
                s_dict[s_ip] = set()

            s_dict[s_ip].update(lst_suspicions)

    final_dict = {}
    for ip, suspicions_set in s_dict.items():
        final_dict[ip] = list(suspicions_set)

    return final_dict



def filtering_suspicions(logs):
    sus_dict = find_suspicions(logs)
    filtered_suspicions = dict()
    for key, value in sus_dict.items():
        if len(value) >= 2:
            filtered_suspicions.update({key: value})
    return filtered_suspicions
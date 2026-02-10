
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
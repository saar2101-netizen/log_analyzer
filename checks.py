import datetime

def find_external_ip(logs):
    external_ip = [log[1] for log in logs if not log[1].startswith("10.") and not log[1].startswith("192.168")]
    return external_ip

def night_activity(logs):
    night_activity = []
    start_time = datetime.datetime.strptime("00:00:00", "%H:%M:%S").time()
    end_time = datetime.datetime.strptime("06:00:00", "%H:%M:%S").time()
    for log in logs:
        date = log[0]
        timestamp = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").time()
        if start_time <= timestamp <= end_time:
            night_activity.append(log[1])
    return night_activity
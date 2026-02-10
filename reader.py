import csv

def load_logs():
    with open("network_traffic.log", "r") as logs:
        return [log for log in csv.reader(logs)]
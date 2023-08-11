
from __future__ import print_function
import time
import json
import os

LOG_FILE_PATH = "/var/log/"
# LOG_FILE_PATH = "/tmp/"
LOG_FILE_NAME = "-awesome-monitoring.log"


def collect_data():
    with open('/proc/stat') as f:
        fields = [float(column) for column in f.readline().strip().split()[1:]]
    first_idle, first_total = fields[3], sum(fields)
    time.sleep(1)
    with open('/proc/stat') as f:
        fields = [float(column) for column in f.readline().strip().split()[1:]]
    second_idle, second_total = fields[3], sum(fields)
    idle_delta, total_delta = second_idle - first_idle, second_total - first_total

    with open('/proc/meminfo') as f:
        mem_total = int(f.readline().strip().split()[1])
        mem_free = int(f.readline().strip().split()[1])
        mem_available = int(f.readline().strip().split()[1])
        mem_buffers = int(f.readline().strip().split()[1])

    utilisation = 100.0 * (1.0 - idle_delta / total_delta)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print(f'{idle_delta} {total_delta}', end=' ')
    print('%5.1f%%' % utilisation, end='\r')
    return {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "util": '%5.1f%%' % utilisation,
            "mem_total": mem_total,
            "mem_free": mem_free,
            "mem_available": mem_available,
            "mem_buffers": mem_buffers,
            }


def append_to_log(new_data: dict):
    date = time.strftime("%y-%m-%d")
    file_name = f'{LOG_FILE_PATH}{date}{LOG_FILE_NAME}'
    print(f'Writing to log "{file_name}"')

    data = []
    if os.path.exists(file_name) and os.stat(file_name).st_size != 0:
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
        except Exception as e:
            print(f'Error reading log file "{file_name}"')

    try:
        data.append(new_data)
    except Exception as e:
        print(f'Error appending to data {data}')
        data = new_data

    print("result:", data)

    try:
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f'Error appending to log file "{file_name}"')


def main():
    data = collect_data()
    if data:
        print(data)
        append_to_log(data)


if __name__ == '__main__':
    main()

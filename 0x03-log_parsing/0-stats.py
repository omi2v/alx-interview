#!/usr/bin/python3
import sys

total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

try:
    for i, line in enumerate(sys.stdin):
        if i > 0 and i % 10 == 0:
            print("Total file size: File size:", total_file_size)
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")

        parts = line.split()
        if len(parts) < 7:
            continue

        ip, _, _, timestamp, _, request, status, size = parts

        if request != "GET" or not request.startswith("/projects/"):
            continue

        try:
            size = int(size)
        except ValueError:
            continue

        total_file_size += size

        try:
            status = int(status)
        except ValueError:
            continue

        if status in status_codes:
            status_codes[status] += 1

except KeyboardInterrupt:
    print("Total file size: File size:", total_file_size)
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


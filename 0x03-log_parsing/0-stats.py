#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys
import signal

file_size = 0
status_codes = {}
line_count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {file_size}")
    for status in sorted(status_codes.keys()):
        print(f"{status}: {status_codes[status]}")


def signal_handler(sig, frame):
    """Handles the SIGINT signal (Ctrl+C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size += int(parts[-1])
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
        except (IndexError, ValueError):
            pass  # Skip lines with invalid format

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()

print_stats()

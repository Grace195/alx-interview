#!/usr/bin/python3

# Define valid status codes
VALID_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables
total_size = 0
line_count = 0
status_code_counts = {code: 0 for code in VALID_STATUS_CODES}

try:
  for line in sys.stdin:
    # Parse the log line
    try:
      ip, date, _, _, status_code, file_size = line.strip().split()
      file_size = int(file_size)
      status_code = int(status_code)
    except ValueError:
      continue  # Skip lines with invalid format

    # Update metrics
    total_size += file_size
    line_count += 1
    status_code_counts[status_code] += 1

    # Print statistics every 10 lines
    if line_count % 10 == 0:
      print(f"Total file size: {total_size}")
      for code, count in sorted(status_code_counts.items()):
        if count > 0:
          print(f"{code}: {count}")
      print()  # Print an empty line for separation

  # Print final statistics on keyboard interrupt
except KeyboardInterrupt:
  print(f"Total file size: {total_size}")
  for code, count in sorted(status_code_counts.items()):
    if count > 0:
      print(f"{code}: {count}")


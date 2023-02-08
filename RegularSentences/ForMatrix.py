import re
import sys

pattern = r"999"

for line in sys.stdin:
    line = line.rstrip()
    duplicate = re.sub(pattern, r"-1", line)
    print(duplicate)
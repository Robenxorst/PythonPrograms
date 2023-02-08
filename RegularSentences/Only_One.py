# В каждой строке замените все вхождения
# нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.

import sys
import re

pattern = r"(\w)\1+"

for line in sys.stdin:
    line = line.rstrip()
    duplicate = re.sub(pattern, r"\1", line)
    print(duplicate)
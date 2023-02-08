import sys
import re

# экранирование обратного слеша
# pattern = r".*\\.*"
# паттерн тандемного повтора
# pattern = r".*\b(.+)\1\b.*"
# паттерн нахождения определенного слова
# pattern = r".*\bcat\b.*"

pattern = r".*\b(.+)\1\b.*"

for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(line)

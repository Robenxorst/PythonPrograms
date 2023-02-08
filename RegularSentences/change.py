# В каждой строке поменяйте местами две первых буквы в каждом слове,
# состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

import sys
import re

# махинации с перестановками букв в словах через группировку
pattern = r"(\b[\W]*)(\w)(\w)"

for line in sys.stdin:
    line = line.rstrip()
    duplicate = re.sub(pattern, r"\1\3\2", line)
    print(duplicate)

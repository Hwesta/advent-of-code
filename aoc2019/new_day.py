#!/usr/bin/python3
import shutil
import stat
import sys
import os

day = sys.argv[1]
dayfile = f'day{day}.rb'

# Copy template
shutil.copy('template.rb', dayfile)
with open(dayfile, 'r') as f:
    contents = f.read()
contents = contents.replace('day##', f'day{day}')
with open(dayfile, 'w') as f:
    f.write(contents)

# Chmod
st = os.stat(dayfile)
os.chmod(dayfile, st.st_mode | stat.S_IEXEC)

# Create input file
with open(f'day{day}.input', 'a') as f:
    os.utime(f'day{day}.input', None)

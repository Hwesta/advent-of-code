#!/usr/bin/python3
import shutil
import stat
import sys
import os

day = sys.argv[1]
dayfile = f'day{day}.py'

# Copy template
shutil.copy('template.py', dayfile)
with open(dayfile, 'r') as f:
    contents = f.read()
contents = contents.replace('day##', f'day{day}')
with open(dayfile, 'w') as f:
    f.write(contents)

# Chmod
st = os.stat(dayfile)
os.chmod(dayfile, st.st_mode | stat.S_IEXEC)

# Add test
with open('test_aoc.py', 'a') as f:
    f.write(f'''
@pytest.mark.parametrize('data,answer,flag', [

])
def test_day_{day}(data, answer, flag):
    assert day{day}.solve(data, flag) == answer
''')

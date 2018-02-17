#!/usr/bin/env ruby
require 'set'

# Based on c, update x and y
def move(char, x, y)
  case char
  when '^'
    x += 1
  when 'v'
    x -= 1
  when '>'
    y += 1
  when '<'
    y -= 1
  end
  [x, y]
end

def solve(data)
  x = y = 0
  visited = Set[[x, y]]
  data.each_char do |c|
    x, y = move(c, x, y)
    visited.add([x, y])
  end
  visited.size
end

def solve2(data)
  sx = sy = rx = ry = 0
  visited = Set[[sx, sy]]
  data.each_char.with_index do |c, i|
    if i.even? # santa
      sx, sy = move(c, sx, sy)
      visited.add([sx, sy])
    else # robosanta
      rx, ry = move(c, rx, ry)
      visited.add([rx, ry])
    end
  end
  visited.size
end

if $PROGRAM_NAME == __FILE__
  data = IO.read('day3.input')

  puts("#{solve(data)} houses receive at least one present.")
  puts("With RoboSanta's help, #{solve2(data)} houses receive at least one present.")
end

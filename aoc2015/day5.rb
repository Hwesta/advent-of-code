#!/usr/bin/env ruby

def solve(data)
  data.each_line.count do |line|
    line.count('aeiou') >= 3 &&
      /(.)\1/.match(line) &&
      line.scan(/ab|cd|pq|xy/).length.zero?
  end
end

def solve2(data)
  data.each_line.count do |line|
    /(..).*\1/.match(line) && /(.).\1/.match(line)
  end
end

if $PROGRAM_NAME == __FILE__
  data = IO.read('day5.input')

  puts "#{solve(data)} strings are nice."
  puts "#{solve2(data)} strings are nice under the better rules."
end

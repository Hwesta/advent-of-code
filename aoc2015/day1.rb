#!/usr/bin/env ruby

def solve1(data)
  floor = 0
  data.each_char do |char|
    if char == '('
      floor += 1
    elsif char == ')'
      floor -= 1
    end
  end
  floor
end

def solve2(data)
  floor = 0
  data.each_char.with_index do |char, i|
    floor += char == '(' ? 1 : -1
    if floor == -1
      return i + 1 # instructions are 1 indexed
    end
  end
end

if $PROGRAM_NAME == __FILE__
  data = IO.read('day1.input')

  puts "Santa goes to floor #{solve1(data)}"
  puts "Santa goes to the basement after #{solve2(data)} instructions"

end

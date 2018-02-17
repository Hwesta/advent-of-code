#!/usr/bin/env ruby

def solve(data)
  data.each_line.sum do |line|
    l, w, h = line.split('x').map(&:to_i)
    min = [l*w, w*h, h*l].min
    # implicit return?
    2 * (l*w + w*h + h*l) + min
  end
end

def solve2(data)
  data.each_line.sum do |line|
    l, w, h = line.split('x').map(&:to_i).sort
    2 * (l + w) + l * w * h
  end
end


if $PROGRAM_NAME == __FILE__
  data = IO.read('day2.input')

  puts "The elves should order #{solve(data)} feet square of wrapping paper."
  puts "The elves should order #{solve2(data)} feet of ribbon."
end

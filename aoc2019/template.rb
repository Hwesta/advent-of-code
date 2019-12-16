#!/usr/bin/env ruby
# frozen_string_literal: true

def solve(input, part2: false)

end

if $PROGRAM_NAME == __FILE__
  input = File.readlines('day##.input').map(&:to_i)
  puts "#{solve(input)}"
  # puts "#{solve(input, part2: true)}"
end

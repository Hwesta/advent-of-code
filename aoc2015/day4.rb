#!/usr/bin/env ruby
require 'digest'

def solve(data, start_with: '00000')
  start = 0
  loop do
    if Digest::MD5.hexdigest(data + start.to_s).start_with?(start_with)
      break start
    end
    start += 1
  end
end

if $PROGRAM_NAME == __FILE__
  data = 'iwrupvqb'

  puts "The lowest number than generates a hash starting with 00000 is #{solve(data)}"
  puts "The lowest number than generates a hash starting with 000000 is #{solve(data, start_with: '000000')}"
end

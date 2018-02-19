#!/usr/bin/env ruby

def update_light(value, action)
  case action
  when 'turn on' then true
  when 'turn off' then false
  when 'toggle' then !value
  end
end

def solve(data)
  lights = []
  (0..999).each do |i|
    lights[i] = [false] * 1000
  end

  data.each_line do |line|
    action, ux, uy, lx, ly = /(.*) (\d+),(\d+) through (\d+),(\d+)/.match(
      line
    )[1..5]

    (ux.to_i..lx.to_i).to_a.product((uy.to_i..ly.to_i).to_a) do |x, y|
      lights[x][y] = update_light(lights[x][y], action)
    end
  end
  lights.flatten.count(true)
end

def update_light2(value, action)
  case action
  when 'turn on' then value + 1
  when 'turn off' then [value - 1, 0].max
  when 'toggle' then value + 2
  end
end


def solve2(data)
  lights = []
  (0..999).each do |i|
    lights[i] = [0] * 1000
  end

  data.each_line do |line|
    action, ux, uy, lx, ly = /(.*) (\d+),(\d+) through (\d+),(\d+)/.match(
      line
    )[1..5]

    (ux.to_i..lx.to_i).to_a.product((uy.to_i..ly.to_i).to_a) do |x, y|
      lights[x][y] = update_light2(lights[x][y], action)
    end
  end
  lights.flatten.sum
end

if $PROGRAM_NAME == __FILE__
  data = IO.read('day6.input').chomp

  puts "#{solve(data)} lights are lit."
  puts "Total light brightness is #{solve2(data)}"
end

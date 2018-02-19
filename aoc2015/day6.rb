#!/usr/bin/env ruby

def update_light(value, action)
  case action
  when 'turn on' then true
  when 'turn off' then false
  when 'toggle' then !value
  end
end

def solve(data)
  lights = Hash.new(false)

  data.each_line do |line|
    # puts line
    action, ux, uy, lx, ly = /(.*) (\d+),(\d+) through (\d+),(\d+)/.match(
      line
    )[1..5]

    (ux..lx).to_a.product((uy..ly).to_a) do |x, y|
      lights[[x, y]] = update_light(lights[[x, y]], action)
    end
  end
  lights.each_value.count(true)
end

def update_light2(value, action)
  case action
  when 'turn on' then value + 1
  when 'turn off' then [value - 1, 0].max
  when 'toggle' then value + 2
  end
end


def solve2(data)
  lights = Hash.new(0)

  data.each_line do |line|
    # puts line
    action, ux, uy, lx, ly = /(.*) (\d+),(\d+) through (\d+),(\d+)/.match(
      line
    )[1..5]

    (ux..lx).to_a.product((uy..ly).to_a) do |x, y|
      lights[[x, y]] = update_light2(lights[[x, y]], action)
    end
  end
  lights.each_value.sum
end

if $PROGRAM_NAME == __FILE__
  data = IO.read('day6.input').chomp

  puts "#{solve(data)} lights are lit."
  puts "Total light brightness is #{solve2(data)}"
end

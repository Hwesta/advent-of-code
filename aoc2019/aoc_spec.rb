# frozen_string_literal: true

require_relative 'day1'
require_relative 'day2'

RSpec.describe 'Advent of Code' do
  describe 'Day 1' do
    context 'part 1' do
      it 'calculates fuel' do
        expect(fuel_for(12)).to eq(2)
      end
      it 'calculates fuel' do
        expect(fuel_for(14)).to eq(2)
      end
      it 'calculates fuel' do
        expect(fuel_for(1969)).to eq(654)
      end
      it 'calculates fuel' do
        expect(fuel_for(100756)).to eq(33583)
      end
    end
    context 'part 2' do
      it 'handles negative numbers' do
        expect(fuel_for(2)).to eq(0)
      end
      it 'calculates all fuel' do
        expect(fuel_for(14, recurse: true)).to eq(2)
      end
      it 'calculates all fuel' do
        expect(fuel_for(1969, recurse: true)).to eq(966)
      end
      it 'calculates all fuel' do
        expect(fuel_for(100756, recurse: true)).to eq(50346)
      end
    end
  end

  describe 'Day 2' do
    context 'part 1' do
      where(:input, :answer) do
        [
          [[1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 3500],
          [[1, 0, 0, 0, 99], 2],
          [[2, 3, 0, 3, 99], 2],
          [[2, 4, 4, 5, 99, 0], 2],
          [[1, 1, 1, 4, 99, 5, 6, 0, 99], 30]
        ]
      end
      with_them do
        it do
          p = ::Program.new(input)
          expect(p.run).to eq answer
        end
      end
    end
    context 'part 2' do
    end
  end
end

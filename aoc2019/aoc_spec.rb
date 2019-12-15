# frozen_string_literal: true

require_relative 'day1'

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
        expect(all_fuel_for(14)).to eq(2)
      end
      it 'calculates all fuel' do
        expect(all_fuel_for(1969)).to eq(966)
      end
      it 'calculates all fuel' do
        expect(all_fuel_for(100756)).to eq(50346)
      end
    end
  end
end

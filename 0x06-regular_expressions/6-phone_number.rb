#!/usr/bin/env ruby
# Regular expression that matches digits of numbers

puts ARGV[0].scan[/^[0-9]{10}$/].join

#!/usr/bash/env ruby
#A regular expression that matches school

puts ARGV[0].scan(/School/).join

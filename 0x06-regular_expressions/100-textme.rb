#!/usr/bin/env ruby

log_line = ARGV[0]

# Extracting relevant information using regular expressions
sender = log_line.scan(/\[from:(.*?)\]/).flatten.first
receiver = log_line.scan(/\[to:(.*?)\]/).flatten.first
flags = log_line.scan(/\[flags:(.*?)\]/).flatten.first

# Outputting the result
puts "#{sender},#{receiver},#{flags}"

#!/usr/bin/env ruby
m = ARGV[0].match(/^\d{10}$/)
puts m[0] if m

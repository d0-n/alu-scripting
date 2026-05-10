#!/usr/bin/env ruby
s = ARGV[0]
if s
  m = s.match(/from:([^\]]+).*to:([^\]]+).*flags:([^\]]+)/)
  puts "#{m[1]},#{m[2]},#{m[3]}" if m
end

#!/usr/bin/env ruby

sender_data = ARGV[0].scan(/\[from:(.+?)\]/).flatten.first || ""
receiver_data = ARGV[0].scan(/\[to:(.+?)\]/).flatten.first || ""
flags = ARGV[0].scan(/\[flags:(.+?)\]/).flatten.first || ""

puts "#{sender_data},#{receiver_data},#{flags}"

#!/usr/bin/ruby

require 'digest'

FILE.foreach('passwords.txt') {|x| puts x}

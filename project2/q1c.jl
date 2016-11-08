#!/usr/bin/env julia

b = [0; 1; 1]
A = [0 0 1; 
     0 1 0;
     1 0 1]
println(abs(A\b))

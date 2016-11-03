#!/usr/bin/julia

b = [0; 0; 0; 0; 0; 1]
A = [1 1 1 1 1 1;
     1 1 1 1 1 0;
     1 1 1 1 0 0;
     1 1 1 0 0 0;
     1 1 0 0 0 0;
     1 0 0 0 0 0]
println("question 2.11.2")
println(abs(A\b))

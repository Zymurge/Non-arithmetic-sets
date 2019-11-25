# Non-Arithemtic Sets #

## A program to solve a problem that I found im a book titled Mensa Mind Challenges. ##

**The problem** (*my paraphrasing*): given the set of integers from 1 to 20 inclusive, find 
9 unique members such that no 3 selections from that group form an arithmetic sequence. 

Specifically, 3 numbers could not be any of: `1,2,3` or `4,7,10` or `7,10,13` or `2,9,17`
Put another way, given 3 integers `a,b,c` where `a < b < c` then `b - a` does not equal `c - b`

My original intention is to submit this to [CodeWars](http://codewars.com) as my first authored problem. My first
solution is in Python. 

Potential variant problems of increasing difficulty:
- Given an array of unique numbers, test whether there are 3 or more that form an arithmetic sequence
- Starting with 1, find the lowest possible value for the nth integer in a non-arithmetic set
- Solve for dynamic mixes of number integers to form a sequence, total number to solve, find the most
  possible in a set ranging from x to y, etc.
# Non-Arithmetic Sets #

## A program to solve a problem that I found in a book titled [Giant Book of Mensa Mind Challenges](https://www.amazon.com/Giant-Book-Mensa-Mind-Challenges/dp/1402710496). ##

**The problem** (*my paraphrasing*): given the set of integers from 1 to 20 inclusive, find 
9 unique members such that no 3 selections from that group form an arithmetic sequence. 

Specifically, the solution set could not include all three of: `1,2,3` or `4,7,10` or `7,10,13` or `2,9,17`

Mathematically, a Non-Arithmetic Sequence can be described as:
- Given three integers `a,b,c` where `a < b < c` then `b - a` must not equal `c - b`

My original intention is to submit this to [CodeWars](http://codewars.com) as my first authored problem. My first
solution is in Python. 

Potential variant problems of increasing difficulty:
- Given an array of unique numbers, test whether there are 3 or more that form an arithmetic sequence
- Starting with 1, find the lowest possible value for the nth integer in a non-arithmetic set
- Find a set of 9 in the numbers from 1 to 20 (*the problem defined in the book*)
- Solve for dynamic mixes of number integers to form a sequence, total number to solve, find the most
  possible in a set ranging from x to y, etc.

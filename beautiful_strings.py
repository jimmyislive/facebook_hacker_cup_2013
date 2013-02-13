#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Beautiful strings
=================

When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it.

The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

Input
The input file consists of a single integer m followed by m lines.
Output
Your output should consist of, for each test case, a line containing the string "Case #x: y" where x is the case number (with 1 being the first case in the input file, 2 being the second, etc.) and y is the maximum beauty for that test case.
Constraints
5 ≤ m ≤ 50
2 ≤ length of s ≤ 500

Example input
--------------
5
ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves

Example output
---------------
Case #1: 152
Case #2: 754
Case #3: 491
Case #4: 729
Case #5: 646
'''

import string
import sys

def find_beauty_score(str):
    d = {}
    bs = 0

    for char in str:
        if char in string.letters:
            try:
                d[char.lower()] += 1
            except KeyError:
                d[char.lower()] = 1

    repetitions = d.values()
    repetitions.sort(reverse=True)

    multiplier = 26
    for rep in repetitions:
        bs += rep*multiplier
        multiplier -= 1

    return bs

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    m = int(f.readline().strip())
    for i in range(1,m+1):
        bs = find_beauty_score(f.readline().strip())
        print 'Case #%d: %d' % (i, bs)



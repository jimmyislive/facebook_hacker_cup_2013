#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Balanced Smileys
================

Your friend John uses a lot of emoticons when you talk to him on Messenger. In addition to being a person who likes to express himself through emoticons, he hates unbalanced parenthesis so much that it makes him go :(

Sometimes he puts emoticons within parentheses, and you find it hard to tell if a parenthesis really is a parenthesis or part of an emoticon.

A message has balanced parentheses if it consists of one of the following:

- An empty string ""
- One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
- An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'.
- A message with balanced parentheses followed by another message with balanced parentheses.
- A smiley face ":)" or a frowny face ":("
Write a program that determines if there is a way to interpret his message while leaving the parentheses balanced.

Input
------
The first line of the input contains a number T (1 ≤ T ≤ 50), the number of test cases. 
The following T lines each contain a message of length s that you got from John.

Output
-------
For each of the test cases numbered in order from 1 to T, output "Case #i: " followed by a string stating whether or not it is possible that the message had balanced parentheses. If it is, the string should be "YES", else it should be "NO" (all quotes for clarity only)

Constraints
------------
1 ≤ length of s ≤ 100

Example input
--------------
5
:((
i am sick today (:()
(:)
hacker cup: started :):)
)(

Example output
---------------
Case #1: NO
Case #2: YES
Case #3: YES
Case #4: YES
Case #5: NO

'''

import copy
import sys


def is_balanced_smiley(str, stack=[]):

    stack = copy.deepcopy(stack)

    for i in range(len(str)):
        if str[i] == ')':
            try:
                stack.pop()
            except IndexError:
                return 'NO'
        if str[i] == ':':
            #if ':' is last char
            if len(str) == i + 1:
                continue
            #if ':' is followed by some other char
            elif len(str) > (i + 1) and str[i+1] not in ['(', ')']:
                continue

            #ignore ':'
            if is_balanced_smiley(str[i+1:], stack) == 'YES':
                return 'YES'

            #consider ':'['('|')']
            try:
                if is_balanced_smiley(str[i+2:], stack) == 'YES':
                    return 'YES'
            except IndexError:
                if not stack:
                    return 'YES'
                else:
                    return 'NO'

            return 'NO'

        if str[i] == '(':
            stack.append('(')

    if not stack:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    m = int(f.readline().strip())
    for i in range(1,m+1):
        print 'Case #%d: %s' % (i, is_balanced_smiley(f.readline().strip(), []))


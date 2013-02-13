#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Find the Min
============

After sending smileys, John decided to play with arrays. Did you know that hackers enjoy playing with arrays? John has a zero-based index array, m, which contains n non-negative integers. However, only the first k values of the array are known to him, and he wants to figure out the rest.

John knows the following: for each index i, where k <= i < n, m[i] is the minimum non-negative integer which is *not* contained in the previous *k* values of m.

For example, if k = 3, n = 4 and the known values of m are [2, 3, 0], he can figure out that m[3] = 1.

John is very busy making the world more open and connected, as such, he doesn't have time to figure out the rest of the array. It is your task to help him.

Given the first k values of m, calculate the nth value of this array. (i.e. m[n - 1]).

Because the values of n and k can be very large, we use a pseudo-random number generator to calculate the first k values of m. Given positive integers a, b, c and r, the known values of m can be calculated as follows:

m[0] = a
m[i] = (b * m[i - 1] + c) % r, 0 < i < k

Input
------
The first line contains an integer T (T <= 20), the number of test cases.
This is followed by T test cases, consisting of 2 lines each.
The first line of each test case contains 2 space separated integers, n, k (1 <= k <= 105, k < n <= 109).
The second line of each test case contains 4 space separated integers a, b, c, r (0 <= a, b, c <= 109, 1 <= r <= 109).

Output
-------
For each test case, output a single line containing the case number and the nth element of m.

Example input
--------------
5
97 39
34 37 656 97
186 75
68 16 539 186
137 49
48 17 461 137
98 59
6 30 524 98
46 18
7 11 9 46

Example output
--------------
Case #1: 8
Case #2: 38
Case #3: 41
Case #4: 40
Case #5: 12


'''

import sys

def cal_next_val(prev, b, c, r):
     return (b * prev + c) % r

def find_min(n, k, a, b, c, r):

    start_through_k = [a]
    prev = a

    for i in range(1,k):
        next = cal_next_val(prev, b, c, r)
        start_through_k.append(next)
        prev = next

    d = {}
    repeated_pattern = []
    while True:
        smallest = min(start_through_k)
        if smallest > 0:
            new_ele = smallest - 1
        else:
            new_ele = 1
            while new_ele in start_through_k:
                new_ele += 1

        if d.has_key(new_ele):
            break
        else:
            d[new_ele] = True
        start_through_k = start_through_k[1:]
        start_through_k.append(new_ele)
        repeated_pattern.append(new_ele)
        

    repeated_pattern_len = len(repeated_pattern)
    remaining_len = n - k
    target_len = remaining_len - repeated_pattern_len
    if target_len < repeated_pattern_len:
        return repeated_pattern[target_len - 1]
    else:
        if target_len % repeated_pattern_len == 0:
            return repeated_pattern[-1]
        else:
            return repeated_pattern[(target_len % repeated_pattern_len) - 1]

def _make_int(x):
    return int(x.strip())

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    m = int(f.readline().strip())
    for i in range(1,m+1):

        n, k = f.readline().strip().split(' ')
        n = _make_int(n)
        k = _make_int(k)

        a, b, c, r = f.readline().strip().split(' ')
        a = _make_int(a)
        b = _make_int(b)
        c = _make_int(c)
        r = _make_int(r)

        print 'Case #%d: %s' % (i, find_min(n, k, a, b, c, r))





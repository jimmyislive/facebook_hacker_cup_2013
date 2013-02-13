#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Card Game
=========

John is playing a game with his friends. The game's rules are as follows: There is deck of N cards from which each person is dealt a hand of K cards. Each card has an integer value representing its strength. A hand's strength is determined by the value of the highest card in the hand. The person with the strongest hand wins the round. Bets are placed before each player reveals the strength of their hand.

John needs your help to decide when to bet. He decides he wants to bet when the strength of his hand is higher than the average hand strength. Hence John wants to calculate the average strength of ALL possible sets of hands. John is very good at division, but he needs your help in calculating the sum of the strengths of all possible hands.

Problem
You are given an array a with N ≤ 10 000 different integer numbers and a number, K, where 1 ≤ K ≤ N. For all possible subsets of a of size K find the sum of their maximal elements modulo 1 000 000 007.

Input
The first line contains the number of test cases T.

Each case begins with a line containing integers N and K. The next line contains N space-separated numbers 0 ≤ a [i] ≤ 2 000 000 000, which describe the array a.

Output
For test case i, numbered from 1 to T, output "Case #i: ", followed by a single integer, the sum of maximal elements for all subsets of size K modulo 1 000 000 007.

Example
For a = [3, 6, 2, 8] and N = 4 and K = 3, the maximal numbers among all triples are 6, 8, 8, 8 and the sum is 30.

Input
======
5
4 3
3 6 2 8 
5 2
10 20 30 40 50 
6 4
0 1 2 3 5 8 
2 2
1069 1122 
10 5
10386 10257 10432 10087 10381 10035 10167 10206 10347 10088 

Output
======
Case #1: 30
Case #2: 400
Case #3: 103
Case #4: 1122
Case #5: 2621483

'''

import sys
import itertools

def card_game2(a,k):
    x = itertools.combinations(a,k)
    m = []
    for arr in x:
        m.append(max(arr))

    return m

def stringify(arr):
    a = ''
    for ele in sorted(arr):
        a += str(ele)
    return a

def card_game(k,a, arr=[], maximal_arr=[], seen=[]):
    if len(arr) == k:
        str_arr = stringify(arr)
        if str_arr not in seen:
            #print str_arr
            #print seen
            #print arr
            maximal_arr.append(max(arr))
            seen.append(str_arr)
        #else:
        #    print 'appending ' + str_arr
        #    seen.append(str_arr)
    else:
        for i in range(len(a)):
            #arr.append(a[i])
            maximal_arr, seen = card_game(k,a[:i]+a[i+1:], arr + [a[i]], maximal_arr, seen)
            #arr.pop()

    return maximal_arr, seen

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    m = int(f.readline().strip())
    for i in range(1,m+1):
        n, k = f.readline().strip().split(' ')
        n = int(n)
        k = int(k)

        a = []
        arr = f.readline().strip().split(' ')
        for ele in arr:
            a.append(int(ele))
        #print n,k,a
        #maximal_arr, ignore = card_game(k,a, [], [], [])
        maximal_arr = card_game2(a,k)
        s = sum(maximal_arr)
        #print s % 1000000007
        print 'Case #%d: %d' % (i, s % 1000000007)



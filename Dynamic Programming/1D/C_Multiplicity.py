"""
C. Multiplicity

time limit per test3 seconds
memory limit per test256 megabytes
You are given an integer array a1,a2,…,an
.

The array b
 is called to be a subsequence of a
 if it is possible to remove some elements from a
 to get b
.

Array b1,b2,…,bk
 is called to be good if it is not empty and for every i
 (1≤i≤k
) bi
 is divisible by i
.

Find the number of good subsequences in a
 modulo 109+7
.

Two subsequences are considered different if index sets of numbers included in them are different. 
That is, the values ​of the elements ​do not matter in the comparison of subsequences. In particular, the array a

 has exactly 2n−1
 different subsequences (excluding an empty subsequence).

Input
The first line contains an integer n
 (1≤n≤100000
) — the length of the array a
.

The next line contains integers a1,a2,…,an
 (1≤ai≤106
).

Output
Print exactly one integer — the number of good subsequences taken modulo 109+7

Examples
Input
2
1 2

Output
3

Input
5
2 2 1 22 14
Output
13

"""
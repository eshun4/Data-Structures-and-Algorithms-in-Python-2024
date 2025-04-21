
"""
Let n
 be an integer. Consider all permutations on integers 1
 to n
 in lexicographic order, and concatenate them into one big sequence p
. For example, if n=3
, then p=[1,2,3,1,3,2,2,1,3,2,3,1,3,1,2,3,2,1]
. The length of this sequence will be n⋅n!
.

Let 1≤i≤j≤n⋅n!
 be a pair of indices. We call the sequence (pi,pi+1,…,pj−1,pj)
 a subarray of p
. Its length is defined as the number of its elements, i.e., j−i+1
. Its sum is the sum of all its elements, i.e., ∑jk=ipk
.

You are given n
. Find the number of subarrays of p
 of length n
 having sum n(n+1)2
. Since this number may be large, output it modulo 998244353
 (a prime number).

Input
The only line contains one integer n
 (1≤n≤106
), as described in the problem statement.

Output
Output a single integer — the number of subarrays of length n
 having sum n(n+1)2
, modulo 998244353
.

Input
3
Output
9

Input
4
Output
56

"""
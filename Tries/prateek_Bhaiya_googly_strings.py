"""
Prateek Bhaiya & Googly Strings!
Prateek bhaiya while working at Google often encounters string problems, so this time he is asking for your help to solve this problem. You are given a list of non-empty strings and you have to return a list of all "Googly" strings found in the input list.

A string is said to be Googly if it is exactly made up of atleast two instances of other string in the input list of strings.

In order for a string to be googly, just containing two instances of other strings isn't sufficient, the string be exactly made up of those strings. For example, in the list ["a", "b", "abc"] the string "abc" isn't googly, even though it contains "a" and "b", but "c" isn't a string in the list.


Note that strings can be repeated to form a special string; for example in the list ["a","aaa"], the string "aaa" is a Googly string because it is made up of three repeated instances of "a".

Sample Input

["goo", "gle", "google", "le","googly","ly","g",""googoole"]


Sample Output

["gle", "google", "googly","googoole"]
Explanation


gle = "g" + "le"

google = "goo" + "g" + "le"

googly = "goo" + "g" + "ly"

googoole = "goo" + "goo" + "le"

All these strings contains atleast 2 instances of other strings in the list.
"""
"""
Phone Numbers Search
You are given a Android Phone smart keypad which looks exactly like the one shown below. No, its not the regular phone keypad problem! 😉

   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----
As we can see every digit is associated with some letters, for example 2 is mapped with (a,b,c). This allowes certain phone numbers to be mapped with actual words. For example - the phone number 666 can be written as mom  or moo. Similarly, 7728335  can be written as prateek or something other string as well. Hence, a given phone number can represent multiple possible strings.

You are given a phone number (as a string input) and a non-empty list of words. Write a function that returns the list of words that can be found in the phone number. The final list can contain words in any order. (Yes, we will use sorting at the backend to compare your result with ours😉)

Sample Input

phoneNumber = "7728335"
words = {"prat","prateek","codingminutes","code","prat335", "teek"};
Sample Output
["prat", "prateek", "teek"]

(can be in any order)


Hint

Try to optimise this problem using Trie Data Structure + Unordered Set.
"""
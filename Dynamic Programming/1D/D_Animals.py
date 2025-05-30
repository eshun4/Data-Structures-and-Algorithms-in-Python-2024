"""
D. Animals
time limit per test2 seconds
memory limit per test64 megabytes
inputinput.txt
outputoutput.txt
Once upon a time DravDe, an outstanding person famous for his professional achievements (as you must remember, he works in a warehouse storing Ogudar-Olok, a magical but non-alcoholic drink) came home after a hard day. That day he had to drink 9875 boxes of the drink and, having come home, he went to bed at once.

DravDe dreamt about managing a successful farm. He dreamt that every day one animal came to him and asked him to let it settle there. However, DravDe, being unimaginably kind, could send the animal away and it went, rejected. There were exactly n days in DravDe’s dream and the animal that came on the i-th day, ate exactly ci tons of food daily starting from day i. But if one day the animal could not get the food it needed, it got really sad. At the very beginning of the dream there were exactly X tons of food on the farm.

DravDe woke up terrified...

When he retold the dream to you, he couldn't remember how many animals were on the farm by the end of the n-th day any more, but he did remember that nobody got sad (as it was a happy farm) and that there was the maximum possible amount of the animals. That’s the number he wants you to find out.

It should be noticed that the animals arrived in the morning and DravDe only started to feed them in the afternoon, so that if an animal willing to join them is rejected, it can’t eat any farm food. But if the animal does join the farm, it eats daily from that day to the n-th.

Input
The first input line contains integers n and X (1≤n≤100,1≤X≤104) — amount of days in DravDev's dream and the total amount of food (in tons) that was there initially. The second line contains integers ci (1 ≤ ci ≤ 300). Numbers in the second line are divided by a space.

Output
Output the only number — the maximum possible amount of animals on the farm by the end of the n-th day given that the food was enough for everybody.

Examples
Input
3 4
1 1 1

Output
2

Input
3 6
1 1 1

Output
3
"""
def newspapers_split(newspapers_read_times: list[int], num_coworkers: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    1. What is the question asking for?
    minimum time needed to read all newspapers.
    2. What is a possible candidate for an answer?
    A guess of a sum limit. We can call k.
    3. What is the lowest possible sum limit we can start our guess from?
    e.g. if we have [7,2,5,10,8] the lowest read time we can have is the one that 
    the fits the maximum news paper read time in the array. in this case max(newpapers_read_times)
    4. What is the highest possible sum limit we can end our guess?
    e.g. looking at the array [7,2,5,10,8] the highest possible guess should be a value that any value 
    beyond that highest still gives us the same minimum time for the number of workers provided.
    Say, we take the sum of the array of the numbers [7, 2, 5, 10, 8] = 32. Now, say we have a guess of
    39, if we assign first element to the first worker so 7 and then the remaining to worker 2 so 25 we 
    can still get minim sum limit that us still less than this value so in other sense, just use the total of the 
    newspaper read times.
    5. Walkthrough and pseudocode:

    [7,2,5,10,8] , num_of_worker = 2 

    def check_guess(k):
        time_so_far = 1
        current_sum_newspaper_read_times = 0 
        for read_time in newspaper_read_times:
            if current_sum_newspaper_read_times + read_time <= k:
                current_sum_newspaper_read_times += read_time
            else:
                current_sum_newspaper_read_times = num 
                time_so_far += 1 
        return time_so_far <= num_of_worker

    # get the left and right pointers for our sreach
    left, right = max(newspapers_read_times), sum(newspapers_read_times)
    # a sum limit variable for to return our result
    sum_limit = -1
    # iterate through our answer search space which in this case is our guess
    while left <= right:
        mid = (left + right) // 2 
        if check_geuess(mid):
            sum_limit = mid 
            right = mid - 1 
        else:
            left = mid + 1 
    return sum_limit

    6. Time complexity for helper function is O(n) and for the binary search is O(logn)
    Space is also: O(1) for both the helper and the search function. 
    """

    def check_guess(k):
        time_so_far = 1
        current_sum_newspaper_read_times = 0 
        for read_time in newspapers_read_times:
            if current_sum_newspaper_read_times + read_time <= k:
                current_sum_newspaper_read_times += read_time
            else:
                current_sum_newspaper_read_times = read_time
                time_so_far += 1 
        return time_so_far <= num_coworkers

    # get the left and right pointers for our sreach
    left, right = max(newspapers_read_times), sum(newspapers_read_times)
    # a sum limit variable for to return our result
    sum_limit = -1
    # iterate through our answer search space which in this case is our guess
    while left < right:
        mid = (left + right) // 2 
        if check_guess(mid):
            # sum_limit = mid 
            right = mid - 1 
        else:
            left = mid 
    return sum_limit
    

if __name__ == "__main__":
    newspapers_read_times = [int(x) for x in input().split()]
    num_coworkers = int(input())
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)

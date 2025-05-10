"""
Housing Problem.

Along one side of a road there is a sequence vacant plots of land. 

Each plot has a different area. So the areas form a sequence A[1], A[2], ... A[N].

You want to buy K acres of land to build a house. You want to find all segments of contiguous plots.
(i.e. a subsection in the sequence) of whose sum is exactly K. 

"""


def housing(houses, k):
    n = len(houses)
    i, j  = 0, 0
    current_sum = 0
    result = []

    while j < n:
        current_sum += houses[j]
        j += 1

        # Shrink the window from the left if the sum exceeds k
        while current_sum > k and i < j:
            current_sum -= houses[i]
            i += 1

        # If the sum equals k, store the start and end indices
        if current_sum == k:
            result.append((i, j - 1))

    return result


def main():
    houses = [1, 3, 2, 1, 4, 1, 3, 2, 1, 1]
    k = 8
    print("Segments with sum equal to", k, ":", housing(houses, k))


if __name__ == '__main__':
    main()
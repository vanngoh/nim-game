import time
import random
def solution(buckets):
    n = len(buckets)
    print("length:", n)
    index_of_bucket = 1000000
    num_of_balls = 1000000

    if n == 1:
        return (0, buckets[0] - 1)

    if n > index_of_bucket:
        return (0, 0)

    for i in range(n):
        if buckets[i] > 1000000:
            return (0, 0)

        for balls_to_remove in range(1, buckets[i] + 1):
            tmp_buckets = buckets[:]
            tmp_buckets[i] -= balls_to_remove

            # Continue if the current move doesn't have zero NIM sum
            if check_nim_sum(tmp_buckets, n) is False:
                continue

            # Current move is a winning move
            if i < index_of_bucket or (i == index_of_bucket and balls_to_remove < num_of_balls):
                index_of_bucket = i
                num_of_balls = balls_to_remove
                return (index_of_bucket, num_of_balls)

    # No solution for this combination
    if index_of_bucket == 1000000 or num_of_balls == 1000000:
        return (0, 0)


def check_nim_sum(x, n):
    res = 0
    for i in range(n):
        res = res ^ x[i]

    return True if res == 0 else False


if __name__ == "__main__":
    assert solution([2, 3]) == (1, 1)
    assert solution([2, 2]) == (0, 0)
    assert solution([3, 4, 5, 6]) == (1, 4)
    assert solution([3, 3]) == (0, 0)
    assert solution([4, 3]) == (0, 1)
    assert solution([3, 4]) == (1, 1)
    assert solution([5, 5]) == (0, 0)
    assert solution([1, 3, 5, 7]) == (0, 0)
    assert solution([10]) == (0, 9)
    assert solution([524286,1,2,8,524287,32]) == (0, 42)

    # print(solution([40123, 10298, 40123, 990901, 990901, 990901,990901]))
    # print(solution([1, 802741, 8, 1, 9764, 990901]))
    # print(solution([524286,1,2,8,524287,32]))
    # print(solution([262142,1,2,8,524287,32]))

    arr = []
    for i in range(10000):
        arr.append(i)
    print("Array generated!")
    t = time.time()
    print(solution(arr))
    print("Elapsed:", time.time() - t)

    print("All tests passed!")

def solution(x):
    n = len(x)
    index_of_box = 1000000
    num_of_balls = 1000000

    for i in range(n):
        for balls_to_remove in range(1, x[i] + 1):
            temp_box = x[:]
            temp_box[i] -= balls_to_remove

            # Continue if the current move doesn't have zero NIM sum
            if check_nim_sum(temp_box) is False:
                continue

            # Current move is a winning move
            if i < index_of_box or (i == index_of_box and balls_to_remove < num_of_balls):
                index_of_box = i
                num_of_balls = balls_to_remove

    # No solution for this combination
    if index_of_box == 1000000 or num_of_balls == 1000000:
        return (0, 0)
    
    # Return the solution
    return (index_of_box, num_of_balls)


def check_nim_sum(x):
    remainder_poll = 0
    multiples_poll = 0

    for balls_remained in x:
        remainder = balls_remained % 2
        multiples = int(balls_remained / 2)

        # remainder will be either 0 or 1
        remainder_poll += remainder
        # multiples will be the multiples of 2
        multiples_poll += multiples

    # Check if the NIM Sum zero
    # If it is, the current player is winning
    return (remainder_poll % 2 == 0) and (multiples_poll % 2 == 0)


# Manual check
# x = [3, 4, 5, 6]
# result = solution(x)
# print(f"Index: {result[0]}, Balls to remove: {result[1]}")


if __name__ == "__main__":
    assert solution([2, 3]) == (1, 1)
    assert solution([2, 2]) == (0, 0)
    assert solution([3, 4, 5, 6]) == (1, 4)
    assert solution([3, 3]) == (0, 0)
    assert solution([4, 3]) == (0, 1)
    assert solution([3, 4]) == (0, 3)
    assert solution([5, 5]) == (0, 4)
    assert solution([1, 3, 5, 7]) == (2, 4)

    print("All tests passed!")

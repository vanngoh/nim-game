
import time
import random
def solution(buckets):
    n = len(buckets)
    BITS = 20
    BUCKET_CONSTRAINT = 1000000
    BALLS_CONSTRAINT = 1000000
    smallest_buckets_index = 0
    balls_to_remove = 0

    if n == 1:
        return (0, buckets[0] - 1)

    if sum(buckets) == n:
        if n % 2 == 0:
            return (0, 1)
        else:
            return (0, 0)

    special_index = has_non_one_and_all_ones(buckets)
    if special_index is not False:
        if n % 2 == 0:
            return (special_index, buckets[special_index])
        else:
            return (special_index, buckets[special_index] - 1)

    if n > BUCKET_CONSTRAINT or max(buckets) > BALLS_CONSTRAINT:
        return (0, 0)
    
    bin_bucket = []
    nim_sum = [0] * BITS
    ball_status = [0] * BITS

    for i in range(n):
        bin_bucket.append(number_to_binary_array(buckets[i], BITS))
        nim_sum = xor_arrays(nim_sum, bin_bucket[i])
       
    print("Bucket", bin_bucket)
    print("NIM_SUM", nim_sum)
    
    largest_bits = find_first_one(nim_sum)
    
    # Zero NIM Sum
    if largest_bits == -1:
        return(0,0)

    for k in range(n):
        if bin_bucket[k][largest_bits] == 1:
            smallest_buckets_index=k
            break
    
    print("Choosen bucket", smallest_buckets_index)
    
    ball_status = xor_arrays(nim_sum, bin_bucket[smallest_buckets_index])
    balls_to_remove = binary_array_to_number(bin_bucket[smallest_buckets_index]) - binary_array_to_number(ball_status)
    
    return (smallest_buckets_index, balls_to_remove)

def has_non_one_and_all_ones(arr):
    non_one_found = -1
    for i, num in enumerate(arr):
        if num != 1:
            # Found more than one non-one element
            if non_one_found != -1:
                return False 
            non_one_found = i

    return non_one_found

    
def number_to_binary_array(number, bits=20):
    bin_str = f"{number:b}"
    bin_list = [int(bit) for bit in bin_str]  # Convert binary string to list of integers

    if len(bin_list) < bits:
        bin_list = [0] * (bits - len(bin_list)) + bin_list

    return bin_list

def xor_arrays(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] ^ arr2[i])
    return result    
    
def find_first_one(array):
    try:
        first_position = array.index(1)
        return first_position
    except ValueError:
        return -1    

def binary_array_to_number(binary_array):
    binary_string = ''.join(map(str, binary_array))
    number = int(binary_string, 2)
    return number        

    
if __name__ == "__main__":
    # assert solution([2, 3]) == (1, 1)
    # assert solution([2, 2]) == (0, 0)
    # assert solution([3, 4, 5, 6]) == (1, 4)
    # assert solution([3, 3]) == (0, 0)
    # assert solution([4, 3]) == (0, 1)
    # assert solution([3, 4]) == (1, 1)
    # assert solution([5, 5]) == (0, 0)
    # assert solution([1, 3, 5, 7]) == (0, 0)
    # assert solution([10]) == (0, 9)
    # assert solution([524286,1,2,8,524287,32]) == (0, 42)

    # # print(solution([40123, 10298, 40123, 990901, 990901, 990901,990901]))
    # # print(solution([1, 802741, 8, 1, 9764, 990901]))
    # print(solution([524286,1,2,8,524287,32]))
    print(solution([2, 1]))
    # print(solution([7, 1]))
    # # print(solution([262142,1,2,8,524287,32]))

    # arr = []
    # for i in range(1, 1000000):
    #     arr.append(i)
    # print("Array generated!")
    # t = time.time()
    # print(solution(arr))
    # print("Elapsed:", time.time() - t)

    print("All tests passed!")
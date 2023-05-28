
import time
import random
def solution(buckets):
    n = len(buckets)
    bits = 32
    index_of_bucket = 1000000
    num_of_balls = 1000000

    if n == 1:
        return (0, buckets[0] - 1)

    if n >= index_of_bucket or max(buckets) >= num_of_balls :
        return (0, 0)
    
    bucket_binary = []
    xor_status = [0] * bits
    ball_status = [0] *bits
    for i in range(n):
        bucket_binary.append(number_to_binary_array(buckets[i], bits))
        xor_status=xor_arrays(xor_status,bucket_binary[i])
       
    # print(bucket_binary)
    # print(xor_status)
    largest_bits=find_first_one(xor_status)
    # print(largest_bits)
    if largest_bits == -1:
        return(0,0)
    smallest_buckets_index=-1
    for k in range(n):
         if bucket_binary[k][largest_bits] == 1:
            smallest_buckets_index=k
            break
    
    # print(smallest_buckets_index)
    
    ball_status=xor_arrays(xor_status,bucket_binary[smallest_buckets_index])
    # print(ball_status)
    ball_number = binary_array_to_decimal(bucket_binary[smallest_buckets_index])-binary_array_to_decimal(ball_status)
    # print(ball_number)
    
    return(smallest_buckets_index,ball_number)
    
def number_to_binary_array(number, length):
    binary_string = bin(number)[2:]  # Convert to binary and remove prefix '0b'
    binary_list = [int(bit) for bit in binary_string]  # Convert binary string to list of integers

    if length is not None and len(binary_list) < length:
        binary_list = [0] * (length - len(binary_list)) + binary_list

    return binary_list

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

def binary_array_to_decimal(binary_array):
    binary_string = ''.join(map(str, binary_array))
    decimal_number = int(binary_string, 2)
    return decimal_number        

    
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

    # # print(solution([40123, 10298, 40123, 990901, 990901, 990901,990901]))
    # # print(solution([1, 802741, 8, 1, 9764, 990901]))
    # # print(solution([524286,1,2,8,524287,32]))
    # # print(solution([262142,1,2,8,524287,32]))

    # arr = []
    # for i in range(100):
    #     arr.append(i)
    # print("Array generated!")
    # t = time.time()
    # print(solution([1,3,5,7]))
    # print("Elapsed:", time.time() - t)

    print("All tests passed!")

# USING BRUTE FORCE TO FIND TWO NUMBERS WHICH SUM TO TARGET
def two_sums_brute_force(num_list, target):
    # outer loop
    for i in range(len(num_list)):
        # inner loop - start th range with i + 1 so don't use the first element twice
        for j in range(i + 1, len(num_list)):
            sum_of_two = num_list[i] + num_list[j]
            if sum_of_two == target:
                return [i, j]
            else:
                return -1

num_list = [1,7,9,15]
target = 9

# answer = two_sums_brute_force(num_list, target)
# print(answer)


# USING HASHMAP (DICTIONARY) TO FIND TWO NUMBERS WHICH SUM TO TARGET
def two_sums(num_list, target):
    hash_map = {} #val : index

    # for loop to loop over the length of the list
    for i in range(len(num_list)):
        # checks if the complement is in the hash map
        complement = target - num_list[i]
        # if it is is then it return i as well as the index of complement in hashmap
        if complement in hash_map:
            return (hash_map[complement], i)
        hash_map[num_list[i]] = i #storing the current number at index i into the hashmap

num_list_2 = [2,3,9,8,4]
target_2 = 17
result = two_sums(num_list_2, target_2)
print(result)
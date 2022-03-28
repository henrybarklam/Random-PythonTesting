class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        good_count = 1
        # sorted_list = sorted(arr)
        for starting_point in range(len(arr) - 1):
            jump_number = 1
            current_index = starting_point
            reached_end = False
            while reached_end == False:
                print(jump_number)
                if jump_number % 2 == 1:  # meaning it is odd

                    remaining_indices = [idx for idx, val in enumerate(arr) if val >= arr[current_index]]
                    #Make sure that it cant go back in the array, currently does all of them
                    if len(remaining_indices) == 0:
                        break
                    smallest_val = arr[remaining_indices[0]]

                    value = 0
                    for num in range(len(remaining_indices)):
                        if smallest_val > arr[remaining_indices[num]]:
                            value = num  # index in the remaining indices array
                    previous_index = current_index
                    current_index = arr[remaining_indices[value]]
                    remaining_indices.remove(previous_index)





                else:  # if its even
                    remaining_indices = [idx for idx, val in enumerate(arr) if val <= arr[current_index]]
                    if len(remaining_indices) == 0:
                        break
                    largest_val = arr[remaining_indices[0]]
                    value = 0
                    for num in range(len(remaining_indices)):
                        if largest_val < arr[remaining_indices[num]]:
                            value = num  # index in the remaining indices array
                    current_index = arr[remaining_indices[value]]

                if current_index == len(arr):
                    good_count += 1
                    reached_end = True
                jump_number += 1
        return good_count

Solution.oddEvenJumps(Solution,[5,1,3,4,2])
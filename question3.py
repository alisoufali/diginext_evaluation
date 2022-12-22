class Utils:

    @staticmethod
    def count_noequal_values(array: list[int], other_array: list[int]) -> int:
        length_array = len(array)
        counter_noequal_values = 0
        for index in range(length_array):
            if array[index] != other_array[index]:
                counter_noequal_values += 1
        return counter_noequal_values

# This is the function used to solve the problem
def find_minimum_number_swaps(array: list[int]) -> int:
    length_array = len(array)
    sorted_array = list(range(1, length_array+1))
    number_misplaced_values = Utils.count_noequal_values(
        array=array, other_array=sorted_array)
    minimum_number_swaps = number_misplaced_values - 1
    return minimum_number_swaps
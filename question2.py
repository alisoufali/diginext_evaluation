class Utils:

    @staticmethod
    def devide_string_into_everyother_substrings(string: str) -> list[str]:
        everyother_substrings: list[str] = []
        string_length = len(string)
        previous_index = 0
        for index in range(string_length-1):
            if string[index] == string[index+1]:
                everyother_substring = string[previous_index: index+1]
                everyother_substrings.append(everyother_substring)
                previous_index = index+1
        else:
            everyother_substring = string[previous_index:]
            everyother_substrings.append(everyother_substring)
        return everyother_substrings


# This is the function used to solve the problem
def find_minimum_number_of_deletions(string: str) -> int:
    everyother_substrings = Utils.devide_string_into_everyother_substrings(
        string=string)
    minimum_number_of_deletions = len(everyother_substrings) - 1
    return minimum_number_of_deletions

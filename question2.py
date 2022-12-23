import sys


class InputManager:

    @staticmethod
    def get_and_convert_input_data() -> str:
        input_data = sys.argv[1]
        converted_input_data = input_data
        return converted_input_data


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


class Main:

    # This is the function used to solve the problem
    @staticmethod
    def find_minimum_number_of_deletions(string: str) -> int:
        everyother_substrings = Utils.devide_string_into_everyother_substrings(
            string=string)
        minimum_number_of_deletions = len(everyother_substrings) - 1
        return minimum_number_of_deletions


if __name__ == "__main__":

    string = InputManager.get_and_convert_input_data()
    minimum_number_deletions = Main.find_minimum_number_of_deletions(
        string=string)
    print(f"For input: {string}, the minimum number of deletions = "
          f"{minimum_number_deletions}")
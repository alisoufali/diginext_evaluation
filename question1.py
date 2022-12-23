import sys


class InputManager:

    @staticmethod
    def get_and_convert_input_data() -> tuple[str, int]:
        input_data = sys.argv[1]
        string, number = input_data.split(",")
        number = int(number)
        converted_input_data = (string, number)
        return converted_input_data


class Utils:

    @staticmethod
    def repeat_string_to_a_number(string: str, number: int) -> str:
        string_length = len(string)
        number_complete_repeats = number // string_length
        length_remaining_string = number % string_length
        created_string = ""
        for _ in range(number_complete_repeats):
            created_string += string
        else:
            created_string += string[:length_remaining_string]
        return created_string

    # Can be replaced by the following expression:
    # string.count(character)
    @staticmethod
    def count_character_in_string(string: str, character: str) -> int:
        number_occurances = 0
        for string_character in string:
            if string_character == character:
                number_occurances += 1
        return number_occurances


class Main:
    # This is the function used to solve the problem
    @staticmethod
    def count_a_chars_in_repeated_string(string: str, number: int) -> int:
        created_string = Utils.repeat_string_to_a_number(
            string=string, number=number)
        number_occurances_a_character = Utils.count_character_in_string(
            string=created_string, character="a")
        return number_occurances_a_character


if __name__ == "__main__":

    string, number = InputManager.get_and_convert_input_data()
    number_occurances_a_character = Main.count_a_chars_in_repeated_string(
        string=string, number=number)
    print(f"For input string: {string} and number: {number}, "
          "the number of a character occurances in string = "
          f"{number_occurances_a_character}")

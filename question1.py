class Utils:

    @staticmethod
    def repeat_string_to_a_number(string: str, number: int) -> str:
        string_length = len(string)
        number_complete_repeats = string_length // number
        length_remaining_string = string_length % number
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


# This is the function used to solve the problem
def count_a_chars_in_repeated_string(string: str, number: int) -> int:
    created_string = Utils.repeat_string_to_a_number(
        string=string, number=number)
    number_occurances_a_character = Utils.count_character_in_string(
        string=created_string, character="a")
    return number_occurances_a_character

def count_a_chars_in_repeated_string(string: str, number: int) -> int:
    number_repeats = len(string) // number
    number_remaining = len(string) % number
    repeated_string: str = ""
    for _ in range(number_repeats):
        repeated_string += string
    else:
        repeated_string += string[:number_remaining]
    number_a_char = repeated_string.count("a")
    return number_a_char

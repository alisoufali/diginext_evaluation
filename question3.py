import sys


class InputManager:

    @staticmethod
    def get_and_convert_input_data() -> list[int]:
        input_data = sys.argv[1]
        converted_input_data = list(map(int, input_data.split(",")))
        return converted_input_data


class Utils:

    @staticmethod
    def get_noequal_values_and_places_conversion_dict(
        array: list[int], other_array: list[int]
    ) -> tuple[dict[int, int], dict[int, int]]:
        places_to_values: dict[int, int] = {}
        values_to_places: dict[int, int] = {}
        for index in range(len(array)):
            if array[index] != other_array[index]:
                places_to_values[index+1] = array[index]
                values_to_places[array[index]] = index+1
        return places_to_values, values_to_places

    @staticmethod
    def count_and_perform_both_win_swaps(
        places_to_values: dict[int, int], values_to_places: dict[int, int]
    ) -> tuple[int, dict[int, int], dict[int, int]]:
        both_win_values: set[int] = set()
        number_both_win_swaps = 0
        for first_value, first_place in values_to_places.items():
            if first_value in both_win_values:
                continue
            second_value = places_to_values[first_value]
            second_place = values_to_places[second_value]
            if first_place == second_value and first_value == second_place:
                both_win_values.add(first_value)
                both_win_values.add(second_value)
                number_both_win_swaps += 1
        for value in both_win_values:
            place = values_to_places[value]
            del values_to_places[value]
            del places_to_values[place]
        return number_both_win_swaps, places_to_values, values_to_places


class Main:

    # This is the function used to solve the problem
    @staticmethod
    def find_minimum_number_swaps(array: list[int]) -> int:
        length_array = len(array)
        sorted_array = list(range(1, length_array+1))
        places_to_values, values_to_places = \
            Utils.get_noequal_values_and_places_conversion_dict(
                array=array, other_array=sorted_array)
        number_both_win_swaps, places_to_values, values_to_places = Utils.\
            count_and_perform_both_win_swaps(
                places_to_values=places_to_values,
                values_to_places=values_to_places)
        if len(values_to_places) > 0:
            number_single_win_swaps = len(values_to_places) - 1
        else:
            number_single_win_swaps = 0
        minimum_number_swaps = number_both_win_swaps + number_single_win_swaps
        return minimum_number_swaps


if __name__ == "__main__":

    array = InputManager.get_and_convert_input_data()
    minimum_number_swaps = Main.find_minimum_number_swaps(array=array)
    print(f"For input: {array}, the minimum number of swaps = "
          f"{minimum_number_swaps}")

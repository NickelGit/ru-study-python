class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return []

        result = []
        max_number = max(input_list)
        for num in input_list:
            result.append(num) if num < 0 else result.append(max_number)

        return result

    @staticmethod
    def max(input_list: list[int]) -> int:
        max_number = input_list[0]
        for number in input_list:
            if number > max_number:
                max_number = number

        return max_number

    @staticmethod
    def search(
        input_list: list[int], query: int, left_border: int = 0, right_border: int = None
    ) -> int:
        if right_border is None:
            right_border = len(input_list) - 1
        if left_border > right_border:
            return -1

        middle_element_index = (right_border + left_border) // 2
        middle_element = input_list[middle_element_index]

        if middle_element == query:
            return middle_element_index

        if query < middle_element:
            return ListExercise.search(input_list, query, left_border, middle_element_index - 1)
        else:
            return ListExercise.search(input_list, query, middle_element_index + 1, right_border)

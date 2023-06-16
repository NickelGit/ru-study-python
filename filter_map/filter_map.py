from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []

        for item in input_array:
            flag, value = func(item)
            if flag:
                result.append(value)

        return result

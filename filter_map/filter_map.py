from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []

        for item in input_array:
            processing_result = func(item)
            if processing_result[0]:
                result.append(processing_result[1])

        return result

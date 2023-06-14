from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        ratings = map(
            lambda film: float(film["rating_kinopoisk"])
            if MapExercise.has_several_countries_and_positive_kinopoisk_rating(film)
            else None,
            list_of_movies,
        )
        filtered_ratings = [rating for rating in ratings if rating is not None]

        return sum(filtered_ratings) / len(filtered_ratings)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        chars_number_in_names = map(
            lambda film: film["name"].count("и")
            if MapExercise.has_rating_gteq(film, rating)
            else 0,
            list_of_movies,
        )

        return sum(chars_number_in_names)

    @staticmethod
    def has_several_countries(film: dict) -> bool:
        return "," in film["country"]

    @staticmethod
    def has_several_countries_and_positive_kinopoisk_rating(film: dict) -> bool:
        return (
            MapExercise.has_several_countries(film)
            and film["rating_kinopoisk"]
            and float(film["rating_kinopoisk"]) > 0
        )

    @staticmethod
    def has_rating_gteq(film: dict, threshold: Union[float, int]) -> bool:
        return film["rating_kinopoisk"] and float(film["rating_kinopoisk"]) >= threshold

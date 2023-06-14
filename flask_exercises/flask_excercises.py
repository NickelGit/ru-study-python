from flask import Flask, request, abort
from http import HTTPStatus


class FlaskExercise:
    users_dictionary: dict = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.post("/user")
        def create():
            request_body = request.json
            if "name" in request_body:
                name = request_body["name"]
                FlaskExercise.users_dictionary[f"{name}"] = {}

                return {"data": f"User {name} is created!"}, HTTPStatus.CREATED
            else:
                abort(HTTPStatus.UNPROCESSABLE_ENTITY)

        @app.get("/user/<name>")
        def show(name):
            if name in FlaskExercise.users_dictionary:
                return {"data": f"My name is {name}"}, HTTPStatus.OK
            else:
                abort(HTTPStatus.NOT_FOUND)

        @app.patch("/user/<name>")
        def update(name):
            if name in FlaskExercise.users_dictionary:
                request_body = request.json
                new_name = request_body["name"]
                FlaskExercise.update_user_name(name, new_name)

                return {"data": f"My name is {new_name}"}, HTTPStatus.OK
            else:
                abort(HTTPStatus.NOT_FOUND)

        @app.delete("/user/<name>")
        def destroy(name):
            if name in FlaskExercise.users_dictionary:
                del FlaskExercise.users_dictionary[f"{name}"]
                return "", HTTPStatus.NO_CONTENT
            else:
                abort(HTTPStatus.NOT_FOUND)

        @app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
        def unprocessable_entity(error):
            return {"errors": {"name": "This field is required"}}, HTTPStatus.UNPROCESSABLE_ENTITY

        @app.errorhandler(HTTPStatus.NOT_FOUND)
        def not_found(error):
            return "", HTTPStatus.NOT_FOUND

    @staticmethod
    def update_user_name(old_name: str, new_name: str) -> None:
        user_data = FlaskExercise.users_dictionary[f"{old_name}"]
        FlaskExercise.users_dictionary[f"{new_name}"] = user_data
        del FlaskExercise.users_dictionary[f"{old_name}"]

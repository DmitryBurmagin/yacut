from http import HTTPStatus

from flask import jsonify, render_template, request

from . import app


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {'message': self.message}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.before_request
def validate_request():
    if request.method == 'POST' and request.path.startswith('/api/'):

        if not request.data:
            raise InvalidAPIUsage(
                'Отсутствует тело запроса',
                status_code=HTTPStatus.BAD_REQUEST
            )

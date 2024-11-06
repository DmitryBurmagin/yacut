from http import HTTPStatus

from flask import jsonify, request

from . import app, db, test_base_url
from .models import URLMap
from .schemas import UrlMapSchema
from .utils import get_unique_short_id
from .validators import validate_request_data, validate_short_id

url_map_schema = UrlMapSchema()


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    original_link, custom_id = validate_request_data(data)

    if not custom_id:
        custom_id = get_unique_short_id()

    new_url = URLMap(original=original_link, short=custom_id)
    db.session.add(new_url)
    db.session.commit()

    response = {
        'url': original_link,
        'short_link': f'{test_base_url}/{custom_id}',
    }
    return jsonify(response), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    url_map = validate_short_id(short_id)
    if not url_map:
        return jsonify({'message': 'ID не найден'}), HTTPStatus.NOT_FOUND
    return jsonify({'url': url_map.original}), HTTPStatus.OK

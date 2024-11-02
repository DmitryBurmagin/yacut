from flask import jsonify, request

from . import app, db
from .models import URLMap
from .schemas import UrlMapSchema
from .utils import get_unique_short_id

url_map_schema = UrlMapSchema()


@app.route('/api/id/', methods=['POST'])
def create_short_link():

    data = request.get_json()

    if data is None:
        return jsonify({'message': "Отсутствует тело запроса"}), 400

    original_link = data.get('url')
    custom_id = data.get('custom_id')

    if not original_link:
        return jsonify({'message': "Поле 'url' обязательно"}), 400
    if not custom_id:
        custom_id = get_unique_short_id()
    if URLMap.query.filter_by(short=custom_id).first():
        return jsonify({'message': 'Идентификатор уже используется'}), 409

    new_url = URLMap(url=original_link, short=custom_id)
    db.session.add(new_url)
    db.session.commit()

    return url_map_schema.jsonify(new_url), 201


@app.route('/api/id/<string:short_id>', methods=['GET'])
def get_original_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        return jsonify(
            {'error': 'Указанный короткий идентификатор не найден'}
        ), 404

    return jsonify({'url': url_map.original}), 200

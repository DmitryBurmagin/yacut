from flask import jsonify, request

from . import app, db
from .models import URLMap
from .schemas import UrlMapSchema

url_map_schema = UrlMapSchema()


@app.route('/api/shorten', methods=['POST'])
def get_url():
    original_link = request.json.get('original_link')
    custom_id = request.json.get('custom_id')

    if not original_link or not custom_id:
        return jsonify({'error': 'error'})

    new_url = URLMap(original=original_link, short=custom_id)
    db.session.add(new_url)
    db.session.commit()

    return url_map_schema.jsonify(new_url), 201

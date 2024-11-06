import re

from .error_handlers import InvalidAPIUsage
from .models import URLMap


def validate_short_id(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', status_code=404)
    return url_map


def validate_unique_custom_id(custom_id):
    existing_url = URLMap.query.filter_by(short=custom_id).first()
    if existing_url:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.',
            status_code=400
        )


def validate_request_data(data):
    url = data.get('url')
    custom_id = data.get('custom_id')

    if not url:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!',
            status_code=400
        )

    if custom_id:
        if len(custom_id) >= 16 or not re.match('^[a-zA-Z0-9]+$', custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
                status_code=400
            )
        validate_unique_custom_id(custom_id)

    return url, custom_id

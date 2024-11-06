from . import ma
from .models import URLMap


class UrlMapSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = URLMap
        load_instance = True
        ordered = True
        fields = ('original', 'short_link')

    original = ma.auto_field(data_key='url')
    short_link = ma.auto_field('short', dump_only=True, data_key='short_link')

from .models import URLMap
from . import ma


class UrlMapSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = URLMap
        load_instance = True
        fields = ('url', 'short_link')

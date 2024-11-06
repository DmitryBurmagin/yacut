from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional


class UrlForm(FlaskForm):
    original_link = URLField(
        'Оригинальная ссылка',
        validators=[
            DataRequired(message='Это поле обязательно для заполнения'),
            URL(message='Введите корректный URL')
        ]
    )
    custom_id = StringField(
        'Короткий идентификатор',
        validators=[
            Length(max=16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')

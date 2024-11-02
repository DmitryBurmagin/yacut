from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, URL, Length, Optional


class UrlForm(FlaskForm):
    original_link = URLField(
        'Оригинальная ссылка',
        validators=[
            DataRequired(message='Это поле обязательно для заполнения'),
            URL(message='Введите корректный URL')
        ]
    )
    custom_id = URLField(
        'Короткий идентификатор',
        validators=[
            Length(max=16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')

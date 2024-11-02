from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField, StringField
from wtforms.validators import DataRequired, URL, Length, Optional


class UrlForm(FlaskForm):
    url = URLField(
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

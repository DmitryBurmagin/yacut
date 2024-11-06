from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import UrlForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data or get_unique_short_id()

        if form.custom_id.data and URLMap.query.filter_by(
            short=form.custom_id.data
        ).first():
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'error'
            )
            return redirect(url_for('index_view'))

        url_map = URLMap(original=original_link, short=custom_id)
        db.session.add(url_map)
        db.session.commit()

        short_url = url_for("redirect_view", short=custom_id, _external=True)
        flash(
            f'Ваша короткая ссылка: <a href="{short_url}">{short_url}</a>',
            'success'
        )

        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


@app.route('/<short>')
def redirect_view(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)

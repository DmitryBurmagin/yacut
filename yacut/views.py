from flask import render_template, redirect, url_for, flash
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
        url_map = URLMap(original=original_link, short=custom_id)
        db.session.add(url_map)
        db.session.commit()
        flash(
            'Ваша короткая ссылка: <a href="{short_url}">{short_url}</a>',
            'success'
        )
        return redirect(url_for('index_view'))
    return render_template('index.html', form=form)

from datetime import datetime, timezone

from . import db

MAX_URL_LENGTH = 256
MAX_SHORT_LENGTH = 16


def get_utc_now():
    return datetime.now(timezone.utc)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL_LENGTH), nullable=False)
    short = db.Column(db.String(MAX_SHORT_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=get_utc_now)

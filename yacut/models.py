from datetime import datetime, timezone
from . import db


def get_utc_now():
    return datetime.now(timezone.utc)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=get_utc_now)

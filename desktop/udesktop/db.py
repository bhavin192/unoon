import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import datetime


BASE = declarative_base()


class history(BASE):
    "history of all processes"
    __tablename__ = "processhistory"

    id = sa.Column(sa.Integer, primary_key=True)
    executable = sa.Column(sa.TEXT, nullable=False)
    command = sa.Column(sa.TEXT, nullable=False)
    local_ip = sa.Column(sa.TEXT, nullable=False)
    local_port = sa.Column(sa.INTEGER, nullable=False)
    remote_ip = sa.Column(sa.TEXT, nullable=False)
    remote_port = sa.Column(sa.INTEGER, nullable=False)
    pid = sa.Column(sa.INTEGER, nullable=False)
    realuid = sa.Column(sa.INTEGER, nullable=False)
    effectiveuid = sa.Column(sa.INTEGER, nullable=False)
    saveduid = sa.Column(sa.INTEGER, nullable=False)
    filesystemuid = sa.Column(sa.INTEGER, nullable=False)
    when = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return u"<ID: %d EXE: %s>" % (self.id, self.executable)


def create_session(db_url, debug=False):
    engine = sa.create_engine(db_url, echo=debug)
    scopedsession = scoped_session(sessionmaker(bind=engine))
    return scopedsession


def create_tables(url):
    # Create an engine that stores data in the local directory
    engine = sa.create_engine(url)
    BASE.metadata.create_all(engine)


if __name__ == "___main___":
    create_tables("sqlite:///var/lib/unoon/unoon.db")

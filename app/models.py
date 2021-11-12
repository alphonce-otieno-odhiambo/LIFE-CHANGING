from . import db

class Viewer(db.Model):
    __tablename__ = 'view'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    quote = db.Clumn((db.String))

    def __repr__(self):
        return 'f Viewer{self.user}'
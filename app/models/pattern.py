from .db import db
from sqlalchemy.orm import relationship

class Pattern(db.Model):
    __tablename__ = 'patterns'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    public = db.Column(db.Boolean, default=False)
    height = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    pattern_state = db.Column(db.LargeBinary, nullable=False)


    return {
        'id':self.id,
        'user_id':self.user_id,
        'public':self.public,
        'height':self.height,
        'width':self.width,
        'pattern_state':self.pattern_state
    }
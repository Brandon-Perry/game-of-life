from .db import db
from sqlalchemy.orm import relationship

class Game(db.Model):
    __tablename__='games'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    public = db.Column(db.Boolean, default=False)
    height = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    board_state = db.Column(db.LargeBinary, nullable=False)


    def to_dict(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'public':self.public,
            'height':self.height,
            'width':self.width,
            'board_state':self.board_state
        }
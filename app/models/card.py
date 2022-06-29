from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)

    @classmethod
    def create(cls, req_body):
        new_card = cls(
            message=req_body["message"],
            likes_count = 0
        )
        return new_card

    def to_json(self):
        return {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }
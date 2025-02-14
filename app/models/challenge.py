from app import db
 

# 6. Défis (Challenge)
class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    reward_points = db.Column(db.Integer)
    expiration_date = db.Column(db.DateTime)

# 7. Participation aux Défis (UserChallenge)
class UserChallenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'))
    completed_at = db.Column(db.DateTime)

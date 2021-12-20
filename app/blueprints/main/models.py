from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    team = db.Column(db.String)
    position = db.Column(db.String)
    age = db.Column(db.Float)
    gp = db.Column(db.Integer)
    mpg = db.Column(db.Float)
    fta = db.Column(db.Integer)
    ftp = db.Column(db.Float)
    tpa = db.Column(db.Integer)
    tpp = db.Column(db.Float)
    thpa = db.Column(db.Integer)
    thpp = db.Column(db.Float)
    ppg = db.Column(db.Float)
    rpg = db.Column(db.Float)
    apg = db.Column(db.Float)
    spg = db.Column(db.Float)
    bpg = db.Column(db.Float)
    topg = db.Column(db.Float)

    # def __init__(self, name, team, position, age, gp, mpg, fta, ftp, tpa, tpp, thpa, thpp, ppg, rpg, apg, spg, bpg, topg):
    #     self.name = name
    #     self.team = team
    #     self.position = position
    #     self.age = age
    #     self.gp = gp
    #     self.mpg = mpg
    #     self.fta = fta
    #     self.ftp = ftp
    #     self.tpa = tpa
    #     self.tpp = tpp
    #     self.thpa = thpa
    #     self.thpp = thpp
    #     self.ppg = ppg
    #     self.rpg = rpg
    #     self.apg = apg
    #     self.spg = spg
    #     self.bpg = bpg
    #     self.topg = topg
        
    def __repr__(self):
        return f'<Player: {self.name}>'
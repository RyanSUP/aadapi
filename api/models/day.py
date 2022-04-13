from datetime import datetime
from api.models.db import db

class Day(db.Model):
  __tablename__= 'days'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(100))
  stand_up = db.Column(db.String(280))
  stand_down = db.Column(db.String(280))
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  #Relationships
  jerbs = db.relationship("Jerb", cascade='all')

  def __repr__(self):
    return f"Day('{self.id}', '{self.date})"

  def serialize(self):
    day = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    serial_jerbs = [jerb.serialize() for jerb in self.jerbs]
    day['jerbs'] = serial_jerbs
    return day
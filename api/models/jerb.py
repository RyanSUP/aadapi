from datetime import datetime
from api.models.db import db

class Jerb(db.Model):
  __tablename__ = 'jerbs'
  id = db.Column(db.Integer, primary_key=True)
  day_id = db.Column(db.Integer, db.ForeignKey('days.id')) 
  title = db.Column(db.String(100))
  company = db.Column(db.String(100))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return f"Jerb('{self.id};, '{self.title}"

  def serialize(self):
    jerb = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    return jerb


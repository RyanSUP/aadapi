from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.day import Day

days = Blueprint('days', 'days')

@days.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  day = Day(**data)
  db.session.add(day)
  db.session.commit()
  return jsonify(day.serialize()), 201

@days.route('/', methods=["GET"])
@login_required
def getAll():
  days = Day.query.all()
  return jsonify([day.serialize() for day in days]), 200

@days.route('/<id>', methods=["GET"])
@login_required
def show(id):
  day = Day.query.filter_by(id=id).first()
  day_data = day.serialize()
  #**** ADD HERE THE FUNCTION TO FILL DAY/JERB Target ASSOCIATION****####
  return jsonify(day=day_data), 200

@days.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  day = Day.query.filter_by(id=id).first()

  if day.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(day, key, data[key])

  db.session.commit()
  return jsonify(day.serialize()), 200

@days.route('/<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  day = Day.query.filter_by(id=id).first()

  if day.profile_id != profile["id"]:
    return 'Forbidden', 403
  
  db.session.delete(day)
  db.session.commit()
  return jsonify(message="Fuck Yeah, DELETING DAYS BITCHES"), 200
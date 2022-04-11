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
  print("    ")
  print("    ")
  print("    ")
  print("    ")
  print("    ")
  print("    ")
  print("    ")
  print("PROFILE MOTHAFUCKA", profile)
  data["profile_id"] = profile["id"]
  day = Day(**data)
  db.session.add(day)
  db.session.commit()
  return jsonify(day.serialize()), 201
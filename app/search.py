from .models import Pitches
from flask import abort

def get_pitches(category): 
  '''Function to obtain pitches according to categories they belong'''
  pitches = Pitches.query.filter_by(pitch_category = category).all()
  if pitches is None: 
    abort(404)
    
  return pitches

def get_pitch(id): 
  '''Function that returns a specific pitch according to id'''
  pitch = Pitches.query.filter_by(id = id).first()
  if pitch is None: 
    abort(404)
  
  return pitch
#!/usr/bin/python3
from .base_model import BaseModel
from models import storage


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

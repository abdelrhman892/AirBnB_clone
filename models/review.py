#!/usr/bin/python3
from .base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

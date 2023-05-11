#!/usr/bin/python3
"""
Base class of all models
"""
import uuid
import datetime
import models


class BaseModel:
    """ Definiton of all common attributes/methods for other classes"""
    def __init__(self, id):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


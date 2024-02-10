#!/usr/bin/python3
import uuid
import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = (datetime.datetime.strptime
                             (value, '%Y-%m-%dT%H:%M:%S.%f'))
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()  # made the storage implementation

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

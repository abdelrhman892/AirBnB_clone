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
        dict_result = {}
        for key, value in self.__dict__.items():
            if key != '__class__':
                if isinstance(value, datetime.datetime):
                    dict_result[key] = value.isoformat()
                else:
                    dict_result[key] = value
        dict_result['__class__'] = self.__class__.__name__
        return dict_result

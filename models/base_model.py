#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                            )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                dict_result[key] = value.isoformat()
            else:
                dict_result[key] = value
        return dict_result

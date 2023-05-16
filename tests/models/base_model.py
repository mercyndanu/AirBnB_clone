#!/usr/bin/python3
"""
Base class of all models
"""
import uuid
import datetime
import models


class BaseModel:
    """ Definiton of all common attributes/methods for other classes"""
    """
    def __init__(self):
        Instantiation of classs
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
     """

    def __init__(self, *args, **kwargs):
        """Instantiation of class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    setattr(self, key, eval(value))
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints out instance created as a string"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()
        # Link BaseModel to FileStorage
        models.storage.save()

    def to_dict(self):
        """Returns dictionary with all keys/values of __dict__ of instance"""
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.__dict__['created_at'].isoformat()
        obj_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return (obj_dict)

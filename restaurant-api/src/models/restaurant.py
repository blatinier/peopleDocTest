from datetime import datetime
from mongoengine import fields, Document


class Restaurant(Document):
    created_at = fields.DateTimeField(default=datetime.now, required=True)
    modified_at = fields.DateTimeField(default=datetime.now, required=True)

    name = fields.StringField(required=True)

    def __repr__(self):
        return '{} {} #{}'.format(self.__class__.__name__,
                                  getattr(self, 'name', ''),
                                  str(self.id))

    def __str__(self):
        return '<{}>'.format(repr(self))

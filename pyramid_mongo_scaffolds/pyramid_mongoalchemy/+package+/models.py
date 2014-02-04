from mongoalchemy.document import Document
from mongoalchemy.fields import *


# A very simple domain class
class MyModel(Document):

    name = StringField()
    value = IntField()

    def __str__(self):
        return "<Model %s: %d>" % (self.name, self.value)


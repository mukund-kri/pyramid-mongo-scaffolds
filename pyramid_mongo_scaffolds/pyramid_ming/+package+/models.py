from mongoengine import (
    Document,
    StringField,
    IntField,
    )


# A very simple domain class
class MyModel(Document):   
    name = StringField(required=True)
    value = IntField(required=True)

    def __str__(self):
        return "<Model %s: %d>" % (self.name, self.value)


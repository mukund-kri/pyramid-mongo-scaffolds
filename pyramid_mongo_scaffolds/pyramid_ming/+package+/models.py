from ming import (
    Field,
    Document,
    Session,
    schema,
    )


# A very simple domain class
class MyModel(Document):

    class __mongometa__:
        session = Session.by_name('default')
        name = 'my_model'
        
    _id = Field(schema.ObjectId)
    name = Field(str)
    value = Field(int)

    def __str__(self):
        return "<Model %s: %d>" % (self.name, self.value)


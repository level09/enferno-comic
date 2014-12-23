from extensions import db

class Comic(db.Document):
    image = db.ImageField()
    title = db.StringField()

    def __unicode__(self):
        return '%s' % self.title
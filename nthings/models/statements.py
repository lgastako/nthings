from google.appengine.ext import db


class Statement(db.Model):
    number_of_things = db.IntegerProperty(required=True)
    quantification_of_target = db.StringProperty(required=True)
    type_of_target = db.StringProperty(required=True)
    should_what_now = db.StringProperty(required=True)
    but_probably_what = db.StringProperty(required=True)
    things = db.StringListProperty(required=True)



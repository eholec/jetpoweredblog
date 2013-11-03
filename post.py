from google.appengine.ext import ndb


class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    postedDate = ndb.DateTimeProperty(auto_now_add=True)

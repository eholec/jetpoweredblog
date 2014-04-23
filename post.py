from google.appengine.ext import ndb


class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    isPosted = ndb.BooleanProperty(default=False)
    postedDate = ndb.DateTimeProperty()
    editedDate = ndb.DateTimeProperty(auto_now=True)
    tags = ndb.StringProperty(repeated=True)

    def get_snippet(self):
        ind = self.content.find('<!-- READMORE -->')

        if ind < 0:
            return None
        else:
            return self.content[:ind]
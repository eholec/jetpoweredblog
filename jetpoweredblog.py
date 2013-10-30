import webapp2
from post import Post


class HomePage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        posts = Post.query().order(-Post.postedDate)
        for post in posts:
            self.response.write(
                post.title + ' ' +
                post.postedDate.strftime('%c') + ': ' +
                post.content + '\n')


application = webapp2.WSGIApplication([
    ('/', HomePage),
], debug=True)

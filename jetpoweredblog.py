import webapp2
from post import Post


class HomePage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        posts = Post.query().order(-Post.postedDate)

        self.response.write('<!DOCTYPE html><html><body>')
        for post in posts:
            self.response.write('<h2>' + post.title + '</h2>')
            self.response.write('<h3>' +
                    post.postedDate.strftime('%c') + '</h3>')
            self.response.write('<p>' + post.content + '</p>')
        self.response.write('</body></html>')


application = webapp2.WSGIApplication([
    ('/', HomePage),
], debug=True)

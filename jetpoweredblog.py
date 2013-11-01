import webapp2
from google.appengine.api import users
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
            self.response.write(post.content)
        self.response.write('</body></html>')


class AdminPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<!DOCTYPE html><html><body>')
        self.response.write('<form action="/admin" method="post">')
        self.response.write('<input type="text" name="title"><br>')
        self.response.write('<textarea name="content" rows="10" cols="60">' +
                '</textarea><br>')
        self.response.write('<input type="submit" value="Create Post">')
        self.response.write('</form>')
        self.response.write('</body></html>')

    def post(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        post = Post(title=self.request.get('title'),
            content=self.request.get('content'))
        post.put()

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<!DOCTYPE html><html><body>')
        self.response.write('<p>Post created</p>')
        self.response.write('</body></html>')


application = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/admin', AdminPage),
], debug=True)

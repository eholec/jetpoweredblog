import os

import webapp2
import jinja2

from google.appengine.api import users
from post import Post


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class HomePage(webapp2.RequestHandler):

    def get(self):
        posts = Post.query().order(-Post.postedDate)

        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        template_values = {
            'posts': posts,
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))


class AdminPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        template = JINJA_ENVIRONMENT.get_template('templates/admin.html')
        template_values = {}

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))

    def post(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        post = Post(title=self.request.get('title'),
            content=self.request.get('content'))
        post.put()

        self.redirect('/')


application = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/admin', AdminPage),
], debug=True)

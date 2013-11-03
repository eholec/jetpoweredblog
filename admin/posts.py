import os

import webapp2
import jinja2

from google.appengine.api import users
from post import Post
import jetpoweredblog


class AdminPostsHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        posts = Post.query().order(-Post.postedDate)

        template = jetpoweredblog.JINJA_ENVIRONMENT.get_template(
            'templates/admin-posts.html')
        template_values = {
            'posts': posts,
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))

    def post(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        post = Post()
        post.put()

        self.redirect('/admin/posts/' + post.key.id())
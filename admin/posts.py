import datetime

import webapp2
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
            'templates/admin/posts.html')
        template_values = {
            'posts': posts,
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))


class AdminPostsCreateHandler(webapp2.RequestHandler):

    def post(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        post = Post()
        post.title = self.request.POST['title']
        post.put()

        self.redirect('/admin/posts/edit/' + str(post.key.id()))


class AdminPostsEditHandler(webapp2.RequestHandler):

    def get(self, id):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        post = Post.get_by_id(int(id))

        if post is None:
            self.response.set_status(404)
            return

        template = jetpoweredblog.JINJA_ENVIRONMENT.get_template(
            'templates/admin/posts-edit.html')
        template_values = {
            'post': post,
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))

    def post(self, id):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
            return

        post = Post.get_by_id(int(id))

        if post is None:
            self.response.set_status(404)
            return

        post.title = self.request.POST['title']
        post.content = self.request.POST['content']

        isPosted = 'isPosted' in self.request.POST
        if(isPosted and not post.isPosted):
            post.postedDate = datetime.datetime.now()

        post.isPosted = isPosted

        post.put()

        self.response.set_status(204)
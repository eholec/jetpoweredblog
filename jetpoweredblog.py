import os

import webapp2
import jinja2

import admin.posts
from post import Post


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class HomePage(webapp2.RequestHandler):

    def get(self):
        posts = Post.query(Post.isPosted == True).order(-Post.postedDate)

        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        template_values = {
            'posts': posts,
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    (r'/', HomePage),
    (r'/admin/posts', admin.posts.AdminPostsHandler),
    (r'/admin/posts/create', admin.posts.AdminPostsCreateHandler),
    (r'/admin/posts/edit/(\d+)', admin.posts.AdminPostsEditHandler),
], debug=True)

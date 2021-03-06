from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    #page = request.args.get('page', 1, type=int)
    posts = Post.objects.all().order_by('-date_posted')
    return render_template ('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template ('about.html', title='about')

from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Rating
from flaskblog.posts.forms import PostForm, RatingForm


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET','POST'])
@login_required
def new_post(): 
    form = PostForm()
    if form.validate_on_submit():
        post = Post(user_id=current_user, title=form.title.data, content=form.content.data, address=form.address.data, opening_hours=form.opening_hours.data, )
        
        
        post.save()
        flash(f'Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@posts.route("/post/<post_id>")
def post(post_id):
    post = Post.objects.get_or_404(id=post_id)
    return render_template('post.html', title=post.title, post=post, address=post.address, opening_hours=post.opening_hours)


@posts.route("/post/<post_id>/update", methods=['GET','POST'])
def update_post(post_id):
    post = Post.objects.get_or_404(id=post_id)
    if post.user_id.id != current_user.id:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.address = form.address.data
        post.opening_hours = form.opening_hours.data
        post.save()
        flash(f'Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.address.data=post.address
        form.opening_hours.data=post.opening_hours
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route("/post/<post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.objects.get_or_404(post_id)
    if post.user_id != current_user:
        abort(403)
    post.delete()
    flash(f'Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/post/<post_id>/rating", methods=['GET','POST'])
@login_required
def rating_post(post_id):

    form = RatingForm()
    if form.validate_on_submit():
        rating = Rating(user_id=current_user, post_id=post_id, rating=form.rating.data, comment=form.comment.data )
        rating.save()
        flash(f'Your rating has been received', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    return render_template('create_rating.html', title= 'Rate the toilet', form=form)

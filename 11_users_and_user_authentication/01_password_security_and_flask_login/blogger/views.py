from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify

from . models import User, Post, db
from . forms import AddPostForm, SignUpForm, SignInForm, AboutUserForm
from flask_login import login_user, logout_user, login_required, current_user
from blogger import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def show_posts():
    if current_user.is_authenticated:
        posts = Post.query.all()
        user = User.query.all()
        return render_template('posts.html', posts=posts, user=user)
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if session['user_available']:
        blogpost = AddPostForm(request.form)
        us = User.query.filter_by(username=session['current_user']).first()
        if request.method == 'POST':
            bp = Post(blogpost.title.data, blogpost.description.data, us.uid)
            db.session.add(bp)
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('add.html', blogpost=blogpost)
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/delete/<pid>/<post_owner>', methods=('GET', 'POST'))
def delete_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        db.session.delete(me)
        db.session.commit()
        return redirect(url_for('show_posts'))
    flash('You are not a valid user to Delete this Post')
    return redirect(url_for('show_posts'))


@app.route('/update/<pid>/<post_owner>', methods=('GET', 'POST'))
def update_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        blogpost = AddPostForm(obj=me)
        if request.method == 'POST':
            bpost = Post.query.get(pid)
            bpost.title = blogpost.title.data
            bpost.description = blogpost.description.data
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('update.html', blogpost=blogpost)
    flash('You are not a valid user to Edit this Post')
    return redirect(url_for('show_posts'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        reg = User(firstname = signupform.firstname.data, lastname = signupform.lastname.data,\
         username = signupform.username.data, password = signupform.password.data,\
         email = signupform.email.data)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', signupform=signupform)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()

    if request.method == 'POST':
        # if form.validate_on_submit():
        email_entered = signinform.email.data
        password_entered = signinform.password.data

        user = User.query.filter_by(email=email_entered).first()

        # make sure that user is not None or it would error
        if user and user.verify_password(password_entered):
            login_user(user, remember = signinform.remember_me.data)

            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                # if signs in successfully then show posts
                next = url_for('show_posts')
            return redirect(next)
            # flash a message that username/password is invalid
        flash("The username/password is invalid")



            # current_user = user.username
            # session['current_user'] = current_user
            # session['user_available'] = True
            # return redirect(url_for('show_posts'))
    return render_template('signin.html', signinform=signinform)


@app.route('/about_user')
def about_user():
    aboutuserform = AboutUserForm()
    if session['user_available']:
        user = User.query.filter_by(username=session['current_user']).first()
        return render_template('about_user.html', user=user, aboutuserform=aboutuserform)
    flash('You are not a Authenticated User')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request

from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

app = Flask(__name__)


@app.route('/')
def index():
    all_post = get_posts_all()
    return render_template("index.html", all_post=all_post)


@app.route("/posts/<int:post_id>")
def posts(post_id):
    comment = get_comments_by_post_id(post_id)
    post = get_post_by_pk(post_id)
    return render_template("post.html", comment=comment, post=post[0])


@app.route("/search/", methods=['GET'])
def search():
    words = request.values.get('s')
    result = search_for_posts(words)
    return render_template("search.html", result=result, words=words)


@app.route("/users/<username>")
def users_post(username):
    user = get_posts_by_user(username)
    return render_template("user-feed.html", user=user)


if __name__ == '__main__':
    app.run()

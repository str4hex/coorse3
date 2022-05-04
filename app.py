from flask import Flask, render_template, request, redirect

from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user, \
    load_json, DATA_PATH, add_bookmarks, BOOKMARKS_PATH, remove_bookmarks

app = Flask(__name__)


@app.route('/')
def index():
    all_post = get_posts_all()
    load_bookmarks = load_json(BOOKMARKS_PATH)
    return render_template("index.html", all_post=all_post, bookmarks=load_bookmarks)


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


@app.route("/api/posts")
def api_post():
    return f"{load_json(DATA_PATH)}"


@app.route("/api/posts/<int:post_id>")
def api_post_id(post_id):
    return f"{get_post_by_pk(post_id)}"


@app.route("/bookmarks")
def bookmarks():
    load_bookmarks = load_json(BOOKMARKS_PATH)
    return render_template("bookmarks.html", bookmarks=load_bookmarks)


@app.route("/bookmarks/add/<int:post_id>")
def bookmarks_add(post_id):
    add_bookmarks(post_id)
    return redirect("/", code=302)


@app.route("/bookmarks/remove/<int:post_id>")
def bookmarks_remove(post_id):
    remove_bookmarks(post_id)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run()

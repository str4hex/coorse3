import json

DATA_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"
BOOKMARKS_PATH = "data/bookmarks.json"


def load_json(data):
    with open(data, "r", encoding="utf8") as file:
        return json.load(file)


# возвращает посты
def get_posts_all():
    load = load_json(DATA_PATH)
    return load


# возвращает посты определенного пользователя
def get_posts_by_user(user_name):
    load_user = load_json(DATA_PATH)
    user_post = []
    for user in load_user:
        if user_name in user["poster_name"]:
            user_post.append(user)
    return user_post


# возвращает комментарии определенного поста
def get_comments_by_post_id(post_id):
    load_comment = load_json(COMMENTS_PATH)
    comment_posts = []
    for comment in load_comment:
        if post_id == comment["post_id"]:
            comment_posts.append(comment)
    return comment_posts


# возвращает список постов по ключевому слову
def search_for_posts(query):
    load_post = load_json(DATA_PATH)
    search_post = []
    for search in load_post:
        if query is None:
            return search_post
        elif query.lower() in search["content"].lower():
            search_post.append(search)
    return search_post


def get_post_by_pk(pk):  # возвращает один пост по его идентификатору
    load_post = load_json(DATA_PATH)
    posts = []
    for post in load_post:
        if pk == post["pk"]:
            posts.append(post)
    return posts

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

# возвращает один пост по его идентификатору
def get_post_by_pk(pk):
    load_post = load_json(DATA_PATH)
    posts = []
    for post in load_post:
        if pk == post["pk"]:
            posts.append(post)
    return posts


# Добавляет закладку в избранное
def add_bookmarks(post_id):
    load_post = load_json(DATA_PATH)
    load_bookmarks = load_json(BOOKMARKS_PATH)
    post = []
    for bookmarks in load_bookmarks:
        if post_id == bookmarks["pk"]:
            post.append(bookmarks["pk"])
    if post_id in post:
        pass
    else:
        with open(BOOKMARKS_PATH, "w", encoding="utf8") as file:
            for post in load_post:
                if post_id == post["pk"]:
                    load_bookmarks.append(post)
                    return json.dump(load_bookmarks, file, ensure_ascii=True)
    return print(post)


#Удалить закладку из избраного
def remove_bookmarks(post_id):
    load_bookmarks = load_json(BOOKMARKS_PATH)
    with open(BOOKMARKS_PATH, "w") as file:
        for bookmarks in range(len(load_bookmarks)):
            if post_id == load_bookmarks[bookmarks]["pk"]:
                load_bookmarks.pop(bookmarks)
                return json.dump(load_bookmarks, file, ensure_ascii=True)
    return load_bookmarks
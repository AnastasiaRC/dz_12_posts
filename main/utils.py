import json
from json import JSONDecodeError


class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        posts = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                posts = json.load(f)
        except JSONDecodeError:
            return posts, 'Ошибка получения данных из JSON'
        return posts, None

    def search_posts(self, substr):
        posts = []
        load_posts, error = self.load_posts()
        for post in load_posts:
            if substr.lower() in post['content'].lower():
                posts.append(post)
        return posts, error

    def save_posts_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False)

    def add_post(self, post):
        posts, error = self.load_posts()
        posts.append(post)
        self.save_posts_to_json(posts)

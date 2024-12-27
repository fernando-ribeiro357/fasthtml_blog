# from app.database import get_db
from app.database import get_db
from bson import ObjectId
from app.utils import random_str

class BlogPost:
    def __init__(self, post_id: str, title: str, content: str):
        self.post_id = post_id
        self.title = title
        self.content = content

def get_all_posts():
    db = get_db('blog')
    posts = [{'post_id': p['post_id'], 'title': p['title'], 'content': p['content']} for p in db.posts.find()]
    return posts

def get_post(id):
    db = get_db('blog')
    post = db.posts.find_one({'post_id': id})
    return post

def create_post(title: str, content: str):
    db = get_db('blog')
    post_id = random_str(8)
    insert_data ={'post_id': post_id, 'title': title,'content': content}
    db.posts.insert_one(insert_data)

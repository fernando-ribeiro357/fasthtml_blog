from fasthtml import FastHTML
from dotenv import load_dotenv
from app.templates import blog_list_template, create_post_template, show_post_template
from app.models import get_all_posts, create_post, get_post

load_dotenv()

app = FastHTML()

@app.route("/")
def index():
    posts = get_all_posts()
    return blog_list_template(posts)

@app.route("/create", methods=["GET"])
def create_post_get():
    return create_post_template()

@app.route("/show/{id}", methods=["GET"])
def show_post_get(id:str):
    post = get_post(id)
    return show_post_template(post)

# Define this as an async function to handle form data properly
@app.route("/create", methods=["POST"])
async def create_post_post(request):
    form_data = await request.form()  # Await for the form data
    title = form_data.get("title")
    content = form_data.get("content")
    create_post(title, content)
    return f"<h2>Post '{title}' created! <a href='/'>Go back</a></h2>"
    
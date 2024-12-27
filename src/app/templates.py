def blog_list_template(posts):
    return f"""
    <html>
        <head><title>Postagens do Blog</title></head>
        <body>
            <h1>Todas as postagens</h1>
            <ul>
                {''.join([f'<li><a href="/show/{post["post_id"]}">{post["title"]}</a></li>' for post in posts])}
            </ul>
            <a href="/create">Novo ⊞</a>
        </body>
    </html>
    """

def show_post_template(post):
    return f"""
    <html>
        <head><title>Postagem | {post["title"]}</title></head>
        <body>
            <a href="/">↰ Voltar</a>
            <h3>{post["title"]}</h3>
            
            <p>{post["content"]}<br><small>post_id: {post["post_id"]}</small></p>
            <a href="/create">Novo ⊞</a>
        </body>
    </html>
    """

def create_post_template():
    return """
    <html>
        <head><title>Criar nova postagem</title></head>
        <body>
            <h1>Criar uma nova postagem</h1>
            <form action="/create" method="post">
                <label for="title">Título:</label><br>
                <input type="text" id="title" name="title"><br>
                <label for="content">Conteúdo:</label><br>
                <textarea id="content" name="content"></textarea><br>
                <input type="submit" value="Enviar">
            </form>
            <a href="/">↰ Voltar</a>
        </body>
    </html>
    """
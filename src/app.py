import flask as f

app = f.Flask(__name__)

@app.route("/")
def home():
    return f.render_template("home.html")

@app.route("/search")
def search():
    query = f.request.args.get('query')
    indices = f.request.args.getlist('index')
    sort = f.request.args.get('sort')
    results = [
        {"url":"https://example.com","title":"An example webpage","extract":"This is an extract from an example webpage."},
        {"url":"https://example.com","title":"An example webpage","extract":"This is an extract from an example webpage."},
        {"url":"https://example.com","title":"An example webpage","extract":"This is an extract from an example webpage."},
        {"url":"https://example.com","title":"An example webpage","extract":"This is an extract from an example webpage."},
        {"url":"https://example.com","title":"An example webpage","extract":"This is an extract from an example webpage."}
    ]
    return f.render_template("search.html", query=query, indices=indices, sort=sort, results=results)
from flask import Flask
from views import views
from flask import render_template

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
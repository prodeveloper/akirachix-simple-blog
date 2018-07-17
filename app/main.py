from flask import (Flask,
                   render_template,
                   redirect,
                   url_for
                   )
import models.blog
from forms.blog import NewBlogForm
from models.blog import Blog

app = Flask('app')
app.secret_key = 'f573617a-832a-11e8-96db-acde48001122'
models.blog.initialize()


@app.route('/')
def index():
    blogs = models.blog.Blog.select()
    return render_template('index.html', blogs=blogs)


@app.route('/new', methods=['POST', 'GET'])
def new_blog():
    form = NewBlogForm()
    if form.validate_on_submit():
        Blog.add_blog(
            title=form.title.data,
            body=form.body.data
        )
        return redirect(url_for('index'))
    return render_template('new_blog.html', form=form)

@app.route('/view/<id>')
def view_blog(id):
    blog = Blog.get(Blog.id == id)
    return render_template('view_blog.html', blog=blog)



app.run(debug=True, host='0.0.0.0', port=8080)

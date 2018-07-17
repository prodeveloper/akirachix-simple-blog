from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    DateTimeField,
                    IntegrityError)
import datetime
db = SqliteDatabase("blogs.db")
sample_blogs = [
    {'title': 'Tuesday class',
     'body': 'Today I learnt how to work with images'},
    {'title': 'Saturday afternoon', 'body': 'Relaxed with my family'}
]


class Blog(Model):
    title = CharField(max_length=1000, default="Blog title", unique=True)
    body = TextField(default="Body of the blog")
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    @classmethod
    def add_blog(cls, title, body):
        try:
            Blog.create(
                title=title,
                body=body
            )
        except IntegrityError:
            raise ValueError("Blog title exists, chose a different one")


def initialize():
    db.connect()
    db.create_tables([Blog], safe=True)
    for blog in sample_blogs:
        try:
            Blog.add_blog(
                title=blog.get('title'),
                body=blog.get('body')
            )
        except ValueError:
            pass

    db.close()

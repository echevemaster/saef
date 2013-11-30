from saef_app.core.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    def __init__(self, name, surname, username, email, password,  active):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<User %r' % self.username


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    pages = db.relationship('Page', backref='category',
                            lazy='dynamic')
    active = db.Column(db.Boolean())

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.active = active

    def __repr__(self):
        return '<name %r' % self.name


class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text())
    date = db.Column(db.DateTime())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    active = db.Column(db.Boolean())

    def __init__(self, title, description, date, category_id):
        self.title = title
        self.description = description
        self.date = date
        self.category_id = category_id

    def __repr__(self):
        return '<Title %r' % self.title

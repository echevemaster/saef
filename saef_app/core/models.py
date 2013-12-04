from saef_app.core.database import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.Integer, default=ROLE_USER)
    active = db.Column(db.Boolean())

    def __init__(self, name, surname, username, email, password, role, active):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.active = active

    def __repr__(self):
        return '<User %r' % self.username


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    pages = db.relationship('Service', backref='category',
                            lazy='dynamic')
    active = db.Column(db.Boolean())

    def __init__(self, name, description, active):
        self.name = name
        self.description = description
        self.active = active

    def __repr__(self):
        return '<name %r' % self.name


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    description = db.Column(db.Text())
    date = db.Column(db.DateTime())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    image_url = db.Column(db.String())
    active = db.Column(db.Boolean())

    def __init__(self, title, slug, description, date, category_id,
                 image_url, active):
        self.title = title
        self.slug = slug
        self.description = description
        self.date = date
        self.image_url = image_url
        self.category_id = category_id
        self.active = active

    def __repr__(self):
        return '<Title %r' % self.title

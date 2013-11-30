from flask import Blueprint, render_template, abort, request, redirect, \
    flash, url_for
from jinja2 import TemplateNotFound
from saef_app.core.database import db
from saef_app.core.forms import AddUserForm, EditUserForm, AddCategoryForm
from saef_app.core.models import User, Category
from saef_app.core.common import RESULTS_PER_PAGE
bundle = Blueprint('admin', __name__, template_folder='templates',
                   static_folder='static')


@bundle.route('/admin', methods=['GET', 'POST'])
def index():
    try:
        return render_template('admin/index.html')
    except TemplateNotFound:
        abort(404)


@bundle.route('/admin/user', methods=['GET', 'POST'])
@bundle.route('/admin/user/<int:page>', methods=['GET', 'POST'])
def user(page=1):
    users = User.query.paginate(page, RESULTS_PER_PAGE, False)
    try:
        return render_template('admin/user.html',
                               title=u'Listar usuarios',
                               users=users)
    except TemplateNotFound:
        abort(404)


@bundle.route('/admin/user/add', methods=['GET', 'POST'])
def adduser():
    form = AddUserForm()
    form_action = url_for('admin.adduser')
    if request.method == 'POST' and form.validate():
        user = User(form.name.data,
                    form.surname.data,
                    form.username.data,
                    form.email.data,
                    form.password.data,
                    form.active.data
                    )
        db.session.add(user)
        db.session.commit()
        flash(u'Usuario Creado')
        return redirect(url_for('admin.user'))
    return render_template('admin/add_user.html',
                           title=u"Crear usuario",
                           form_action=form_action,
                           form=form)


@bundle.route('/admin/user/edit/<user_id>', methods=['GET', 'POST'])
def edituser(user_id):
    quser = User.query.filter(User.username == user_id).first_or_404()
    form = EditUserForm(obj=quser)
    form_action = url_for('admin.edituser', user_id=user_id)
    if request.method == 'POST' and form.validate():
        form.populate_obj(quser)
        db.session.commit()
        flash(u'Usuario actualizado')
        return redirect(url_for('admin.user'))
    return render_template('admin/add_user.html',
                           title=u"Editar usuario",
                           form_action=form_action,
                           form=form,
                           user_id=user_id)


@bundle.route('/admin/user/delete', methods=['GET', 'POST'])
def deleteuser():
    ret_data = request.args.get('item')
    duser = User.query.filter(User.username == ret_data).first_or_404()
    if request.method == 'GET':
        db.session.delete(duser)
        db.session.commit()
        flash(u'Usuario eliminado')
    return "OK"


@bundle.route('/admin/categories', methods=['GET', 'POST'])
@bundle.route('/admin/categories/<int:page>', methods=['GET', 'POST'])
def category(page=1):
    categories = Category.query.paginate(page, RESULTS_PER_PAGE, False)
    try:
        return render_template('admin/category.html',
                               title=u'Listar categorias',
                               categories=categories)
    except TemplateNotFound:
        abort(404)


@bundle.route('/admin/category/add', methods=['GET', 'POST'])
def addcategory():
    form = AddCategoryForm()
    form_action = url_for('admin.addcategory')
    if request.method == 'POST' and form.validate():
        category = Category(form.name.data,
                            form.description.data,
                            form.active.data
                            )
        db.session.add(category)
        db.session.commit()
        flash(u'categoria Creada')
        return redirect(url_for('admin.category'))
    return render_template('admin/category_forms.html',
                           title=u"Crear Categoria",
                           form_action=form_action,
                           form=form)

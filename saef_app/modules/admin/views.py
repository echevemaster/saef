from flask import Blueprint, render_template, abort, request, redirect, \
    flash, url_for
from jinja2 import TemplateNotFound
from saef_app.core.database import db
from saef_app.core.forms import AddUserForm, EditUserForm
from saef_app.core.models import User
from saef_app.core.common import RESULTS_PER_PAGE
bundle = Blueprint('admin', __name__, template_folder='templates',
                   static_folder='static')


@bundle.route('/admin', methods=['GET', 'POST'])
def index():
    try:
        return render_template('admin/index.html')
    except TemplateNotFound:
        abort(404)


@bundle.route('/admin', methods=['GET', 'POST'])
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
    quser = User.query.filter_by(username=user_id).first()
    form = EditUserForm(obj=quser)
    form_action = url_for('admin.edituser', user_id=user_id)
    if request.method == 'POST' and form.validate():
        quser.name = form.name.data,
        quser.surname = form.surname.data,
        quser.username = form.username.data,
        quser.email = form.email.data,
        quser.active = form.active.data
        db.session.commit()
        flash(u'Usuario actualizado')
    return render_template('admin/add_user.html',
                           title=u"Editar usuario",
                           form_action=form_action,
                           form=form,
                           user_id=user_id)

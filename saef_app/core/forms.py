#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SelectField, \
    TextAreaField, DateField, FileField
from wtforms.validators import Required, Email, EqualTo


class AddUserForm(Form):
    name = TextField(u'Nombres <small>Requerido</small>',
                     [Required(message=u'Debe proporcionar su nombre')])
    surname = TextField(u'Apellidos',
                        [Required(message=u'Debe proporcionar su apellido')])
    username = TextField(u'Username', [Required(message=u'Campo Requerido')])
    email = TextField(u'Email', [Email(message=u'Email no válido')])
    password = PasswordField(u'Contraseña', [
                             Required(message=u'Campo Requerido'),
                             EqualTo('confirm', message=u'Las contraseñas \
                                                         no coinciden')
                             ])
    role = SelectField(u'Rol',
                       choices=[(0, 'Usuario'),
                                (1, 'Admin')
                                ],
                       coerce=int
                       )
    confirm = PasswordField(u'Repita su contraseña')
    active = BooleanField(u'Activar usuario?')


class EditUserForm(AddUserForm):
    password = None
    confirm = None


class AddCategoryForm(Form):
    name = TextField(u'Categoria', [Required(message=u'Campo requerido')])
    description = TextField(u'Descripcion',
                            [Required(message=u'Campo requerido')])
    active = BooleanField(u'Activar categoria?')


class AddServiceForm(Form):
    title = TextField(u'Titulo', [Required(message=u'Campo requerido')])
    slug = TextField(u'Slug', [Required(message=u'Campo requerido')])
    description = TextAreaField(u'Contenido',
                                [Required(message=u'Campo requerido')])
    date = DateField(u'Fecha',
                     [Required(message=u'Campo requerido')],
                     format='%Y-%m-%d')
    image_url = FileField(u'Imagen')
    category_id = SelectField(u'Categoria', coerce=int)
    active = BooleanField(u'Activar Servicio?')

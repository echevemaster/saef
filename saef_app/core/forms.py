#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required, Email, EqualTo


class AddUserForm(Form):
    name = TextField(u'Nombres', [Required(message=u'Campo Requerido')])
    surname = TextField(u'Apellidos', [Required(message=u'Campo Requerido')])
    username = TextField(u'Username', [Required(message=u'Campo Requerido')])
    email = TextField(u'Email', [Email(message=u'Email no válido')])
    password = PasswordField(u'Contraseña', [
                             Required(message=u'Campo Requerido'),
                             EqualTo('confirm', message=u'Las contraseñas \
                                                         no coinciden')
                             ])
    confirm = PasswordField(u'Repita su contraseña')
    active = BooleanField(u'Activar usuario?', [Required(message=u'Campo \
                                                         Requerido')])


class EditUserForm(AddUserForm):
    password = PasswordField(u'Contraseña', [
                             Required(message=u'Campo Requerido'),
                             ])
    confirm = None

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask.ext import wtf
import wtforms


class AddVBSpeedyForm(wtf.Form):
    script = wtforms.TextAreaField(
        'Script:',
        [wtforms.validators.Required()])
    title = wtforms.TextField(
        'Title',
        [wtforms.validators.Required()])

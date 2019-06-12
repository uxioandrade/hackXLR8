from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import (Required, Length, Email, ValidationError,
                                EqualTo)
from app.models import User

class Submission(Form):

    ''' User login form. '''

    url = TextField(validators=[Required()],
                      description='Url')


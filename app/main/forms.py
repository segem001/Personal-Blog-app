from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import input_required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [input_required()])
    submit = SubmitField('Submit')



class CommentForm(FlaskForm):
    comment = TextAreaField('Leave your comment...',validators = [input_required()])
    submit = SubmitField('Submit')


class AddPost(FlaskForm):
    title = TextAreaField('Title.')
    subtitle = TextAreaField('Subtitle.')
    content = TextAreaField('Content')
    submit = SubmitField('Submit')


class SubscriberForm(FlaskForm):

    email = StringField('Your Email Address...')
    name = StringField('Enter your name')
    submit = SubmitField('Subscribe')


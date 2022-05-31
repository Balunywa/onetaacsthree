from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, 
                     SubmitField, RadioField, 
                     SelectField, DateTimeField, 
                     BooleanField, TextAreaField)
from wtforms.validators import DataRequired

class PostEventForm(FlaskForm):
    event_types = StringField('Event name:', validators=[DataRequired()])
    phone_or_email = StringField('Loved one phone or email:',validators=[DataRequired()])
    accompained_by = StringField('Who are are you with:')
    comment = StringField('Comments:')
    submit = SubmitField('Post event type')
    
class DelEventForm(FlaskForm):
    id = IntegerField('Id number of the event to remove: ')
    submit = SubmitField('Remove Event')
    
    
    
    
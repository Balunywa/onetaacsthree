from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, 
                     SubmitField, RadioField, 
                     SelectField, DateTimeField, 
                     BooleanField, TextAreaField)
from wtforms.validators import DataRequired

class PostEventForm(FlaskForm):
    event_types = StringField('Event name:', validators=[DataRequired()])
    phone_or_email = StringField('Loved one phone or email:',validators=[DataRequired()])
    acompained_by = StringField('Who are you with:')
    submit = SubmitField('Post event type')
    
class DelEventForm(FlaskForm):
    event_type_id = IntegerField('Id Number of the Event to Remove: ')
    submit = SubmitField('Remove Event')
    
    
    
    
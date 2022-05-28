from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class PostEventForm(FlaskForm):
    event_types = StringField('Event name: ')
    loved_ones_name = StringField('Loved ones name: ')
    phone_or_email = StringField('Phone no or Email: ')
    submit = SubmitField('Post event type')
    
class DelEventForm(FlaskForm):
    event_type_id = IntegerField('Id Number of the Event to Remove: ')
    submit = SubmitField('Remove Event')
    
    
    
    
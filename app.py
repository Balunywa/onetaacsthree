from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, 
                     BooleanField, DateTimeField, 
                     RadioField, SelectField, 
                     TextAreaField)

from wtforms.validators import DataRequired

# from flask import Flask  # From 'flask' module import 'Flask' class
app = Flask(__name__)  # Construct an instance of Flask class for our webapp

app.config['SECRET_KEY'] = 'test'

class InfoForm(FlaskForm):
    
    timedeparted = StringField ('Departure Time')
    location = StringField ('Location',validators=[DataRequired()])
    carplate = StringField('Car No Plate', validators=[DataRequired()])
    phonenumber = StringField('Phone Number', validators=[DataRequired()])
    select = SelectField('Person Your Visiting', choices=[('Lukman', 'Lukman'), 
                                                         ('Dawne', 'Dawne')], validators=[DataRequired()])
    relationship = RadioField('Please chose relationship', 
                              choices=[('Family', 'Family'), 
                              ('Old-Friend', 'Old_Friend'), ('New_Friend', 'New_Friend')])
    event = RadioField('Please chose the event',
                       choices=[('Party', 'Party'), ('Clubing','Clubing'), 
                                ('Shopping', 'Shopping'), ('Other', 'Other')])
    feedback = TextAreaField('Any Other Notes')
    enter = SubmitField('Enter')
        
@app.route('/',methods=['GET', 'POST'])

def index():
         
    form = InfoForm()
    
    if form.validate_on_submit(): 
        
        session['timedeparted'] = form.timedeparted.data
        session['location'] = form.location.data
        session['carplate'] = form.carplate.data
        session['phonenumber'] = form.phonenumber.data
        session['select'] = form.select.data
        session['relationship'] = form.relationship.data
        session['event'] = form.event.data
        session['feedback'] = form.feedback.data
        
        return redirect(url_for('thankyou'))
            
    return render_template('home.html',form=form)

@app.route('/thankyou')
def thankyou ():
    
    return render_template('thankyou.html')

    
if __name__ == '__main__':
    app.run(debug=True)
    
    
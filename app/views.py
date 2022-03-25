"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app,db
from flask import render_template, request, redirect, session, url_for, flash, send_from_directory

from flask import render_template, request, redirect, url_for
from .forms import AddPropertyForm
from werkzeug.utils import secure_filename
from app.model import Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Wayne Clarke")


@app.route('/properties/create',methods = ['POST','GET'])
def addprop():
    form = AddPropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            property_title = form.property_title.data
            no_of_rooms = form.no_of_rooms.data
            no_of_bath = form.no_of_bath.data
            location = form.location.data
            price = form.price.data
            property_type = form.property_type.data
            desc = form.description.data
            img = form.photo.data
            imgName = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], imgName))
            prop = Property(property_title = property_title,description =desc, no_of_rooms = no_of_rooms, no_of_bath = no_of_bath,
             price = price, property_type = property_type, location = location, photo = imgName)
            db.session.add(prop)
            db.session.commit()

            flash('Property has been Successfully added!!', 'success')

            return redirect(url_for('properties'))
        
    return render_template('addprop.html',form = form)    


@app.route('/properties')
def properties():
    prop = db.session.query(Property).all()
    return render_template('properties.html',prop = prop)


@app.route('/properties/<propertyid>')
def propid(propertyid):
    propertyid = Property.query.filter_by(property_id = int(propertyid)).first()
    return render_template('property.html', prop = propertyid)


@app.route('/uploads/<imgname>')
def property_photo(imgname):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), imgname)




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

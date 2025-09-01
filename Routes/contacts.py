from flask import Blueprint, render_template, request, redirect, url_for, flash
from Models.contact import contact
from Utils.database import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    
    contacts = contact.query.all()
    return render_template("Index.html", contacts=contacts)

@contacts.route("/new" , methods=["POST"])
def add_contact():

    name = request.form.get("name")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")
    contact_new = contact(name, phone_number, email)
    db.session.add(contact_new)
    db.session.commit()

    flash("Contacto agregado satisfactoriamente")

    return redirect(url_for('contacts.home'))

@contacts.route("/update/<id>", methods=["GET", "POST"])
def update_contact(id):

    contact_to_update = contact.query.get(id)

    if request.method == "POST":
        
        contact_to_update.name = request.form.get("name")
        contact_to_update.email = request.form.get("email")
        contact_to_update.phone_number = request.form.get("phone_number")
        db.session.commit()

        flash("Contacto actualizado satisfactoriamente")

        return redirect(url_for('contacts.home'))

    return render_template('Update.html', contact=contact_to_update)

@contacts.route('/delete/<id>')
def delete_contact(id):

    contact_to_delete = contact.query.get(id)
    db.session.delete(contact_to_delete)
    db.session.commit()
    flash("Contacto eliminado satisfactoriamente")

    return redirect(url_for('contacts.home'))
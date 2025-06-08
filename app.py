from flask import Flask, request, render_template, url_for, redirect, flash
import os
from dotenv import load_dotenv
from pydb import PyDB, Contacto
app = Flask(__name__)
load_dotenv()  # Cargar las variables de entorno desde el archivo .env

app.secret_key =  os.getenv('SECRET_KEY')

@app.route('/')
def index():
    with PyDB('agenda.db') as db:
        contactos = db.get_contacts()
    if contactos:
        
        return render_template('index.html', contactos=contactos)
    else:
        
        return render_template('index.html', mensage='No hay contactos en la agenda')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        contacto = Contacto(nombre, telefono, email)
        with PyDB('agenda.db') as db:
          db.insert_contact(contacto)
          db.close()
        return render_template('index.html', mensage='Contacto agregado exitosamente')
    return render_template('registro.html')

@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete(contact_id):
    with PyDB('agenda.db') as db:
        db.delete_contact(contact_id)
    flash('Contacto eliminado exitosamente')
    return redirect(url_for('index'))

@app.route('/update/<int:contact_id>', methods=['GET', 'POST'])
def update(contact_id):
    with PyDB('agenda.db') as db:
        contacto = db.get_contacts()
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        contacto = Contacto(nombre, telefono, email)
        with PyDB('agenda.db') as db:
            db.update_contact(contact_id, contacto)
            flash('Contacto actualizado exitosamente')
        return redirect(url_for('index'))
    return render_template('update.html', contact_id=contact_id)
   


if __name__ == '__main__':
    
    app.run(debug=True)
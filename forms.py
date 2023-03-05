from wtforms import Form, StringField, IntegerField, EmailField, validators

#Al poner en el parentesis el nombre de una clase esta se hereda
class UserForm(Form):
    id = IntegerField("id")
    nombre = StringField("nombre")
    apellidos = StringField("apellidos")
    email = EmailField("correo")
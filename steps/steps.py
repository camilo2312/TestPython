from behave import *
import requests


base_url = "http://localhost:6061"
token = None

@given('soy un usuario nuevo')
def newUser(context):
        

    @when('se envia solicitud para crear un usuario con cedula {cedula}, nombre {nombre}, apellido {apellido}, correo electrónico {correo}, contraseña {contrasena}')
    def create_user(context, cedula, nombre, apellido, correo, contrasena):
        end_point = base_url + '/users'
        payload = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "email": correo,
            "contrasena": contrasena
        }
        
        response = requests.post(end_point, json=payload)
        context.response = response

@given('soy un usuario registrado')
def old_user(context):

    @when('se enviá una solicitud para hacer login cn un email {email} y contraseña {contrasena}')
    def login(context, email, contrasena):
        end_point = base_url + '/login'
        payload = {
            'email': email,
            'password': contrasena
        }
        response = requests.post(end_point, json=payload)
        context.response = response

@then('se recibe una respuesta exitosa')
def validate_success_response(context):
    assert context.response.status_code == 200, 'Error al realizar el login'

@then('se valida el token generado')
def validate_token(context):
    token = context.response.json()['token']
    assert token != '', 'Token no generado'

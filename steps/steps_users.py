from behave import *
import requests
import json


base_url = "http://localhost:6061"
token = ''

# Escenario de creación de usuario
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
        
@then('se recibe una respuesta exitosa después de crear el usuario')
def validate_create_user_success_response(context):
    assert context.response.status_code == 200, 'Error al crear el usuario'
    
#Fin de escenario de creación de usuario

# Esenario de login
@given('soy un usuario registrado')
def old_user(context):

    @when('se enviá una solicitud para hacer login cn un email {email} y contraseña {contrasena}')
    def login(context, email, contrasena):
        global token
        end_point = base_url + '/login'
        payload = {
            'email': email,
            'password': contrasena
        }
        response = requests.post(end_point, json=payload)
        if response.status_code == 200:
            token = response.json()["token"]
        context.response = response

@then('se recibe una respuesta exitosa al realizar el login')
def validate_success_response(context):
    assert context.response.status_code == 200, 'Error al realizar el login'

@then('se valida el token generado')
def validate_token(context):
    assert "token" in context.response.json()
    
#Fin de escenario de login

# Escenario Obtener información de un usuario existente
@given('exista un token')
def exist_token(context):
    assert token != '', 'No hay token'
    
@when('se envía una solicitud para obtener la información de un usuario con cedula {cedula}')
def validate_exists_user(context, cedula):
    end_point = base_url + "/user/" + cedula
    headers = {"Authorization": f'Bearer {token}'}
    response = requests.get(end_point, headers=headers)
    context.response = response

@then('se recibe una respuesta existosa con la información del usuario')
def validate_response_information_user(context):
    users = context.response.json()['data']
    first_user = users[0]
    name = first_user['nombre']
    assert name == 'Daniel', 'No existe el usuario'

#Fin escenario obtener información de un usuario

#Escenario Actualizar la información de un usuario existente
@given('que exista un usuario con cedula {cedula}')
def validate_exists_user(context, cedula):
    end_point = base_url + "/user/" + cedula
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(end_point, headers=headers)
    context.response = response
    user_cedula = response.json()['data'][0]['cedula'];
    assert user_cedula == cedula, 'No existe el usuario con cedula ' + cedula

@when('se envía una solicitud para actualizar la información del usuario con cedula {cedula} correo {email}, nombre {nombre}, apellido {apellido}')
def update_user(context, cedula, email, nombre, apellido):
    end_point = base_url + "/users/" + cedula            
    
    payload = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "contrasena": '1234'
        }
    headers = {"Authorization": f'Bearer {token}'}
    response = requests.put(end_point, json=payload, headers=headers)
    context.response = response

@then('se recibe una respuesta exitosa después de actualizar el usuario')
def validate_response(context):
    print(context.response.status_code)
    assert context.response.status_code == 200, 'Error al actualizar el usuario'

@then('el correo electrónico del usuario con cedula {cedula} se actualiza a {email} en la base de datos')
def is_update(context, cedula, email):
    end_point = base_url + "/user/" + cedula
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(end_point, headers=headers)
    user_email = response.json()['data'][0]['email']
    assert user_email == email, 'No se actualizó el usuario'

#Fin escenario de actualización

#Escenario elmiminar un usuario
@given('exista un usuario con cedula {cedula}')
def validate_exists_user(context, cedula):
    end_point = base_url + "/user/" + cedula
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(end_point, headers=headers)
    user_cedula = response.json()['data'][0]['cedula']
    assert user_cedula == cedula, 'No existe usuario con cedula ' + cedula

@when('se envía una solicitud para eliminar el usuario con cedula {cedula}')
def delete_user(context, cedula):
    end_point = base_url + "/users/" + cedula
    headers = {"Authorization": "Bearer " + token}
    response = requests.delete(end_point, headers=headers)
    context.response = response

@then('se recibe una respuesta exitosa al eliminar un usuario')
def validate_success_response(context):
    assert context.response.status_code == 200, 'Error al eliminar el usuario'

@then('el usuario con cedula {cedula} se elimino correctamente de la base de datos')
def validate_delete_user(context, cedula):
    end_point = base_url + "/user/" + cedula
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(end_point, headers=headers)
    assert 'No existe usuario' in  response.json()['message'], 'Error al validar usuario'
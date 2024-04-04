Feature: Gestión de usuarios

  Scenario: Crear un nuevo usuario
    Given Soy un usuario nuevo
    When se envia solicitud para crear un usuario con cedula 1007603570, nombre John, apellido Perez, correo electrónico john@example.com, contraseña 1234 
    Then se recibe una respuesta exitosa después de crear el usuario
  
  Scenario: Iniciar sesión
    Given soy un usuario registrado
    When se enviá una solicitud para hacer login cn un email camiramos234@gmail.com y contraseña 1234
    Then se recibe una respuesta exitosa al realizar el login
    And se valida el token generado
  
  Scenario: Obtener información de un usuario existente
    Given exista un token
    When se envía una solicitud para obtener la información de un usuario con cedula 222
    Then se recibe una respuesta existosa con la información del usuario
  
  Scenario: Actualizar la información de un usuario existente
    Given que exista un usuario con cedula 333
    When se envía una solicitud para actualizar la información del usuario con cedula 333 correo newbob@example.com, nombre Orlando, apellido Narvaez
    Then se recibe una respuesta exitosa después de actualizar el usuario
    And el correo electrónico del usuario con cedula 333 se actualiza a newbob@example.com en la base de datos

  Scenario: Eliminar un usuario existente
    Given exista un usuario con cedula 987654321
    When se envía una solicitud para eliminar el usuario con cedula 987654321
    Then se recibe una respuesta exitosa al eliminar un usuario
    And el usuario con cedula 987654321 se elimino correctamente de la base de datos 
 
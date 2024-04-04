Feature: Gestión de usuarios

  Scenario: Crear un nuevo usuario
    Given Soy un usuario nuevo
    When se envia solicitud para crear un usuario con cedula 1234567890, nombre John, apellido Perez, correo electrónico john@example.com, contraseña 1234 
    Then se recibe una respuesta exitosa
  
  Scenario: Iniciar sesión
    Given soy un usuario registrado
    When se enviá una solicitud para hacer login cn un email camiramos234@gmail.com y contraseña 1234
    Then se recibe una respuesta exitosa
    And se valida el token generado
  
  Scenario: Obtener información de un usuario existente
    Given que exista un usuario con cedula 222
    When se envía una solicitud para obtener la información de un usuario con cedula 222
    Then se reciba una respuesta existosa con la información del usuario
  
  Scenario: Actualizar la información de un usuario existente
    Give que exista un usuario con cedula 333
    When se envía una solicitud para actualizar el correo electrónico del usuario con cedula 333 a newbob@example.com
    Then se recibe una respuesta exitosa
    And el correo electrónico del usuario con cedula 333 se actualiza a newbob@example.com en la base de datos

  Scenario: Eliminar un usuario existente
    Given que exista un usuario con cedula 123456789
    When se envía una solicitud para eliminar el usuario con cedula 123456789
    Then se recibe una respuesta exitosa
    And el usuario con cedula 123456789 se elimino correctamente de la base de datos 
  
  Scenario: Recuperar la contraseña de un usuario
    Given que exista un usuario con cedula 1005308685
    When se envía una solicitud para recuperar la contraseña de un usuario con cedula 1005308685
    Then se recibe una respuesta exitosa
    And el link de la url para el cambio de contraseña se obtiene correctamente
 
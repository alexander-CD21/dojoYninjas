from dojo_app.config.mysqlconnection import connectToMySQL
from dojo_app.modelos import modelo_ninjas

class Dojo:
    def __init__( self, datos ):
        self.id = datos['id']
        self.name = datos['name']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        self.ninjas = []
    
    @classmethod
    def mostrarNinjas( cls):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL( "dojos_and_ninjas_schema" ).query_db( query)
        dojos = []

        for dojo in resultado:
            dojos.append(cls(dojo))
        return dojos 

    @classmethod
    def mostrarDojosYNinjas( cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id  WHERE ninjas.dojo_id = %(dojoId)s;"
        resultado = connectToMySQL( "dojos_and_ninjas_schema" ).query_db( query, data )

        if len( resultado ) > 0:
            dojo = cls(resultado[0])
        else:
            dojo = []

        for alumno in resultado:
            print(alumno)
            ninjaData = {
                "id": alumno['ninjas.id'],
                "first_name": alumno['first_name'],
                "last_name": alumno['last_name'],
                "age": alumno['age'],
                "created_at": alumno['ninjas.created_at'],
                "updated_at": alumno['ninjas.updated_at']
            }
            dojo.ninjas.append(modelo_ninjas.Ninja(ninjaData))
        return dojo

    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)


























    @classmethod
    def obtenerListaUsuarios( self ):
        query = "SELECT * FROM usuarios;"
        resultado = connectToMySQL( "usuarios_db" ).query_db( query )
        listaUsuarios = []
        for usuario in resultado:
            listaUsuarios.append( Usuario( usuario["nombre"], usuario["apellido"], usuario["nombreusuario"], usuario["password"], usuario["id_departamento"]) )
        return listaUsuarios
    
    @classmethod
    def eliminarUsuario( self, usuario ):
        query = "DELETE FROM usuarios WHERE nombreusuario = %(nombreusuario)s;"
        resultado = connectToMySQL( "usuarios_db" ).query_db( query, usuario )
        return resultado

    @classmethod
    def obtenerDatosUsuario( self, usuario ):
        query = "SELECT * FROM usuarios WHERE nombreusuario = %(nombreusuario)s;"
        resultado = connectToMySQL( "usuarios_db" ).query_db( query, usuario )
        return resultado
    
    @classmethod
    def editarUsuario( self, usuarioAEditar ):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, password = %(password)s, id_departamento = %(id_departamento)s WHERE nombreusuario = %(nombreusuario)s;"
        resultado = connectToMySQL( "usuarios_db" ).query_db( query, usuarioAEditar )
        return resultado
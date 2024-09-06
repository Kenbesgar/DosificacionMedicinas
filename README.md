# Dosificacion Medica 

https://dosificacion-fqdafxhqe9d7hgd0.brazilsouth-01.azurewebsites.net/

  

## Descripción 

Nuestra aplicación de dosificación médica, alojada en la nube de Azure, está diseñada para optimizar y personalizar la administración de medicamentos para pacientes. Utilizando las capacidades avanzadas de Azure Health Data Services, la aplicación garantiza la seguridad y privacidad de los datos médicos protegidos. 

  

## Descripción de la Arquitectura 

1.Desarrollo de Interfaz gráfica en visual studio 

2.Base de Datos en PgAdmin  

3.Se subio la app grafica a azure 

4.Se creo y conecto la base de dtos con azure 

5.Se interconecto la app service y data base. 

## Pasos de Despliegue

### Preparativos Iniciales
1. Asegúrate de tener una cuenta en azure.
2. Instala visual y configura data base en postgres.

### Instrucciones de Despliegue
1. Clona el repositorio: git clone [URL del Repositorio]
2. Configura las variables de entorno en el archivo .env.
3. Ejecuta el script de despliegue: ./deploy.sh
4. Verifica el estado de la aplicación accediendo a [URL de la Aplicación].
5.Configurar la Base de Datos: Asegúrate de que la base de datos esté configurada y accesible desde el servidor.
Esto puede incluir la creación de tablas, usuarios, y permisos necesarios.
6.Desplegar la Aplicación: Usa las herramientas del servidor para desplegar la aplicación. Por ejemplo, en Tomcat, puedes copiar el archivo WAR a la carpeta webapps.
7.Probar la Aplicación: Accede a la aplicación desde un navegador web para asegurarte de que todo funcione correctamente.
Realiza pruebas exhaustivas para verificar que no haya errores.

###Conexión ADB

##Instalar ADB:

1.Descarga ADB desde el sitio oficial de Android o usa un paquete independiente1.
2.Descomprime el archivo ZIP en una carpeta accesible, por ejemplo, C:\ADB.

##Activar la Depuración USB en tu Android:

1.Ve a Ajustes > Acerca del teléfono.
2.Pulsa varias veces sobre Número de compilación hasta activar las Opciones de desarrollador.
3.En Opciones de desarrollador, activa Depuración por USB.

##Conectar el Dispositivo:

1.Conecta tu dispositivo Android al PC mediante un cable USB.
2.Abre una terminal de comandos en la carpeta donde descomprimiste ADB (C:\ADB).
3.Ejecuta adb devices para verificar que tu dispositivo está conectado.
  

### Componentes y Servicios 

- *Servidor de Aplicaciones:  Implementado en Azure, gestiona la lógica de la aplicación. 

- *Base de Datos: Desarrollado en MySQL, almacena toda la información de los usuarios. 

- *Servicio de Autenticación: Flask, Microsoft Defender for cloud que asegura la autenticidad de los usuarios. 

###CRUD

##CONECCION A LA BASE DE DATOS

<?php
$servername = "nombre_del_servidor"; 
$username = "usuario";
$password = "contraseña";
$dbname = "nombre_base_datos";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
?>

##CREAR

<?php
if(isset($_POST['submit'])){
    $nombre = $_POST['nombre'];
    $dosis = $_POST['dosis'];

    $sql = "INSERT INTO medicamentos (nombre, dosis) VALUES ('$nombre', '$dosis')";

    if ($conn->query($sql) === TRUE) {
        echo "Nuevo medicamento añadido correctamente.";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
?>
<form method="POST">
    Nombre: <input type="text" name="nombre" required>
    Dosis: <input type="text" name="dosis" required>
    <button type="submit" name="submit">Añadir Medicamento</button>
</form>

##LEER

<?php
$sql = "SELECT id, nombre, dosis FROM medicamentos";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["id"]. " - Nombre: " . $row["nombre"]. " - Dosis: " . $row["dosis"]. "<br>";
    }
} else {
    echo "0 resultados";
}
?>

##ACTUALIZAR

<?php
if(isset($_POST['update'])){
    $id = $_POST['id'];
    $nombre = $_POST['nombre'];
    $dosis = $_POST['dosis'];

    $sql = "UPDATE medicamentos SET nombre='$nombre', dosis='$dosis' WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        echo "Medicamento actualizado correctamente.";
    } else {
        echo "Error actualizando el medicamento: " . $conn->error;
    }
}
?>
<form method="POST">
    ID del Medicamento: <input type="text" name="id" required>
    Nuevo Nombre: <input type="text" name="nombre">
    Nueva Dosis: <input type="text" name="dosis">
    <button type="submit" name="update">Actualizar Medicamento</button>
</form>

##ELIMINAR

<?php
if(isset($_POST['delete'])){
    $id = $_POST['id'];

    $sql = "DELETE FROM medicamentos WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        echo "Medicamento eliminado correctamente.";
    } else {
        echo "Error eliminando el medicamento: " . $conn->error;
    }
}
?>
<form method="POST">
    ID del Medicamento a Eliminar: <input type="text" name="id" required>
    <button type="submit" name="delete">Eliminar Medicamento</button>
</form>

### Tecnologías Utilizadas 

- *Lenguaje de Programación: HTML (PHP) 

- *Framework: Django 

- *Servicio de Nube: Azure 

- *Otros Servicios: Github 

 

     

  

### Middleware 

- Django se utiliza para manejar solicitudes http y conectarse a las bases de datos. 

- Este middleware facilita no tener que escribir el codigo desde cero para esas tareas y brinda herramientas y componentes que simplifican estas tareas. 



## Contacto 

Para consultas o soporte, por favor contacta a Kendry Esteban Becerra en 

kebecerra@uts.edu.co o Juan Diego Bueno en juandiegobueno@uts.edu.co 

 

 

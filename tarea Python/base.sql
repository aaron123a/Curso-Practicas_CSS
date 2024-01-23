	CREATE DATABASE IF NOT EXISTS Empleados;
	USE Empleados;
	
	CREATE TABLE IF NOT EXISTS ControlDeEmpleados (
	    ID INT AUTO_INCREMENT PRIMARY KEY,
	    Nombre VARCHAR(255) NOT NULL,
	    Telefono VARCHAR(255) NOT NULL,
	    Domicilio VARCHAR(255) NOT NULL,
	    DNI VARCHAR(255) NOT NULL,
	    Contraseña VARCHAR(255) NOT NULL,
	    Designacion VARCHAR(255) NOT NULL
	);
	
	CREATE TABLE IF NOT EXISTS facturacion(
			N_Factura INT AUTO_INCREMENT PRIMARY KEY,
			Nombre VARCHAR(255) NOT NULL,
			Telefono VARCHAR(255) NOT NULL,
			Categoria VARCHAR(255) NOT NULL,
			Sub_categoria VARCHAR(255) NOT NULL,
			Articulo VARCHAR(255) NOT NULL,
			Cantidad VARCHAR(255) NOT NULL,
			Precio VARCHAR(255) NOT NULL
			);
		
	

INSERT INTO ControlDeEmpleados (Nombre, Telefono, Domicilio, DNI, Contraseña, Designacion) 
VALUES ('Pepito', '987475621', 'Surco', '786412147', '1233211', 'DesignacionEmpleado');

INSERT INTO facturacion (Nombre, Telefono, Categoria, Sub_categoria, Articulo, Cantidad, Precio)
VALUES ('Carlos2', '748747854', 'Jueguetes', 'electronico', 'Pistola', '5', '40');

SELECT * FROM controldeempleados;
SELECT * FROM facturacion;

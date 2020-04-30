create database Trafico
use Trafico

create table Marca_vehiculo(
    id_marcavehiculo int primary Key,
    Nombre_marcavehiculo char(20) Not null,
    Direccion_marcavehiculo char(20) Not null )

create table Modelo_vehiculo(
    id_modelo_vehiculo int primary key,
    Nombre_modelo_vehiculo char(25) Not null,
    Cantidad_vehiculo int Not null,
    potencia_vehiculo char(25) Not null,
    id_marcavehiculo int  Not null,
    foreign key(id_marcavehiculo) references marca_vehiculo(id_marcavehiculo)
    );
create table Modelo_vehiculo(
    id_modelo_vehiculo int primary key,
    Nombre_modelo_vehiculo char(25) Not null,
    Cantidad_vehiculo int Not null,
    potencia_vehiculo char(25) Not null,
    id_marcavehiculo int  Not null,
    foreign key(id_marcavehiculo) references marca_vehiculo(id_marcavehiculo)
    );
create table Departamento(
    id_departamento_persona int primary key,
    Nombre_departamento_persona char(25) Not null
    );
create table Ciudad(
    id_ciudad_persona int primary key,
    Nombre_ciudad_persona char(25) Not null
    );

create table persona(
    id_persona int primary key,
    Nombre_persona char(25) Not null,
    Apellido_persona char(25) Not null,
    Fecha_nacimiento_persona Date Not null,
    Direccion_persona char(25) Not null,
    id_ciudad_persona int Not null,
    foreign key(id_ciudad_persona) references Ciudad(id_ciudad_persona),
    id_departamento_persona int Not null,
    foreign key(id_departamento_persona)references Departamento(id_departamento_persona)
    );
    
create table vehiculo(
    id_matricula_vehiculo int primary key,
    fecha_matriculavehiculo Date Not null,
    id_modelo_vehiculo int Not null,
    foreign key(id_modelo_vehiculo) references Modelo_vehiculo(id_modelo_vehiculo),
    id_persona int Not null,
    foreign key(id_persona) references persona(id_persona)
    );
    
create table agente(
    id_registro_agente int primary key,
    Nombre_agente char(25) Not null
    );

create table Lugar_multa(
    id_lugar_multa int primary key,
    Nombre_carretera char(25) Not null,
    kilometro char(25) Not null
    );


create table infraccion(
    id_multas_vehiculo int primary key,
    Nombre_multavehiculo char(25) Not null,
    Descripcion_multavehiculo char(50) Not null,
    Fecha_multavehiculo Date Not null,
    importe_multavehiculo int Not null,
    id_lugar_multa int Not null,
    foreign key(id_lugar_multa) references Lugar_multa(id_lugar_multa),
    id_matricula_vehiculo int Not null,
    foreign key(id_matricula_vehiculo) references vehiculo(id_matricula_vehiculo),
    id_persona int Not null,
    foreign key(id_persona) references persona(id_persona),
    id_registro_agente int Not null,
    foreign key(id_registro_agente) references agente(id_registro_agente)
    
    );
    12:24 19/11/2017
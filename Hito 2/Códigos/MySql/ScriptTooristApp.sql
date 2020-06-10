drop database if exists TooristApp;
create database if not exists TooristApp;
use TooristApp;

create table if not exists Turista (

	Id int not null auto_increment,
    Nombre_Usuario varchar(40) not null,
    Correo varchar(50) not null,
    Clave varchar(20) not null,
    Nombre_1 varchar(20) not null,
    Nombre_2 varchar(20) not null,
    Apellido_P varchar(20) not null,
    Apellido_M varchar(20) not null,
    Rut varchar(10) not null,
    Nro_Doc_Carnet int not null,
    Nro_Telefono int not null,
    
    primary key (Id)
    
);
create table if not exists GuiaTuristico (

	Id int not null auto_increment,
    Nombre_Usuario varchar(40) not null,
    Correo varchar(50) not null,
    Clave varchar(20) not null,
    Nombre_1 varchar(20) not null,
    Nombre_2 varchar(20) not null,
    Apellido_P varchar(20) not null,
    Apellido_M varchar(20) not null,
    Rut varchar(10) not null,
    Nro_Doc_Carnet int not null,
    Nro_Telefono int not null,
    
    primary key (Id)

);
create table if not exists Tour (

	Id int not null auto_increment,
    Nombre varchar(30) not null,
    Fecha date not null,
    Distancia_Recorrido float not null,
    Costo float not null,
    Id_Turista int not null,
    Id_Guia int not null,
    
    primary key (Id),
    foreign key (Id_Turista) references Turista(Id),
    foreign key (Id_Guia) references GuiaTuristico(Id)
    
);
create table if not exists Comentario (

	Id int not null auto_increment,
    Fecha date not null,
    Detalle varchar(500),
    Id_Turista int not null,
    Id_Tour int not null,
    
    primary key (Id),
    foreign key (Id_Turista) references Turista(Id),
    foreign key (Id_Tour) references Tour(Id)

);
create table if not exists Clasificacion (

	Id int not null auto_increment,
    Detalle int,
    Id_Turista int not null,
    Id_Tour int not null,
    
    primary key (Id),
    foreign key (Id_Turista) references Turista(Id),
    foreign key (Id_Tour) references Tour(Id)
    
);
create table if not exists Administrador (

	Id int not null auto_increment,
    Correo varchar(50) not null,
    Clave varchar(20) not null,
	Id_Guia int not null,
    
    primary key (Id),
	foreign key (Id_Guia) references GuiaTuristico(Id)
);
create table if not exists Ruta (

	Id int not null auto_increment,
    Nombre varchar(30) not null,
    Distancia_Recorrido float not null,
    Id_Tour int not null,
    Id_Administrador int not null,
    
    primary key (Id),
    foreign key (Id_Tour) references Tour(Id),
    foreign key (Id_Administrador) references Administrador(Id)
    
);
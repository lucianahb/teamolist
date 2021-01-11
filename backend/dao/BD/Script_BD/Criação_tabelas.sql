

create table Product
(
	id serial PRIMARY KEY,
	name varchar(200) not null,
	description varchar(400) not null,
	price money not null
	
)

create table Marketplace
(
	id serial,
	name varchar(200) not null,
	description varchar(400) not null,
	 CONSTRAINT pk PRIMARY key (id)
	
)

create table Seller
(
	id serial PRIMARY KEY,
	fullname varchar(200) not null,
	email varchar(100) not null,
	phone varchar(60) null
	
)

create table Category
(
	id serial PRIMARY KEY,
	name varchar(200) not null,
	description varchar(400) not null
	
)

create table Log
(
	id serial PRIMARY KEY,
	datetime timestamp not null,
	action varchar(400) not null
	
)
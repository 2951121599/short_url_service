create database short_url_service charset utf8;
use short_url_service;
create table url_info (
    url_id int primary key auto_increment,
    long_url varchar(255) not null,
    short_url varchar(255) not null
) charset utf8;

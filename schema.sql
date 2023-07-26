drop table if exists link_to_code;
drop table if exists links;
drop table if exists codes;

create table links (
    id serial primary key,
    link varchar(255)
);

create table codes (
    id serial primary key,
    code varchar(10)
);

create table link_to_code (
    id serial primary key,
    link_id int not null references links,
    code_id int not null references codes,
    unique (link_id, code_id)
);
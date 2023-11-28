CREATE TABLE user (
        id INTEGER NOT NULL,
        username VARCHAR(20) NOT NULL,
        password VARCHAR(80) NOT NULL,
        PRIMARY KEY (id)
);

insert into user (username, id, password) values ('test',1,'test');
insert into user (username, id, password) values ('test2',2,'test2');
insert into user (username, id, password) values ('test3',3,'test3');

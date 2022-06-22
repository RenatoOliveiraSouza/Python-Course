create table if not exists cidades (
    id int UNSIGNED not null AUTO_INCREMENT,
    nome VARCHAR(255) not null,
    estado_id int UNSIGNED not null,
    area DECIMAL(10,2),
    PRIMARY Key (id),
    foreign key (estado_id) references estados(id)
);
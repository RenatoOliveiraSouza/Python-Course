create table if not exists prefeitos(
    id int UNSIGNED not null AUTO_INCREMENT,
    nome VARCHAR(255) not null,
    Cidade_id int UNSIGNED,
    PRIMARY key (id),
    UNIQUE key (Cidade_id),
    foreign key (Cidade_id) references cidades(id)
);
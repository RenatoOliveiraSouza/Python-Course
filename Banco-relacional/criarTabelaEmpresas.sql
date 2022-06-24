create table if not exists empresas(
    id int UNSIGNED not null AUTO_INCREMENT,
    nome VARCHAR(255) not null,
    cnpj int UNSIGNED,
    PRIMARY key (id),
    UNIQUE key (cnpj)

);


-- cidades_empresas
create table if not exists empresas_unidades(
    empresas_id int UNSIGNED not null,
    cidade_id int UNSIGNED not null,
    sede tinyint(1) not null,
    PRIMARY key (empresas_id, cidade_id)

);

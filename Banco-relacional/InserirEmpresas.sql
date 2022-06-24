alter table empresas modify cnpj VARCHAR(14);
    
    
insert into empresas
    (nome, cnpj)

values
    ('Bradesco', 123456789),
    ('Vale', 987654321),
    ('Cielo', 456123789);


desc empresas;
desc prefeitos;
select * from empresas;
select * from cidades;


insert into empresas_unidades
    (empresas_id, cidade_id, sede)

values
    (1,1,1),
    (1,2,0),
    (2,1,0),
    (2,2,1);



# power_bi_analyst

Repositório relacionado a formação de Power BI Analyst

# Criação da tabela de Gerentes
select Fname, Minit, Lname, Ssn, Address, Sex, Super_ssn, Dno from employee where Super_ssn is null

# Criando uma tabela somente de Colaboradores
select Fname, Minit, Lname, Ssn, Address, Sex, Super_ssn, Dno from employee where Super_ssn is not null 

Com as tabelas criadas, mesclar as duas tabelas Gerente com Colaboradores, criando tabela unica Gerente_Colaboradores 
com o nome de gerente de seus colaboradores. 

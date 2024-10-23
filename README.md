# power_bi_analyst

Repositório relacionado a formação de Power BI Analyst

# Criação da tabela de Gerentes
select Fname, Minit, Lname, Ssn, Address, Sex, Super_ssn, Dno from employee where Super_ssn is null

# Criando uma tabela somente de Colaboradores
select Fname, Minit, Lname, Ssn, Address, Sex, Super_ssn, Dno from employee where Super_ssn is not null 

Com as tabelas criadas, mesclar as duas tabelas Gerente com Colaboradores, criando tabela unica Gerente_Colaboradores 
com o nome de gerente de seus colaboradores. 

# Criação da Modelagem de Dados

## Processo

O processo consiste na criação das tabelas com base na tabela original. A partir da cópia serão selecionadas as colunas que irão compor a visão da nova tabela. Sendo assim, a partir da tabela principal serão criadas as tabelas.

-Base Original: Financial Sample.xlsx

Tabelas Dimensão:
-D_Produtos (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)
-D_Descontos (ID_produto, Discount, Discount Band)
-D_Detalhes (ID_Produtos,Discount Band,Units Sold,Manufacturing Price,Sale Price)
-D_Produtos_Detalhes (ID_produtos, Discount Band, Sale Price,  Units Sold, Manufactoring Price)
Foi criado o campo de índice para relacionar com a tabela Fato F_Vendas, renomeando para ID_Produtos
Foi criado a tabela D_Calendar com a função CALENDARAUTO() que retorna uma tabela com apenas uma coluna chamada “Date” que contém um conjunto de datas de acordo com a tabela Fato D_Vendas campo Date. 

Tabela Fato:
-F_Vendas (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount  Band, Segment, Country, Salers, Profit, Date (campos))

Foi criadas campos agregadores conforme a figura abaixo:
![alt text](image-1.png)


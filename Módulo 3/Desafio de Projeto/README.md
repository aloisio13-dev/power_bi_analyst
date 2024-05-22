
# DESAFIO DE PROJETO ![Logo da DIO](assets/logo.png)



Processamento e tratamento de dados SQL (MySQL) em Power BI.

# Descrição do desafio módulo 3 – Processamento de Dados Simplificado com Power BI

1. Criação de uma instância na Azure para MySQL

2. Criar o Banco de dados com base disponível no github

3. Integração do Power BI com MySQL no Azure

4. Verificar problemas na base a fim de realizar a transformação dos dados

## Diretrizes para transformação dos dados

1. Verifique os cabeçalhos e tipos de dados

2. Modifique os valores monetários para o tipo double preciso

3. Verifique a existência dos nulos e analise a remoção

4. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente

5. Verifique se há algum departamento sem gerente

6. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas

7. Verifique o número de horas dos projetos

8. Separar colunas complexas

9. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção

10. Neste processo elimine as colunas desnecessárias.

11. Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.


12. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores

13. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.

14. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.

15. Agrupe os dados a fim de saber quantos colaboradores existem por gerente

16. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela
 
 # Elaboração do desafio
 - Durante inserções das etapas supracitadas no MySQL, foi necessário utilizar correção no código disponibilizado.
 - Adicionado código para inserção dos valores das colunas, foi necessário configurar query para erro de Primary Key. {SET foreign_key_checks = 0;} -Desabilitar função & {SET foreign_key_checks = 1;} - Para habilitar após inserção de valores das colunas/tabelas.

 - Realizado junção das tabelas criadas no MySQL por meio da query: SELECT AS & LEFT JOIN: 

 CREATE VIEW [nomear] AS SELECT 

    e.Fname,
    e.Minit,
    e.Lname,
    e.Ssn,
    e.Bdate AS Employee_Bdate,
    e.Address,
    e.Sex AS Employee_Sex,
    e.Salary,
    e.Super_ssn,
    e.Dno,
    d.Dname,
    d.Mgr_ssn,
    d.Mgr_start_date,
    d.Dept_create_date,
    dl.Dlocation,
    p.Pname,
    p.Pnumber,
    p.Plocation,
    p.Dnum,
    wo.Hours,
    dep.Dependent_name,
    dep.Sex AS Dependent_Sex,
    dep.Bdate AS Dependent_Bdate,
    dep.Relationship
FROM 

    employee e
    LEFT JOIN departament d ON e.Dno = d.Dnumber
    LEFT JOIN dept_locations dl ON d.Dnumber = dl.Dnumber
    LEFT JOIN works_on wo ON e.Ssn = wo.Essn
    LEFT JOIN project p ON wo.Pno = p.Pnumber
    LEFT JOIN dependent dep ON e.Ssn = dep.Essn;

 - Migração dos dados para plataforma Azure por meio da conexão estabelecida no MySQL Workbench.
 - Processamento de dados com Power BI - Utilizado função mesclar para estabelecer o que se pede nas alíneas do desafio, para mesclagens supracitadas.
 - Criação de relatório no Power BI.

 # God bless you!


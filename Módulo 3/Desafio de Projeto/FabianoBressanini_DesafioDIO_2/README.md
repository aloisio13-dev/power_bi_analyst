# Desafio DIO #2 
Elaborado por: Fabiano Bressanini

## 📓 Documentação


**1. Criar uma instância na Azure para MySQL:**

Assinatura: Azure subscription 1
Grupo de recursos: powerbiclient
Localização: Brazil South
Nome do servidor: desafio-pjto-dio.mysql.database.azure.com
Configuração: Intermitente, B1ms, 1 vCores, 2 GiB RAM, 20 GiB storage
Versão MySQL: 8.0

**2. Criar o Banco de dados com base disponível no github:**

https://github.com/fabianobressanini/power_bi_analyst/tree/main/M%C3%B3dulo%203/Desafio%20de%20Projeto
Utilização dos arquivos:
script_bd_company.sql e insercao_de_dados_e_queries_sql.sql

**3. Integrar Power BI com MySQL no Azure:**

Realizado download do arquivo: desafio-pjto-dio_azure_company.pbids
 
**4. Verificar problemas na base a fim de realizar a transformação dos dados
Diretrizes para transformação dos dados:**

***4.1. Verificar os cabeçalhos e tipos de dados***

Todos se apresentaram corretos, de acordo com o arquivo: script_bd_company.sql

***4.2. Modificar os valores monetários para o tipo double preciso***

A coluna 'Salary' da tabela 'employee' teve o Tipo Alterado de Número Decimal, para Número Decimal Fixo

***4.3. Verificar a existência dos nulos e analise a remoção***

A tabela 'employee' apresenta um valor nulo na linha 5, coluna 'Super_ssn' o que pode indicar que é um gerente. Logo não será removido

***4.4. Os employees com nulos em Super_ssn podem ser os gerentes. Verificar se há algum colaborador sem gerente***

Não há nenhum colaborador sem gerente

***4.5. Verificar se há algum departamento sem gerente***

Não há nenhum departamento sem gerente, de acordo com a coluna 'Mgr_ssn' da tabela 'departament'

***4.6. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas***

Não houve necessidade

***4.7. Verifique o número de horas dos projetos***

Ao todo foram 275 horas, para 6 projetos, sendo que o projeto que mais consumiu horas foi 'Computerization' com 55 horas e o que menos consumiu foi 'Reorganização' com 25 horas

***4.8. Separar colunas complexas***

Foi encontrada uma coluna complexa 'Address' na tabela 'employee

Foi subistituído o termo 'Fire-Oak' por Fire Oak

Em seguida a coluna foi separada pelo delimitador '-', resultando em 4 colunas

As colunas foram renomeadas da seguinte forma:
- Address.1 para Address No,
- Address.2 para Address Disctrict,
- Address.3 para Address City,
- Address.4 para Adress State

Com isso a coluna 'Adress No' teve o tipo alterado para Número Inteiro

***4.9. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção***

Foram mescladas as tabelas 'employee' pela coluna 'Dno' e 'departament' pela coluna 'Dnumber', resultando em uma nova tabela 'employee_departament'

***4.10. Neste processo elimine as colunas desnecessárias.***

Foram removidas as colunas 'Dno', 'azure_company.departament', 'azure_company.dependent', 'azure_company.works.on', 'azure_company.dept_locations', 'azure_company.employee' e 'azure_company.project'

***4.11. Realize a junção dos colaboradores e respectivos nomes dos gerentes. Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.***

Foram mescladas as tabelas 'employee' pela coluna 'Super_ssn' e 'employee' pela coluna 'Ssn', gerando uma nova tabela 'employee_manager'

Foram mescladas as colunas 'azure_company employee.Fname', 'azure_company employee.Minit', 'azure_company employee.Lname', com separador de espaço, gerando a coluna 'Mname', em referência ao nome do gerente 

***4.12. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores***

Foram mescladas as colunas 'azure_company employee.Fname', 'azure_company employee.Minit', 'azure_company employee.Lname', com separador de espaço, gerando a coluna 'Ename', da tabela 'employee_manager'

Foram removidas as colunas 'azure_company.departament', 'azure_company.dependent' e 'azure_company.works_on'

As colunas 'Dlocation' e 'Dname' foram reordenadas e mescladas com o nome de 'Store'

***4.13. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.***

Foram mescladas as tabelas 'departament' pela coluna 'Dnumber' e 'dept_locations' pela coluna 'Dnumber', gerando uma nova tabela 'departament_dlocations'

Foram removidas as colunas 'azure_company.dept_locations', 'azure_company.employee', 'azure_company.project', 'azure_company.departament' e 'Dnumber.1'

***4.14. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.***

Pois não trata-se de uma aglutinação (acréscimo de linhas) e sim de uma mesclagem de colunas, como um 'join' do SQL

***4.15. Agrupe os dados a fim de saber quantos colaboradores existem por gerente***

Foi duplicada a tabela 'employee_manager' e renomeada para 'employee_manageragg'
A coluna Mnane' foi agrupada, e a contagem foi realizada na coluna 'Qty_employees'*** 

***4.16. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela***


| Tabela         | Colunas eliminadas                                                                 |
|----------------|------------------------------------------------------------------------------------|
| departament    | 'azure_company.dept_locations', 'azure_company.employee' e 'azure_company.project' |
| dependent      | 'azure_company.employee'                                                           |
| dept_locations | 'azure_company.departament'                                                        |
| project        | 'azure_company.departament e 'azure_company.works_on'                              |
| works_on       | 'azure_company.employee e 'azure_company.project'                                  |


 Elaborado em: 11/04/2024 | Última atualização: 11/04/2024
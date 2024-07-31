
# Desafio Módulo 3 - Processamento de Dados Simplificado com Power BI

Projeto para o desafio Módulo 3 da DIO.

Passo a Passo.

1. Criação de uma instância na Azure para MySQL
    - 
Criado uma instância em SQL na Azure.

2. Criar o Banco de dados com base disponível no github
    - 
Criado todas as tabelas e relacionamento em SQL.

3. Integração do Power BI com MySQL no Azure
    - 
Importação do SQL no Power BI

4. Verificar problemas na base a fim de realizar a transformação dos dados
    - 
Tratamento dos dados através do Power Query.


## Diretrizes para transformação dos dados
1. Verifique os cabeçalhos e tipos de dados
    -
Alterado os nomes das consultas e campos para melhor identificação.

2. Modifique os valores monetários para o tipo double preciso
    -
Alterado o Salário de Funcionários para valor monetário.

3. Verifique a existência dos nulos e analise a remoção
    -
Apenas o Id do Gerente de James E. Borg está nulo em Employee, pois o mesmo é o gerente.

4. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente
    -
Apenas o Id do Gerente de James E. Borg está nulo em Employee, pois o mesmo é o gerente.

5. Verifique se há algum departamento sem gerente
    -
Todos os departamentos tem gerentes.
Headquarters - James E. Borg
Administration - Jennifer S. Wallace
Research - Franklin T. Wong

6. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas
    -
Todos os departamentos possuem gerentes.

7. Verifique o número de horas dos projetos
    -
Existe um único projeto com 0 horas.

8. Separar colunas complexas
    -
Separado o endereço em Número - Rua - Cidade - Estado

9. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção
    -
Mesclado os dados das tabelas Funcionários com a tabela Departamento, unidos pela coluna Número Departamento.

10. Neste processo elimine as colunas desnecessárias.
    -
Excluído as colunas Número Departamento(nova) e Gerente Id(nova), vindos duplicados da tabela Departamento.

11. Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.
    -
Criado coluna com o nome dos gerentes utilizando coluna de exemplo no Power Query.

12. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores
    -
Colunas FName, MInit e LName mescladas em coluna Nome.

13. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.
    -
Mesclado tabela Departamento e Dpt_Localização.

14. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.
    -
Ao MESCLAR, nós definimos um elemento em comum que une dados das 2 tabelas. Enquanto que ACRESCENTAR, apenas adicionamos dados novos de uma tabela a outra, não sendo o nosso caso neste momento.

15. Agrupe os dados a fim de saber quantos colaboradores existem por gerente
    -
Franklin - 3 colaboradores
James - 2 colaboradores
Jennifer - 2 colaboradores

16. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tab
    -
Dados limpos.

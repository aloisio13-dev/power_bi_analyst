# Projeto de Desafio - Modelagem e Transformação de Dados com DAX no Power BI #
<br>
<br>
Neste desafio o objetivo foi realizar as instruções indicadas na descrição do desafio com o objetivo de treinar as técnicas de modelagem de DAX.
<br>
Na minha concepção, não seguindo as instruções, teria feito em cima da financials:
<br>
01) Criar Domínios para: País, Produto, Segmento e Tipo de Desconto. Nestas tabelas também armazenaria totais como: Quantidades Vendidas, Total de Vendas, Total de Lucro
02) Criar Calendário
03) Criado tabela de detalhe substituindo colunas descritivas pelos seus respectivos índices
<br>
Caso tivesse que fazer a extração de banco dados, já traria estas informações transformadas.
<br>
<br>
<br>
### ======================================================================== ###
<br>
<br>
<br>
# Projeto de Desafio - Processando e Transformando Dados com Power BI - Instruções
<br>
## Explicação solicitada para o Readme.md
<br>
11.	Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.
select *
  from employee             a
      ,departament          b
 where b.Mgr_ssn            = a.Super_ssn 
<br>
## Documento "Desafio de Projeto - Processando e Transformando Dados com Power BI - Instruções.docx" possui todas as ações tomadas
<br>
## Relatório DIO_08_Desafio_Dashboard_corporativo_integração_MySQL_Azure.pbix feito visualização simples
<br>

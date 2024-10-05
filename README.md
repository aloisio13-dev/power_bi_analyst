# Power_Bi_Analyst


## Desafio Schema Start Modelagem com DAX


## Lists

### Etapas Realizadas

* Limpeza dos dados da tabela Financial
* Criação de Novas Tabelas a partir da tabela "Finacial"
* Originando as tabelas:Fato e Dimencionais comforme o schema start


### Tabelas

1. F_Vendas
2. D_Produtos
3. D_Produtos_Detalhes
4. D_Descontos
5. D_Vendas_Detalhes
6. Calendário

## Image

![This is an alt text.](/Modulo_4/Desafios_de_Projeto/schema_start_Power_BI.jpg "This is a sample image.")

## Etapas com DAX
1. Construção da tabela Calendário
  Nova Tabela 
2.D_Calendario = CALENDARAUTO(12)

3. Novas colunas 
    D_Calendario = CALENDARAUTO(12)
    Day_Week = WEEKDAY('D_Calendario'[Date])
    Day_week_name = FORMAT('D_Calendario'[Date],"DDDD")
    Month = MONTH('D_Calendario'[Date])
    Month_name = FORMAT('D_Calendario'[Date],"MMMM")
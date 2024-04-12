# Log de Alterações

## Data da Importação da Base

- **Alteração:** Importação da base de dados.
- **Descrição:** A base de dados foi importada com sucesso para o projeto e conectada ao servidor flexivel MYSQL na Azure.

## Data da Adição do Número de Gerente

- **Alteração:** Adição de número de gerente ao colaborador que estava nulo.
- **Descrição:** Um número de gerente foi atribuído aos colaboradores que anteriormente não possuíam essa informação.

## Data da Mudança do Tipo da Coluna Salário

- **Alteração:** Troca do tipo da coluna "salário" de float para float fixo.
- **Descrição:** A coluna "salário" foi alterada para float fixo para melhorar a consistência dos dados.

## Data da Criação da Coluna Personalizada Fullname

- **Alteração:** Criação da coluna personalizada "Fullname".
- **Descrição:** A coluna "Fullname" foi criada concatenando as colunas "Fname", "Minit" e "Lname" para formar o nome completo do colaborador.

## Criação da Coluna Personalizada name_location_dpt

- **Alteração:** Criação da coluna personalizada "name_location_dpt".
- **Descrição:** A coluna "name_location_dpt" foi criada concatenando as colunas "azure_company.departament.Dname" e "Dlocation" para formar um nome composto que inclui o nome do departamento e a localização.


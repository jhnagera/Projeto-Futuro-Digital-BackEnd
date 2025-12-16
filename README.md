Criar um software capas de gerar uma escala de serviço que possua 8 postos de serviço, o rodizio entre os postos possa ser atribuído.
O nome dos postos são Alfa 2, Ronda P1, Delta 4, Alfa 3, Ronda P2 e P3, Galeria/QAP e  Monitoramento,
os postos Alfa 2 e Alfa 3 tem prioridades sobre os demais. Os funcionários que trabalharam nos postos,
devem ser alocados, conforme seus horários de trabalho, devendo ter um equilíbrio sobre os postos de trabalho.
Esse código deve usar o banco de dados postgres para a inserção dos dados dos nomes dos postos, nome dos funcionários bem como a hora de começo e fim da escala do dia. Esse banco deve salvar a escala diariamente, apos ser feita.
O banco deve possuir uma tabela de funcionários, uma de horários de entrada e saída dos funcionários, uma tabela de postos. O horário de rodizio, dos postos deve ser ajustado(no mínimo 30 minutos e no max. 1 hora)


Requisitos para a Confecção do Software de Geração de Escala
Este modelo é dividido em Requisitos Funcionais (o que o software deve fazer), Requisitos Não Funcionais (como o software deve ser) e Regras de Negócio (lógica específica da operação).

#1. Requisitos Funcionais (RF)
---
ID	Requisito	Descrição Detalhada
RF01	Gestão de Postos de Serviço	O software deve permitir o cadastro, visualização, edição e exclusão dos 8 postos de serviço.
RF02	Gestão de Funcionários	O software deve permitir o cadastro, visualização, edição e exclusão de funcionários, incluindo seus nomes.
RF03	Gestão de Horários de Trabalho	O software deve permitir o cadastro dos horários de entrada e saída (início e fim do turno) de cada funcionário.
RF04	Geração de Escala Automática	O software deve gerar a escala diária, atribuindo funcionários aos postos de serviço com base nos horários de trabalho e nas regras de prioridade/rodízio.
RF05	Aplicação do Rodízio	O software deve aplicar o rodízio de funcionários entre os postos de serviço. O intervalo do rodízio deve ser configurável, com limites entre 30 minutos (mínimo) e 1 hora (máximo).
RF06	Equilíbrio de Postos	A lógica de geração deve buscar um equilíbrio na alocação, garantindo que os funcionários sejam distribuídos de forma justa pelos postos ao longo do tempo (evitando que o mesmo funcionário fique sempre no mesmo posto ou nos postos mais/menos prioritários).
RF07	Persistência de Dados	O software deve salvar a escala gerada diariamente no banco de dados, registrando a alocação de funcionários e os horários de início e fim da escala do dia.

#2. Requisitos Não Funcionais (RNF)
---
ID	Requisito	Categoria	Descrição Detalhada
RNF01	Armazenamento de Dados	Desempenho/Dados	O software deve utilizar o PostgreSQL como sistema de gerenciamento de banco de dados para todas as operações de persistência.
RNF02	Disponibilidade	Confiabilidade	O software deve estar disponível para geração de escala diariamente no horário programado.
RNF03	Usabilidade (Interface)	Usabilidade	A interface para a geração e visualização da escala deve ser clara e intuitiva.
RNF04	Segurança (Acesso)	Segurança	Deve haver um mecanismo simples de autenticação (e.g., login) para acessar as funcionalidades de cadastro e geração de escala.
RNF05	Linguagem de Desenvolvimento	Tecnológico	O software deve ser confeccionado utilizando a linguagem de programação Python.

#3. Regras de Negócio (RN)
---
ID	Regra de Negócio	Detalhe da Regra
RN01	Nomes dos Postos	Os 8 postos de serviço são: Alfa 2, Ronda P1, Delta 4, Alfa 3, Ronda P2 e P3, Galeria/QAP, e Monitoramento.
RN02	Prioridade de Postos	Os postos Alfa 2 e Alfa 3 têm prioridade sobre os demais postos na atribuição de funcionários (isto pode significar que devem ser preenchidos primeiro, dependendo da sua definição de "prioridade").
RN03	Horário de Rodízio	O intervalo de tempo para o rodízio de funcionários entre os postos deve ser configurável pelo administrador e limitado ao mínimo de 30 minutos e máximo de 1 hora.
RN04	Alocação por Turno	Os funcionários só podem ser alocados aos postos dentro de seus horários de trabalho (início e fim do turno cadastrados).


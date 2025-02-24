# Documentação de Requisitos - Observabilidade no Airbnb

&emsp;&emsp; O Airbnb é uma plataforma de aluguel de acomodações que conecta anfitriões e hóspedes ao redor do mundo. Para garantir a confiabilidade da plataforma, a observabilidade é essencial, permitindo monitoramento e diagnóstico em tempo real das operações.

## Requisito Funcional (RF)

### RF1 - Registro de Eventos de Reserva

**Descrição:** O sistema deve registrar eventos relevantes ao processo de reserva, incluindo criação, modificação e cancelamento de reservas pelos usuários.

**Critérios de Aceitação:**

- Deve armazenar logs detalhados de cada evento de reserva.

- Logs devem conter ID do usuário, ID da reserva, timestamp e status da operação.

## Requisito Não Funcional (RNF)

### RNF1 - Monitoramento da Saúde da API de Reservas

**Descrição:** O sistema deve monitorar e registrar a disponibilidade e tempo de resposta da API responsável pelo gerenciamento de reservas.

**Critérios de Aceitação:**

- Deve registrar logs de requisições à API de reservas, incluindo tempo de resposta e status HTTP.

- Deve alertar quando a API estiver fora do ar ou responder com erro.


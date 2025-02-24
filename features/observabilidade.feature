Feature: Monitoramento de eventos de reserva e saúde da API

  Scenario: Registro de evento de reserva
    Given o usuário com ID "12345" realiza uma reserva com ID "abcde"
    When o evento de reserva é registrado
    Then um log deve ser gerado contendo o ID do usuário "12345", o ID da reserva "abcde" e o status "confirmed"
    

  Scenario: Falha na saúde da API de reservas
    Given a API de reservas está fora do ar
    When a saúde da API é verificada
    Then a falha deve ser registrada com a mensagem de erro
    And a API deve ser considerada fora do ar

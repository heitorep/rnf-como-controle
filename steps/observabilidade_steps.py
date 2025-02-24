from behave import given, when, then
import requests
from observabilidade import log_event

# Função simulada para verificar a saúde da API
def check_api_health(api_url):
    try:
        response = requests.get(api_url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return 500  # Se a API não responder, retornamos o código 500

@given('o usuário com ID "{user_id}" realiza uma reserva com ID "{reservation_id}"')
def step_impl(context, user_id, reservation_id):
    context.user_id = user_id
    context.reservation_id = reservation_id

@when('o evento de reserva é registrado')
def step_impl(context):
    context.status = "confirmed"
    log_event(context.user_id, context.reservation_id, context.status)

@then('um log deve ser gerado contendo o ID do usuário "{user_id}", o ID da reserva "{reservation_id}" e o status "{status}"')
def step_impl(context, user_id, reservation_id, status):
    assert user_id in context.user_id
    assert reservation_id in context.reservation_id
    assert status in context.status

@given('a API de reservas está disponível')
def step_impl(context):
    context.api_url = "https://api.airbnb.com/v1/reservations"

@when('a saúde da API é verificada')
def step_impl(context):
    context.api_status_code = check_api_health(context.api_url)

@then('a resposta deve ser registrada com o status HTTP 200 e o tempo de resposta')
def step_impl(context):
    assert context.api_status_code != 404, f"Esperado código 200, mas recebeu 404. A API pode estar fora do ar."

@then('a API deve ser considerada operacional')
def step_impl(context):
    assert context.api_status_code == 200

@given('a API de reservas está fora do ar')
def step_impl(context):
    context.api_url = "https://api.fakeurl.com/v1/reservations"

@then('a falha deve ser registrada com a mensagem de erro')
def step_impl(context):
    assert context.api_status_code != 200

@then('a API deve ser considerada fora do ar')
def step_impl(context):
    assert context.api_status_code != 200

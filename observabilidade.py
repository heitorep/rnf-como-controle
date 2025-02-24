import requests
import json
import time
from datetime import datetime

def log_event(user_id, reservation_id, status):
    """Simula o registro de um evento de reserva."""
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "service": "airbnb_reservations",
        "user_id": user_id,
        "reservation_id": reservation_id,
        "event_type": "reservation_update",
        "status": status
    }
    print(json.dumps(log, indent=2)) 

def check_api_health(api_url):
    """Testa a disponibilidade da API de reservas."""
    try:
        start_time = time.time()
        response = requests.get(api_url, timeout=5)
        response_time = time.time() - start_time
        
        log_event("system", "health_check", f"API response: {response.status_code} ({response_time:.2f}s)")
        return response.status_code  # Retorna o código de status HTTP
    except requests.RequestException as e:
        log_event("system", "health_check", f"API down: {str(e)}")
        return 500  # Retorna 500 em caso de erro de rede


demo_user_id = "12345"
demo_reservation_id = "abcde"
log_event(demo_user_id, demo_reservation_id, "confirmed")

api_status = check_api_health("https://api.airbnb.com/v1/reservations")
print(f"API está {'operacional' if api_status else 'fora do ar'}")

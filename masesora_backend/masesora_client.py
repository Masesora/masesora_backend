import requests

BASE_URL = "http://127.0.0.1:8000"

def get_symptoms():
    response = requests.get(f"{BASE_URL}/symptom-master/")
    response.raise_for_status()
    return response.json()

def evaluate_symptom(client_id, master_id, data):
    url = f"{BASE_URL}/clinical/client/{client_id}/symptom/{master_id}"
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()

def get_department_overview(client_id, department):
    url = f"{BASE_URL}/clinical/client/{client_id}/department/{department}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

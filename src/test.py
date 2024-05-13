import requests

def test_home():
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200
    assert 'vIAjando' in response.text

def test_user_input():
    data = {'input_text': 'Hola, ¿cómo estás?'}
    response = requests.post('http://localhost:8000/user_input', json=data)
    assert response.status_code == 200
    assert 'Entrada del usuario recibida correctamente' in response.json()['message']

def test_historial():
    response = requests.get('http://localhost:8000/historial')
    assert response.status_code == 200
    assert  list

def test_historial_completo():
    response = requests.get('http://localhost:8000/historial_completo')
    assert response.status_code == 200
    assert  list
import pytest
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from views import impact_2024
from models import Impact2024

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.mark.django_db
def test_impact_2024_valid_post_request(request_factory):
    # Crea una solicitud POST simulada con un archivo de carga válido
    file_content = b'content'  # Contenido simulado del archivo
    uploaded_file = SimpleUploadedFile('test.xls', file_content, content_type='application/vnd.ms-excel')
    request = request_factory.post('/impact_2024/', {'data': 'your_data'}, files={'archivos': uploaded_file})
    
    # Ejecuta la vista
    response = impact_2024(request)
    
    # Verifica que se haya redirigido correctamente o se haya renderizado una página específica
    assert response.status_code == 200
    assert 'pages/components/2024/impacto.html' in response.template_name

    # Verifica que los objetos se hayan creado en la base de datos
    assert Impact2024.objects.count() == 1  # Se espera que se cree un objeto

@pytest.mark.django_db
def test_impact_2024_invalid_post_request(request_factory):
    # Crea una solicitud POST simulada sin un archivo de carga
    request = request_factory.post('/impact_2024/', {'data': 'your_data'})
    
    # Ejecuta la vista
    response = impact_2024(request)
    
    # Verifica que se haya devuelto un error o una redirección a una página de error
    assert response.status_code == 500  # Esto depende de cómo manejes los errores en tu vista

@pytest.mark.django_db
def test_impact_2024_get_request(request_factory):
    # Crea una solicitud GET simulada
    request = request_factory.get('/impact_2024/')
    
    # Ejecuta la vista
    response = impact_2024(request)
    
    # Verifica que se haya devuelto una página de error o redirección
    assert response.status_code == 500  # Esto depende de cómo manejes las solicitudes GET en tu vista

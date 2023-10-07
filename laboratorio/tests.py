from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio


class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear objetos Laboratorio para pruebas
        Laboratorio.objects.create(
            nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')
        Laboratorio.objects.create(
            nombre='Laboratorio 2', ciudad='Ciudad 2', pais='País 2')

    def test_datos_iniciales(self):
        # Obtener los objetos Laboratorio creados en setUpTestData
        laboratorio_1 = Laboratorio.objects.get(nombre='Laboratorio 1')
        laboratorio_2 = Laboratorio.objects.get(nombre='Laboratorio 2')

        # Verificar que los datos coinciden con los datos iniciales
        self.assertEqual(laboratorio_1.nombre, 'Laboratorio 1')
        self.assertEqual(laboratorio_1.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio_1.pais, 'País 1')

        self.assertEqual(laboratorio_2.nombre, 'Laboratorio 2')
        self.assertEqual(laboratorio_2.ciudad, 'Ciudad 2')
        self.assertEqual(laboratorio_2.pais, 'País 2')

    def test_url_laboratorio(self):
        # Obtener la URL para la vista 'laboratorio'
        # Reemplazamos 'laboratorio' con 'laboratorio:mostrar'
        url = reverse('laboratorio:mostrar')

        # Hacer una solicitud HTTP GET a la URL
        response = self.client.get(url)

        # Verificar que devuelve una respuesta HTTP 200
        self.assertEqual(response.status_code, 200)

    def test_vista_laboratorio(self):
        # Obtener la URL para la vista 'laboratorio'
        # Reemplazamos 'laboratorio' con 'laboratorio:mostrar'
        url = reverse('laboratorio:mostrar')

        # Hacer una solicitud HTTP GET a la URL
        response = self.client.get(url)

        # Verificar que se utiliza la plantilla correcta
        # Reemplazamos 'laboratorio.html' con 'mostrar.html'
        self.assertTemplateUsed(response, 'mostrar.html')

        # Verificar que el contenido HTML coincide con lo esperado
        # Puedes agregar más aserciones aquí para verificar el contenido específico de la plantilla
        self.assertContains(response, '<h2>Información de Laboratorios</h2>')

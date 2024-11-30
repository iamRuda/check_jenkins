import unittest
from main import app

class FlaskTestCase(unittest.TestCase):
    # Метод для настройки тестового клиента
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Тест для главной страницы
    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<!DOCTYPE html>", response.data)  # Проверка, что это HTML-страница
        self.assertIn(b"Welcome to the Main Page!", response.data)  # Пример, проверьте заголовок или контент

    # Тест для страницы списка
    def test_list_page(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Item 1", response.data)  # Проверка наличия элемента в списке
        self.assertIn(b"Item 2", response.data)  # Проверка наличия элемента в списке
        self.assertIn(b"Item 3", response.data)  # Проверка наличия элемента в списке
        self.assertIn(b"Item 4", response.data)  # Проверка наличия элемента в списке

    # Тест для страницы контактов
    def test_contact_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Contact Us", response.data)  # Пример, проверка наличия текста на странице

if __name__ == "__main__":
    unittest.main()

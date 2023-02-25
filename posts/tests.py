from django.test import TestCase, Client
from django.urls import reverse

class HelloTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        responce = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Hello<h1>"
        expected_header = "Alex"

        self.assertEqual(responce.content.decode(), expected_data)
        self.assertEqual(responce.status_code, 300)
        self.assertEqual(responce.headers["names"], expected_header)
    
    def test_get_index(self):
        responce_get = self.client.get(reverse("index-page"))
        responce_post = self.client.post(reverse("index-page"))

        expected_get = "Главная страница"
        expected_post = "Не тот метод запроса"

        self.assertEqual(responce_get.status_code ,200)
        self.assertEqual(responce_post.status_code , 200)
        self.assertEqual(responce_get.content.decode(), expected_get)
        self.assertEqual(responce_post.content.decode(), expected_post)

    def test_get_contacts(self):
        responce_get_contact = self.client.get(reverse("endpoint-contact"))

        expect_contact = "Hi"

        self.assertEqual(responce_get_contact.content.decode(),expect_contact)
        self.assertEqual(responce_get_contact.status_code,200)
        
    def test_get_about(self):
        responce_get_about = self.client.get(reverse("get-about"))

        expected_about ="Good"

        self.assertEqual(responce_get_about.content.decode(), expected_about)
        self.assertEqual(responce_get_about.status_code,200)

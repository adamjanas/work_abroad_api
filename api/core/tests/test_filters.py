from django.urls import reverse
from rest_framework.test import APITestCase
from api.structure.models import Offer, Application
from api.chat.models import Message
from api.structure.tests.test_model_view_sets_2 import AuthenticateMixin
from django.core.files.uploadedfile import SimpleUploadedFile


class FiltersTestCase(AuthenticateMixin, APITestCase):

    def setUp(self):

        super().setUp()
        self.objects_number = 10
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())
        for i in range(1, self.objects_number + 1):
            Offer.objects.create(title=f'title{i}', author=self.test_user,
                                 content=f'content{i}', start_date="2021-07-23",
                                 finish_date="2021-08-23", salary=500, country="AF")
            Message.objects.create(recipient=self.test_user, author=self.test_user,
                                   content='title{i}', attachment=self.file)
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())
        for i in range(1, self.objects_number + 1):
            Application.objects.create(offer=Offer.objects.get(title='title1'), author=self.test_user,
                                       title=f"title{i}", content=f"content{i}", attachment=self.file)

    def test_offer_list_filter_by_author_exact(self):

        url = f"{reverse('offers-list')}?author={self.test_user.pk}"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_offer_list_filter_by_title_exact(self):

        url = f"{reverse('offers-list')}?title=title2"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_offer_list_filter_by_title_contains(self):

        url = f"{reverse('offers-list')}?title_contains=title"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_offer_list_filter_by_content_contains(self):

        url = f"{reverse('offers-list')}?content_contains=content"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_application_list_filter_by_author_exact(self):

        url = f"{reverse('applications-list')}?author={self.test_user.pk}"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_application_list_filter_by_title_exact(self):

        url = f"{reverse('applications-list')}?title=title2"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_application_list_filter_by_title_contains(self):

        url = f"{reverse('applications-list')}?title_contains=title"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_application_list_filter_by_content_contains(self):

        url = f"{reverse('applications-list')}?content_contains=content"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_message_list_filter_by_author_exact(self):

        url = f"{reverse('messages-list')}?author={self.test_user.pk}"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_message_list_filter_by_content_contains(self):

        url = f"{reverse('messages-list')}?content_contains=content"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

from django.urls import reverse
from rest_framework.test import APITestCase
from api.users.models import User
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from api.chat.models import Message

class AuthenticateMixin():
    '''
    Forcing authentication of user
    '''

    def setUp(self):

        self.credentials = {
            'username': 'testuser1',
            'email': 'test1@email.com',
            'password': 'testpassword1'
        }

        self.test_user = User.objects.create_user(**self.credentials)

        self.client.force_authenticate(user=self.test_user)


class ViewSetTest(AuthenticateMixin, APITestCase):

    def setUp(self):

        super().setUp()
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/chat/tests/test_data/test.txt', 'rb').read())
        self.message = Message.objects.create(recipient=self.test_user, author=self.test_user,
                                              content='content1', attachment=self.file)
        self.message_list = Message.objects.all()
        self.message_1 = Message.objects.get(content='content1')
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/chat/tests/test_data/test.txt', 'rb').read())

    def test_message_list(self):

        url = reverse('messages-list')

        response = self.client.get(url, format='json')

        for model in self.message_list:
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_detail(self):

        url = reverse('messages-detail', args=(self.message_1.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_update(self):

        url = reverse('messages-detail', args=(self.message_1.pk,))

        data = {
            'recipient': self.test_user.pk,
            'content': 'content - updated',
            'attachment': self.file
        }

        response = self.client.put(url, data=data, format='multipart', follow=True)

        self.assertIn(data['content'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_partial_update(self):

        url = reverse('messages-detail', args=(self.message_1.pk,))

        data = {
            'recipient': self.test_user.pk,
            'content': 'content - updated',
        }

        response = self.client.put(url, data=data, follow=True)

        self.assertIn(data['content'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_delete(self):

        url = reverse('messages-detail', args=(self.message_1.pk,))

        response = self.client.delete(url)

        self.assertFalse(self.message_1 in self.message_list)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

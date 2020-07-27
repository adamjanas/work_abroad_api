from django.urls import reverse
from rest_framework.test import APITestCase
from api.users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from api.structure.tests.test_model_view_sets_2 import AuthenticateMixin
from api.chat.models import Message
from api.structure.models import (
    Offer,
    Application,
    OfferReview,
    UserReview
)


class MixinTest(APITestCase):
    '''
    Testing ActionPermissionMixin (IsAuthor, IsSender, IsApplicant) permission
    '''

    def setUp(self):

        self.credentials_test_user = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password': 'testpassword'
        }

        self.credentials_author = {
            'username': 'author_test',
            'email': 'author_test@email.com',
            'password': 'author_testpassword'
        }

        self.test_user = User.objects.create_user(**self.credentials_test_user)
        self.author = User.objects.create_user(**self.credentials_author)
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/core/tests/test_data/test.txt', 'rb').read())
        self.offer = Offer.objects.create(title=f'title1', author=self.author, content=f'content1',
                             start_date="2021-07-23", finish_date="2021-08-23", salary=500, country="AF")
        self.application = Application.objects.create(offer=Offer.objects.get(title='title1'), author=self.author,
                                                      title="title1", content="content1", attachment=self.file)
        self.offer_1 = Offer.objects.get(title='title1')
        self.application_1 = Application.objects.get(title='title1')
        self.offer_list = Offer.objects.all()
        self.application_list = Application.objects.all()
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/core/tests/test_data/test.txt', 'rb').read())
        self.user_review = UserReview.objects.create(user=self.test_user, author=self.author, title='title1',
                                                     content='content1', review=2)
        self.offer_review = OfferReview.objects.create(offer=self.offer_1, author=self.author, title='title1',
                                                       content='content1', review=2)
        self.user_review_1 = UserReview.objects.get(title='title1')
        self.offer_review_1 = OfferReview.objects.get(title='title1')
        self.user_review_list = UserReview.objects.all()
        self.offer_review_list = OfferReview.objects.all()
        self.message = Message.objects.create(recipient=self.test_user, author=self.author,
                                              content='content1', attachment=self.file)
        self.message_list = Message.objects.all()
        self.message_1 = Message.objects.get(content='content1')
        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())

    def test_update_offer_by_unauthorized_user(self):

        '''
        Ensure that offer's updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        data = {
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'start_date': '2021-07-24',
            'finish_date': '2021-08-25',
            'salary': 500,
            'country': 'AF',
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_partial_update_offer_by_unauthorized_user(self):
        '''
        Ensure that offer's partial updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        data = {
            'title': 'testtitle - updated',
            'start_date': '2021-07-24',
            'finish_date': '2021-08-25',
        }

        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_delete_offer_by_unauthorized_user(self):
        '''
        Ensure that offer's deleting by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(self.offer_1 in self.offer_list)

    def test_update_application_by_unauthorized_user(self):

        '''
        Ensure that application's updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('applications-detail', args=(self.application_1.pk,))

        data = {
            'offer': self.offer_1.pk,
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'attachment': self.file
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_partial_update_application_by_unauthorized_user(self):

        '''
        Ensure that application's partial updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('applications-detail', args=(self.application_1.pk,))

        data = {
            'title': 'testtitle - updated'
        }

        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_delete_application_by_unauthorized_user(self):
        '''
        Ensure that application's deleting by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('applications-detail', args=(self.application_1.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(self.application_1 in self.application_list)

    def test_update_user_review_by_unauthorized_user(self):

        '''
        Ensure that user review's updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        data = {
            'user': self.test_user.pk,
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'review': 2
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_partial_update_user_review_by_unauthorized_user(self):

        '''
        Ensure that user review's partial updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        data = {
            'title': 'testtitle - updated',
        }

        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_delete_user_review_by_unauthorized_user(self):
        '''
        Ensure that user review's deleting by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(self.user_review_1 in self.user_review_list)

    def test_update_offer_review_by_unauthorized_user(self):

        '''
        Ensure that offer review's updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        data = {
            'offer': self.offer_1.pk,
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'review': 2
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_partial_update_offer_review_by_unauthorized_user(self):
        '''
        Ensure that offer review's partial updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        data = {
            'title': 'testtitle - updated',
        }

        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_delete_offer_review_by_unauthorized_user(self):
        '''
        Ensure that offer review's deleting by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(self.offer_review_1 in self.offer_review_list)

    def test_update_message_by_unauthorized_user(self):

        '''
        Ensure that message's updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('messages-detail', args=(self.message_1.pk,))

        data = {
            'recipient': self.test_user.pk,
            'content': 'content - updated',
            'attachment': self.file
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_partial_update_message_by_unauthorized_user(self):

        '''
        Ensure that message's partial updating by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('messages-detail', args=(self.message_1.pk,))

        data = {
            'recipient': self.test_user.pk,
            'content': 'content - updated',
        }

        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_delete_message_by_unauthorized_user(self):

        '''
        Ensure that message's deleting by non-author user is forbidden
        '''

        self.client.login(username='testuser', password='testpassword')

        url = reverse('messages-detail', args=(self.message_1.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(self.offer_review_1 in self.offer_review_list)


class TestForceAuthenticationMixin(AuthenticateMixin, APITestCase):

    def setUp(self):

        super().setUp()

    def test_forcing_authentication(self):
        ''''
        Testing forcing authentication of user
        '''

        self.assertTrue(self.test_user.is_authenticated, True)
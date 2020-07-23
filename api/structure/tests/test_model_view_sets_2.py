from django.urls import reverse
from rest_framework.test import APITestCase
from api.users.models import User
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from api.structure.models import (
    Offer,
    Application,
    OfferReview,
    UserReview
)


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

        self.objects_number = 5

        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())

        for i in range(1, self.objects_number + 1):
            Offer.objects.create(title=f'title{i}', author=self.test_user,
                                 content=f'content{i}', start_date="2021-07-23",
                                 finish_date="2021-08-23", salary=500, country="AF")

        self.application = Application.objects.create(offer=Offer.objects.get(title='title1'), applicant=self.test_user,
                                                      title="title1", content="content1", attachment=self.file)

        self.offer_1 = Offer.objects.get(title='title1')

        self.application_1 = Application.objects.get(title='title1')

        self.offer_list = Offer.objects.all()

        self.application_list = Application.objects.all()

        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())

        self.user_review = UserReview.objects.create(user=self.test_user, author=self.test_user, title='title1',
                                                     content='content1', review=2)

        self.offer_review = OfferReview.objects.create(offer=self.offer_1, author=self.test_user, title='title1',
                                                       content='content1', review=2)

        self.user_review_1 = UserReview.objects.get(title='title1')

        self.offer_review_1 = OfferReview.objects.get(title='title1')

        self.user_review_list = UserReview.objects.all()

        self.offer_review_list = OfferReview.objects.all()

    def test_offer_list(self):

        url = reverse('offers-list')

        response = self.client.get(url, format='json')

        for model in self.offer_list:
            self.assertIn(model.title, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_create(self):

        url = reverse('offers-list')

        data = {
            'title': 'testtitle',
            'author': self.test_user,
            'content': 'testcontent',
            'start_date': '2021-07-23',
            'finish_date': '2021-08-23',
            'salary': 500,
            'country': 'AF',
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertIn(data['content'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_offer_detail(self):

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_update(self):

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        data = {
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'start_date': '2021-07-24',
            'finish_date': '2021-08-25',
            'salary': 500,
            'country': 'AF',
        }

        response = self.client.put(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertIn(data['content'], response.content.decode())
        self.assertIn(data['start_date'], response.content.decode())
        self.assertIn(data['finish_date'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_partial_update(self):

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        data = {
            'title': 'testtitle - updated',
            'start_date': '2021-07-25',
            'finish_date': '2021-08-26',
        }

        response = self.client.patch(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertIn(data['start_date'], response.content.decode())
        self.assertIn(data['finish_date'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_delete(self):

        url = reverse('offers-detail', args=(self.offer_1.pk,))

        response = self.client.delete(url)

        self.assertFalse(self.offer_1 in self.offer_list)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_application_list(self):

        url = reverse('applications-list')

        response = self.client.get(url, format='json')

        for model in self.application_list:
            self.assertIn(model.title, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_application_detail(self):

        url = reverse('applications-detail', args=(self.application_1.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_application_create(self):

        url = reverse('applications-list')

        data = {
            'offer': self.offer_1.pk,
            'applicant': self.test_user.pk,
            'title': 'testtitle',
            'content': 'testcontent',
            'attachment': self.file
        }

        response = self.client.post(url, data=data, format='multipart', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_application_update(self):

        url = reverse('applications-detail', args=(self.application_1.pk,))

        data = {
            'offer': self.offer_1.pk,
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'attachment': self.file
        }

        response = self.client.put(url, data=data, format='multipart', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertIn(data['content'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_application_partial_update(self):

        url = reverse('applications-detail', args=(self.application_1.pk,))

        data = {
            'title': 'testtitle - updated',
        }

        response = self.client.patch(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_application_application_delete(self):

        url = reverse('applications-detail', args=(self.application_1.pk,))

        response = self.client.delete(url)

        self.assertFalse(self.application_1 in self.application_list)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_review_list(self):

        url = reverse('users_reviews-list')

        response = self.client.get(url, format='json')

        for model in self.user_review_list:
            self.assertIn(model.title, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_review_detail(self):

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_review_update(self):

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        data = {
            'user': self.test_user.pk,
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'review': 2
        }

        response = self.client.put(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertIn(data['content'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_review_partial_update(self):

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        data = {
            'title': 'testtitle - updated',
        }

        response = self.client.patch(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_review_delete(self):

        url = reverse('users_reviews-detail', args=(self.user_review_1.pk,))

        response = self.client.delete(url)

        self.assertFalse(self.user_review_1 in self.user_review_list)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_offer_review_list(self):

        url = reverse('offers_reviews-list')

        response = self.client.get(url, format='json')

        for model in self.offer_review_list:
            self.assertIn(model.title, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_review_detail(self):

        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_review_update(self):

        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        data = {
            'offer': self.offer_1.pk,
            'title': 'testtitle - updated',
            'content': 'testcontent - updated',
            'review': 2
        }

        response = self.client.put(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertIn(data['content'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_review_partial_update(self):


        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        data = {
            'title': 'testtitle - updated',
        }

        response = self.client.patch(url, data=data, format='json', follow=True)

        self.assertIn(data['title'], response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_review_delete(self):

        url = reverse('offers_reviews-detail', args=(self.offer_review_1.pk,))

        response = self.client.delete(url)

        self.assertFalse(self.offer_review_1 in self.offer_review_list)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from api.structure.tests.test_model_view_sets_2 import AuthenticateMixin
from django.core.paginator import Paginator
from api.chat.models import Message
from api.structure.models import (
    Offer,
    Application,
    OfferReview,
    UserReview
)


class FiltersTestCase(AuthenticateMixin, APITestCase):

    def setUp(self):

        super().setUp()

        self.objects_number = 25

        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())

        for i in range(1, self.objects_number + 1):
            Offer.objects.create(title=f'title{i}', author=self.test_user,
                                 content=f'content{i}', start_date="2021-07-23",
                                 finish_date="2021-08-23", salary=500, country="AF")

        self.file = SimpleUploadedFile(name='test.txt',
                                       content=open('api/structure/tests/test_data/test.txt', 'rb').read())

        for i in range(1, self.objects_number + 1):
            Application.objects.create(offer=Offer.objects.get(title='title1'), applicant=self.test_user,
                                       title=f'title{i}', content=f'content{i}', attachment=self.file)
            OfferReview.objects.create(offer=Offer.objects.get(title='title1'), author=self.test_user,
                                       title=f'title{i}', review=2)
            UserReview.objects.create(user=self.test_user, author=self.test_user,
                                       title=f'title{i}', review=2)
            Message.objects.create(recipient=self.test_user, sender=self.test_user,
                                   content='title{i}', attachment=self.file)

    def test_offer_list_is_paginated(self):

        url = reverse('offers-list')

        paginator = Paginator(Offer.objects.all(), 10)

        response = self.client.get(url)

        self.assertEqual(paginator.count, 25)
        self.assertEqual(paginator.num_pages, 3)

    def test_application_list_is_paginated(self):

        url = reverse('applications-list')

        paginator = Paginator(Application.objects.all(), 10)

        response = self.client.get(url)

        self.assertEqual(paginator.count, 25)
        self.assertEqual(paginator.num_pages, 3)

    def test_user_review_list_is_paginated(self):

        url = reverse('offers-list')

        paginator = Paginator(UserReview.objects.all(), 10)

        response = self.client.get(url)

        self.assertEqual(paginator.count, 25)
        self.assertEqual(paginator.num_pages, 3)

    def test_offer_review_list_is_paginated(self):

        url = reverse('offers-list')

        paginator = Paginator(OfferReview.objects.all(), 10)

        response = self.client.get(url)

        self.assertEqual(paginator.count, 25)
        self.assertEqual(paginator.num_pages, 3)

    def test_message_list_is_paginated(self):

        url = reverse('offers-list')

        paginator = Paginator(Message.objects.all(), 10)

        response = self.client.get(url)

        self.assertEqual(paginator.count, 25)
        self.assertEqual(paginator.num_pages, 3)
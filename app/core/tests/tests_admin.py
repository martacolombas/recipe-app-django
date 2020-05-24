from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@bcn.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@bcn.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """ test that users are listed on the user page """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        """ Performs an http get request to our url """

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        """ assertContains, besides checking containing the item, \
        asserts that the response is 200 and that it looks into the actual \
        content of this res (i.e if the response was an object) """

    def test_user_change_page(self):
        """ test that the user edit page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        #  /admin/core/user/1 --> where id is the id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

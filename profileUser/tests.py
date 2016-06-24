from django.test import TestCase
from django.test.client import RequestFactory

from profileUser.views import ProfileInfo


class ProfileGetInfoPageViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get('/info/')
        request.session = {"patient": 1}
        view_func = ProfileInfo.as_view()
        response = view_func(request)
        self.assertFalse(response.content)


class AppointmentListRedirect(TestCase):
    def test_homepage(self):
        response = self.client.get('/sheet_assignment/')
        self.assertEqual(response.status_code, 200)

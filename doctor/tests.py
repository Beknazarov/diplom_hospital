from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory


# class SnippetCreateViewTest(TestCase):
#     """
#     Test the snippet create view
#     """
#     def setUp(self):
#         self.user = UserFactory()
#         self.factory = RequestFactory()
#     def test_get(self):
#         """
#         Test GET requests
#         """
#         request = self.factory.get(reverse('snippet_create'))
#         request.user = self.user
#         response = SnippetCreateView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context_data['user'], self.user)
#         self.assertEqual(response.context_data['request'], request)


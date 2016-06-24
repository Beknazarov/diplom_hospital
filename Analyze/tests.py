# coding: utf-8
import unittest

from django.test import TestCase
from django.test.client import RequestFactory, Client

from Analyze.models import BloodChemistry
from Analyze.views import GenerateAnalyze


class CreateAnalyzeModelTest(TestCase):
    def test_for_analyze_bloodchemistry(self):
        blood_chm_analyze = BloodChemistry(gamma=5, total_protein=3, albumin=2, globulins=8, betta=3, thymol_test=23)
        self.assertEqual(5, blood_chm_analyze.gamma)
        self.assertEqual(3, blood_chm_analyze.total_protein)
        self.assertEqual(2, blood_chm_analyze.albumin)
        self.assertEqual(8, blood_chm_analyze.globulins)
        self.assertEqual(23, blood_chm_analyze.thymol_test)


class GenerateAnalyzeViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get('/analyze/')
        request.session = {"patient": 1}
        view_func = GenerateAnalyze.as_view()
        response = view_func(request)
        response.render()
        print(request.session)
        self.assertIn('<html lang="en">', response.content)




# coding: utf-8
from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from KIF.models import Drug, Doctor, Patient, Citizenship, Area, Region, Town
# create element
from pharmacy.models import StockTacking, AppointmentList


class DrugNameEqualTest(TestCase):
    def test_string_representation(self):
        drug = Drug(name_drug='drug')
        self.assertEqual(str(drug), drug.name_drug)


class DrugAppViewRedirectTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/admin_pharmacy/')
        self.assertEqual(response.status_code, 200)


class DrugSaveTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='nursultan')

    def test_one_drug(self):
        g = StockTacking(drugSt=Drug.objects.create(name_drug='analgin'), date=datetime.now(), amount=5, rest=5,
                         doctor=Doctor.objects.create(loginDoc=self.user, date_born_doc=datetime.now()))
        g.full_clean()
        g.save()
        self.assertEqual(StockTacking.objects.filter(drugSt__name_drug="analgin").count(), 1)


class AppointmentListCreateModel(TestCase):
    def setUp(self):
        self.area = Area.objects.create(name_area="Osh")
        self.region = Region.objects.create(name_reg='Ozgon', area_fk=self.area)
        self.town = Town.objects.create(name_town="Kurshab", region_fk=self.region)
        self.patient = Patient(surname_pat="Kadyrov", name_pat="Asan", last_name_pat="Kangeldievich",
                               date_born_pat=datetime.now(), rhesusfactor_pat="Rh2+", bloodgroup_pat='2', gender_pat=1,
                               citizenship_fk=Citizenship.objects.create(name_citiz="Kyrgyz"), num_social_protec=1234,
                               area_fk=self.area, region_fk=Region.objects.create(name_reg='Ozgon', area_fk=self.area),
                               num_medic_record=123, street_pat="Bokonbaeva", insurance_territory="Osh",
                               town_fk=self.town)
        self.drug = Drug.objects.create(name_drug='analgin')

    def test_appointment_list(self):
        app_list = AppointmentList(
            drugAl=self.drug,
            descriptionDrinkDrug="one day", amount=3, beginAppointment=datetime.now())
        app_list.save()
        self.assertEqual(AppointmentList.objects.count(), 1)


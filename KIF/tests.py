from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase

from KIF.models import Hospital, Area, Region, Town, Patient, Citizenship, RecordPatient, Department


class CreateAndDeleteHospital(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name_hospit="Kamek")

    def test_add_hospital(self):
        self.assertEqual(self.hospital.name_hospit, "Kamek")

    def test_delete_hospital(self):
        self.hospital = self.hospital.delete()
        self.assertTrue(self.hospital)  # has object


class AuthenticationUserSystem(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="beknazarov", password="12345678n")

    def test_login_user(self):
        self.client.login(username=self.user.username, password=self.user.password)
        user = User.objects.get(username=self.user.username)
        self.assertTrue(user)


def PatientRegister():
    area = Area.objects.create(name_area="Osh")
    region = Region.objects.create(name_reg='Ozgon', area_fk=area)
    town = Town.objects.create(name_town="Kurshab", region_fk=region)
    patient = Patient(surname_pat="Kadyrov", name_pat="Asan", last_name_pat="Kangeldievich",
                      date_born_pat=datetime.now(), rhesusfactor_pat="Rh2+", bloodgroup_pat='2', gender_pat=1,
                      citizenship_fk=Citizenship.objects.create(name_citiz="Kyrgyz"), num_social_protec=1234,
                      area_fk=area, region_fk=Region.objects.create(name_reg='Ozgon', area_fk=area),
                      num_medic_record=123, street_pat="Bokonbaeva", insurance_territory="Osh",
                      town_fk=town)
    return patient


class AddPatientTest(TestCase):
    def test_create_patient(self):
        patient = PatientRegister()
        patient.save()
        self.assertEqual(Patient.objects.count(), patient.id)


class RecordPatientToDoctor(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name_hospit="Kamek")
        self.department = Department.objects.create(name_dept="Urology", hospit_fk=self.hospital, count_ward=2)

    def test_zapis_patient(self):
        patient = PatientRegister()
        patient.save()
        rpatient = RecordPatient.objects.create(patient_fk=patient, num_ward=1, dept_fk=self.department,
                                                hospit_fk=self.hospital)
        self.assertTrue(rpatient)

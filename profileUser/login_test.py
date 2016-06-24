# coding: utf-8
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginPatient(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_auth_patient(self):
        driver = self.driver
        driver.get("https://medlenovo.herokuapp.com/profile/login/")
        username = driver.find_element_by_name("login")
        username.send_keys("nursultan")
        username.send_keys(Keys.RETURN)
        password = driver.find_element_by_name('password')
        password.send_keys("12345")
        driver.find_element_by_class_name("login-submit").click()
        assert u"РНЦУ" in driver.title


class LoginDoctor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_auth_doctor(self):
        driver = self.driver
        driver.get("https://medlenovo.herokuapp.com/doctor/login/")
        username = driver.find_element_by_name("username")
        username.send_keys("zlobin_vladimir")
        password = driver.find_element_by_name('password')
        password.send_keys("12345678n")
        driver.find_element_by_id("signDoc").click()
        assert u"РНЦУ" in driver.title


class LoginPharmacy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_auth_pharmacy(self):
        driver = self.driver
        driver.get("https://medlenovo.herokuapp.com/doctor/login/")
        username = driver.find_element_by_name("username")
        username.send_keys("nadya_batr_68")
        password = driver.find_element_by_name('password')
        password.send_keys("12345678n")
        driver.find_element_by_id("signDoc").click()
        assert u"РНЦУ" in driver.title


class LoginAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_auth_admin(self):
        driver = self.driver
        driver.get("https://medlenovo.herokuapp.com/admin/login/")
        username = driver.find_element_by_name("username")
        username.send_keys("beknazarov")
        password = driver.find_element_by_name('password')
        password.send_keys("nurs11111n")
        driver.find_element_by_xpath("//*[@value='Войти']")
        assert u"Войти | РНЦУ" in driver.title


if __name__ == "__main__":
    unittest.main()

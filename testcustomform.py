import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\driverweb\\chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def take_screenshot(self, name):
        self.driver.save_screenshot(name)

    def test_case1(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohn", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case1_screenshot.png")

    def test_case2(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("Johnj")
        lastNameInput.send_keys("canoncanoncano")
        ageInput.send_keys("149")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: Johnj", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case2_screenshot.png")

    def test_case3(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjo")
        lastNameInput.send_keys("canoncanoncanon")
        ageInput.send_keys("150")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjo", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case3_screenshot.png")

    def test_case4(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohnjohnjo")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohnjohnjo", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case4_screenshot.png")

    def test_case5(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohnjohnjoh")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohnjohnjoh", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case5_screenshot.png")

    def test_case6(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("John")
        lastNameInput.send_keys("cannoncan")
        ageInput.send_keys("75")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Detail Form", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case6_screenshot.png")

    @unittest.skip("Example of skipping a test")
    def test_case7(self):
        self.driver.get("http://localhost/customer/form.html")
        # Test case implementation here

    def test_case8(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("cano")
        ageInput.send_keys("75")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Detail Form", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case8_screenshot.png")

    @unittest.skip("Example of skipping a test")
    def test_case9(self):
        self.driver.get("http://localhost/customer/form.html")
        # Test case implementation here

    def test_case10(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("0")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Detail Form", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case10_screenshot.png")

    def test_case11(self):
        self.driver.get("http://localhost/customer/form.html")
        
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("151")

        # Submit the form
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Detail Form", result)
        
        # Capture screenshot
        self.take_screenshot("img/test_case11_screenshot.png")

if __name__ == "__main__":
    unittest.main()

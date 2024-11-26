import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class FrontendTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver (e.g., Chrome)
        cls.driver = webdriver.Chrome()  # Specify the path if not in PATH
        cls.driver.get('http://localhost:5001')  # Adjust the port if necessary
        cls.driver.maximize_window()
        time.sleep(2)  # Wait for the page to load

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_chat_interface(self):
        driver = self.driver
        # Locate the input field
        input_field = driver.find_element(By.ID, 'user-input')
        # Enter a message
        input_field.send_keys('Hello, how are you?')
        input_field.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for the AI response to appear

        # Verify user's message appears
        user_messages = driver.find_elements(By.CSS_SELECTOR, '.message.user')
        self.assertTrue(any('Hello, how are you?' in msg.text for msg in user_messages))

        # Verify AI's response appears
        ai_messages = driver.find_elements(By.CSS_SELECTOR, '.message.ai')
        self.assertGreater(len(ai_messages), 0)

    def test_empty_message_submission(self):
        driver = self.driver
        input_field = driver.find_element(By.ID, 'user-input')
        # Clear input field and press Enter
        input_field.clear()
        input_field.send_keys(Keys.RETURN)
        time.sleep(1)

        # Check that no new messages have been added
        messages = driver.find_elements(By.CSS_SELECTOR, '.message')
        message_texts = [msg.text.strip() for msg in messages]
        self.assertNotIn('', message_texts)

    def test_directory_loading(self):
        driver = self.driver
        # Click on "Load Directory" button
        load_button = driver.find_element(By.ID, 'browse-button')
        load_button.click()
        time.sleep(1)

        # Note: Handling file upload dialogs requires additional tools like AutoIt (Windows)
        # or PyAutoGUI, as Selenium cannot interact with OS-level dialogs.

        # For testing purposes, verify that the file input exists
        file_input = driver.find_element(By.ID, 'directory-input')
        self.assertIsNotNone(file_input)

    def test_ui_responsiveness(self):
        driver = self.driver
        # Resize window to mobile dimensions
        driver.set_window_size(375, 667)  # iPhone 6/7/8 dimensions
        time.sleep(1)
        # Verify that elements are still accessible
        chat_area = driver.find_element(By.ID, 'chat-container')
        self.assertTrue(chat_area.is_displayed())

        # Resize back to original size
        driver.maximize_window()

    # Additional tests can be added here for other features

if __name__ == '__main__':
    unittest.main() 
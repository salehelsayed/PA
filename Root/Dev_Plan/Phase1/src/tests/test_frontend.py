import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class FrontendTestCase(unittest.TestCase):
    """Test cases for the frontend functionality using Selenium WebDriver.

    This suite tests the UI components, interactions, and responsiveness of the application.

    Important:
    - Before running these tests, ensure the Flask application is running on localhost:5001.
    - WebDriver (e.g., ChromeDriver) must be installed and properly configured.
    """

    @classmethod
    def setUpClass(cls):
        """Initialize the WebDriver and navigate to the application's URL."""
        # Set up the WebDriver (e.g., Chrome)
        cls.driver = webdriver.Chrome()  # Specify the path if not in PATH
        cls.driver.get('http://localhost:5001')  # Adjust the port if necessary
        cls.driver.maximize_window()
        time.sleep(2)  # Wait for the page to load completely

    @classmethod
    def tearDownClass(cls):
        """Quit the WebDriver after all tests have been executed."""
        cls.driver.quit()

    def test_chat_interface(self):
        """Test sending a message through the chat interface and receiving a response."""
        driver = self.driver
        # Locate the input field
        input_field = driver.find_element(By.ID, 'user-input')
        # Enter a message
        input_field.send_keys('Hello, how are you?')
        input_field.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for the AI response to appear

        # Verify user's message appears in the chat
        user_messages = driver.find_elements(By.CSS_SELECTOR, '.message.user')
        self.assertTrue(any('Hello, how are you?' in msg.text for msg in user_messages))

        # Verify AI's response appears in the chat
        ai_messages = driver.find_elements(By.CSS_SELECTOR, '.message.ai')
        self.assertGreater(len(ai_messages), 0)

    def test_empty_message_submission(self):
        """Test that submitting an empty message does not add a new message to the chat."""
        driver = self.driver
        input_field = driver.find_element(By.ID, 'user-input')
        # Clear input field and press Enter
        input_field.clear()
        input_field.send_keys(Keys.RETURN)
        time.sleep(1)

        # Check that no new empty messages have been added
        messages = driver.find_elements(By.CSS_SELECTOR, '.message')
        message_texts = [msg.text.strip() for msg in messages]
        self.assertNotIn('', message_texts)

    def test_directory_loading(self):
        """Test that the 'Load Directory' button and input field are functional."""
        driver = self.driver
        # Click on "Load Directory" button
        load_button = driver.find_element(By.ID, 'browse-button')
        load_button.click()
        time.sleep(1)

        # Note: Handling file upload dialogs requires additional tools like AutoIt or PyAutoGUI,
        # as Selenium cannot interact with OS-level dialogs directly.

        # Verify that the file input element exists
        file_input = driver.find_element(By.ID, 'directory-input')
        self.assertIsNotNone(file_input)

    def test_ui_responsiveness(self):
        """Test the application's responsiveness to different window sizes."""
        driver = self.driver
        # Resize window to simulate a mobile device
        driver.set_window_size(375, 667)  # iPhone 6/7/8 dimensions
        time.sleep(1)
        # Verify that key elements are still accessible
        chat_area = driver.find_element(By.ID, 'chat-container')
        self.assertTrue(chat_area.is_displayed())

        # Resize back to the original size
        driver.maximize_window()

    # Additional tests can be added here for other features.
    # When adding new tests, ensure they do not interfere with existing ones.

    # Encourage Testing:
    # After making changes to the frontend code, run these tests to ensure functionality is intact.

if __name__ == '__main__':
    unittest.main() 
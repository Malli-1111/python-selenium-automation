from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
import time 
import imaplib 
import email 
import re 

# ------------------------ 
# Configuration 
# ------------------------ 
GMAIL_USER = 'mallienturi+test2@gmail.com' 
GMAIL_PASSWORD = 'osud tbcc kfep tlxe'  # Use Gmail App Password (not real password)

# ------------------------ 
# Function: Get OTP from Gmail 
# ------------------------ 
def get_otp_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_USER, GMAIL_PASSWORD)
        mail.select("inbox")

        # Search for emails from Agoda
        result, data = mail.search(None, '(FROM "no-reply@agoda.com")')

        ids = data[0].split()
        print("Debug - Found Agoda emails:", ids)

        if not ids:
            print(" No OTP emails from Agoda found.")
            return None

        latest_email_id = ids[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg["subject"]
        print("Debug - Agoda Email Subject:", subject)

        # Extract body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    charset = part.get_content_charset()
                    if not charset:
                        charset = 'utf-8'
                    body = part.get_payload(decode=True).decode(charset, errors='replace')
                    break
        else:
            charset = msg.get_content_charset()
            if not charset:
                charset = 'utf-8'
            body = msg.get_payload(decode=True).decode(charset, errors='replace')

        print("Debug - Agoda Email Body:", body[:500])  # Print part of body

        match = re.search(r'\b\d{6}\b', body)
        if match:
            return match.group()
        else:
            print("OTP not found in the email body.")
            return None

    except Exception as e:
        print("Failed to retrieve OTP:", e)
        return None

# ------------------------ 
# Function: Login to Agoda 
# ------------------------ 
def login_to_agoda(driver, email):
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.agoda.com/en-gb/")
    driver.maximize_window()

    # Close popup if exists
    try:
        popup_close = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Close"]'))
        )
        popup_close.click()
        print("Popup closed.")
    except:
        print("No popup to close.")

    # Click Sign in / Create Account
    try:
        sign_in_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Sign in"] or .//span[text()="Create account"]]'))
        )
        sign_in_button.click()
        print("Sign-in button clicked.")
    except TimeoutException:
        print("Could not find sign-in button.")
        return

    # Switch to login iframe
    try:
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@data-cy="ul-app-frame"]')))
        driver.switch_to.frame(iframe)
        print("Switched to login iframe.")
    except TimeoutException:
        print("Could not locate iframe.")
        return

    # Enter email and click Continue
    try:
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "id@email.com")]')))
        email_input.clear()
        email_input.send_keys(email)
        print("Email entered.")

        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cy="unified-email-continue-button"]:not([disabled])')))
        continue_button.click()
        print("Continue button clicked.")
    except TimeoutException:
        print("Could not find email input or continue button.")
        return

# ------------------------ 
# Function: Fill Profile 
# ------------------------ 
def fill_profile(driver):
    wait = WebDriverWait(driver, 20)

    # Switch to default content then back into iframe
    driver.switch_to.default_content()
    try:
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@data-cy="ul-app-frame"]')))
        driver.switch_to.frame(iframe)
        print("Switched to profile iframe.")
    except TimeoutException:
        print("Could not locate profile iframe.")
        return

    try:
        # First Name
        first_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-cy="profile-firstname"]')))
        first_name_input.clear()
        first_name_input.send_keys("Mallikarjuna")

        # Last Name
        last_name_input = driver.find_element(By.XPATH, '//input[@data-cy="profile-lastname"]')
        last_name_input.clear()
        last_name_input.send_keys("Naidu")

        print("First name and last name entered.")

        # Continue
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        submit_button.click()
        print("Continue button clicked (profile).")
    except TimeoutException:
        print("Failed to fill profile or submit.")

# ------------------------ 
# Function: Enter OTP 
# ------------------------ 
def enter_otp(driver, otp):
    wait = WebDriverWait(driver, 20)

    driver.switch_to.default_content()
    try:
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@data-cy="ul-app-frame"]')))
        driver.switch_to.frame(iframe)
        print("Switched to OTP iframe.")
    except TimeoutException:
        print("Could not locate OTP iframe.")
        return

    try:
        # Try locating all 6 OTP input fields by data-cy attribute
        otp_inputs = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//input[@type="tel" and @data-cy and contains(@data-cy, "otp-box")]')
        ))

        if len(otp_inputs) != 6:
            print(f"Expected 6 OTP fields, but found {len(otp_inputs)}.")
            return

        for i in range(6):
            otp_inputs[i].clear()
            otp_inputs[i].send_keys(otp[i])
        print("OTP entered.")
    except TimeoutException:
        print("OTP input fields not found.")
    except Exception as e:
        print(f"Failed to enter OTP: {e}")

# ------------------------ 
# Main Test Flow 
# ------------------------ 
if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        login_to_agoda(driver, GMAIL_USER)
        time.sleep(3)  # Wait briefly for transition

        fill_profile(driver)
        time.sleep(5)  # Wait for OTP screen to load

        print("Waiting for OTP email...")
        time.sleep(45)  # Wait before polling Gmail

        otp = get_otp_from_gmail()
        if otp:
            print("OTP received:", otp)
            enter_otp(driver, otp)
            print("Login completed.")
        else:
            print("OTP not received or not found.")

        time.sleep(5)
    finally:
        driver.quit()

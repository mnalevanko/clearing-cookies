import os
import sqlite3
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Expand user directory for file paths
firefox_cookie_path = os.path.expanduser(os.getenv("FIREFOX_PROFILE_PATH"))
chrome_cookie_path = os.path.expanduser(os.getenv("CHROME_COOKIE_PATH"))


def delete_firefox_cookies(cookie_path):
    """Delete cookies from Firefox's cookies.sqlite database."""
    if os.path.exists(cookie_path):
        try:
            conn = sqlite3.connect(cookie_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM moz_cookies")
            conn.commit()
            conn.close()
            print("Firefox cookies deleted successfully.")
        except Exception as e:
            print(f"Error deleting Firefox cookies: {e}")
    else:
        print(f"Firefox cookie file not found at {cookie_path}.")


def delete_chrome_cookies(cookie_path):
    """Delete cookies from Chrome's cookies database."""
    if os.path.exists(cookie_path):
        try:
            conn = sqlite3.connect(cookie_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cookies")
            conn.commit()
            conn.close()
            print("Chrome cookies deleted successfully.")
        except Exception as e:
            print(f"Error deleting Chrome cookies: {e}")
    else:
        print(f"Chrome cookie file not found at {cookie_path}.")


# Delete cookies for both browsers
delete_firefox_cookies(firefox_cookie_path)
delete_chrome_cookies(chrome_cookie_path)

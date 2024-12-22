# Cookie Cleaner Script

This project is a Python script designed to delete cookies stored by Firefox and Chrome/Chromium browsers on a Linux-based system (e.g., Linux Mint). It uses the `sqlite3` library to modify the cookie database files and the `python-dotenv` library to securely manage configuration settings.

## Features
- Deletes all cookies from Firefox and Chrome/Chromium.
- Uses a hidden `.env` file for storing cookie file paths.
- Secure and modular design for easier maintenance.

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.6 or later.
- Required libraries installed (see [Installation](#installation)).
- The browsers (Firefox/Chrome) installed and their profile paths correctly configured.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and specify your browser cookie paths:
   ```env
   FIREFOX_PROFILE_PATH=~/.mozilla/firefox/<profile_folder>/cookies.sqlite
   CHROME_COOKIE_PATH=~/.config/google-chrome/Default/Cookies
   ```
   Replace `<profile_folder>` with your actual Firefox profile folder name.

## Usage

1. Ensure both Firefox and Chrome/Chromium are closed before running the script to prevent database locking errors.

2. Run the script:
   ```bash
   python cookie_cleaner.py
   ```

3. The script will delete all cookies from the specified browser paths.

## File Structure
```
.
├── cookie_cleaner.py     # Main Python script
├── .env                  # Hidden configuration file for storing cookie paths
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
```

## Troubleshooting

### Database is locked
If you encounter the error `database is locked`, ensure that the browsers are completely closed, including any background processes. Use the following commands to terminate lingering processes:
```bash
ps aux | grep firefox
kill <PID>  # Replace <PID> with the process ID
```

### Missing Profile Paths
If you don’t know the profile paths for your browsers, you can find them here:
- **Firefox:**
  Navigate to `about:profiles` in the Firefox address bar to locate your profile folder.
- **Chrome/Chromium:**
  The cookie file is typically located in `~/.config/google-chrome/Default/Cookies` or `~/.config/chromium/Default/Cookies`.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
- Python's `sqlite3` library for database manipulation.
- `python-dotenv` for managing environment variables.
- Open-source tools and libraries that make this project possible.

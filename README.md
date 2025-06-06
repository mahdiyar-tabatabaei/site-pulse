# site-pulse
🌐 Website Status Checker (Python)
A simple Python script that continuously monitors the status of a website and reports whether it's accessible or not.

📌 Features

	- Sends a request to a given URL every 3 seconds

	- Prints the HTTP status code with success/error messages

	- Handles connection errors gracefully

	- Stops monitoring with Ctrl + C

🚀 How to Run

	1.Make sure you have Python 3.x installed.

	2.Install the required library if not already installed:
		pip install requests

	3.Clone the repository or download the script:
		git clone https://github.com/mahdiyar-tabatabaei/site-pulse
		cd site-pulse

	4.Run the script:
		python SitePulse.py

🛠️ How It Works

	The user enters a website URL (e.g., https://example.com).

	The script checks the site’s availability every 3 seconds.

It shows:

	✅ [SUCCESS] if status code is 200 or 201

	❌ [ERROR] for other status codes

	⚠️ [CONNECTION ERROR] if the site is unreachable

	Press Ctrl + C to stop monitoring.

🗂️ File Structure

	status_checker.py          # Main script for website monitoring
	README.md                  # Project documentation
👤 Author
	[Mahdiyar Tabatabaei](https://github.com/mahdiyar-tabatabaei)

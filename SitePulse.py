import requests
import time


def check_website_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code in [200, 201]:
            print(f"[SUCCESS] {url} --> Status Code: {status_code}")
        else:
            print(f"[ERROR] {url} --> Status Code: {status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[CONNECTION ERROR] {url} --> Error: {e}")


def main():
    url = input("Enter the website URL (https://example.com): ").strip()

    if not url.startswith("http"):
        url = "https://" + url

    print(f"Checking website status every 3 seconds for: {url} (CTRL + C to stop)")

    try:
        while True:
            check_website_status(url)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()

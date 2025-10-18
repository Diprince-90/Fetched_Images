import requests
import os
from urllib.parse import urlparse

def get_filename(url):
    # Try to get the filename from the URL
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    return name if name else "downloaded_image.jpg"

def fetch_image(url, folder):
    try:
        # Add a User-Agent to avoid 403 errors
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check if it's an image
        if not response.headers.get("Content-Type", "").startswith("image/"):
            print(f"⚠️ Not an image: {url}")
            return

        # Create filename and save path
        filename = get_filename(url)
        path = os.path.join(folder, filename)

        # Save the image
        with open(path, "wb") as file:
            file.write(response.content)

        print(f"✅ Saved: {filename}")
        print(f"📁 Location: {os.path.abspath(path)}")

    except requests.exceptions.RequestException as err:
        print(f"❌ Error downloading {url}: {err}")

def main():
    print("🌍 Ubuntu Image Fetcher")
    print("Collect and save images from the web\n")

    # Ask user for image URLs
    urls = input("Enter image URLs separated by commas:\n").split(',')

    # Create folder to store images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    # Download each image
    for url in map(str.strip, urls):
        if url:
            fetch_image(url, folder)

    print("\n🤝 All done! Images are saved and ready to share.")

if __name__ == "__main__":
    main()
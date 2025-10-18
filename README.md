# Fetched_Images
🌍 Ubuntu Image Fetcher
A simple Python tool for respectfully and mindfully collecting images from the web — built on the Ubuntu philosophy: "A person is a person through other persons."

🧰 What It Does
Ubuntu Image Fetcher lets you:
- ✅ Download one or more images from the internet using their URLs
- ✅ Save them in a neatly organized folder called Fetched_Images
- ✅ Handle errors gracefully (like broken links or non-image files)
- ✅ Print the full path to each saved image so you can find it easily

🚀 How to Use
- Install Python (if you haven’t already):
Download Python
- Install the requests library:
pip install requests
- Run the script:
python ubuntu_image_fetcher.py
- Enter image URLs when prompted, separated by commas:
https://example.com/image1.jpg, https://example.com/image2.png
- Find your images in the Fetched_Images folder created next to the script.

📁 Project Structure
Ubuntu_Requests/
├── image_fetcher.py          # Main script
├── README.md                 # This file
└── Fetched_Images/           # Folder where images are saved


🛡️ Safety Tips
- Only download images from trusted sources.
- Avoid URLs that point to unknown or suspicious websites.
- The script checks for valid image content types before saving.

🙌 Contributing
Want to improve the tool? Add features like:
- Duplicate detection
- Image previews
- GUI interface
Pull requests welcome!

📜 License
This project is open-source under the MIT License.


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

# URL of the website
url = input("Enter the URL: ")
article_name = input("Enter the Article-Name: ")

# Create the "products" directory if it doesn't exist
directory = "products/" + article_name
if not os.path.exists(directory):
    os.makedirs(directory)

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all img tags on the page
img_tags = [tag for tag in soup.find_all("img") if not tag.get("src", "").endswith(".svg")]

# Find all source tags with type="video/mp4"
mp4_tags = soup.find_all("source", type="video/mp4")

# Function to sanitize filenames
def sanitize_filename(filename):
    # Replace invalid characters with underscores
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized


# Function to check if a URL has a specific extension
def has_extension(url, extension):
    return url.lower().endswith(extension)

# Download and save each image
for img_tag in img_tags:
    # Get the source URL of the image
    img_url = img_tag.get("src")

    # If the URL is relative, convert it to an absolute URL
    img_url = urljoin(url, img_url)

    # Extract the filename from the URL
    filename = os.path.basename(urlparse(img_url).path)

    # Check if the file has an SVG extension and skip it
    if has_extension(filename, ".svg"):
        continue

    # Sanitize the filename
    filename = sanitize_filename(filename)

    # Save the image to the "products" directory
    filepath = os.path.join(directory, filename)

    # Send a GET request to download the image
    img_response = requests.get(img_url)

    # Save the image to the file
    with open(filepath, "wb") as file:
        file.write(img_response.content)

    print(f"Downloaded: {filepath}")

# Download and save each MP4 file
for mp4_tag in mp4_tags:
    # Get the source URL of the MP4 file
    mp4_url = mp4_tag.get("data-src") or mp4_tag.get("src")

    # If the URL is relative, convert it to absolute URL
    mp4_url = urljoin(url, mp4_url)

    # Extract the filename from the URL
    filename = os.path.basename(urlparse(mp4_url).path)

    # Sanitize the filename
    filename = sanitize_filename(filename)

    # Save the MP4 file to the "products" directory
    filepath = os.path.join(directory, filename)

    # Send a GET request to download the MP4 file
    mp4_response = requests.get(mp4_url)

    # Save the MP4 file to the file
    with open(filepath, "wb") as file:
        file.write(mp4_response.content)

    print(f"Downloaded: {filepath}")
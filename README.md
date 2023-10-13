# Article - Picture and Video Downloader

This Python script allows you to download images and MP4 files from a web page. It's a simple and efficient tool for web scraping. Just provide the URL of the webpage you want to scrape, as well as the name you'd like to give to the downloaded files, and the script will do the rest.

## Getting Started

These instructions will help you get the script up and running on your local machine.

### Prerequisites

To use this script, you'll need:

- Python (version 3.x)
- The following Python libraries: `os`, `requests`, `BeautifulSoup`, and `re`

You can install these libraries using pip:

```
pip install requests
pip install beautifulsoup4
```

### Installing

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the script.

3. Run the script using the following command:

```
python web_scraper.py
```

## Usage

1. Upon running the script, it will prompt you to enter the URL of the webpage you want to scrape.

2. You'll also be asked to provide a name for the article you are downloading. This will be used to create a directory where the downloaded files will be stored.

3. The script will create a directory named after the article name you provided in the "products" directory.

4. It will then fetch the content of the provided URL and search for all image and MP4 file links on the page.

5. Images are downloaded and saved in the article's directory, while MP4 files are saved in the same directory.

6. Filenames are sanitized to replace invalid characters with underscores, ensuring compatibility with your system.

7. Once the download is complete, the script will display a message for each downloaded file.

## Example

```
Enter the URL: https://example.com/some-webpage
Enter the Article-Name: my-article

...
Downloaded: products/my-article/image_1.jpg
Downloaded: products/my-article/image_2.png
Downloaded: products/my-article/video_1.mp4
```

## Customization

- You can customize the script to handle additional file types or perform other actions based on your specific requirements.

- You can modify the script to download files from multiple URLs or web pages by wrapping the existing code in a loop.

## Disclaimer

Please be aware that web scraping may be subject to legal restrictions and ethical considerations. Always ensure that you have the right to access and download content from a website before using this script.

## Authors

- [Your Name]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the creators of the Python libraries used in this script: [requests](https://docs.python-requests.org/en/latest/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and [Python's re module](https://docs.python.org/3/library/re.html).
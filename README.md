# Amazon Product Scraper

This Python script allows you to scrape product information from an Amazon search results page for a specific query. It retrieves the titles, prices, and reviews (if available) of the products and saves the data in a CSV file for further analysis.

## Prerequisites

To run this script, you need to have the following dependencies installed:

- Python 3
- requests library (`pip install requests`)
- pandas library (`pip install pandas`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Getting Started

1. Clone this repository or download the `scraper.py` file.

2. Open the `scraper.py` file in a text editor or an integrated development environment (IDE).

3. Replace the value of the `url` variable with the desired Amazon search results page URL for your query. Make sure to enclose the URL within quotes.

4. Run the script using Python: `python scraper.py`.

5. The script will scrape the product titles, prices, and reviews (if available) from the specified Amazon page. The data will be saved in a CSV file named "dataNew.csv" in the same directory.

6. Once the script finishes executing, you can open the CSV file to access the scraped data.

## Customization

- If you want to scrape a different Amazon search results page, you can modify the `url` variable in the script accordingly.

- You can customize the CSV file name and location by changing the value of the `to_csv()` method in the script.

## Limitations

Please note that web scraping is subject to the terms of service of the website you are scraping. Make sure to review and comply with Amazon's terms of service or any other website you intend to scrape.

## Troubleshooting

If any exceptions or errors occur during the execution of the script, an error message will be printed to the console. Make sure you have a stable internet connection and all the necessary dependencies installed.

If you encounter any issues or have any questions, feel free to reach out for assistance.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use the code according to your needs.

**Note:** This script is provided as a starting point for web scraping Amazon product data and is intended for educational purposes only. Use it responsibly and respect the terms of service of the websites you scrape.

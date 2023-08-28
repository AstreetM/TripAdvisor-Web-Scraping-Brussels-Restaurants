# TripAdvisor Web Scraping - Brussels Restaurants

This repository contains code for extracting information about Brussels restaurants from TripAdvisor using web scraping techniques.

## Prerequisites

Before running the code, make sure you have the following dependencies installed on your system:

- Python 3.x
- Python Libraries: advertools, selenium, beautifulsoup4, pandas, openpyxl, requests

## Usage

### Part 1 - Extracting URLs

1. Run the code for Part 1 by executing the `partie1.py` file.
2. Ensure that the collected URLs are saved in the `url_brussels_tripadvisor.xlsx` file.

### Part 2 - Web Scraping Data

1. Make sure the `url_brussels_tripadvisor.xlsx` file containing the collected URLs is present.
2. Run the code for Part 2 by executing the `partie2.py` file.
3. The scraped data will be saved in the `resultats_new_tripadvisor.xlsx` file.

## Execution

1. Open your terminal.
2. Navigate to the directory where the `partie1.py` and `partie2.py` files are located.
3. Use the command `python partie1.py` to run Part 1.
4. Then, use the command `python partie2.py` to run Part 2.

## Output Files

- `url_brussels_tripadvisor.xlsx`: Excel file containing the collected restaurant URLs.
- `resultats_new_tripadvisor.xlsx`: Excel file containing the scraped data for each restaurant.

## Customization

You can customize the behavior of the code by modifying certain parameters in the scripts:

- Change the `timeout` parameter in the `requests.get` function to adjust the timeout duration for making web requests.
- Modify the number of URLs processed by adjusting the range in the loop (e.g., `for e in list_url[0:4200]:`).

## Additional Information

For additional information on how the code works and its specific features, refer to the comments within the code files.

---

Feel free to personalize these instructions based on your code and specific needs. Make sure to include all necessary steps for users to successfully run your code.

# Divar Car Scraper 

A Python-based web scraper for collecting car advertisements from Divar and storing the data in a SQLite database.

This project is part of my journey in data collection, web scraping, and machine learning development.  
The goal is to gradually improve the scraper and later use the collected data for data analysis and ML models such as car price prediction.

---

## Features

- Scrape car advertisements from Divar
- Extract:
  - Car title
  - Mileage
  - Price
- Store data in SQLite database
- Simple and lightweight structure
- Easy to extend and improve

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- SQLite3

---

## Project Structure

```bash
divar-car-scraper/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── cars.db
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/divar-car-scraper.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scraper with:

```bash
python main.py
```

The scraped data will be stored in:

```bash
cars.db
```

---

## Future Improvements

- Better error handling
- Data cleaning
- Export to CSV/JSON
- Selenium integration
- Proxy/User-Agent rotation
- Machine Learning price prediction
- REST API
- Dashboard & visualization

---

## Notes

This project is for educational purposes only.

Divar may block scraping requests if too many requests are sent in a short period of time. Future versions will include anti-blocking improvements.

---

## Author

Developed by Shiva Badalzadeh

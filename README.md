# Fake Store API ETL Pipeline

A simple ETL pipeline that extracts product and user data from the
[Fake Store API](https://fakestoreapi.com), transforms it using pandas,
and loads it into a PostgreSQL database.

## Architecture

```
Fake Store API  -->  Extract (requests)  -->  Transform (pandas)  -->  Load (SQLAlchemy)  -->  PostgreSQL
```

## Tech Stack

- Python 3.13
- pandas, requests
- SQLAlchemy, psycopg 3
- PostgreSQL

## Project Structure

```
Fake_Api Project/
├── etl/
│   ├── extract.py      # Fetches data from the API
│   ├── transform.py    # Cleans and reshapes the data
│   └── load.py         # Loads data into PostgreSQL
├── main.py             # Runs the full pipeline
├── requirements.txt
├── .env.example
└── README.md
```

## How It Works

1. **Extract**: calls the `/products` and `/users` endpoints and builds DataFrames.
2. **Transform**: renames columns, flattens nested user fields (name, address), fixes data types.
3. **Load**: writes the cleaned data to PostgreSQL tables `products` and `users`.

## Database Tables

**products**: product_id, product_name, product_price, product_category, description

**users**: user_id, user_email, username, first_name, last_name, street, city, zipcode

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create a PostgreSQL database named `fake_store_db`
4. Copy `.env.example` to `.env` and fill in your credentials
5. Run the pipeline
   ```bash
   python main.py
   ```

## Sample Output

(Yahan terminal ka screenshot aur pgAdmin me table ka screenshot daalo)

## Future Improvements

- Add logging and error handling
- Incremental loads instead of `replace`
- Dockerize the project
- Schedule with Apache Airflow
- Add data quality checks

## Author

Azeem Akhtar | [LinkedIn][https://www.linkedin.com/in/azeemakhtar-] | [GitHub][https://github.com/Azeem8541]

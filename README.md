# Customer Churn Data Pipeline

## Overview

This project demonstrates an end-to-end data engineering pipeline for an e-commerce customer churn use case.

The pipeline extracts transactional and customer data from PostgreSQL, exports it into CSV files, and loads the data into an AWS S3 data lake. The entire workflow is orchestrated using Apache Airflow and runs inside Docker containers.

This project showcases core data engineering concepts including ETL pipelines, workflow orchestration, containerized environments, and cloud storage integration.

---

## Data Source

The dataset used in this project is **synthetic data generated for demonstration purposes**.

The tables simulate a typical e-commerce environment and include:

* customers
* orders
* payments
* support_tickets

The data was generated to mimic realistic customer behavior and transaction patterns for the purpose of building and demonstrating a data pipeline.

No real customer or sensitive data is used in this project.

---

## Architecture

PostgreSQL → Airflow DAG → CSV Files → AWS S3 Data Lake

**Workflow Steps**

1. Extract data from PostgreSQL
2. Convert tables into CSV format using Python and Pandas
3. Store data locally as raw files
4. Upload the files to AWS S3

---

## Technologies Used

* Python
* Apache Airflow
* Docker
* PostgreSQL
* AWS S3
* Pandas
* SQLAlchemy
* Boto3

---

## Project Structure

```
customer-churn-pipeline
│
├── dags
│   └── etl_pipeline.py
│
├── scripts
│   ├── export_data.py
│   └── upload_to_s3.py
│
├── data
│   └── raw
│
├── docker-compose.yaml
├── README.md
├── .gitignore
```

---

## Pipeline Workflow

### 1. Data Extraction

The pipeline connects to PostgreSQL and exports the following tables:

* customers
* orders
* payments
* support_tickets

These tables represent customer activity and support interactions used for churn analysis.

### 2. Data Transformation

The extracted tables are converted to CSV format using Pandas.

Example output:

```
data/raw/customers.csv
data/raw/orders.csv
data/raw/payments.csv
data/raw/support_tickets.csv
```

### 3. Data Load

The CSV files are uploaded to AWS S3.

Example structure in S3:

```
s3://ash-customer-churn-pipeline/raw/customers.csv
s3://ash-customer-churn-pipeline/raw/orders.csv
s3://ash-customer-churn-pipeline/raw/payments.csv
s3://ash-customer-churn-pipeline/raw/support_tickets.csv
```

---

## Running the Pipeline

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/customer-churn-pipeline.git
cd customer-churn-pipeline
```

### 2. Configure Environment Variables

Create a `.env` file containing:

```
AIRFLOW_UID=50000

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
S3_BUCKET=ash-customer-churn-pipeline

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=host.docker.internal
DB_PORT=5432
DB_NAME=churn_db
```

### 3. Start Airflow

```
docker compose up
```

### 4. Access Airflow UI

```
http://localhost:8080
```

Default credentials:

```
Username: airflow
Password: airflow
```

### 5. Trigger the DAG

Run the pipeline:

```
customer_churn_etl
```

---

## Future Improvements

Planned improvements for this pipeline include:

* Add a **processed data layer**
* Implement **data quality checks**
* Build a **feature engineering pipeline**
* Train a **customer churn prediction model**
* Add **Spark-based transformations**
* Implement **data warehouse analytics layer**

---

## Learning Outcomes

This project demonstrates practical experience with:

* Building ETL pipelines
* Workflow orchestration using Airflow
* Containerized data pipelines using Docker
* Managing credentials securely using environment variables
* Loading data into cloud storage (AWS S3)

---

## Author

Ashraf

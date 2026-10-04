# IBM Data Engineering Capstone Projects

This repository contains coursework completed during the IBM Data Engineering Professional Certificate on Coursera. It collects examples of SQL data modeling, batch data movement, Apache Airflow orchestration, Apache Spark analytics, and Spark ML.

The files are presented as a learning portfolio. They are not currently packaged as a one-command production application: several exercises were designed to run inside the IBM Skills Network/Coursera environment and use course-provided services, files, and paths.

## What is included

### Apache Spark and Spark ML

`Bigdata and Spark_Spark_MLOps_v3.ipynb` demonstrates:

- downloading the course search-term dataset;
- loading and analyzing e-commerce search data with PySpark;
- using Spark ML components such as `StringIndexer`, `VectorAssembler`, `StandardScaler`, and `LinearRegression`;
- loading a saved Spark regression model and generating predictions.

The notebook downloads `searchterms.csv` and `model.tar.gz` from the IBM Skills Network course storage when its setup cells are run.

### SQL data warehousing

- `CREATE_SCRIPT.sql` creates a dimensional sales model with date, category, country, and sales fact tables.
- `schema.sql` contains a related PostgreSQL star-schema definition for the SoftCart sales model.
- `sales.sql`, `sales_data.sql`, and `backup.sql` are SQL exports used as source or sample data for the exercises.
- `Designrelationships.png` shows the database relationships.

### Incremental database loading

`automation.py` demonstrates an incremental load from a MySQL staging database to a PostgreSQL data warehouse. It finds the largest existing `rowid`, selects newer rows, inserts them into the destination, and commits the transaction.

The script expects a MySQL database named `sales` and a PostgreSQL database containing a compatible `sales_data` table. Connection settings are currently placeholders in the script and must be configured before use.

### Airflow web-log pipeline

`process_web_log.py` defines an Airflow DAG with three tasks:

1. extract IP addresses from `accesslog.txt`;
2. remove the unwanted IP address;
3. archive the transformed output as `weblog.tar`.

The DAG was written for the course Airflow environment and currently uses `/home/project/airflow/dags/capstone/` as its working directory.

### Database export

`datadump.sh` is a small MySQL export command for the `sales_data` table. It expects a MySQL service named `mysql`, such as the service used in the course environment.

The PDF files contain dashboard/report deliverables from the course:

- `finaldashboardibm.pdf`
- `sales_report.pdf`

## Environment and reproducibility

This repository is **partially configurable**, but not fully portable yet.

| Component | Expected environment |
| --- | --- |
| Spark notebook | Python, Java, PySpark 3.1.2, findspark, and a working Spark installation |
| Incremental load | MySQL, PostgreSQL, `mysql-connector-python`, and `psycopg2` |
| Airflow pipeline | Apache Airflow with BashOperator and a writable DAG directory |
| SQL scripts | MySQL for the `sales` exports and PostgreSQL for the dimensional schemas |

The original course environment supplied some of these dependencies and database services. The repository does not include Docker Compose files, database credentials, the Airflow input log, or a pinned dependency file, so a new user should expect setup work.

## Running the notebook

1. Open `Bigdata and Spark_Spark_MLOps_v3.ipynb` in Jupyter or VS Code with a Python environment that can run PySpark.
2. Install or enable Java and Spark.
3. Run the setup cells first. They install the notebook dependencies and download the course datasets/models.
4. Run the cells from top to bottom.

The notebook requires internet access for the course downloads. If the download URLs change, download the files manually and place them beside the notebook before running the corresponding Spark cells.

## Running the database examples

1. Create the required MySQL and PostgreSQL databases.
2. Load only the SQL export or schema intended for that database.
3. Configure the connection values in `automation.py` using environment variables or another local secret store before running it.
4. Run the script from an environment containing the MySQL and PostgreSQL Python drivers.

Do not commit real database passwords, private connection strings, customer data, or production exports. The SQL files should be verified as synthetic or course-provided before public release.

## Running the Airflow DAG

1. Place `process_web_log.py` in the Airflow DAGs directory.
2. Place a permitted `accesslog.txt` input file in the directory expected by the DAG.
3. Update the working directory in the Bash commands if your Airflow installation uses a different path.
4. Enable the `process_web_log` DAG and run it after Airflow discovers the file.

## Known limitations

- `requirements.txt` is not populated yet, so dependencies are not reproducibly installed.
- Database connection settings and Airflow paths are embedded in the example scripts.
- There are no automated tests or local service definitions.
- The notebook contains course download commands and saved execution outputs.
- The SQL exports may contain large sample datasets and should be reviewed for redistribution rights.

## Attribution

This work was completed as part of the IBM Data Engineering Professional Certificate on Coursera. Course-provided datasets, models, and infrastructure remain subject to their original terms of use.

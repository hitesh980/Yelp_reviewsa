# Yelp_reviews

Data architecture
![Screenshot 2025-03-25 at 9 16 19 PM](https://github.com/user-attachments/assets/07d4aa1c-dcdc-462e-9812-269d1e752140)

Project Overview
The project involves processing and analyzing Yelp data, including reviews and business information, using a combination of technologies. The workflow is structured as follows:

Data Sources:
Yelp Reviews: A large dataset (~5GB, 7 million reviews) in JSON format.
Yelp Businesses: A smaller dataset (~100MB) in JSON format.

Data Processing:
A Python program is used to preprocess the JSON data and split it into smaller chunks for efficient handling.
The processed JSON files are stored in Amazon S3, a cloud storage service.

Data Loading and Transformation:
The JSON files are loaded into Snowflake, a cloud-based data warehouse.
Snowflake flattens the hierarchical JSON data into tabular format for easier querying.

Analysis:
Sentiment analysis is performed using a User-Defined Function (UDF) integrated into Snowflake.
SQL queries are used for further data analysis and visualization.

Technologies Used
Python: For preprocessing the JSON data and splitting it into manageable chunks.

Amazon S3: For cloud storage of the processed JSON files.
Snowflake: For data warehousing, flattening JSON data, and running SQL queries.
UDF (User-Defined Function): For sentiment analysis on review data.
SQL: For querying and analyzing the transformed data.
This setup efficiently handles large-scale data processing, storage, and analysis while leveraging cloud-based tools for scalability.

# Tokyo Olympics 2020 Data Engineering and Analytical Project

## Description

This project provides a data engineering and analytical journey on the Tokyo Olympic dataset. Starting with a CSV on GitHub, the data is ingested into the Azure ecosystem via Azure Data Factory. It's initially stored in Azure Data Lake Storage Gen2, then transformed in Azure Databricks. The enriched data, once again housed in ADLS Gen2, undergoes advanced analytics in Azure Synapse. The insights are finally visualized in Azure Synapse or Power BI, offering a comprehensive view of the dataset.

## Architecture
![Architecture](https://github.com/FarhanAK20/Olympics-Data-Analytics/assets/86559747/d5d4188e-25e7-466f-9df7-aee415036ac0)


### Dataset Used

This dataset contains the details of over 11,000 athletes, with 47 disciplines, along with 743 teams taking part in the 2021 (2020) Tokyo Olympics. It includes information about athletes, coaches, teams participating, and entries by gender. The dataset provides details such as names, countries represented, discipline, gender of competitors, and names of the coaches.

Source (Kaggle): [2021 Olympics in Tokyo](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo)

### Azure Services Used

- **Azure Data Factory:** For data ingestion from GitHub.
- **Azure Data Lake Storage Gen2:** As the primary data storage solution.
- **Azure Databricks:** For data transformation tasks.
- **Azure Synapse Analytics:** To perform in-depth data analytics.
- **Power BI:** For data visualization and reporting.

## Workflow

### Initial Setup

1. **Create Azure Free Subscription Account**
2. **Create a Resource Group:** 'tokyo-olympic-data' to house and manage all the Azure resources associated with this project.
3. **Set Up a Storage Account:** Specifically configured to leverage Azure Data Lake Storage (ADLS) Gen2 capabilities.
4. **Create a Container:** Inside this storage account to hold the project's data. Two directories, 'raw-data' and 'transformed-data', are created to store raw data and transformed data.
<img width="959" alt="Blob storage" src="https://github.com/FarhanAK20/Olympics-Data-Analytics/assets/86559747/bb36758b-9552-4927-afa4-f6f1487b8893">


### Data Ingestion using Azure Data Factory

1. **Create an Azure Data Factory Workspace:** Within the previously established resource group.
2. **Launch Azure Data Factory Studio.**
3. **Upload the Tokyo Olympics Dataset:** From Kaggle to GitHub.
4. **Initialize a New Data Integration Pipeline:** Use the task Copy Data to move data efficiently between various supported sources and destinations.
5. **Configure the Data Source:** Use HTTP template as we are using an HTTP request to get the data from the GitHub repo.
6. **Establish the Linked Service for Source.**
7. **Configure the File Format and Linked Service Sink.**
8. **Repeat the Above Steps:** To load all the datasets.
9. **Run the Pipeline:** Connect all the copy data activities together and run them all at once.
10. **Validate the Data:** After the pipeline completes its execution, navigate to your Azure Data Lake Storage Gen2. Check the "raw_data" folder to ensure that the files, like "athletes.csv", "medals.csv", etc., are present and populated with the expected data.
![datafactory_pipeline](https://github.com/FarhanAK20/Olympics-Data-Analytics/assets/86559747/729a64b7-856c-4e32-95c4-710b6d052373)


### Data Transformation using Azure Databricks

1. **Create a Databricks Workspace:** Within the previously established resource group and launch it.
2. **Configure Compute in Databricks.**
3. **Create a New Notebook:** Within Databricks and rename it appropriately, reflecting its purpose or the dataset it pertains to.
4. **Establish a Connection to Azure Data Lake Storage (ADLS):** Using the credentials (Client ID, Tenant ID, Secret), write the appropriate code in the Databricks notebook to mount ADLS.
5. **Write Data Transformations:** Mount ADLS Gen2 to Databricks.
6. **Write Transformed Data to ADLS Gen2.**


### Setting Up and Using Azure Synapse Analytics

1. **Create a Synapse Analytics Workspace.**
2. **Create a Database:** Within the Workspace, navigate to the "Data" section, choose "Lake Database," and create a Database "TokyoOlympicDB".
3. **Create Tables from Data Lake:** Use the Transformed Data folder within your ADLS Gen2 storage.

### Performing Data Analysis

1. **Generate Analysis Reports:** Use Power BI for visualization.

Refer to the Power BI for data analysis: [Tokyo Olympic Data Analysis](https://app.powerbi.com/links/sWv9tGnbRh?ctid=e4d98dd2-9199-42e5-ba8b-da3e763ede2e&pbi_source=linkShare)

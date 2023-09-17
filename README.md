# Automated BigQuery Data Loader

Automate the process of loading data into BigQuery from various sources.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

This project provides a Python script that automates the loading of data into BigQuery from various sources like CSV files.

## Getting Started

Create a Google Cloud Account
Create Service Account
Manage Keys - Create New Key
Create Dataset
Create Table

### Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed
- pip install pandas
- pip install google-cloud-bigquery
- pip install pyarrow
- Install Google Cloud SDK

### Installation

Clone this repository:

   git clone https://github.com/your-username/automated-bigquery-data-loader.git

## Usage

1. Place your CSV file with the data in the data/ folder.

2. Configure the script (e.g., BigQuery table details, column mappings) in automated-data.py.

3. Run the script:

  python automated-data.py

### License

This project is licensed under the MIT License.

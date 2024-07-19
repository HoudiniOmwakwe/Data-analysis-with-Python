# Data Analysis with Pandas

This project demonstrates how to analyze a dataset using the Pandas library in Python. The dataset consists of information about individuals, including their age, workclass, education, marital status, occupation, race, sex, capital gain, capital loss, hours per week, native country, and salary.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Questions Answered](#questions-answered)
- [Code Explanation](#code-explanation)

## Installation

To run this project, you need to have Python and Pandas installed. You can install Pandas using pip:

```bash
pip install pandas

## Usage
Save the provided script as data_analysis.py.
Run the script using Python: 
python data_analysis.py

## Questions Answered

The script answers the following questions using the dataset:

How many people of each race are represented in this dataset?
What is the average age of men?
What is the percentage of people who have a Bachelor's degree?
What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
What percentage of people without advanced education make more than 50K?
What is the minimum number of hours a person works per week?
What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
What country has the highest percentage of people that earn >50K and what is that percentage?
Identify the most popular occupation for those who earn >50K in India.

## Code Explanation
The script performs the following steps:

Create the DataFrame: The dataset is hard-coded into a dictionary and converted to a Pandas DataFrame.

Race Count: Uses value_counts() to count occurrences of each race in the dataset.

Average Age of Men: Filters the DataFrame for males and then computes the mean age.

Percentage with Bachelor's Degree: Checks for 'Bachelors' in the 'education' column and computes the mean (as a percentage).

Percentage of People with Advanced Education Earning >50K: Uses isin() to filter for advanced education levels, then computes the mean of those earning >50K.

Percentage of People without Advanced Education Earning >50K: Uses the negation (~) of the advanced education filter to compute the mean of those earning >50K.

Minimum Hours Worked per Week: Uses min() on the 'hours-per-week' column.

Percentage of Min Hours Workers Earning >50K: Filters for minimum hours worked, then computes the mean of those earning >50K.

Country with Highest Percentage of People Earning >50K: Counts occurrences of >50K earners by country, then computes the percentage relative to the total number of people from each country.

Most Popular Occupation for >50K Earners in India: Filters for individuals from India earning >50K, then uses mode() to find the most common occupation.

By running the script, you will get answers to all the questions listed above based on the provided dataset.



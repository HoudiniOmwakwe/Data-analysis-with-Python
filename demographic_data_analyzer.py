import pandas as pd

# Creating the DataFrame from the provided data
data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}

df = pd.DataFrame(data)

# 1. How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()
print("Race count:\n", race_count)

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print("Average age of men:", average_age_men)

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
print("Percentage with Bachelor's degree:", percentage_bachelors)

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_advanced_education_rich = ((advanced_education) & (df['salary'] == '>50K')).mean() * 100
print("Percentage of advanced education >50K:", percentage_advanced_education_rich)

# 5. What percentage of people without advanced education make more than 50K?
percentage_non_advanced_education_rich = ((~advanced_education) & (df['salary'] == '>50K')).mean() * 100
print("Percentage of non-advanced education >50K:", percentage_non_advanced_education_rich)

# 6. What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()
print("Minimum hours per week:", min_hours_per_week)

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
percentage_min_hours_rich = (min_hours_workers['salary'] == '>50K').mean() * 100
print("Percentage of min hours >50K:", percentage_min_hours_rich)

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
countries = df[df['salary'] == '>50K']['native-country'].value_counts()
total_people = df['native-country'].value_counts()
highest_percentage_country = (countries / total_people * 100).idxmax()
highest_percentage = (countries / total_people * 100).max()
print(f"Country with highest percentage of >50K: {highest_percentage_country} ({highest_percentage}%)")

# 9. Identify the most popular occupation for those who earn >50K in India.
india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india_rich = india_rich['occupation'].mode()[0] if not india_rich.empty else 'None'
print("Most popular occupation in India >50K:", most_popular_occupation_india_rich)

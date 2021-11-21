import pathlib
import numpy as np
import pandas as pd

# 1. Check and display the head of the DataFrame
df = pd.read_csv('Python-Basics\Day7\two_pandas_Salaries.csv')

print(df.head())

# 2. Use the .info() method to find out how many entries there are.

print(df.info())

# 3. What is the average of first 10000 items in BasePay ?

print(round(sum(df.iloc[:10000]['BasePay']/10000), 2))

# 4. What is the highest amount of TotalPayBenefits in the dataset ?
df_size = len(df.index)
highest = max(df.iloc[:df_size]['TotalPayBenefits'])

print(highest)

# 5. What is the job title of JOSEPH DRISCOLL ?
person = df.loc[df['EmployeeName']== 'JOSEPH DRISCOLL']

print(person['JobTitle'].iloc[0])

# 6. How much does JOSEPH DRISCOLL make (including benefits)?
print(person['TotalPayBenefits'].iloc[0])

# 7. What is the name of highest paid person (including benefits)?
person = df.loc[df['TotalPayBenefits'] == highest]

print(person['EmployeeName'].iloc[0])

# 8. What is the name of lowest paid person (including benefits)? Do you notice something
# strange about how much he or she is paid?
lowest = min(df.iloc[:df_size]['TotalPayBenefits'])
person = df.loc[df['TotalPayBenefits'] == lowest]

print(person['EmployeeName'].iloc[0])

# 9. What was the average (mean) TotalPay of all employees per year? (2011-2014) ?

print(df.groupby('Year').mean()['TotalPay'])

# 10. How many unique job titles are there?

print(df['JobTitle'].nunique())

# 11. What are the top 7 most common jobs?

print(df['JobTitle'].value_counts(dropna=True)[:6])

# 12. How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with
# only one occurence in 2013?)

print(len([job_title for job_title, count in df['JobTitle'].value_counts(dropna=True).to_dict().items() if count == 1]))

# 13. How many people have the word Chief in their job title? (This is pretty tricky)

print(len([job_title for job_title in df['JobTitle'].value_counts(dropna=True).to_dict().keys() if 'CHIEF' in job_title.upper()]))

# 14. Is there a correlation between length of the Job Title string and Salary?

print(df['JobTitle'].corr(df['BasePay']))

Hands on Lab
Import pandas module.
In [1]:

import pandas as pd
Load the dataset into a dataframe.
In [2]:

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")
Finding duplicates
In this section you will identify duplicate values in the dataset.
Find how many duplicate rows exist in the dataframe.
In [3]:

num_duplicate_rows = df.duplicated().sum()
​
print("Number of duplicate rows:", num_duplicate_rows)
​
Number of duplicate rows: 154
Removing duplicates
Remove the duplicate rows from the dataframe.
In [4]:

df_without_duplicates = df.drop_duplicates()
​
Verify if duplicates were actually dropped.
In [5]:

original_num_rows = df.shape[0]
df_without_duplicates = df.drop_duplicates()
new_num_rows = df_without_duplicates.shape[0]
​
if new_num_rows < original_num_rows:
    print("Duplicates were removed.")
else:
    print("No duplicates were found.")
​
​
Duplicates were removed.
Finding Missing values
Find the missing values for all columns.
In [6]:

missing_values = df.isnull().sum()
​
print("Missing values for each column:")
print(missing_values)
​
Missing values for each column:
Respondent        0
MainBranch        0
Hobbyist          0
OpenSourcer       0
OpenSource       81
               ... 
Sexuality       547
Ethnicity       683
Dependents      144
SurveyLength     19
SurveyEase       14
Length: 85, dtype: int64
Find out how many rows are missing in the column 'WorkLoc'
In [7]:

missing_workloc = df['WorkLoc'].isnull().sum()
​
print("Number of missing values in the 'WorkLoc' column:", missing_workloc)
​
Number of missing values in the 'WorkLoc' column: 32
Imputing missing values
Find the value counts for the column WorkLoc.
In [8]:

workloc_value_counts = df['WorkLoc'].value_counts()
​
print("Value counts for the 'WorkLoc' column:")
print(workloc_value_counts)
​
​
Value counts for the 'WorkLoc' column:
Office                                            6905
Home                                              3638
Other place, such as a coworking space or cafe     977
Name: WorkLoc, dtype: int64
Identify the value that is most frequent (majority) in the WorkLoc column.
In [9]:

workloc_value_counts = df['WorkLoc'].value_counts()
​
most_frequent_workloc = workloc_value_counts.index[0]
​
print("Most frequent value in the 'WorkLoc' column:", most_frequent_workloc)
​
Most frequent value in the 'WorkLoc' column: Office
Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
In [10]:

most_frequent_workloc = workloc_value_counts.index[0]
​
df['WorkLoc'].fillna(most_frequent_workloc, inplace=True)
​
​
After imputation there should ideally not be any empty rows in the WorkLoc column.
Verify if imputing was successful.
In [11]:

remaining_missing_workloc = df['WorkLoc'].isnull().sum()
​
if remaining_missing_workloc == 0:
    print("Imputation was successful. There are no empty rows in the 'WorkLoc' column.")
else:
    print("Imputation was not successful. There are still", remaining_missing_workloc, "empty rows in the 'WorkLoc' column.")
​
​
Imputation was successful. There are no empty rows in the 'WorkLoc' column.
Normalizing data
There are two columns in the dataset that talk about compensation.
One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly, Weekly).
The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq".
This makes it difficult to compare the total compensation of the developers.
In this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.
Once this column is ready, it makes comparison of salaries easy.
List out the various categories in the column 'CompFreq'
In [12]:

comp_freq_categories = df['CompFreq'].unique()
​
print("Categories in the 'CompFreq' column:")
print(comp_freq_categories)
​
​
Categories in the 'CompFreq' column:
['Yearly' 'Monthly' 'Weekly' nan]
Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.
Double click to see the Hint.
In [13]:

# Define a function to normalize compensation values to annual
def normalize_compensation(row):
    if row['CompFreq'] == 'Yearly':
        return row['CompTotal']
    elif row['CompFreq'] == 'Monthly':
        return row['CompTotal'] * 12
    elif row['CompFreq'] == 'Weekly':
        return row['CompTotal'] * 52
    else:
        return None
​
# Apply the function to create the 'NormalizedAnnualCompensation' column
df['NormalizedAnnualCompensation'] = df.apply(normalize_compensation, axis=1)
​
In [14]:

df.head()
Out[14]:
Respondent	MainBranch	Hobbyist	OpenSourcer	OpenSource	Employment	Country	Student	EdLevel	UndergradMajor	...	SONewContent	Age	Gender	Trans	Sexuality	Ethnicity	Dependents	SurveyLength	SurveyEase	NormalizedAnnualCompensation
0	4	I am a developer by profession	No	Never	The quality of OSS and closed source software ...	Employed full-time	United States	No	Bachelor’s degree (BA, BS, B.Eng., etc.)	Computer science, computer engineering, or sof...	...	Tech articles written by other developers;Indu...	22.0	Man	No	Straight / Heterosexual	White or of European descent	No	Appropriate in length	Easy	61000.0
1	9	I am a developer by profession	Yes	Once a month or more often	The quality of OSS and closed source software ...	Employed full-time	New Zealand	No	Some college/university study without earning ...	Computer science, computer engineering, or sof...	...	NaN	23.0	Man	No	Bisexual	White or of European descent	No	Appropriate in length	Neither easy nor difficult	138000.0
2	13	I am a developer by profession	Yes	Less than once a month but more than once per ...	OSS is, on average, of HIGHER quality than pro...	Employed full-time	United States	No	Master’s degree (MA, MS, M.Eng., MBA, etc.)	Computer science, computer engineering, or sof...	...	Tech articles written by other developers;Cour...	28.0	Man	No	Straight / Heterosexual	White or of European descent	Yes	Appropriate in length	Easy	90000.0
3	16	I am a developer by profession	Yes	Never	The quality of OSS and closed source software ...	Employed full-time	United Kingdom	No	Master’s degree (MA, MS, M.Eng., MBA, etc.)	NaN	...	Tech articles written by other developers;Indu...	26.0	Man	No	Straight / Heterosexual	White or of European descent	No	Appropriate in length	Neither easy nor difficult	348000.0
4	17	I am a developer by profession	Yes	Less than once a month but more than once per ...	The quality of OSS and closed source software ...	Employed full-time	Australia	No	Bachelor’s degree (BA, BS, B.Eng., etc.)	Computer science, computer engineering, or sof...	...	Tech articles written by other developers;Indu...	29.0	Man	No	Straight / Heterosexual	Hispanic or Latino/Latina;Multiracial	No	Appropriate in length	Easy	90000.0
5 rows × 86 columns

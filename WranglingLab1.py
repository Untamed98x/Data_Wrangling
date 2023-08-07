Hands on Lab
Import pandas module.
In [15]:

import pandas as pd
Load the dataset into a dataframe.
In [16]:

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")
Finding duplicates
In this section you will identify duplicate values in the dataset.
Find how many duplicate rows exist in the dataframe.
In [17]:

num_duplicate_rows = df.duplicated().sum()
​
print("Number of duplicate rows:", num_duplicate_rows)
​
Number of duplicate rows: 154
Removing duplicates
Remove the duplicate rows from the dataframe.
In [18]:

df_without_duplicates = df.drop_duplicates()
​
Verify if duplicates were actually dropped.
In [19]:

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
In [20]:

# Assuming df is your DataFrame after removing duplicates
yearly_paid_count = df[df['CompFreq'] == 'Yearly'].shape[0]
​
print("Number of respondents being paid yearly:", yearly_paid_count)
​
Number of respondents being paid yearly: 6163
In [24]:

Q1 = df['ConvertedComp'].quantile(0.25)
Q3 = df['ConvertedComp'].quantile(0.75)
IQR = Q3 - Q1
​
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
​
filtered_df = df[(df['ConvertedComp'] >= lower_bound) & (df['ConvertedComp'] <= upper_bound)]
​
median_converted_comp_after_outliers = filtered_df['ConvertedComp'].median()
​
print("Median ConvertedComp after removing outliers:", median_converted_comp_after_outliers)
​
Median ConvertedComp after removing outliers: 52704.0
In [26]:

Q1_age = df['Age'].quantile(0.25)
Q3_age = df['Age'].quantile(0.75)  # Add this line to calculate Q3_age
IQR_age = Q3_age - Q1_age
​
lower_bound_age = Q1_age - 1.5 * IQR_age
​
outliers_below_Q1 = df[df['Age'] < lower_bound_age]
​
num_outliers_below_Q1 = outliers_below_Q1.shape[0]
​
print("Number of outliers below Q1:", num_outliers_below_Q1)
​
​
Number of outliers below Q1: 0
In [27]:

mean_converted_comp_after_outliers = filtered_df['ConvertedComp'].mean()
print("Mean ConvertedComp after removing outliers:", mean_converted_comp_after_outliers)
​
Mean ConvertedComp after removing outliers: 59878.65515139199
In [22]:

median_converted_comp_woman = df[df['Gender'] == 'Woman']['ConvertedComp'].median()
​
print("Median ConvertedComp for respondents who identified as 'Woman':", median_converted_comp_woman)
​
​
Median ConvertedComp for respondents who identified as 'Woman': 57636.0
In [28]:

correlation_matrix = df.corr()
​
# Negative correlation with "Age"
negative_correlation = correlation_matrix['Age'].sort_values().head(1)
​
# Highest correlation with "Age"
highest_correlation = correlation_matrix['Age'].sort_values(ascending=False).head(2).iloc[1:]
​
print("Column with negative correlation with 'Age':", negative_correlation.index[0])
print("Column with the highest correlation with 'Age':", highest_correlation.index[0])
​
Column with negative correlation with 'Age': CodeRevHrs
Column with the highest correlation with 'Age': ConvertedComp
In [23]:

import matplotlib.pyplot as plt
​
# Create a histogram of ages
plt.hist(df['Age'], bins=10, edgecolor='black')
​
# Add labels and title
plt.xlabel('Age')
plt.ylabel('Number of Respondents')
plt.title('Histogram of Respondent Ages')
​
# Show the plot
plt.show()
​

In [29]:

import pandas as pd
import matplotlib.pyplot as plt
​
​
​
In [30]:

# Replace 'Age' and 'WorkWeekHrs' with your actual column names
plt.scatter(df['Age'], df['WorkWeekHrs'])
​
# Add labels and title
plt.xlabel('Age')
plt.ylabel('WorkWeekHrs')
plt.title('Scatter Plot of Age vs. WorkWeekHrs')
​
# Show the plot
plt.show()
​

In [31]:

correlation = df['Age'].corr(df['WorkWeekHrs'])
print("Correlation between Age and WorkWeekHrs:", correlation)
​
Correlation between Age and WorkWeekHrs: 0.03688694959626343
In [32]:

import seaborn as sns
sns.regplot(x='Age', y='WorkWeekHrs', data=df)
​
Out[32]:
<AxesSubplot:xlabel='Age', ylabel='WorkWeekHrs'>

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

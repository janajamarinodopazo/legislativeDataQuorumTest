# legislativeDataQuorumTest

1. For every legislator in the dataset, how many bills did the legislator support(voted for the bill)? How many bills did the legislator oppose?
2. For every bill in the data set, how many legislators supported the bill? How many legislators opposed the bill? Who was the primary sponsor of the bill?


# Answers
1. Time Complexity: The strategy involves merging the CSV files to create a comprehensive DataFrame, which can have a time complexity of O(n*m), where n is the number of rows in the largest CSV file and m is the number of CSV files. The subsequent operations, such as grouping and aggregating, have a time complexity of O(n), where n is the number of rows in the DataFrame.

2. Effort Cost: The implementation uses pandas for data manipulation, which simplifies the code and reduces development effort. However, ensuring the correctness and efficiency of the data processing steps requires careful planning and testing.
 - Technologies Used:  Python was used along with pandas for data processing and manipulation and IPython.display was used for displaying the results.

 - Considering scalability and maintainability, the code is structured in a modular way, separating data loading, processing, and result display into distinct steps. This allows for easier future modifications or additions. 
I'd prefer separate this in distinct paths but as I strugled issues to run python in my machine in a first momet, I choose do not spend mor time at this momeent.

2. Future Columns:
   - To account for future columns such as "Bill Voted On Date" or "Co-Sponsors," the CSV files would need to be updated to include these columns. 
   - In the code, additional merges and operations would be required to incorporate these new columns into the analysis. For example, to include "Bill Voted On Date," a merge operation could be performed with a DataFrame containing the date information.

3. List of Legislators or Bills
   - If given a list of legislators or bills to generate a CSV for, the code would need to be modified to create a DataFrame from the list and then write this DataFrame to a CSV file. 
   - This could be achieved by creating a DataFrame from the list, defining column names based on the expected CSV format, and then using the `to_csv` method to write the DataFrame to a CSV file.

4. Time Spent: About 5 hours to actually code and research into pandas domumentation. However, I can't spet all this time all at once and I faced issues to run python on my machine and decide use codeSpace from github tho



# Requirements
The following software is required to run this application:
```bash 
Python 3.10.13
```

Installation
Clone the repository from GitHub:
```bash
git clone 
```
Install pandas

```
pip install pandas
```


# Run
Into the project path, run:

```bash 
python main.py
```


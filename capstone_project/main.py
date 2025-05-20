import pandas as pd
import os
import matplotlib.pyplot as plt

# Input Excel file
input_file = r'D:\business_analytics\capstone_project\datasheets.xlsx'

# Get the folder where the Excel file is located
output_folder = os.path.dirname(input_file)

# Load the Excel file
xls = pd.ExcelFile(input_file)

# Process each sheet
for sheet_name in xls.sheet_names:
    # Read the sheet
    df = xls.parse(sheet_name)

    # Clean the data
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    df.columns = df.columns.str.strip()
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.fillna(0, inplace=True)

    # Save the cleaned data to CSV
    output_file = os.path.join(output_folder, f"{sheet_name}.csv")
    df.to_csv(output_file, index=False)

    # Plot a line chart for "Sheet1"
    if sheet_name.lower() == 'sheet1':
        numeric_df = df.select_dtypes(include='number')

        if not numeric_df.empty:
            plt.figure(figsize=(10, 6))
            numeric_df.plot(kind='line', title=f'Line Plot - {sheet_name}')
            plt.xlabel("Index")
            plt.ylabel("Values")
            plt.grid(True)
            plt.tight_layout()

            # Show the plot in Spyder's plot pane
            plt.show()
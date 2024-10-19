import pandas as pd


# Step 1: Load the data
df = pd.read_csv(r'e:\New folder\DOTPY\final project\pizza_sales...csv') 

# Step 2: Display the first few rows of the data
print(df.head())

# Step 3: Data Cleaning
# Check for null values
print(df.isnull().sum())
# Fill or drop missing values as needed
df.dropna(inplace=True)  
print(df.columns)  # Print column names for reference
df.columns = df.columns.str.strip()  # Strip whitespace if any

# Step 4: Convert data types
df['total_price'] = df['total_price'].astype(float)  # Ensure total_price is of type float

# Check for required columns before summarizing
if 'pizza_name' in df.columns and 'total_price' in df.columns:
    # Summarize total sales
    total_sales = df.groupby('pizza_name')['total_price'].sum().reset_index()
    print(total_sales)  # Print total_sales to check if it has been defined
else:
    print("Columns 'pizza_name' or 'total_price' are not found in the DataFrame.")

# Step 5: Save cleaned data if total_sales exists
if 'total_sales' in locals():  # Check if total_sales is defined
    df.to_csv(r'e:\New folder\DOTPY\final project\cleaned_pizza_sales.csv', index=False)  # Save the cleaned data
    print("Cleaned data saved to 'cleaned_pizza_sales.csv'.")
else:
    print("Total sales were not calculated. Data not saved.")
    # Save cleaned data to a specified location

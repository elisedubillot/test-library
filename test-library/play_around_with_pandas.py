import pandas as pd

def test_pandas_operations(df):
    print("Original DataFrame:")
    print(df)
    
    # Fill NaN values with specific strategies
    df_filled = df.fillna({"integers": 0, "floats": df["floats"].mean(), "strings": "missing"})
    print("\nAfter Filling NaN values:")
    print(df_filled)

    # Drop rows and columns with NaN
    df_dropped = df.dropna()
    print("\nAfter Dropping Rows with NaN:")
    print(df_dropped)
    
    # Sort values
    df_sorted = df.sort_values(by="floats", ascending=False)
    print("\nAfter Sorting by 'floats':")
    print(df_sorted)

    # Add new columns based on operations
    df["float_squared"] = df["floats"] ** 2
    df["is_integer"] = df["integers"].apply(lambda x: isinstance(x, int))
    print("\nAfter Adding New Columns:")
    print(df)

    # Group by and aggregation
    grouped = df.groupby("categories").agg({"integers": "sum", "floats": "mean"})
    print("\nGroup By 'categories' with Aggregation:")
    print(grouped)

    # Filtering
    filtered = df[df["floats"] > 2]
    print("\nFiltered Rows Where 'floats' > 2:")
    print(filtered)

    # Reshaping: Pivot table
    pivot = df.pivot_table(values="floats", index="categories", columns="booleans", aggfunc="mean")
    print("\nPivot Table with 'categories' and 'booleans':")
    print(pivot)

    # Handling datetime
    df["day_of_week"] = df["dates"].dt.day_name()
    print("\nAfter Extracting Day of the Week from 'dates':")
    print(df)

    # String operations
    df["strings_upper"] = df["strings"].str.upper()
    print("\nAfter Converting 'strings' to Uppercase:")
    print(df)

    # Boolean operations
    df["is_true"] = df["booleans"].fillna(False) & (df["floats"] > 3)
    print("\nAfter Boolean Operations on 'booleans' and 'floats':")
    print(df)

    # Merging DataFrames
    merge_df = pd.DataFrame({
        "categories": ["A", "B", "C"],
        "description": ["Alpha", "Beta", "Gamma"]
    })
    merged = pd.merge(df, merge_df, on="categories", how="left")
    print("\nAfter Merging with Additional DataFrame:")
    print(merged)

    # Resampling (requires datetime index)
    df.set_index("dates", inplace=True)
    resampled = df["floats"].resample("D").mean().fillna(0)
    print("\nResampled Data (Daily Mean of 'floats'):")
    print(resampled)

    return df

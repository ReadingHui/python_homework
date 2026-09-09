import sqlite3
import pandas as pd

def main():
    # Task 5: Read Data into a DataFrame
    # Connect to the database
    try:
        with sqlite3.connect("../db/lesson.db") as conn:
            cursor = conn.cursor()

    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")

    q = """
        SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price FROM line_items as li
        JOIN products as p
        ON li.product_id = p.product_id
        """
    
    try:
        df = pd.read_sql(q, conn)
    except sqlite3.Error as e:
        print(f'SQL Error {e}')
    
    # Print first 5 lines
    print('DataFrame after loading from database')
    print(df.head())
    print()

    # Add the 'total' column
    df['total'] = df['quantity'] * df['price']
    print('DataFrame after adding the "total" column')
    print(df.head())
    print()

    # Add groupby code by 'product_id'
    order_summary = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'})
    print('Groupby product_id df')
    print(order_summary.head())
    print()

    # Sort df by `product_name`
    order_summary = order_summary.sort_values('product_name')

    # Save as csv file
    order_summary.to_csv('order_summary.csv')
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
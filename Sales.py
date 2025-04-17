import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def sales_trend_analysis(db_path):
    # establish connection and cursor within function scope
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()

    query = ("""
    SELECT 
        strftime('%Y-%m', sale_date) AS month, 
        SUM(sale_amount) AS total_sales
    FROM 
        sales
    GROUP BY 
        month
    ORDER BY 
        month;
    """)

    try: 
        cursor.execute(query)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['month', 'total_sales'])
        # using correct column names: 'month', 'total_sales'
        df['month'] = pd.to_datetime(df['month'], format='%Y-%m')  
        

        plt.figure(figsize=(10, 6))
        # using correct column names: 'month', 'total_sales'
        plt.plot(df['month'], df['total_sales'], marker='o', linestyle='-', color='b') 
        plt.title('Sales Trend Analysis')
        plt.xlabel('Month')
        plt.ylabel('Total Sales (Rs)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

db_path = 'sales.db'
sales_trend_analysis(db_path)

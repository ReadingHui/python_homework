import sqlite3

LESSON_DB = '../db/lesson.db'

def main():
    with sqlite3.connect(LESSON_DB) as conn:
        conn.execute("PRAGMA foreign_keys = 1;")
        cursor = conn.cursor()

        # Task 1: Complex JOINs with Aggregation
        query = """
        SELECT o.order_id, SUM(li.quantity * p.price) AS total_price FROM orders AS o
        LEFT JOIN line_items as li
        ON o.order_id = li.order_id
        LEFT JOIN products AS p
        ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """

        cursor.execute(query)
        print('Total price of each of the first 5 orders:')
        for row in cursor.fetchall():
            print(row)
        print()

        # Task 2: Understanding Subqueries
        query = """
        WITH cte AS (SELECT li.order_id, li.quantity * p.price AS total_price FROM line_items AS li
        LEFT JOIN products AS p
        ON li.product_id = p.product_id
        GROUP BY li.order_id)

        SELECT c.customer_name, AVG(cte.total_price) AS average_total_price FROM orders AS o
        LEFT JOIN cte
        ON o.order_id = cte.order_id
        LEFT JOIN customers AS c
        ON o.customer_id = c.customer_id
        GROUP BY o.customer_id;
        """

        cursor.execute(query)
        print("Average price of customers' orders:")
        for row in cursor.fetchall():
            print(row)
        print()

        # Task 3: An Insert Transaction Based on Data
        # Getting the customer_id, employee_id and products
        queries = {
            'customer_id': """
            SELECT customer_id FROM customers
            WHERE customer_name = "Perez and Sons";
            """,
            'employee_id': """
            SELECT employee_id FROM employees
            WHERE first_name = "Miranda"
            AND last_name = "Harris";
            """,
            'products': """
            SELECT product_id FROM products
            ORDER BY price ASC
            LIMIT 5;
            """
        }

        results = {}
        for k, q in queries.items():
            results[k] = [r[0] for r in cursor.execute(q).fetchall()]

        # Check length of orders, it was 249 before inserting
        if cursor.execute("SELECT COUNT(1) FROM orders").fetchall()[0][0] <= 249:
            # Insert to orders
            orders_q = """
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?, ?)
            RETURNING order_id;
            """
            cursor.execute(orders_q, (results['customer_id'][0], results['employee_id'][0]))
            order_id = cursor.fetchone()[0] # Get order_id

        # Check length of line_items, it was 1109 before inserting
        if cursor.execute("SELECT COUNT(1) FROM line_items").fetchall()[0][0] <= 1109:
            # Insert to line_items
            li_q = """
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
            """
            entries = [(order_id, product_id, 10) for product_id in results['products']]
            cursor.executemany(li_q, entries)
        
        conn.commit()
        
        # Last line_item_id entry before inserting was 1109
        check_q = """
        SELECT li.line_item_id, li.quantity, p.product_name FROM line_items AS li
        LEFT JOIN products AS p
        ON li.product_id = p.product_id
        WHERE li.line_item_id > 1109;
        """
        check_res = cursor.execute(check_q).fetchall()
        print('Added line_items:')
        for row in check_res:
            print(row)
        print()

        # Clean up the inserted lines
        cursor.execute("DELETE FROM line_items WHERE line_item_id > 1109")
        cursor.execute("DELETE FROM orders WHERE order_id > 249")        
        
        # Task 4: Aggregation with HAVING
        agg_q = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_counts FROM employees AS e
        LEFT JOIN orders AS o
        ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        """
        agg_res = cursor.execute(agg_q).fetchall()
        print('Employees with more than 5 orders:')
        for row in agg_res:
            print(row)
        print()


    conn.close()    


if __name__ == "__main__":
    main()
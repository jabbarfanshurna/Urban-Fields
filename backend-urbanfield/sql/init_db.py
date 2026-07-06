import pymysql
import os

def run_sql_file(cursor, filepath):
    print(f"Executing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # Split queries by semicolon, ignoring those inside comments or strings (simple split is usually enough for these scripts)
    # But since we have multiline statements and scrypt password hashes with '$', let's be careful.
    # Split on ';' that is followed by whitespace/newline
    queries = sql_content.split(';')
    for query in queries:
        clean_query = query.strip()
        if not clean_query:
            continue
        # Skip SQL comments if any
        if clean_query.startswith('--') or clean_query.startswith('#'):
            # Some queries might start with comment but have actual query after newline
            lines = clean_query.split('\n')
            lines = [line for line in lines if not (line.strip().startswith('--') or line.strip().startswith('#'))]
            clean_query = '\n'.join(lines).strip()
            if not clean_query:
                continue
        
        try:
            cursor.execute(clean_query)
        except Exception as e:
            print(f"Error executing query: {clean_query[:100]}...\nError: {e}")
            raise e

def main():
    # Connect to MySQL
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            autocommit=True
        )
        cursor = conn.cursor()
        print("Connected to MySQL successfully.")
        
        # Run CreateDBQuery.sql
        create_db_path = os.path.join(os.path.dirname(__file__), 'CreateDBQuery.sql')
        run_sql_file(cursor, create_db_path)
        
        # Run InsertDummyData.sql
        insert_dummy_path = os.path.join(os.path.dirname(__file__), 'InsertDummyData.sql')
        run_sql_file(cursor, insert_dummy_path)
        
        print("Database initialized and populated successfully!")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to initialize database: {e}")

if __name__ == '__main__':
    main()

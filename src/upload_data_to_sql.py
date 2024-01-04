import os
import wx
import pandas as pd
from sqlalchemy import text
from src.config_loader import load_database_config


def upload_data_to_sql(selected_files):
    """
    Uploads data from CSV files to a MySQL database.

    Args:
        selected_files (list): List of file names to be imported.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the data import process.

    The function reads CSV files from the 'csv' folder, creates or
    updates corresponding MySQL tables, and uploads the data using
    SQLAlchemy. The table names are derived from the file names with
    spaces replaced by underscores and converted to lowercase.

    Example:
        upload_data_to_sql(['Alapfok A1_1', 'Felsőfok C1_1'])
    """

    input_folder = "csv"
    try:
        for file in selected_files:
            file_path = os.path.join(input_folder, f"{file}.csv")
            df = pd.read_csv(file_path)

            # Database table name
            table_name = os.path.splitext(os.path.basename(file))[0]

            # Renaming tables ( Alapfok A1_1 => alapfok_a1_1 )
            table_rename = table_name.replace(" ", "_").lower()

            # Database configuration
            engine = load_database_config()
            # Change table structure so that column 'id' is AUTO_INCREMENT
            with engine.connect() as conn:
                conn.execute(text(f'''
                    CREATE TABLE IF NOT EXISTS {table_rename} (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        hun_text VARCHAR(255),
                        eng_text VARCHAR(255)
                    )
                '''))
            # Upload DataFrame data to a MySQL table using pymysql and SQLAlchemy
            df.to_sql(name=table_rename, con=engine,
                      if_exists='append', index=False)

        # It writes which file we imported
        files = "\n- ".join(selected_files)
        wx.MessageBox(f'The selected files have been imported.\n- {files}',
                      "Success", wx.OK | wx.ICON_INFORMATION)

    except Exception as e:
        wx.MessageBox(f"An error occurred while importing data: {str(e)}",
                      "Error", wx.OK | wx.ICON_ERROR)

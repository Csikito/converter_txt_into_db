# 🖹 .txt file conversion in the database 🖹

1. **Convert to CSV:**

   - Select specific text files from the 'data' folder to convert.
   - The application reads the selected text files and extracts relevant information from them.
   - It generates corresponding CSV files with the extracted data in the 'csv' folder.
   - The CSV files are formatted for easy integration with other applications and databases.

2. **Upload to SQL:**
   - After converting the text files to CSV, the application enables the user to upload the generated CSV files to a MySQL database.
   - The user is prompted to select the specific CSV files for upload.
   - The application creates or updates MySQL tables based on the selected CSV files.
   - Data from the CSV files is then inserted into the corresponding MySQL tables, making it accessible for various database operations.

## Requirements

- Python 3.9 or later
- wxPython 4.2.1a or later
- pandas 2.1.4
- SQLAlchemy 2.0.25

## Setup

1.  Install required Python packages:

    `$ pip install -r requirements.txt `

2.  Configure the database connection by editing the config.ini file:
    <?>

        [Database]

        host=localhost
        user=username
        password=user_password
        database=database_name

3.  Run the application:

    `$ python main.py `

## Usage

1. Launch the application.
2. The GUI window will appear, displaying a list of available text files in the 'data' folder.
3. Select the files you want to convert and upload by checking the corresponding checkboxes.
4. Click the "Import" button to initiate the conversion and upload process.
5. A success message will be displayed, and the uploaded CSV files.

## Notes

- The application uses wxPython for the graphical user interface and SQLAlchemy/Python for database connectivity.

- The first column displays checkboxes for table selection, and the second column shows the file names.

- The CSV files are imported into the database after conversion.

# 🖹 .txt file conversion in the database 🖹

The tasks are divided into two steps. Firstly, the software extracts relevant information from text files selected from the 'data' folder and converts them into CSV files, saving them in the 'csv' folder. Subsequently, the program allows the user to upload the generated CSV files to a MySQL database. The user selects specific CSV files for upload, and the software creates or updates MySQL tables based on the chosen CSV files. Data from the CSV files is then inserted into the corresponding MySQL tables, making it accessible for various database operations. Finally, it deletes the csv folder.

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

## Used data

The data used was taken from the following youtube channel:

▶️ https://www.youtube.com/@365angol ▶️

## GIF of how the software works

![softwer](https://github.com/Csikito/converter_txt_into_db/assets/84712542/912b29f3-05e4-4e31-9c9f-8dd4b9ad6547)

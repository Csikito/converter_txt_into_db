import os
import csv


def convert_to_csv(selected_files):
    """
    Converts text files to CSV format.

    Args:
        selected_files (list): List of file names to be processed.

    Returns:
        None

    Raises:
        FileNotFoundError: If a specified input file is not found.

    The function reads text files from the 'data' folder, extracts
    specific lines, and creates a CSV file in the 'csv' folder with
    Hungarian and English text.

    Example:
        convert_to_csv(['Alapfok A1_1', 'Felsőfok C1_1'])
    """

    def rows_filter(input_file_path):
        """
        Extracts specific lines from a text file.

        Args:
            input_file_path (str): Path of the input text file.

        Returns:
            None

        The function reads lines from the text file, selects
        alternating lines as Hungarian and English text, and stores
        them in the first_line and third_line lists.

        Example:
            rows_filter('Alapfok A1_1')
        """

        input_folder = "data"
        try:
            txt_filename = os.path.join(input_folder, f"{input_file_path}.txt")
            with open(txt_filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                all_rows = len(lines)

                # Select rows
                hu_text = 0
                en_text = 2

                # Select all the rows you need
                while hu_text < all_rows:
                    first_line.append(lines[hu_text].strip())
                    hu_text += 10

                while en_text < all_rows:
                    third_line.append(lines[en_text].strip())
                    en_text += 10

        except FileNotFoundError:
            print(f"File not found: {input_file_path}")
            return

    # Create a CSV file
    def create_csv(output_csv_file_path):
        """
        Creates a CSV file from extracted lines.

        Args:
            output_csv_file_path (str): Path of the output CSV file.

        Returns:
            None

        The function creates a CSV file in the 'csv' folder and writes
        Hungarian and English text from first_line and third_line lists.

        Example:
            create_csv('Alapfok A1_1')
        """

        # Separate folder for CSV files
        output_folder = "csv"
        os.makedirs(output_folder, exist_ok=True)

        try:
            csv_filename = os.path.join(
                output_folder, f"{output_csv_file_path}.csv"
                )
            with open(csv_filename, 'w', newline='',
                      encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['hun_text', 'eng_text'])
                for first, third in zip(first_line, third_line):
                    csv_writer.writerow([first, third])
            # print(f"A CSV fájl létrehozva: {output_csv_file_path}")
        except Exception as e:
            print(f"An error occurred while creating the CSV file: {str(e)}")

    # File path , rows_filter , create_csv
    for file in selected_files:
        input_file_path = file
        output_csv_file_path = file
        first_line = []
        third_line = []
        rows_filter(input_file_path)
        create_csv(output_csv_file_path)

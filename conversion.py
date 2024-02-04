import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from tkinter import Tk, filedialog

def ask_input_file():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select Input File",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )

    return file_path

def convert_file(input_file, output_format):
    if not input_file:
        print("No input file selected. Exiting.")
        return

    if output_format not in ['csv', 'parquet', 'arrow', 'json', 'tsv', 'excel']:
        print("Invalid output format. Supported formats: csv, parquet, arrow, json, tsv, excel")
        return

    # Assume Downloads folder for output
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Create output file path in Downloads folder
    output_file = os.path.join(downloads_folder, f"output_file.{output_format}")

    if output_format == 'csv':
        df = pd.read_csv(input_file)
        df.to_csv(output_file, index=False)
    elif output_format == 'parquet':
        df = pd.read_csv(input_file)
        df.to_parquet(output_file)
    elif output_format == 'arrow':
        df = pd.read_csv(input_file)
        table = pa.Table.from_pandas(df)
        pa.parquet.write_table(table, output_file)
    elif output_format == 'json':
        df = pd.read_csv(input_file)
        df.to_json(output_file, orient='records', lines=True)
    elif output_format == 'tsv':
        df = pd.read_csv(input_file, sep='\t')
        df.to_csv(output_file, sep='\t', index=False)
    elif output_format == 'excel':
        df = pd.read_csv(input_file)
        df.to_excel(output_file, index=False, engine='openpyxl')

    return output_file

if __name__ == "__main__":
    input_file = ask_input_file()
    output_format = input("Enter the desired output format (csv, parquet, arrow, json, tsv, excel): ")

    output_file = convert_file(input_file, output_format)
    if output_file:
        print(f"Conversion complete. Output file saved at {output_file}")

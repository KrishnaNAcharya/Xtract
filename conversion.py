import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from tkinter import Tk, filedialog
from pandas.plotting import table

def ask_input_file():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select Input File",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xls;*.xlsx"),
            ("Parquet Files", "*.parquet"),
            ("Arrow Files", "*.arrow"),
            ("JSON Files", "*.json"),
            ("TSV Files", "*.tsv"),
            ("All Files", "*.*")
        ]
    )

    return file_path

def convert_file(input_file, output_format):
    if not input_file:
        print("No input file selected. Exiting.")
        return

    if output_format not in ['csv', 'parquet', 'arrow', 'json', 'tsv', 'excel', 'pdf', 'html', 'xlsx']:
        print("Invalid output format. Supported formats: csv, parquet, arrow, json, tsv, excel, pdf, html, xlsx")
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
    elif output_format == 'pdf':
        # Save DataFrame as PDF
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        tbl = table(ax, df, loc='center', colWidths=[0.2]*len(df.columns))
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(10)
        tbl.auto_set_column_width(col=list(range(len(df.columns))))
        tbl.auto_set_column_width(col=list(range(len(df.columns))))
        plt.savefig(output_file, format='pdf', bbox_inches='tight')
        plt.close(fig)
    elif output_format == 'html':
        # Save DataFrame as HTML
        df.to_html(output_file, index=False)
    elif output_format == 'xlsx':
        # Save DataFrame as XLSX
        df.to_excel(output_file, index=False, engine='openpyxl')

    return output_file

if __name__ == "__main__":
    input_file = ask_input_file()
    output_format = input("Enter the desired output format (csv, parquet, arrow, json, tsv, excel, pdf, html, xlsx): ")

    output_file = convert_file(input_file, output_format)
    if output_file:
        print(f"Conversion complete. Output file saved at {output_file}")

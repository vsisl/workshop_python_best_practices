"""Showcasing how to read a table in a fixed width format from a text file to pandas.

source: https://towardsdatascience.com/parsing-fixed-width-text-files-with-pandas-f1db8f737276

"""
import pathlib
import pandas as pd


def main():
    # path to text file containing a table in a fixed-width format
    path_table = pathlib.Path('pandas_example/fixed_width_format_table.txt')

    # this defines the widths of individual columns of the table
    #  see https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html
    colspecs = [(0, 14), (14, 30), (30, 41), (41, 53), (53, 60), (60, -1)]

    df = pd.read_fwf(
        path_table, skiprows=36, skipfooter=5, colspecs=colspecs,
        names=['gene_name', 'chromosomal_position', 'uniprot', 'entry_name', 'mtm_code', 'description'])

    print(df.info())

    return df


if __name__ == '__main__':
    main()

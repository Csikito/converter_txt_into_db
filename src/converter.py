import os
import shutil
import wx
import wx.grid as grid
from src.convert_to_csv import convert_to_csv
from src.upload_data_to_sql import upload_data_to_sql


class Converter(wx.Frame):

    """
    GUI application for converting and uploading data from text files to a MySQL database.

    Attributes:
        list (list): List of all available text files in the 'data' folder.
        selected_files (list): List of selected text files to be processed.

    Methods:
        __init__(self, parent, title): Constructor method to initialize the Converter object.
        on_cell_click(self, event): Event handler for a left-click on a cell in the wxPython Grid.
        convert_and_upload(self, event): Method to convert selected files to CSV and upload data to a MySQL database.

    Example:
        app = wx.App(False)
        frame = Converter(None, "Data Converter")
        frame.Show()
        app.MainLoop()
    """
    def __init__(self, parent, title):
        """
        Constructor method to initialize the Converter object.

        Parameters:
            parent: Parent window or frame.
            title (str): Title of the frame.

        Returns:
            None
        """
        super(Converter, self).__init__(parent, title=title, size=(500, 300))

        # Defining Panel and BoxSizer
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.list = []  # All files (".txt")
        self.selected_files = []  # New list to store selected files

        # Add files to the list
        folder_path = 'data'
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                self.list.append(filename.split(".")[0])

        # Create a table
        self.grid = wx.grid.Grid(panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.grid.CreateGrid(len(self.list), 2)
        self.grid.SetColLabelValue(0, "✔")
        self.grid.SetColLabelValue(1, "Name\n( .txt )")

        # Add Checkboxes and Table Names
        self.grid.SetColFormatBool(0)
        for index, table in enumerate(self.list):
            self.grid.SetCellValue(index, 1, table)
            self.grid.SetCellAlignment(
                index, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE,
            )
            self.grid.SetCellAlignment(
                index, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE,
            )

        # Removing serial numbers
        self.grid.SetRowLabelSize(0)

        # Setting the width of the first column
        self.grid.SetColSize(0, 30)

        # Set text size
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.grid.SetDefaultCellFont(font)

        # Automatically adjust cell size to text size
        self.grid.AutoSize()

        # Select a cell with one click
        self.grid.Bind(grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_click)

        # Display table
        vbox.Add(
            self.grid, proportion=1, flag=wx.EXPAND | wx.ALL, border=5
        )
        panel.SetSizer(vbox)

        # Save btn
        save_button = wx.Button(panel, label="Import")
        save_button.Bind(wx.EVT_BUTTON, self.convert_and_upload)
        vbox.Add(save_button, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM,
                    border=10)
        panel.SetSizer(vbox)

    def on_cell_click(self, event):
        """
        Event handler for a left-click on a cell in the wxPython Grid.

        Parameters:
        - event: The wxPython event object.
        """
        row = event.GetRow()
        col = event.GetCol()

        self.grid.EnableCellEditControl()
        self.grid.SetGridCursor(row, col)
        event.Skip()

    def convert_and_upload(self, event):
        """
        Method to convert selected files to CSV and upload data to a MySQL database.

        Parameters:
            event: The wxPython event object.

        Returns:
            None
        """

        self.selected_files = [self.grid.GetCellValue(item, 1) for item in range(self.grid.GetNumberRows()) if self.grid.GetCellValue(item, 0)]
        if not self.selected_files:
            wx.MessageBox("Select at least one file!", "Missing data", wx.OK | wx.ICON_ERROR)
            return
        convert_to_csv(self.selected_files)
        upload_data_to_sql(self.selected_files)

        # Delete folder after uploading .csv to db
        shutil.rmtree("csv")

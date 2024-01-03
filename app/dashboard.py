import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.scrolled import ScrolledText

from tkinter import filedialog as fd

from pdf_toolbox import PdfToolbox
from get_combo_dialog import GetComboDialog

import random
from pdf2image import convert_from_path
from PIL import Image, ImageTk
from icecream import ic
import os
import os.path
from os import path

class DashBoard(ttk.Frame):
    def __init__(self):
        self.test = 'test dashboard'
        ic(self.test)
        # def __init__(self, master_window):
        #     super().__init__(master_window, padding=(0, 0))

        self.nj_dashboard_create()


    def nj_dashboard_create(self):
        self.nj_dash_0 = ttk.Frame(
            self.app_mgr_container,
            width=500,
            height=500,
            # style=SUCCESS
        )
        self.nj_dash_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        # def __init__(self, master_window):
        #     super().__init__(master_window, padding=(0, 0))






# class DashBoard(tk.Tk):
#     def __init__(self):
#         def __init__(self, master_window):
#             super().__init__(master_window, padding=(0, 0))
#
#     def nj_dashboard_create(self):
#         self.nj_dash_0 = ttk.Frame(
#             self.app_mgr_container,
#             width=500,
#             height=500,
#             # style=SUCCESS
#         )
#         self.nj_dash_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')
#
#         self.nj_dashboard_header()
#         self.nj_dashboard_top_bar()
#         self.nj_dashboard_main()
#         self.nj_dashboard_bottom_bar()
#
#     def nj_dashboard_header(self):
#         self.nj_dashboard_header = ttk.Frame(
#             master=self.nj_dash_0,
#             width=200,
#             height=500,
#             # style=PRIMARY,
#         )
#         self.nj_dashboard_header.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')
#
#         self.nj_dashboard_header_lbl = ttk.Label(
#             master=self.nj_dashboard_header,
#             text='DashBoard',
#             font='helvetica 20 bold',
#             style=LIGHT,
#         )
#         self.nj_dashboard_header_lbl.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')
#
#     def nj_dashboard_top_bar(self):
#         self.pn_top_bar = ttk.Frame(
#             master=self.nj_dash_0,
#             # width=500,
#             # height=10,
#             # style=DARK,
#         )
#         self.pn_top_bar.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='n')
#
#         self.pn_top_bar.rowconfigure(0, weight=2)
#
#         self.pn_top_bar.columnconfigure(0, weight=1)
#         self.pn_top_bar.columnconfigure(1, weight=1)
#         self.pn_top_bar.columnconfigure(2, weight=1)
#         self.pn_top_bar.columnconfigure(3, weight=1)
#         self.pn_top_bar.columnconfigure(4, weight=1)
#
#         self.dashboard_operations = ttk.Frame(
#             master=self.pn_top_bar,
#             # style=DARK
#         )
#         self.dashboard_operations.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')
#
#         button_0 = ttk.Button(
#             master=self.dashboard_operations,
#             text='Load PDF File - TST',
#             style=PRIMARY,
#             cursor='hand2',
#             command=lambda: self.load_pdf_file(),
#         )
#         button_0.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')
#
#         button_1 = ttk.Button(
#             master=self.dashboard_operations,
#             text='Generate PDF Pages',
#             style=PRIMARY,
#             cursor='hand2',
#             command=lambda: self.gen_pdf_pages_from_all_infiles(),
#         )
#         button_1.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')
#
#         button_2 = ttk.Button(
#             master=self.dashboard_operations,
#             text='Generate Combo Infiles',
#             style=PRIMARY,
#             cursor='hand2',
#             command=lambda: self.build_combo_all(),
#         )
#         button_2.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky='')
#
#         button_3 = ttk.Button(
#             master=self.dashboard_operations,
#             text='Generate Combo Pages',
#             style=PRIMARY,
#             cursor='hand2',
#             command=lambda: self.gen_combo_pages_from_combo_pages(),
#         )
#         button_3.grid(row=1, column=3, padx=(5, 5), pady=(5, 5), sticky='')
#
#         button_4 = ttk.Button(
#             master=self.dashboard_operations,
#             text='Generate Combo Images',
#             style=PRIMARY,
#             cursor='hand2',
#             command=lambda: self.generate_combo_pages_images(),
#         )
#         button_4.grid(row=1, column=4, padx=(5, 5), pady=(5, 5), sticky='')
#
#         button_5 = ttk.Button(
#             master=self.dashboard_operations,
#             text='Full Wash Cycle',
#             style=DANGER,
#             cursor='hand2',
#             command=lambda: self.full_wash_cycle(),
#         )
#         button_5.grid(row=1, column=5, padx=(5, 5), pady=(5, 5), sticky='')

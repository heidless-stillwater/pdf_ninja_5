import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.scrolled import ScrolledText

from tkinter import filedialog as fd

from dashboard import DashBoard
from pdf_toolbox import PdfToolbox
from get_combo_dialog import GetComboDialog

import random
from pdf2image import convert_from_path
from PIL import Image, ImageTk
from icecream import ic
import os
import os.path
from os import path

# pathlib
# setuptools

from constants import *

class PdfNinja(ttk.Frame):
    root_dir = os.getcwd()
    # ic(root_dir)
    def __init__(self, master_window):
        super().__init__(master_window, padding=(0, 0))
        # self.pack(fill=BOTH, expand=YES)

        self.pdf_t = PdfToolbox()

        self.current_combo_name = ''

        # reveal app window
        self.grid(row=0, column=0)

        self.name = ttk.StringVar(value='')
        self.student_id = ttk.StringVar(value='')
        self.course_name = ttk.StringVar(value='')
        self.final_score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = master_window.style.colors

        self.app_mgr_container = ttk.Frame(
            master_window,
            width=500,
            height=500,
            # style=WARNING,
        )
        self.app_mgr_container.grid(row=0, column=0, rowspan=1, padx=(20, 20), pady=(20, 20), sticky='nsew')

        self.app_mgr_container.rowconfigure(0, weight=1)
        self.app_mgr_container.columnconfigure(0, weight=1)
        self.app_mgr_container.columnconfigure(1, weight=1)

        self.app_mgr_create()

        #############################
        # dashboard test
        #############################
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(self.app_mgr_container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        #
        # self.nj_dashboard_create()
        #
        # # self.nj_support_create()
        #
        # # table
        # # colors =

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def app_mgr_create(self):
        # ic('in app mgr create')
        self.app_mgr_sidebar = ttk.Frame(
            master=self.app_mgr_container,
            width=500,
            height=500,
            # style=INFO,
        )
        self.app_mgr_sidebar.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='ne')

        self.app_mgr_sidebar.columnconfigure(0, weight=1)
        self.app_mgr_sidebar.rowconfigure(0, weight=1)
        self.app_mgr_sidebar.rowconfigure(1, weight=1)
        #
        self.app_mgr_create_branding()
        self.app_mgr_create_controls()

    def app_mgr_create_branding(self):
        self.branding_container = ttk.Frame(
            master=self.app_mgr_sidebar,
            width=300,
            height=300,
            # style=SUCCESS,
        )
        self.branding_container.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        self.app_mgr_logo()

    def app_mgr_logo(self):
        # logo
        # sz_h = int(sz_w * 1.41)

        sz_w = 150
        sz_h = sz_w
        # sz_h = int(sz_w * 1.41)
        id('load image...)')
        # ic(PDF_NINJA_LOGO)

        icon_img = Image.open(PDF_NINJA_LOGO).resize((sz_w, sz_h))
        logo_img = ImageTk.PhotoImage(icon_img)

        # logo_img = ImageTk.PhotoImage(master=self, file=PDF_NINJA_LOGO)
        # ic(logo_img)

        self.logo_widget = ttk.Label(
          master=self.branding_container,
          image=logo_img,
        )
        self.logo_widget.image = logo_img
        self.logo_widget.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), ipady=0, sticky='n')

    def app_mgr_create_controls(self):
        self.app_mgr_controls = ttk.Frame(
            master=self.app_mgr_sidebar,
            # width=600,
            height=600,
            # style=PRIMARY,
        )
        self.app_mgr_controls.grid(row=1, column=0, rowspan=1, padx=5, pady=5, sticky='')

        self.app_mgr_controls.columnconfigure(0, weight=1)
        self.app_mgr_controls.rowconfigure(0, weight=1)
        self.app_mgr_controls.rowconfigure(1, weight=1)
        self.app_mgr_controls.rowconfigure(2, weight=1)

        self.app_mgr_create_buttonbox()

    def app_mgr_create_buttonbox(self):
        self.button_container = ttk.Frame(
            self.app_mgr_controls,
            width=200,
            height=200,
            # style=INFO,
        )
        self.button_container.grid(row=0, column=0, rowspan=1, padx=(20, 20), pady=(20, 20), sticky='ew')
        self.button_container.columnconfigure(0, weight=1)
        self.button_container.rowconfigure(0, weight=1)
        self.button_container.rowconfigure(1, weight=1)
        self.button_container.rowconfigure(2, weight=1)

        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        page_1_button = ttk.Button(
            master=self.button_container,
            text='Cancel',
            command=self.app_mgr_on_cancel,
            style=DANGER,
            width=6
        )
        page_1_button.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        cancel_btn = ttk.Button(
            master=self.button_container,
            text='Cancel',
            command=self.app_mgr_on_cancel,
            style=DANGER,
            width=6
        )
        cancel_btn.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        cancel_btn = ttk.Button(
            master=self.button_container,
            text='Cancel',
            command=self.app_mgr_on_cancel,
            style=DANGER,
            width=6
        )
        cancel_btn.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        cancel_btn_1 = ttk.Button(
            master=self.button_container,
            text='Cancel 1',
            command=self.app_mgr_on_cancel,
            style=SECONDARY,
            width=6
        )
        cancel_btn_1.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        cancel_btn_2 = ttk.Button(
            master=self.button_container,
            text='Cancel 2',
            command=self.app_mgr_on_cancel,
            style=WARNING,
            width=6
        )
        cancel_btn_2.grid(row=2, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

######################
# SUPPORT
    def nj_support_create(self):
        self.nj_supp_0 = ttk.Frame(
            self.app_mgr_container,
            width=500,
            height=500,
            # style=SUCCESS
        )
        self.nj_supp_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_support_header()
        self.nj_support_top_bar()
        self.nj_support_main()
        self.nj_support_bottom_bar()

        ###########################
        # refresh listings

        # infiles
        self.combo_infiles_refresh()

        # pages
        self.combo_pages_refresh()

        # pages images
        self.combo_pages_images_refresh()

    def nj_support_header(self):
        self.nj_support_header = ttk.Frame(
            master=self.nj_supp_0,
            width=200,
            height=500,
            # style=PRIMARY,
        )
        self.nj_support_header.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        self.nj_support_header_lbl = ttk.Label(
            master=self.nj_support_header,
            text='Support - master',
            # style=LIGHT,
        )
        self.nj_support_header_lbl.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

    def nj_support_top_bar(self):
        self.pn_supp_top_bar = ttk.Frame(
            master=self.nj_supp_0,
            # width=500,
            # height=10,
            # style=DARK,
        )
        self.pn_supp_top_bar.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='n')

        self.pn_supp_top_bar.rowconfigure(0, weight=2)

        self.pn_supp_top_bar.columnconfigure(0, weight=1)
        self.pn_supp_top_bar.columnconfigure(1, weight=1)
        self.pn_supp_top_bar.columnconfigure(2, weight=1)
        self.pn_supp_top_bar.columnconfigure(3, weight=1)
        self.pn_supp_top_bar.columnconfigure(4, weight=1)

        self.support_operations = ttk.Frame(
            master=self.pn_supp_top_bar,
            # style=DARK
        )
        self.support_operations.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        sup_button_0 = ttk.Button(
            master=self.support_operations,
            text='Refresh COMBO Infiles',
            style=PRIMARY,
            cursor='hand2',
            command=self.combo_infiles_refresh
        )
        sup_button_0.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        sup_button_1 = ttk.Button(
            master=self.support_operations,
            text='Refresh Combo Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.combo_pages_refresh()
,
        )
        sup_button_1.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')

        combo_pages_listing = self.get_combo_pages_listing()
        combo_pages_in_dir = COMBO_PAGES_DIR
        sup_button_2 = ttk.Button(
            master=self.support_operations,
            text='Refresh Combo Images',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.combo_pages_images_refresh()
            #command = lambda: self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)
        )
        sup_button_2.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky='')

    def nj_support_main(self):
        self.nj_support_main = ttk.Frame(
            master=self.nj_supp_0,
            # width=200,
            # height=500,
            style=DANGER,
        )
        self.nj_support_main.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_support_main.columnconfigure(0, weight=1)
        self.nj_support_main.columnconfigure(1, weight=1)
        self.nj_support_main.columnconfigure(2, weight=1)
        self.nj_support_main.rowconfigure(0, weight=1)
        self.nj_support_main.rowconfigure(1, weight=1)

        SCROLLFRAME_WIDTH = 400
        SCROLLFRAME_HEIGHT = 500

        self.nj_support_combo_infiles = ScrolledFrame(
            master=self.nj_support_main,
            autohide=True,
            width=SCROLLFRAME_WIDTH,
            height=SCROLLFRAME_HEIGHT,
            # style=DARK,
        )
        self.nj_support_combo_infiles.grid(row=0, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        self.nj_support_scroll_combo_pages = ScrolledFrame(
            master=self.nj_support_main,
            autohide=True,
            width=SCROLLFRAME_WIDTH,
            height=SCROLLFRAME_HEIGHT,
            # style=DARK,
        )
        self.nj_support_scroll_combo_pages.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        self.nj_support_scroll_combo_pages_images = ScrolledFrame(
            master=self.nj_support_main,
            autohide=True,
            width=SCROLLFRAME_WIDTH,
            height=SCROLLFRAME_HEIGHT,
            # style=DARK,
        )
        self.nj_support_scroll_combo_pages_images.grid(row=0, column=2, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')
        self.nj_support_scroll_combo_pages_images_switches = []

        #
        # self.test_button = ttk.Button(
        #     master=self.nj_dash_0,
        #     style=WARNING
        # )
        # self.test_button.grid(row=1, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

    def nj_support_bottom_bar(self):
        # pdf_ninja
        self.pn_supp_bottom_bar = ttk.Frame(
            master=self.nj_supp_0,
            # width=500,
            # height=10,
            # style=SECONDARY,
        )
        self.pn_supp_bottom_bar.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky='')

        self.pn_supp_bottom_bar.rowconfigure(0, weight=2)
        self.pn_supp_bottom_bar.rowconfigure(1, weight=1)

        self.pn_supp_bottom_bar.columnconfigure(0, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(1, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(2, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(3, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(4, weight=1)

        supp_bottom_btn_0 = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Gen COMBO Infiles',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        supp_bottom_btn_0.grid(row=0, column=0, padx=(10, 5), pady=(5, 5), sticky='')

        supp_bottom_btn_1 = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Gen COMBO Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.gen_combo_pages_from_combo_pages(),
        )
        supp_bottom_btn_1.grid(row=0, column=1, padx=(10, 5), pady=(5, 5), sticky='')

        supp_bottom_btn_2 = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Gen COMBO Pages Images',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.generate_combo_pages_images(),
        )
        supp_bottom_btn_2.grid(row=0, column=2, padx=(10, 5), pady=(5, 5), sticky='')

        # st = ScrolledText(app, padding=5, height=10, autohide=True)

        self.support_info_txt = ScrolledText(
            master=self.pn_supp_bottom_bar,
            # autohide=False,
            # hbar=True,
            width=80,
            height=5,
            # style=PRIMARY,
        )
        self.support_info_txt.grid(row=0, column=3, padx=(10, 5), pady=(5, 5), sticky='')


    ######################
    # DASHBOARD
    ######################

    def nj_dashboard_create(self):
        self.nj_dash_0 = ttk.Frame(
            self.app_mgr_container,
            width=500,
            height=500,
            # style=SUCCESS
        )
        self.nj_dash_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_dashboard_header()
        self.nj_dashboard_top_bar()
        self.nj_dashboard_main()
        self.nj_dashboard_bottom_bar()

    def nj_dashboard_header(self):
        self.nj_dashboard_header = ttk.Frame(
            master=self.nj_dash_0,
            width=200,
            height=500,
            # style=PRIMARY,
        )
        self.nj_dashboard_header.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        self.nj_dashboard_header_lbl = ttk.Label(
            master=self.nj_dashboard_header,
            text='DashBoard',
            font='helvetica 20 bold',
            style=LIGHT,
        )
        self.nj_dashboard_header_lbl.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

    def nj_dashboard_top_bar(self):
        self.pn_top_bar = ttk.Frame(
            master=self.nj_dash_0,
            # width=500,
            # height=10,
            # style=DARK,
        )
        self.pn_top_bar.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='n')

        self.pn_top_bar.rowconfigure(0, weight=2)

        self.pn_top_bar.columnconfigure(0, weight=1)
        self.pn_top_bar.columnconfigure(1, weight=1)
        self.pn_top_bar.columnconfigure(2, weight=1)
        self.pn_top_bar.columnconfigure(3, weight=1)
        self.pn_top_bar.columnconfigure(4, weight=1)

        self.dashboard_operations = ttk.Frame(
            master=self.pn_top_bar,
            # style=DARK
        )
        self.dashboard_operations.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        button_0 = ttk.Button(
            master=self.dashboard_operations,
            text='Load PDF File - TST',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.load_pdf_file(),
        )
        button_0.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        button_1 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate PDF Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.gen_pdf_pages_from_all_infiles(),
        )
        button_1.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')

        button_2 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate Combo Infiles',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.build_combo_all(),
        )
        button_2.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky='')

        button_3 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate Combo Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.gen_combo_pages_from_combo_pages(),
        )
        button_3.grid(row=1, column=3, padx=(5, 5), pady=(5, 5), sticky='')

        button_4 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate Combo Images',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.generate_combo_pages_images(),
        )
        button_4.grid(row=1, column=4, padx=(5, 5), pady=(5, 5), sticky='')

        button_5 = ttk.Button(
            master=self.dashboard_operations,
            text='Full Wash Cycle',
            style=DANGER,
            cursor='hand2',
            command=lambda: self.full_wash_cycle(),
        )
        button_5.grid(row=1, column=5, padx=(5, 5), pady=(5, 5), sticky='')

    def full_wash_cycle(self):
        # print(f'\nfull_wash_cycle')
        self.load_pdf_file()

        # print(f'full_wash_cycle:gen pdf pages')
        self.gen_pdf_pages_from_all_infiles()

        # print(f'full_wash_cycle: building combo')
        self.build_combo_all()

        # print(f'full_wash_cycle: building combo pages')
        self.gen_combo_pages_from_combo_pages()

        # print(f'full_wash_cycle: building combo pages images')
        self.generate_combo_pages_images()

        # combo_pages_listing = self.get_combo_pages_listing()
        # combo_pages_in_dir = COMBO_PAGES_DIR
        # self.refresh_all_combo_pages_images(combo_pages_listing, combo_pages_in_dir)

        # refreshing dnd listing
        # self.combo_sort_refresh()

    def nj_dashboard_main(self):
        self.nj_dashboard_main = ttk.Frame(
            master=self.nj_dash_0,
            # width=200,
            # height=500,
            # style=WARNING,
        )
        self.nj_dashboard_main.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_dashboard_main.columnconfigure(0, weight=1)
        self.nj_dashboard_main.rowconfigure(0, weight=1)
        self.nj_dashboard_main.rowconfigure(1, weight=1)

        self.nj_dashboard_scroll_pages = ScrolledFrame(
            master=self.nj_dashboard_main,
            autohide=True,
            width=1000,
            height=600,
            style=SECONDARY,
        )
        self.nj_dashboard_scroll_pages.grid(row=0, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        self.combo_pages_images_refresh()

        #
        # self.test_button = ttk.Button(
        #     master=self.nj_dash_0,
        #     style=WARNING
        # )
        # self.test_button.grid(row=1, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

    def nj_dashboard_bottom_bar(self):
        # pdf_ninja
        self.pn_bottom_bar = ttk.Frame(
            master=self.nj_dash_0,
            # width=500,
            # height=10,
            # style=SECONDARY,
        )
        self.pn_bottom_bar.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky='')

        self.pn_bottom_bar.rowconfigure(0, weight=2)
        self.pn_bottom_bar.rowconfigure(1, weight=1)

        self.pn_bottom_bar.columnconfigure(0, weight=1)
        self.pn_bottom_bar.columnconfigure(1, weight=1)
        self.pn_bottom_bar.columnconfigure(2, weight=1)
        self.pn_bottom_bar.columnconfigure(3, weight=1)
        self.pn_bottom_bar.columnconfigure(4, weight=1)

        self.combo_filename_entry_frame = ttk.Frame(
            master=self.pn_bottom_bar,
            width=50,
            height=50,
            style=WARNING,
        )
        self.combo_filename_entry_frame.grid(row=0, column=1, rowspan=2, padx=(5, 5), pady=(5, 0), sticky='N')

        self.combo_filename_entry = ttk.Entry(
            master=self.combo_filename_entry_frame,
            # placeholder_text="combo filename"
        )
        self.combo_filename_entry.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='N')

        self.button_merge_pages = ttk.Button(
            master=self.combo_filename_entry_frame,
            text='Build Combo',
            command=self.build_combo_all
        )
        self.button_merge_pages.grid(row=2, column=0, padx=(5, 5), pady=(5, 5))

        self.bottom_lbl_0 = ttk.Label(
            master=self.pn_bottom_bar,
            text='Status Label: ',
            style=LIGHT,
            font='Helvetica, 12',
        )
        self.bottom_lbl_0.grid(row=1, column=2, columnspan=3, padx=(10, 5), pady=(5, 5), sticky='')

        bottom_btn_0 = ttk.Button(
            master=self.pn_bottom_bar,
            text='Merge Final Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        bottom_btn_0.grid(row=0, column=2, padx=(10, 5), pady=(5, 5), sticky='')

        bottom_btn_1 = ttk.Button(
            master=self.pn_bottom_bar,
            text='Build Combo',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        bottom_btn_1.grid(row=0, column=3, padx=(10, 5), pady=(5, 5), sticky='')

        bottom_btn_2 = ttk.Button(
            master=self.pn_bottom_bar,
            text='POPUP: get combo name',
            style=DANGER,
            cursor='hand2',
            command=lambda: self.open_get_combo_dialog(),
        )
        bottom_btn_2.grid(row=0, column=4, padx=(10, 5), pady=(5, 5), sticky='')

    def open_get_combo_dialog(self):
        getComboDialog = GetComboDialog(self.refresh_combo_name)

    def refresh_combo_name(self, combo_name):
        ic('update function from main window...')
        self.current_combo_name = combo_name.get()
        ic(self.current_combo_name)
        self.bottom_lbl_0.configure(text=f'Current Combo: {self.current_combo_name}')


    ####################################
    # utiities
    #

    #
    # def gen_all_combo_pages_from_combo(self):
    #     print(f'\ngen_all_combo_pages_from_combo')
    #     # get selection
    #     row = 0
    #
    #     combo_infiles_lst = self.combo_infiles_listing()
    #     print(f'gen_all_combo_pages_from_combo:combo_infiles_lst: {combo_infiles_lst}')
    #
    #     # which combo infiles have been selected
    #     selection = []
    #     row = 0
    #     for in_file in combo_infiles_lst:
    #         is_set = 1
    #         # is_set = self.combo_sort_infiles_listing_frame_switches[row].get()
    #         print(f'gen_all_combo_pages_from_combo:is_set: {is_set}')
    #         print(f'gen_all_combo_pages_from_combo:in_file: {in_file}')
    #
    #         # print(f'is_set:    {is_set} :: infile: {infile}')
    #         if is_set:
    #             selection.append(in_file)
    #         row += 1
    #
    #     # print(f'gen_all_combo_pages_from_combo:selection: {selection}')
    #     # generate combo_pages from selected combo_infiles
    #     for combo_infile in selection:
    #         combo_infile = f'{combo_infile}'
    #         name_of_split = f'{combo_infile}-path'
    #         in_dir = COMBO_INFILES_DIR
    #         out_dir = COMBO_PAGES_DIR
    #         # print(f'out_dir: {out_dir}')
    #
    #         # print(f'gen_all_combo_pages_from_combo:combo_infile: {combo_infile}')
    #         self.pdf_t.split_combo_infiles_2_pages(
    #             combo_infile,
    #             name_of_split,
    #             in_dir,
    #             out_dir
    #         )
    #
    #         print(f'gen_all_combo_pages_from_combo: calling combo_images_refresh')
    #         self.combo_pages_refresh()
    #         # self.combo_images_refresh()


    def get_combo_name_input(self):
        self.current_combo_name = ''

        # create label
        self.combo_name_lbl = ttk.Label(
            master=self.dashboard_operations,
            # text='Enter your preferred Combo name: '
        )
        self.combo_name_lbl.grid(row=0, column=3, rowspan=1, columnspan=1, padx=(0, 0), pady=(10, 10), sticky='w')

        def get_combo_name():
            self.combo_name_lbl.config(text=f'You typed: {self.combo_name_entry.get()}')
            new_combo_name = self.combo_name_entry.get()
            # ic(new_combo_name)
            self.current_combo_name = new_combo_name
            # ic(self.current_combo_name)
            return new_combo_name

        # create entry widget
        self.combo_name_entry = ttk.Entry(
            master=self.dashboard_operations,
            style=SUCCESS,
            width=28,
            font=('Helvetica', 10)
        )
        # combo_name_entry.insert(0, "Enter Combo Name: ")
        self.combo_name_entry.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(0, 0), pady=(10, 10), sticky='')

        # create button
        self.combo_name_btn = ttk.Button(
            master=self.dashboard_operations,
            style='SUCCESS OUTLINE',
            text='Use Name',
            command=get_combo_name(),
        )
        self.combo_name_btn.grid(row=0, column=2, rowspan=1, columnspan=1, padx=(0, 0), pady=(10, 10), sticky='w')

        self.combo_name_btn.wait_variable(self.current_combo_name)

        return self.current_combo_name

    def build_combo_all(self):
        # get name of combo from user
        # form variables
        self.combo_name = ttk.StringVar(value="")
        self.current_combo_name = ''

        # create entry function
        #
        # rand_prefix = random.randint(1, 1000000)
        # outfile = f'{rand_prefix}.pdf'

        outfile = self.combo_filename_entry.get()
        # self.outfile_global = outfile

        outfile_global = outfile
        # ic(f'outfile set: {outfile}')

        if len(outfile) == 0:
            dummy = 0
            # ic(f'no Entry')
            # self.textbox.delete("0.0", "end")  # delete all text
            # out_txt = 'No Entry'
            # self.textbox.insert("0.0", out_txt)
        else:
            # ic(outfile)
            if len(outfile) == 0:
                ic(f'No Pages Selected...')
            else:
                selection = self.get_page_all_selected(outfile_global)
                # print(f'build_combo_all:selection: {selection}')
                self.pdf_t.merge_files(selection, outfile)

                # c_lst_frame = self.combo_listing_frame.grid_columnconfigure(0, weight=1)
                # self.combo_refresh()
                # FileMgr.combo_refresh(c_lst_frame)
        # print(f'xxxxxxxxxx-#####-xxxxxxxx: build_combo_all: calling combo refresh')

        # self.combo_refresh()

    def get_page_all_selected(self, pattern):
        ic('in get_page_all_selected')
        pdf_pages_listing = self.pdf_t.list_pages_dir(pattern)
        ic(pattern, pdf_pages_listing)

        # ic(f'{__name__} : {pdf_pages_listing}')

        selection = []
        for i in enumerate(pdf_pages_listing):
            is_selected = 1
            # is_selected = self.page_listing_frame_switches[i].get()

            # ic(is_selected)
            # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
            if is_selected == 1:
                selection.append(pdf_pages_listing[i[0]])
        # ic(selection)
        return selection

    def combo_infiles_refresh(self):
        # ic(f'combo_infiles_refresh')

        self.combo_sort_infiles_listing_frame_switches = []
        row = 0

        combo_infiles_lst = self.combo_infiles_listing()

        for in_file in combo_infiles_lst:
            # print(f'combo_pages_refresh:combo:{combo}')
            switch_name = ttk.Checkbutton(
                master=self.nj_support_combo_infiles,
                text=f"{in_file}",
                # fg_color='yellow',
                style=DANGER
            )
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_sort_infiles_listing_frame_switches.append(switch_name)

        return combo_infiles_lst

    def combo_infiles_listing(self):
        listing = self.pdf_t.combo_infiles_listing()
        # print(f'combo_infiles_listing:listing: {listing}')
        # self.display_listing(listing)
        return listing

    def combo_infiles_listing_PROTO(self):
        listing = self.pdf_t.combo_infiles_listing()
        # ic(listing)

        # ic(self.outfile_global)

        # print(f'combo_infiles_listing:listing: {listing}')
        # print(f'combo_infiles_listing:listing: {listing}')
        # self.display_listing(listing)
        return listing

    def combo_pages_refresh(self):
        self.combo_pages_listing_frame_switches = []
        row = 0
        combo_lst = self.get_combo_pages_listing()
        # ic(f'combo_pages_refresh: {combo_lst}')
        #
        # combo_page_switches = ttk.Frame(
        #     master=self.nj_dashboard_main,
        # )
        for combo in combo_lst:
            # print(f'combo_pages_refresh:combo:{combo}')
            switch_name = ttk.Checkbutton(
                master=self.nj_dashboard_main,
                text=f"{combo}",
                style=PRIMARY,
            )
            # switch_name.grid(row=row, column=0, padx=(5, 5), pady=(5, 5))
            row += 1
            self.combo_pages_listing_frame_switches.append(switch_name)

    def get_combo_pages_listing(self):
        listing = self.pdf_t.list_combo_pages_dir()
        # print(f'XXXX:get_combo_pages_listing: {listing}')
        # ic(listing)
        # self.display_listing(listing)
        return listing

    def combo_pages_images_refresh(self):
        row = 0
        col_index = 0
        combo_lst = self.get_combo_pages_images_listing()
        # ic(f'combo_pages_images_refresh: {combo_lst}')

        ##############################

        ##############################

        self.combo_pages_images_listing_frame_switches = []

        for combo in combo_lst:
            # ic(row, col_index)
            if col_index >= DASHBOARD_NUM_COLS:
                col_index = 0
                row += 1
            # ic(row, col_index)

            combo_pages_image_frame = ttk.Frame(
                master=self.nj_dashboard_scroll_pages,
            )
            combo_pages_image_frame.grid(row=row, column=col_index, padx=(0, 0), pady=(0, 0))

            combo_pages_image_frame.rowconfigure(0, weight=1)
            combo_pages_image_frame.rowconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(0, weight=1)
            combo_pages_image_frame.columnconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(2, weight=1)

            # ic(row, col_index)
            # ic(combo)
            # ic(row, col_index)

            sz_w = COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)
            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            img_path = f'{COMBO_IMAGES_DIR}/{combo}'
            ic(img_path)
            # skip if image already exists
            # if img_path.exists():


            icon_img = Image.open(img_path).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            switch_initial_state = ttk.IntVar(value=1)
            switch_name = ttk.Checkbutton(
                master=combo_pages_image_frame,
                # width=50,
                # height=50,
                style=WARNING,
                variable=switch_initial_state,
            )
            switch_name.grid(row=1, column=0, padx=(5, 5), pady=(5, 10), sticky='')
            self.combo_pages_images_listing_frame_switches.append(switch_name)

            # test_pages_image_label = ttk.Label(
            #     master=combo_pages_image_frame,
            #     # image=photo_img,
            #     # font='helvetica 18 bold',
            #     # width=100,
            #     text='TESTER',
            #     # compound='top',
            #     style=LIGHT,
            # )
            # test_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            combo_pages_image_label = ttk.Label(
                master=combo_pages_image_frame,
                image=photo_img,
                # font='helvetica 18 bold',
                # width=100,
                text=combo,
                compound='top',
                style=LIGHT,
            )
            combo_pages_image_label.image = photo_img
            combo_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            col_index += 1

    def dashboard_combo_pages_images_refresh(self):
        row = 0
        di_col_index = 0
        combo_lst = self.get_combo_pages_images_listing()
        self.combo_pages_images_listing_frame_switches = []

        combo_pages_image_frame = ttk.Frame(
            master=self.nj_dashboard_scroll_pages,
        )
        combo_pages_image_frame.grid(row=row, column=0, padx=(10, 10), pady=(10, 10))

        combo_pages_image_frame.rowconfigure(0, weight=1)
        combo_pages_image_frame.columnconfigure(0, weight=1)
        combo_pages_image_frame.columnconfigure(1, weight=1)
        combo_pages_image_frame.columnconfigure(2, weight=1)

        for combo in combo_lst:
            # ic(row, di_col_index)
            # ic(combo)

            if di_col_index >= DASHBOARD_NUM_COLS:
                row += 1
                di_col_index = 0
            else:
                di_col_index += 1

            sz_w = COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)

            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            # photo_img = tk.PhotoImage(icon_img)
            img_path = f'{COMBO_IMAGES_DIR}/{combo}'

            # ic(img_path)

            icon_img = Image.open(img_path).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            # ic(photo_img)

            switch_name = ttk.Checkbutton(
                master=combo_pages_image_frame,
                # text=f"{combo}",
                style=PRIMARY,
                # fg_color='yellow',
            )
            switch_name.grid(row=row, column=di_col_index, padx=(5, 5), pady=(5, 5))
            self.combo_pages_images_listing_frame_switches.append(switch_name)

            combo_pages_image_label = ttk.Label(
                master=combo_pages_image_frame,
                image=photo_img,
                # font='helvetica 18 bold',
                # width=100,
                text=combo,
                compound='top'
            )
            combo_pages_image_label.image = photo_img
            combo_pages_image_label.grid(row=row, column=1, padx=(0, 0), pady=(0, 20))

            row += 1

    def get_combo_pages_images_listing(self):
        listing = self.pdf_t.list_combo_images_dir()
        # print(f'XXXX:get_combo_pages_listing: {listing}')
        # self.display_listing(listing)
        return listing

    def generate_combo_pages_images(self):
        c_lst = self.get_combo_pages_listing()
        ic(f'c_lst: {c_lst}')

        # define out images
        folder_img = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
        list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((60, 60)))
        icon_lst = []
        # ic(c_lst)

        for in_file in c_lst:

            ic(in_file)
            images_path = f'{COMBO_IMAGES_DIR}/{in_file}.png'
            ic(images_path)

            if path.exists(images_path):
                ic(in_file, 'already exists', path.exists(images_path) )
            else:
                ic(in_file, 'path does NOT exists')

                # ic(in_file)
                with open(in_file, 'wb') as in_img:
                    f_path = f'{COMBO_PAGES_DIR}/{in_file}'
                    # ic(f_path)
                    img = convert_from_path(f_path)

                    for i in range(len(img)):
                        save_file = COMBO_IMAGES_DIR + '/' + in_file + '.png'
                        # ic(save_file)

                        img[i].save(save_file, 'PNG')

        self.combo_pages_images_refresh()

    def gen_combo_pages_from_combo_pages(self):
        # converts ALL infiles
        # ic(f'gen_combo_pages_from_combo')
        # get selection
        row = 0

        combo_infiles_lst_PROTO = self.combo_infiles_listing_PROTO()
        # ic(combo_infiles_lst_PROTO)

        # remove all not equal to outfile_global

        # print(f'combo_infiles_lst: {combo_infiles_lst}')

        # which combo infiles have been selected
        selection = []
        row = 0
        # ic(self.combo_pages_listing_frame_switches)

        for in_file in combo_infiles_lst_PROTO:
            # is_set = self.combo_pages_listing_frame_switches[row].get()
            is_set = True
            #
            # print(f'gen_combo_pages_from_combo:is_set: {is_set}')
            # print(f'gen_combo_pages_from_combo:in_file: {in_file}')

            # print(f'is_set:    {is_set} :: infile: {infile}')
            if is_set:
                selection.append(in_file)
            row += 1

        # print(f'gen_combo_pages_from_combo:selection: {selection}')
        # generate combo_pages from selected combo_infiles
        for combo_infile in selection:
            combo_infile = f'{combo_infile}'
            name_of_split = f'{combo_infile}'
            in_dir = COMBO_INFILES_DIR
            out_dir = COMBO_PAGES_DIR
            # print(f'out_dir: {out_dir}')

            # print(f'gen_pdf_pages_from_infile:combo_infile: {combo_infile}')
            self.pdf_t.split_combo_infiles_2_pages(
                combo_infile,
                name_of_split,
                in_dir,
                out_dir
            )

            # print(f'gen_combo_pages_from_combo: calling combo_images_refresh')
            self.combo_pages_refresh()
            # self.combo_images_refresh()

    def load_pdf_file(self):
        # self.refresh_f_listings()
        # ic(f'in load_PDF_file')

        # get entry value
        # load_pdf_file_name = f'{self.load_file_entry.get()}'

        self.current_combo_name = fd.askopenfilename()
        ic(self.current_combo_name, self.current_combo_name.split('/')[-1])

        # read input file'
        try:
            # ic('opening', self.load_pdf_file )
            with open(self.current_combo_name, 'rb') as in_img:
                pdf_contents = in_img.read()
                # print(f'pdf_contents: {pdf_contents}')
        except:
            print(f'unable to open: {self.current_combo_name}')

        # ic(pdf_contents)

        # write local infile
        out_split = self.current_combo_name.split('/')[-1]
        # ic(out_split)

        # print(f'out_split: {out_split}')

        pdf_save_file = f'{PDF_INFILES}/{out_split}'
        # ic(pdf_save_file)

        combo_infilea = f'{COMBO_INFILES_DIR}/{out_split}'
        # ic(combo_infilea)

        # print(f'pdf_save_file: {pdf_save_file}')
        try:
            # ic(pdf_save_file)
            with open(pdf_save_file, 'wb') as save_file:
                save_file.write(pdf_contents)
        except FileNotFoundError:
            print(f'unable to save file: {pdf_save_file}')

        try:
            # ic(combo_infilea)
            with open(combo_infilea, 'wb') as save_file:
                save_file.write(pdf_contents)
        except FileNotFoundError:
            print(f'unable to save file: {combo_infilea}')

        # self.refresh_pdf_infiles_listing()

    def refresh_pdf_infiles_listing(self):
        row = 0
        pdf_infiles_list = self.pdf_infiles_listing()

        # pdf_infiles_listing
        # print(f's_lst: {s_lst}')
        for in_file in pdf_infiles_list:
            switch_name = customtkinter.CTkSwitch(master=self.file_list_scrollable_frame, text=f"{in_file}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.file_list_scrollable_frame_switches.append(switch_name)
        # print(f'switches: {self.f_scrollable_frame_switches}')

    def pdf_infiles_listing(self):
        listing = self.pdf_t.pdf_infiles_listing()
        # print(f'pdf_infiles_listing:listing: {listing}')
        # self.display_listing(listing)
        return listing


############55555555555555555555555555555555555555555555555555
    def gen_pdf_pages_from_all_infiles(self):
        # ic(f'\nXXX:gen_pdf_pages_from_all_infiles')

        # get selection
        row = 0

        pdf_infiles_list = self.pdf_infiles_listing()
        # ic(pdf_infiles_list)

        selection = []
        row = 0
        for infile in pdf_infiles_list:
            # select ALL
            is_set = 1
            # is_set = self.file_list_scrollable_frame_switches[row].get()
            # print(f'is_set: {is_set} :: infile: {infile}')
            if is_set:
                # print(f'gen_pdf_pages_from_all_infiles: {infile}')
                selection.append(infile)
            row += 1

        # ic(selection)

        #TOD enforce as least one selection

        # for each of selection
            # split into pages & save to pdf_pages directory
        s_cnt = 0
        for pdf_infile in selection:
            pdf_file = f'{pdf_infile}'
            # ic(pdf_file)
            name_of_split = f'{pdf_file}'
            in_dir = PDF_INFILES
            out_dir = PDF_PAGES_DIR
            # ic(pdf_file)

            self.pdf_t.split_pdf_infiles_2_pages(
                pdf_file,
                f'{name_of_split}',
                in_dir,
                out_dir
            )

            # self.pdf_pages_refresh()

    def display_listing(self, lst):
        # print(f'display_pdf_listing:lst: {lst}')
        out_txt = ''
        for f in lst:
            out_txt += f'{f}\n'
            # ic(out_txt)
        self.support_info_txt.delete("0.0", "end")  # delete all text
        self.support_info_txt.insert("0.0", out_txt)

    # action when user clicks cancel
    def app_mgr_on_cancel(self):
        self.quit()

    def dummy_func(self):
        ic('in dummy_func()')


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


























class GradeBook(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.name = ttk.StringVar(value='')
        self.student_id = ttk.StringVar(value='')
        self.course_name = ttk.StringVar(value='')
        self.final_score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = master_window.style.colors

        instruction_text = 'Please enter your contact information: '
        instruction = ttk.Label(
            self,
            text=instruction_text,
            width=50,
        )
        instruction.pack(fill=X, pady=10)

        self.create_form_entry('Name: ', self.name)
        self.create_form_entry('Student ID: ', self.student_id)
        self.create_form_entry('Course Name: ', self.course_name)
        self.final_score_input = self.create_form_entry('Final Score: ', self.final_score)

        self.create_meter()
        self.create_buttonbox()
        self.table = self.create_table()

    # create text/numerical inputs
    def create_form_entry(self, label, variable):
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)

        form_field_label = ttk.Label(
            master=form_field_container,
            text=label,
            width=50,
        )
        form_field_label.pack(side=LEFT, padx=12)

        form_input = ttk.Entry(
            master=form_field_container,
            textvariable=variable,
        )
        form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

        add_regex_validation(form_input, r'^[a-zA-Z0-9_]*$')

        return form_input

    # create meter
    def create_meter(self):
        meter = ttk.Meter(
            master=self,
            metersize=150,
            padding=5,
            amounttotal=100,
            amountused=50,
            metertype='full',
            interactive=True,
        )
        meter.pack()
        self.final_score.set(meter.amountusedvar)
        self.final_score_input.configure(textvariable=meter.amountusedvar)

    # create button
    def create_buttonbox(self):
        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))

        cancel_btn = ttk.Button(
            master=button_container,
            text='Cancel',
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6
        )
        cancel_btn.pack(side=RIGHT, padx=5)

        submit_btn = ttk.Button(
            master=button_container,
            text='Submit',
            command=self.on_submit,
            style=SUCCESS,
            width=6
        )
        submit_btn.pack(side=RIGHT, padx=5)

    # action when user clicks submit
    def on_submit(self):
        name = self.name.get()
        student_id = self.student_id.get()
        course_name = self.course_name.get()
        final_score = self.final_score_input.get()

        toast = ToastNotification(
            title='Submission Successful',
            message='Your data has been successfully submitted.',
            duration=3000,
        )

        toast.show_toast()

        self.data.append((name, student_id, course_name, final_score))
        self.table.destroy()
        self.table = self.create_table()

    # action when user clicks cancel
    def on_cancel(self):
        self.quit()

    def create_table(self):
        coldata = [
            {'text': 'Name'},
            {'text': 'Student ID', 'stretch': False},
            {'text': 'Course Name: '},
            {'text': 'Final Score', 'stretch': False},
        ]

        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(self.colors.light, None),
        )
        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        return table

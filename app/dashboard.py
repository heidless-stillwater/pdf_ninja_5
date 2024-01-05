import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

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
        font=TITLE_FONT,
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

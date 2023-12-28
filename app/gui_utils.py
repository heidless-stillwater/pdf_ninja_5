import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledFrame



from PIL import Image, ImageTk
from icecream import ic
import os

# pathlib
# setuptools

from constants import *

class PdfNinja(ttk.Frame):
    root_dir = os.getcwd()
    ic(root_dir)
    def __init__(self, master_window):
        super().__init__(master_window, padding=(0, 0))
        # self.pack(fill=BOTH, expand=YES)

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
            style=WARNING,
        )
        self.app_mgr_container.grid(row=0, column=0, rowspan=1, padx=(20, 20), pady=(20, 20), sticky='nsew')

        self.app_mgr_container.rowconfigure(0, weight=1)
        self.app_mgr_container.columnconfigure(0, weight=1)
        self.app_mgr_container.columnconfigure(1, weight=1)

        self.app_mgr_create()

        self.nj_dashboard_create()

        # self.nj_support_create()
        # self.nj_support_top_bar()

        # table
        # colors =

    def app_mgr_create(self):
        ic('in app mgr create')
        self.app_mgr_sidebar = ttk.Frame(
            master=self.app_mgr_container,
            width=500,
            height=500,
            style=INFO,
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
            style=SUCCESS,
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
        ic(PDF_NINJA_LOGO)

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
            style=PRIMARY,
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
            style=INFO,
        )
        self.button_container.grid(row=0, column=0, rowspan=1, padx=(20, 20), pady=(20, 20), sticky='ew')
        self.button_container.columnconfigure(0, weight=1)
        self.button_container.rowconfigure(0, weight=1)
        self.button_container.rowconfigure(1, weight=1)
        self.button_container.rowconfigure(2, weight=1)

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
            style=DANGER,
            width=6
        )
        cancel_btn_2.grid(row=2, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

    def nj_dashboard_create(self):
        self.nj_dash_0 = ttk.Frame(
            self.app_mgr_container,
            width=500,
            height=500,
            style=SUCCESS
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
            style=PRIMARY,
        )
        self.nj_dashboard_header.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        self.nj_dashboard_header_lbl = ttk.Label(
            master=self.nj_dashboard_header,
            text='DashBoard - master',
            style=INFO,
        )
        self.nj_dashboard_header_lbl.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

    def nj_dashboard_top_bar(self):
        self.pn_top_bar = ttk.Frame(
            master=self.nj_dash_0,
            # width=500,
            # height=10,
            style=DARK,
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
            style=DARK
        )
        self.dashboard_operations.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        button_0 = ttk.Button(
            master=self.dashboard_operations,
            text='Load PDF File',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        button_0.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        button_1 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate PDF Pages',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        button_1.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')

        button_2 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate Combo Infiles',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        button_2.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky='')

        button_3 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate Combo Pages',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        button_3.grid(row=1, column=3, padx=(5, 5), pady=(5, 5), sticky='')

        button_4 = ttk.Button(
            master=self.dashboard_operations,
            text='Generate Combo Images',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        button_4.grid(row=1, column=4, padx=(5, 5), pady=(5, 5), sticky='')

        button_5 = ttk.Button(
            master=self.dashboard_operations,
            text='Full Wash Cycle',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        button_5.grid(row=1, column=5, padx=(5, 5), pady=(5, 5), sticky='')

    def nj_dashboard_main(self):
        self.nj_dashboard_main = ttk.Frame(
            master=self.nj_dash_0,
            # width=200,
            # height=500,
            style=WARNING,
        )
        self.nj_dashboard_main.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_dashboard_main.columnconfigure(0, weight=1)
        self.nj_dashboard_main.rowconfigure(0, weight=1)
        self.nj_dashboard_main.rowconfigure(1, weight=1)

        self.nj_dashboard_scroll_pages = ScrolledFrame(
            master=self.nj_dashboard_main,
            autohide=True,
            width=1000,
            height=400,
            style=INFO,
        )
        self.nj_dashboard_scroll_pages.grid(row=0, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

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
            style=SECONDARY,
        )
        self.pn_bottom_bar.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky='')

        self.pn_bottom_bar.rowconfigure(0, weight=2)
        self.pn_bottom_bar.rowconfigure(1, weight=1)

        self.pn_bottom_bar.columnconfigure(0, weight=1)
        self.pn_bottom_bar.columnconfigure(1, weight=1)
        self.pn_bottom_bar.columnconfigure(2, weight=1)
        self.pn_bottom_bar.columnconfigure(3, weight=1)
        self.pn_bottom_bar.columnconfigure(4, weight=1)

        bottom_btn_0 = ttk.Button(
            master=self.pn_bottom_bar,
            text='Merge Final Pages',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        bottom_btn_0.grid(row=0, column=0, padx=(10, 5), pady=(5, 5), sticky='')

        bottom_btn_1 = ttk.Button(
            master=self.pn_bottom_bar,
            text='Build Combo',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        bottom_btn_1.grid(row=0, column=1, padx=(10, 5), pady=(5, 5), sticky='')

        bottom_btn_2 = ttk.Button(
            master=self.pn_bottom_bar,
            text='Gen Doc Based on Selection',
            style=DANGER,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        bottom_btn_2.grid(row=0, column=2, padx=(10, 5), pady=(5, 5), sticky='')

    def nj_support_create(self):
        self.nj_support_0 = ttk.Frame(
            self.app_mgr_container,
            style=INFO
        )
        self.nj_support_0.grid(row=0, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')
        self.nj_support_top_bar()

    def nj_support_top_bar(self):
        # pdf_ninja
        self.support_top_bar = ttk.Frame(
            self.nj_support_0,
            # width=500,
            # height=10,
            style=SECONDARY,
        )
        self.support_top_bar.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.support_top_bar.rowconfigure(0, weight=2)
        self.support_top_bar.rowconfigure(1, weight=1)
        self.support_top_bar.columnconfigure(0, weight=1)
        self.support_top_bar.columnconfigure(1, weight=1)
        #
        # self.support_top_bar.columnconfigure(2, weight=1)
        # self.support_top_bar.columnconfigure(3, weight=1)
        # self.support_top_bar.columnconfigure(4, weight=1)

        ic(self.support_top_bar)


        self.support_top_bar_lbl = ttk.Label(
            master=self.support_top_bar,
            text='Support'
        )
        self.support_top_bar_lbl.grid(row=0, column=0, rowspan=1, columnspan=6, padx=(10, 10), pady=(5, 5), sticky='')

        self.support_operations = ttk.Frame(
            master=self.support_top_bar,
            style=DARK
        )
        self.support_top_bar.rowconfigure(0, weight=2)
        self.support_top_bar.rowconfigure(1, weight=1)
        self.support_operations.columnconfigure(0, weight=1)
        self.support_operations.columnconfigure(1, weight=1)
        self.support_operations.columnconfigure(2, weight=1)
        self.support_operations.columnconfigure(3, weight=1)
        self.support_operations.columnconfigure(4, weight=1)
        self.support_operations.grid(row=1, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')


        support_button_0 = ttk.Button(
            master=self.support_operations,
            text='Load PDF File',
            style=SUCCESS,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        support_button_0.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        support_button_1 = ttk.Button(
            master=self.support_operations,
            text='Operation',
            style=INFO,
            cursor='hand2',
            command=lambda: self.dummy_func(),
        )
        support_button_1.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky='')

    # action when user clicks cancel
    def app_mgr_on_cancel(self):
        self.quit()

    def dummy_func(self):
        ic('in dummy_func()')



























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

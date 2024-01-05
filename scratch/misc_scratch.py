self.current_combo_name = ''

row = 0
title_combo_pages = ttk.Label(
    master=self.nj_support_scroll_combo_images,
    font=HEADING_FONT,
    style=LIGHT,
    text='combo pages'
)
title_combo_pages.grid(row=row, column=0, padx=(125, 0), pady=(0, 0), sticky='NSEW')
row += 1

support_combo_pages_images_refresh

# dashboard frame
self.nj_dash_0

def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()


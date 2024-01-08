self.combo_filename_entry_frame = ttk.Frame(
    master=self.pn_bottom_bar,
    width=50,
    height=50,
    style=WARNING,
)
self.combo_filename_entry_frame.grid(row=0, column=1, padx=(5, 5), pady=(5, 0), sticky='N')

self.combo_filename_entry = ttk.Entry(
    master=self.combo_filename_entry_frame,
    # placeholder_text="combo filename"
)
self.combo_filename_entry.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='N')

self.button_merge_pages = ttk.Button(
    master=self.combo_filename_entry_frame,
    text='Build Combo',
    command=self.buildComboAll
)
self.button_merge_pages.grid(row=2, column=0, padx=(5, 5), pady=(5, 5))
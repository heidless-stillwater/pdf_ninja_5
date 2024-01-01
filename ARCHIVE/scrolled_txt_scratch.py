import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

app = ttk.Window()

# scrolled text with autohide vertical scrollbar
st = ScrolledText(app, padding=5, height=10, autohide=True)
st.pack(fill=BOTH, expand=YES)

# add text
st.insert(END, 'Insert your text here.')

app.mainloop()
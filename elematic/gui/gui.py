import customtkinter as ctk
import tkinter as tk




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # Configure window
        self.title("elematic")
        self.geometry(f"{1100}x{580}")

        # Configure grid layout (2,1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        # Create left sidebar
        self.sidebar_frame = ctk.CTkFrame(self,width=280,corner_radius=0)
        self.sidebar_frame.grid(row=0,column=0,sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2,weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame,text="elematic",font=ctk.CTkFont(size=20,weight="bold"))
        self.logo_label.grid(row=0,column=0,padx=20,pady=(20,10))

        # Create tabview
        self.tabview = ctk.CTkTabview(self.sidebar_frame,width=280,command=self.set_tab_view,fg_color="transparent")
        self.tabview.grid(row=1,column=0,padx=(10,10),pady=(0,0),sticky="nsew")
        self.tabview.add("Materials")
        self.tabview.tab("Materials").grid_columnconfigure(0,weight=1)
        self.tabview.add("Metadata")
        self.tabview.tab("Metadata").grid_columnconfigure(0,weight=1)

        # Create Materials tab
        self.material_select = ctk.CTkOptionMenu(self.tabview.tab("Materials"))
        self.material_select.grid(row=0,column=0,padx=0,sticky="ew")
        self.material_id = ctk.CTkLabel(self.tabview.tab("Materials"),text="id",anchor="w")
        self.material_id.grid(row=1,column=0,sticky="ew")
        self.material_id_entry = ctk.CTkEntry(self.tabview.tab("Materials"),placeholder_text="id1001")
        self.material_id_entry.grid(row=2,column=0,sticky="ew")
        self.material_layers = ctk.CTkLabel(self.tabview.tab("Materials"),text="layers",anchor="w")
        self.material_layers.grid(row=3,column=0,sticky="ew")
        self.material_layers_entry = ctk.CTkEntry(self.tabview.tab("Materials"),placeholder_text="0")
        self.material_layers_entry.grid(row=4,column=0,sticky="ew")
        self.material_for = ctk.CTkLabel(self.tabview.tab("Materials"),text="local frame of reference",anchor="w")
        self.material_for.grid(row=5,column=0,sticky="ew")
        self.material_for_entry = ctk.CTkEntry(self.tabview.tab("Materials"),placeholder_text="1,1,1")
        self.material_for_entry.grid(row=6,column=0,sticky="ew")

        # Create sidebar buttons
        self.button_frame = ctk.CTkFrame(self.sidebar_frame,width=280,corner_radius=0,fg_color="transparent")
        self.button_frame.grid(row=2,sticky="s",pady=(0,10))
        self.button_cancel = ctk.CTkButton(self.button_frame,text="Cancel")
        self.button_cancel.grid(row=0,column=0,padx=(10,5))
        self.button_apply = ctk.CTkButton(self.button_frame,text="Apply")
        self.button_apply.grid(row=0,column=1,padx=(5,10))

        self.menubar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menubar,tearoff=0)
        self.file_menu.add_command(label="New",command=self.not_implemented)
        self.file_menu.add_command(label="Open",command=self.not_implemented)
        self.file_menu.add_command(label="Save",command=self.not_implemented)
        self.file_menu.add_command(label="Save as",command=self.not_implemented)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.quit)
        self.config(menu=self.menubar)
        self.menubar.add_cascade(label="File",menu=self.file_menu)

        self.help_menu = tk.Menu(self.menubar,tearoff=0)
        self.help_menu.add_command(label="About",command=self.not_implemented)
        self.help_menu.add_command(label="Documentation",command=self.not_implemented)
        self.config(menu=self.menubar)
        self.menubar.add_cascade(label="Help",menu=self.help_menu)

        self.set_tab_view()

    def set_tab_view(self):
        tab = self.tabview.get()
        if tab == "Materials":
            self.material_tabs = ctk.CTkTabview(self,fg_color="transparent")
            self.material_tabs.grid(row=0,column=1,sticky="nsew")
            self.material_tabs.add("BulkDetails")
            self.material_tabs.add("ComponentDetails")
            self.material_tabs.add("Graphs")
            self.material_tabs.add("Glossary")
    
    def not_implemented(self):
        print("Not yet implemented")

if __name__ == "__main__":
    app = App()
    app.mainloop()
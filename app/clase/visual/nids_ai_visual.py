import customtkinter as ctk
from PIL import Image, ImageTk

class NIDS_AI_Visual:
    
    def __init__(self, root):
        self.root = root
        self.root.title("NIDS-AI")
        self.root.resizable(False, False)
        self.root.iconpath = ImageTk.PhotoImage(file="app/clase/visual/upc.png")
        self.root.wm_iconbitmap()
        self.root.iconphoto(False, self.root.iconpath)


        ctk.set_appearance_mode("dark")

        self.current_mode = 0

        sun_image = Image.open("app/clase/visual/sun.png").resize((24, 24), Image.Resampling.LANCZOS)
        moon_image = Image.open("app/clase/visual/moon.png").resize((24, 24), Image.Resampling.LANCZOS)
        out_image = Image.open("app/clase/visual/close.png").resize((24, 24), Image.Resampling.LANCZOS)

        self.sun = ctk.CTkImage(dark_image=sun_image, size=(24, 24))
        self.moon = ctk.CTkImage(dark_image=moon_image, size=(24, 24))
        self.out = ctk.CTkImage(dark_image=out_image, size=(24, 24))

        self.create_widgets()
        self.v_detection = False
        self.view_detection("")
        self.execute_bool = False
        self.previous_lines = set()
        print("NIDSVisualClass inicialized!")

    def create_widgets(self):
        input_frame = ctk.CTkFrame(self.root)
        input_frame2 = ctk.CTkFrame(self.root)

        input_frame.pack(side="left", expand=True, padx=20, pady=20)

        prompt_label = ctk.CTkLabel(input_frame, text="NIDS-AI", fg_color="transparent", anchor='center', font=("Heivana", 20))
        prompt_label.grid(row=0, columnspan=2, pady=10)

        button_run = ctk.CTkButton(input_frame, text="Ejecutar", command=self.execute)
        button_run.grid(row=1, column=0, padx=10, pady=20)
        
        button_stop = ctk.CTkButton(input_frame, text="Parar", command=self.stop)
        button_stop.grid(row=1, column=1, padx=10, pady=20)

        input_frame2.pack(side="right", expand=True, padx=20, pady=20)
        self.scrollable_frame = ctk.CTkScrollableFrame(input_frame2, width=512, height=512, corner_radius=0, fg_color="transparent")
        self.scrollable_frame.pack(side="top", padx=20, pady=20, anchor="ne")

        self.button_toggle = ctk.CTkButton(self.root, image=self.sun, text="", command=self.toggle_bg, width=24, height=24)
        self.button_toggle.place(x=25, y=25)

        self.button_out = ctk.CTkButton(self.root, image=self.out, text="", command=self.close, width=24, height=24)
        self.button_out.place(x=25, y=512)
    
    def view_detection(self, data):
        if self.v_detection == True:
            w_detection = ctk.CTk()
            w_detection.title("NIDS-AI")
            w_detection.resizable(False, False)

            input_frame = ctk.CTkFrame(w_detection)
            input_frame.pack(expand=True, padx=20, pady=20)
            ctk.CTkButton(input_frame, text="Close", width=24, height=24)
            w_detection.mainloop()
            
    
    def close_view_detection(self):
        self.v_detection = False
    
    def execute(self):
        if not self.execute_bool:
            try:     
                ctk.CTkLabel(self.scrollable_frame, text="Comenzando la ejecucion...").pack(anchor="w")
            except:
                    pass
        self.execute_bool = True

    def stop(self):
        if self.execute_bool:
            try:     
                ctk.CTkLabel(self.scrollable_frame, text="Parando la ejecucion...").pack(anchor="w")
            except:
                pass
        self.execute_bool = False

    def toggle_bg(self):
        if self.current_mode == 0:
            ctk.set_appearance_mode("light")
            self.button_toggle.configure(image=self.moon)
            self.current_mode = 1
        else:
            ctk.set_appearance_mode("dark")
            self.button_toggle.configure(image=self.sun)
            self.current_mode = 0

    def close(self):
        self.root.destroy()

    def update_scrollable_frame(self, data):
        try:   
            row_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
            row_frame.pack(fill="x", padx=5, pady=5)

            # Crear y añadir el label al frame
            ctk.CTkLabel(row_frame, text=data).pack(side="left", anchor="w")

            # Crear y añadir el botón al frame
            ctk.CTkButton(row_frame, text="i", command=lambda d=data: self.info(d)).pack(side="left", padx=5)

            # self.previous_lines.add(data) 
            self.scrollable_frame.update_idletasks()  # Update the scrollable frame to reflect new changes
            self.scrollable_frame._parent_canvas.yview_moveto(1.0)  # Scroll to the bottom
        except:
            pass

    def info(self, data):
        self.v_detection=True
        self.view_detection(data)
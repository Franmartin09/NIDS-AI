import customtkinter as ctk
from PIL import Image, ImageTk
import json

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
        self.w_detection = ""
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
            self.w_detection = ctk.CTk()
            self.w_detection.title("NIDS-AI")
            self.w_detection.resizable(False, False)

            window_width = 512
            window_height = 512
            screen_width = self.w_detection.winfo_screenwidth()
            screen_height = self.w_detection.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            self.w_detection.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

            input_frame = ctk.CTkFrame(self.w_detection)
            input_frame.pack(side="top", expand=True, padx=20, pady=20)

            srcip_label = ctk.CTkLabel(input_frame, text="SOURCE IP", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=0, column=0, pady=10, padx=25)
            
            srcip_label = ctk.CTkLabel(input_frame, text="DESTINATION IP", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=0, column=1, pady=10, padx=25)

            srcip_label = ctk.CTkLabel(input_frame, text=f"{data['src_ip']}", fg_color="transparent", anchor='center', font=("Heivana", 15))
            srcip_label.grid(row=1, column=0, pady=10, padx=25)
            
            srcip_label = ctk.CTkLabel(input_frame, text=f"{data['dst_ip']}", fg_color="transparent", anchor='center', font=("Heivana", 15))
            srcip_label.grid(row=1, column=1, pady=10, padx=25)
            
            srcip_label = ctk.CTkLabel(input_frame, text="", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=2, column=0, pady=10, padx=25)

            srcip_label = ctk.CTkLabel(input_frame, text="SOURCE PORT", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=3, column=0, pady=10, padx=25)
            
            srcip_label = ctk.CTkLabel(input_frame, text="DESTINATION PORT", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=3, column=1, pady=10, padx=25)

            srcip_label = ctk.CTkLabel(input_frame, text=f"{data['src_port']}", fg_color="transparent", anchor='center', font=("Heivana", 15))
            srcip_label.grid(row=4, column=0, pady=10, padx=25)
            
            srcip_label = ctk.CTkLabel(input_frame, text=f"{data['dst_port']}", fg_color="transparent", anchor='center', font=("Heivana", 15))
            srcip_label.grid(row=4, column=1, pady=10, padx=25)

            srcip_label = ctk.CTkLabel(input_frame, text="", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=5, column=0, pady=10, padx=25)
            
            srcip_label = ctk.CTkLabel(input_frame, text="PROBABILITY", fg_color="transparent", anchor='center', font=("Heivana", 20))
            srcip_label.grid(row=6, columnspan=2, pady=10, padx=25)

            srcip_label = ctk.CTkLabel(input_frame, text=f"{data['prediction']} %", fg_color="transparent", anchor='center', font=("Heivana", 15))
            srcip_label.grid(row=7, columnspan=2, pady=10, padx=25)

            # Botón para cerrar la ventana
            ctk.CTkButton(input_frame, text="Close", width=40, height=30, command=self.close_view_detection).grid(row=9, columnspan=2, pady=30, padx=20)
            self.w_detection.mainloop()
            
    
    def close_view_detection(self):
        self.v_detection = False
        self.w_detection.destroy()
    
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

            if "error" not in data:
                texto=f"{data['ts']} - src_ip: {data['src_ip']} - Amb una probabilitat de : {data['prediction']}"
            else:
                texto=f"{data['error']}"

            row_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
            row_frame.pack(fill="x", padx=5, pady=5)
            ctk.CTkLabel(row_frame, text=texto).pack(side="left", anchor="w")

            # Crear y añadir el botón al frame
            if "error" not in data:
                ctk.CTkButton(row_frame, text="i", command=lambda d=data: self.info(d)).pack(side="left", padx=5)

            self.scrollable_frame.update_idletasks()  # Update the scrollable frame to reflect new changes
            self.scrollable_frame._parent_canvas.yview_moveto(1.0)  # Scroll to the bottom
        except:
            pass

    def info(self, data):
        self.v_detection=True
        self.view_detection(data)
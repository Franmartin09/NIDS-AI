#library imports
import customtkinter as ctk
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app.clase.visual.nids_ai_visual import NIDS_AI_Visual
from app.clase.read.readlog import ReadLog
from app.clase.modulo.model import Model

def main():
    root = ctk.CTk()
    #Model Class
    model = Model()
    #Visual Class
    app = NIDS_AI_Visual(root)
    #ReadLog Class
    read = ReadLog()
    
    read.read_log(app, model)
    root.mainloop()

if __name__ == "__main__":
    main()

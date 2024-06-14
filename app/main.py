import customtkinter as ctk
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from clase.visual.nids_ai_visual import NIDS_AI_Visual
from clase.read.readlog import ReadLog
from clase.modulo.model import Model

def install_requirements():
    #comadnos para requirements
    print("·")

def main():
    #VISUAL
    root = ctk.CTk()
    model = Model()
    app = NIDS_AI_Visual(root)
    read = ReadLog()
    
    # app.read_log()
    read.read_log(app, model)
    root.mainloop()

if __name__ == "__main__":
    # install_requirements()
    main()

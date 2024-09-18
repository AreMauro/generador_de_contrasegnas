from tkinter import Tk, Frame, Entry, Button, Label, END

from funciones import creadorDeContraseña

class vista():

    def __init__(self) -> None:
        self.raiz = Tk()

        self.raiz.title("Generador de contraseñas")

        self.raiz.resizable(1,1)

        self.raiz.geometry("900x600")

        self.raiz.iconbitmap("logo.ico")

        self.raiz.config(bg="#4379F2", highlightcolor="red", highlightthickness=5  )

        """
        El siguiente codigo se usa para centrar la pantalla principal a la pantalla del ordenador
        """

        self.raiz.update_idletasks()

        self.width = self.raiz.winfo_width()

        self. frm_width = self.raiz.winfo_rootx() - self.raiz.winfo_x()
        
        self.win_width = self.width + 2 * self.frm_width
        
        self.height = self.raiz.winfo_height()
        
        titlebar_height = self.raiz.winfo_rooty() - self.raiz.winfo_y()

        self.win_height = self.height + titlebar_height + self.frm_width
        
        self.x = self.raiz.winfo_screenwidth() // 2 - self.win_width // 2
        self.y = self.raiz.winfo_screenheight() // 2 - self.win_height // 2
        
        self.raiz.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        
        self.raiz.deiconify()

        self.frame = Frame(self.raiz)

        self.frame.config(bg ="#E5D9F2", highlightcolor="red", highlightthickness=10, 
                    width="600", height="600", relief="sunken", bd=20,
                    cursor="hand2")

        self.frame.place(relx=0.5, rely=0.5, anchor="center")


        self.label_principal = Label(self.frame,text="Bienvenido al generador de contraseñas",
                      fg="red", font=("Arial", 26 ))

        self.label_principal.pack(pady=20)

        self.label_principal.config(bg="black")

        self.entry_datos = Entry(self.frame, width=30, font=("Arial", 18))

        self.entry_datos.pack(pady=10)

        self.boton_generar = Button(self.frame, text="Generar Password", 
                                    command=self.creador_de_contraseña,
                                    font=("Arial", 18) )
        
        self.boton_generar.config(bg="#D91656")

        self.boton_generar.pack(pady=10)


    def creador_de_contraseña(self):

        password = creadorDeContraseña()

        self.entry_datos.delete(0, END)

        self.entry_datos.insert(0, password)

    
    def run(self):

        self.raiz.mainloop()



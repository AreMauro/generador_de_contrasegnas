from tkinter import Tk, Frame, Entry, Button, Label, END

from funciones import creadorDeContraseña

class vista():

    def __init__(self) -> None:
        self.raiz = Tk()

        self.raiz.resizable(1,1)

        self.raiz.geometry("700x600")

        self.raiz.iconbitmap("logo.ico")

        self.raiz.config(bg="#4379F2", highlightcolor="red", highlightthickness=5  )

        self.frame = Frame(self.raiz)

        self.frame.config(bg ="white", highlightcolor="red", highlightthickness=10, 
                    width="600", height="600", relief="sunken", bd=20,
                    cursor="hand2")

        self.frame.place(relx=0.5, rely=0.5, anchor="center")


        self.label_principal = Label(self.frame,text="Bienvenido al generador de contraseñas",
                      fg="red", font=("Arial", 26 ))

        self.label_principal.pack(pady=20)

        self.entry_datos = Entry(self.frame, width=30)

        self.entry_datos.pack(pady=10)

        self.boton_generar = Button(self.frame, text="Generar Password", 
                                    command=self.creador_de_contraseña,
                                    font=("Arial", 18) )

        self.boton_generar.pack(pady=10)


    def creador_de_contraseña(self):

        password = creadorDeContraseña()

        self.entry_datos.delete(0, END)

        self.entry_datos.insert(0, password)



    
    def run(self):

        self.raiz.mainloop()



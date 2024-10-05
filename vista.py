from tkinter import Tk, Frame, Entry, Button, Label, END, Checkbutton, BooleanVar, StringVar

from string import ascii_letters

from funciones import generadorDeContraseñas, generarPasswordConPalabras

class vista():

    def __init__(self) -> None:
        self.raiz = Tk()

        self.raiz.title("Generador de contraseñas")

        self.raiz.resizable(1,1)

        self.raiz.geometry("900x600")

#        self.raiz.iconbitmap("logo.ico")

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

        self.label_principal.grid(row=0, column=3)

        self.label_principal.config(bg="black")

        self.entry_datos = Entry(self.frame, width=30, font=("Arial", 18))

        self.entry_datos.grid(row=1, column=3)

        self.isMinuscula = BooleanVar()
        self.isMayuscula = BooleanVar()
        self.isNumber = BooleanVar()
        self.isSymbol = BooleanVar()
        self.hasSalt = BooleanVar()
        self.isEncripted = BooleanVar()

        self.CheckButton_minusculas = Checkbutton(self.frame, 
                                                  text="Minusculas", font=("Arial", 18),
                                                  justify= "center", offvalue=False, onvalue=True,
                                                  variable= self.isMinuscula
                                                  )

        self.CheckButton_minusculas.grid(row=2, column=0)

        self.CheckButton_mayusculas = Checkbutton(self.frame, text="Mayusculas", font=("Arial", 18),
                                                  justify= "center", offvalue=False, onvalue=True,
                                                  variable= self.isMayuscula)

        self.CheckButton_mayusculas.grid(row=2, column=1)

        self.CheckButton_Digitos = Checkbutton(self.frame, text="Numeros", font=("Arial", 18),
                                               justify= "center", offvalue=False, onvalue=True,
                                                  variable= self.isNumber)

        self.CheckButton_Digitos.grid(row=2, column=2)

        self.CheckButton_Simbolos = Checkbutton(self.frame, text="Caracteres especiales", 
                                                font=("Arial", 18),justify= "center", 
                                                offvalue=False, onvalue=True,
                                                  variable= self.isSymbol)

        self.CheckButton_Simbolos.grid(row=3, column=0)

        self.CheckButton_Salt = Checkbutton(self.frame, text="Con salting", font=("Arial", 18),
                                            justify= "center", offvalue=False, onvalue=True,
                                                  variable= self.hasSalt)

        self.CheckButton_Salt.grid(row=3, column=1)

        self.CheckButton_Encriptacion = Checkbutton(self.frame, text="Encriptada",
                                                     font=("Arial", 18), justify= "center", 
                                                     offvalue=False, onvalue=True,
                                                  variable= self.isEncripted)

        self.CheckButton_Encriptacion.grid(row=3, column=2)


        self.boton_generar = Button(self.frame, text="Generar Password", 
                                    command=self.creador_de_contraseña,
                                    font=("Arial", 18) )
        
        self.boton_generar.config(bg="#D91656")

        self.boton_generar.grid(row=5, column=3)

        self.boton_generarContraseñaconPalabras = Button(self.frame, text="Generar Password con palabras", 
                                    command=self.crearPanel,
                                    font=("Arial", 18) )
        
        self.boton_generarContraseñaconPalabras.config(bg="#D91656")

        self.boton_generarContraseñaconPalabras.grid(row=6, column=3)


    def creador_de_contraseña(self):


        password = generadorDeContraseñas(isLowercase=self.isMinuscula.get(),
                                          isUppercase=self.isMayuscula.get(),
                                          isSymbol=self.isSymbol.get(),
                                          isNumber=self.isNumber.get(),
                                          hasSalt=self.hasSalt.get(),
                                          isEncripted=self.isEncripted.get())

        self.entry_datos.delete(0, END)

        self.entry_datos.insert(0, password)

    def crearPanel(self):
        
        self.variablePrincipal = StringVar()

        self.frame.destroy()

        self.frame = Frame(self.raiz)

        self.frame.config(bg ="#E5D9F2", highlightcolor="red", highlightthickness=10, 
                    width="600", height="600", relief="sunken", bd=20,
                    cursor="hand2")

        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        principalLabel = Label(self.frame, 
                               text="Bienvenido al generador de contraseñas con palabras",
                                fg="red", font=("Arial", 22 ),
                                bg="black")

        principalLabel.grid(row=0, column=0)

        palabrasLabel = Label(self.frame, text="Ingrese las palabras que desea usar separadas por ','",
                                fg="red", font=("Arial", 18),
                                bg="black")

        palabrasLabel.grid(row=1, column=0)

        vcmd = (self.raiz.register(self.validate), '%P')

        self.entryPalabras = Entry(self.frame, width=30, font=("Arial", 18),
                              validate="key", validatecommand=vcmd,
                              textvariable=self.variablePrincipal)
        
        self.entryPalabras.bind('<KeyPress>', self.keyPress)

        self.entryPalabras.focus()

        self.entryPalabras.grid(row=1, column=2)

        buttonGenerarContraseña = Button(self.frame, text="Generar Contraseña",
                                         command=self.obtenerPasswordConLetras,
                                         font=("Arial", 18), bg="#D91656")
        
        buttonGenerarContraseña.grid(row=2, column=2)

        buttonLimpiarConssola = Button(self.frame, text="limpiar consola",
                                         command=self.limpiarConsola,
                                         font=("Arial", 18), bg="#D91656")
        
        buttonLimpiarConssola.grid(row=3, column=2)



    def keyPress(self, event):
        if event.char in ascii_letters:
            return event.char
        elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace', 'Return', 'comma'):
            print (event.keysym)
            return 'break'

    def validate(self, P):
        
        if len(P) <=25:
            return True

        else:
            # Anything else, reject it
            return False

    def limpiarConsola(self):
        
        self.entryPalabras.delete(0,END)
        

    def obtenerPasswordConLetras(self):

        passwordGenerada = generarPasswordConPalabras(self.variablePrincipal.get())
        self.entryPalabras.delete(0,END)
        self.entryPalabras.insert(0, passwordGenerada)


    def run(self):

        self.raiz.mainloop()



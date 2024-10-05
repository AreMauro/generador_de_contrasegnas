from secrets import SystemRandom
from string import ascii_letters, digits, punctuation, ascii_lowercase, ascii_uppercase
from hashlib import sha256

def longitudAleatoria() -> int:

    numeroAleatorio = SystemRandom()

    return numeroAleatorio.choice(range(15,20))

def creadorDeContraseña(abecedario: str) -> str:

    longitud = longitudAleatoria()

    password = ""

    i = 0

    while i <= longitud:

        i += 1

        eleccion = SystemRandom().choice([char for char in abecedario])

        password += eleccion

    return password


def generadordeSalt() ->str:

    salt = ""

    i = 0

    while i <= 3:

        i += 1

        eleccion = SystemRandom().choice([char for char in ascii_letters + digits + punctuation])

        if(i <= 3):

            salt += eleccion

       
    return salt

def encriptadorDeContraseñas (contrasegna : str) -> str:

    passwordEncriptada = sha256(contrasegna.encode(encoding="UTF-8"))

    return passwordEncriptada.hexdigest()


def generadorDeContraseñas(isNumber: bool = False,
                           isUppercase: bool = False,
                           isSymbol: bool = False,
                           isLowercase: bool = True,
                           hasSalt: bool = False, 
                           isEncripted: bool = False
                           ) -> str:

    if(isEncripted == False):

        #Sin encriptacion
        if(hasSalt == False):

            #Sin sal

            if (isSymbol == False):

                #No hay simbbolos

                #Solo letras minusculas
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return creadorDeContraseña(ascii_lowercase)

                #Solo numeros    
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return creadorDeContraseña(digits)
                
                #Solo letras mayusculas
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase)
                
                #Numeros y mayusculas
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase + digits)
                
                #Numeros y minusculas
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_lowercase + digits)
                
                #Minusculas y mayusculas
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_letters)

                #Letras Mayusculas, numeros y letras minusculas
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(digits + ascii_letters)

                #Todo desactivado:

                if((isNumber == False) and (isUppercase == False) and (isLowercase == False) ):

                    return "Seleccione un checkbutton"


            else: 

                #Todos llevan simbolos

                #Solo letras minusculas y simbolos
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return creadorDeContraseña(ascii_lowercase + punctuation)

                #Solo numeros  y simbolos
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return creadorDeContraseña(digits + punctuation)
                
                #Solo letras mayusculas  y simbolos
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase + punctuation)
                
                #Solo simbolos
                if((isNumber == False) and (isUppercase == False) and (isLowercase == False) ):

                    return creadorDeContraseña(punctuation)

                #Numeros y mayusculas  y simbolos
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase + digits + punctuation)
                
                #Numeros y minusculas y simbolos
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_lowercase + digits + punctuation)
                
                #Minusculas y mayusculas  y simbolos
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_letters + punctuation)

                #Letras Mayusculas, numeros y letras minusculas  y simbolos
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(digits + ascii_letters +  punctuation)

        
        else: 

            #Aqui lleva sal
            
            if (isSymbol == False):

                #No hay simbbolos

                #Solo letras minusculas + sal
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return creadorDeContraseña(ascii_lowercase) + generadordeSalt()

                #Solo numeros + sal
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return creadorDeContraseña(digits) + generadordeSalt()
                
                #Solo letras mayusculas + sal
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase)+ generadordeSalt()
                
                #Numeros y mayusculas + sal
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase + digits) + generadordeSalt()
                
                #Numeros y minusculas + sal
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_lowercase + digits) + generadordeSalt()
                
                #Minusculas y mayusculas + sal
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_letters)+ generadordeSalt()

                #Letras Mayusculas, numeros y letras minusculas + sal
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(digits + ascii_letters)+ generadordeSalt()

            else: 

                #Aqui tambien hay sal

                #Todos llevan simbolos

                #Solo letras minusculas y simbolos + sal
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return creadorDeContraseña(ascii_lowercase + punctuation) + generadordeSalt()

                #Solo numeros  y simbolos + sal
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return creadorDeContraseña(digits + punctuation) + generadordeSalt()
                
                #Solo letras mayusculas  y simbolos + sal
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase + punctuation) + generadordeSalt()
                
                #Solo simbolos + sal
                if((isNumber == False) and (isUppercase == False) and (isLowercase == False) ):

                    return creadorDeContraseña(punctuation) + generadordeSalt()

                #Numeros y mayusculas  y simbolos + sal
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return creadorDeContraseña(ascii_uppercase + digits + punctuation) + generadordeSalt()
                
                #Numeros y minusculas y simbolos + sal
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_lowercase + digits + punctuation) + generadordeSalt()
                
                #Minusculas y mayusculas  y simbolos + sal
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(ascii_letters + punctuation) + generadordeSalt()

                #Letras Mayusculas, numeros y letras minusculas  y simbolos+ sal
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return creadorDeContraseña(digits + ascii_letters +  punctuation)+ generadordeSalt()
        
    else:

        #Con encriptacion

        if(hasSalt == False):
            #Encriptado y sin sal
            if (isSymbol == False):

                #No hay simbolos 

                #Solo letras minusculas + encriptacion
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return encriptadorDeContraseñas (creadorDeContraseña(ascii_lowercase))

                #Solo numeros  + encriptacion
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return encriptadorDeContraseñas (creadorDeContraseña(digits))
                
                #Solo letras mayusculas + encriptacion
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return encriptadorDeContraseñas (creadorDeContraseña(ascii_uppercase))
                
                #Numeros y mayusculas + encriptacion
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return encriptadorDeContraseñas (creadorDeContraseña(ascii_uppercase + digits))
                
                #Numeros y minusculas + encriptacion
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return encriptadorDeContraseñas ( creadorDeContraseña(ascii_lowercase + digits))
                
                #Minusculas y mayusculas + encriptacion
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return encriptadorDeContraseñas (creadorDeContraseña(ascii_letters))

                #Letras Mayusculas, numeros y letras minusculas + encriptacion
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return encriptadorDeContraseñas (creadorDeContraseña(digits + ascii_letters))

            else: 

                #Todos llevan simbolos

                #Solo letras minusculas y simbolos + encriptacion
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return encriptadorDeContraseñas (creadorDeContraseña(
                                            ascii_lowercase + punctuation))

                #Solo numeros  y simbolos + encriptacion
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return encriptadorDeContraseñas (
                                creadorDeContraseña(digits + punctuation))
                
                #Solo letras mayusculas  y simbolos + encriptacion
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return encriptadorDeContraseñas (
                            creadorDeContraseña(ascii_uppercase + punctuation))
                
                #Solo simbolos + encriptacion
                if((isNumber == False) and (isUppercase == False) and (isLowercase == False) ):

                    return encriptadorDeContraseñas (creadorDeContraseña(punctuation))

                #Numeros y mayusculas  y simbolos + encriptacion
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_uppercase + digits + punctuation))
                
                #Numeros y minusculas y simbolos + encriptacion
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return encriptadorDeContraseñas (
                            creadorDeContraseña(ascii_lowercase + digits + punctuation)
                    )
                #Minusculas y mayusculas  y simbolos + encriptacion
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_letters + punctuation))

                #Letras Mayusculas, numeros y letras minusculas  y simbolos + encriptacion
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(digits + ascii_letters +  punctuation))

        
        else: 
            
            if (isSymbol == False):


                #Aqui hay sal
                #No hay simbbolos

                #Solo letras minusculas + sal + encriptado
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_lowercase) + generadordeSalt())

                #Solo numeros + sal + encriptado
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(digits) + generadordeSalt())
                
                #Solo letras mayusculas + sal + encriptado
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_uppercase)+ generadordeSalt()
                    )
                
                #Numeros y mayusculas + sal + encriptado
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_uppercase + digits) + generadordeSalt()
                    )
                #Numeros y minusculas + sal + encriptado
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_lowercase + digits) + generadordeSalt()
                    )
                
                #Minusculas y mayusculas + sal + encriptado
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_letters)+ generadordeSalt())

                #Letras Mayusculas, numeros y letras minusculas + sal + encriptado
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(digits + ascii_letters)+ generadordeSalt()
                    )
            else: 

                #Todos llevan simbolos

                #Solo letras minusculas y simbolos + sal + encriptado
                if((isNumber == False) and (isUppercase == False) and (isLowercase == True)):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_lowercase + punctuation) + generadordeSalt()
                    )
                #Solo numeros  y simbolos + sal + encriptado
                if((isNumber == True) and (isUppercase == False) and (isLowercase == False)):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(digits + punctuation) + generadordeSalt()
                    )
                
                #Solo letras mayusculas  y simbolos + sal + encriptado
                if((isNumber == False) and (isUppercase == True) and (isLowercase == False) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_uppercase + punctuation) + generadordeSalt()
                    )
                #Solo simbolos + sal + encriptado
                if((isNumber == False) and (isUppercase == False) and (isLowercase == False) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(punctuation) + generadordeSalt()
                    )
                
                #Numeros y mayusculas  y simbolos + sal + encriptado
                if((isNumber == True) and (isUppercase == True) and (isLowercase == False) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_uppercase + digits + punctuation) + generadordeSalt()
                    )
                #Numeros y minusculas y simbolos + sal + encriptado
                if((isNumber == True) and (isUppercase == False) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_lowercase + digits + punctuation) + generadordeSalt()
                    )
                
                #Minusculas y mayusculas  y simbolos + sal + encriptado
                if((isNumber == False) and (isUppercase == True) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(ascii_letters + punctuation) + generadordeSalt()
                    )
                #Letras Mayusculas, numeros y letras minusculas  y simbolos+ sal + encriptado
                if((isNumber == True) and (isUppercase == True) and (isLowercase == True) ):

                    return  encriptadorDeContraseñas (
                        creadorDeContraseña(digits + ascii_letters +  punctuation)+ generadordeSalt()
                    )

def generarPasswordConPalabras(palabras: str):

    listaDePalabras = palabras.split(",")

    print(listaDePalabras)

    password = ""

    passwordValida = False

    indices = []

    vuelta = 0

    while passwordValida == False:

        indice = SystemRandom().randint(0, len(listaDePalabras) - 1)

        print(indice)

        if (indice not in indices and indice != 0):

            #Cualquier numero puede ser generado excepto el 0

            palabra = listaDePalabras[indice]

            password += palabra

            password += generadordeSalt()

            indices.append(indice)

            vuelta += 1

            print(f"vuelta: {vuelta}")

        if((indice == 0) and 0 not in indices):

            #Se obtiene el indice 0 por primera vez

            palabra = listaDePalabras[0]

            password += palabra

            password += generadordeSalt()

            indices.append(0)

            vuelta += 1

            print(f"vuelta: {vuelta}")


        if((indice == 0) and (0 in indices) and len(indices) == 2):

            #Se acabaron los indices (palabras) y el generador solo crea 0s

            vuelta += 1

            print(f"vuelta: {vuelta}")

            passwordValida = True


        if(len(password) >= 16 and len(password) <= 25): passwordValida = True    

    cambios = 0
    
    while cambios <= 10:

        letra = SystemRandom().choice(password)

        if(letra.isalpha()):

            nuevaLetra = letra.upper()

            password = password.replace(letra,nuevaLetra, 1)

            cambios += 1
    
    return password





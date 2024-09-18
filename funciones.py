from secrets import SystemRandom
from string import ascii_letters, digits, punctuation 

def longitudAleatoria() -> int:

    numeroAleatorio = SystemRandom()

    return numeroAleatorio.choice(range(15,20))

def creadorDeContraseña() -> str:

    longitud = longitudAleatoria()

    abecedario = ascii_letters + digits + punctuation

    password = ""

    i = 0

    while i <= longitud:

        eleccion = SystemRandom().choice([char for char in abecedario])

        password += eleccion

        i += 1
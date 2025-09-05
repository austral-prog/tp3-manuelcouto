def check_vowels():
   
    nombre = input("Ingresa tu nombre: ")
    nombre = nombre.lower()

    tiene_a = "a" in nombre
    tiene_e = "e" in nombre
    tiene_i = "i" in nombre
    tiene_o = "o" in nombre
    tiene_u = "u" in nombre

    print("Contiene a:", tiene_a)
    print("Contiene e:", tiene_e)
    print("Contiene i:", tiene_i)
    print("Contiene o:", tiene_o)
    print("Contiene u:", tiene_u)

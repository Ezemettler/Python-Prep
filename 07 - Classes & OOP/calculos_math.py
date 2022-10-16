class calculos_math():      #Creacion de la clase
    def __init__(self):     #Creacion del constructor, da estado inicial a los objetos de una clase.
        pass                    #Propiedades iniciales de la clase.

#---------------------------------------------------------------------
    def verificar_primo(self, parametro):
        lista_nros_primos = []
    
        for i in range (0, len(parametro)):
        #Iteramos los elementos del parametro.

            cont_divisibles = 0

            for n in range (2, parametro[i]-1):
            #Comparamos si existen divisibles dentro del rango 2 a parametro-1
                if parametro[i] % n == 0:
                    cont_divisibles += 1
                
            if cont_divisibles == 0:
                lista_nros_primos.append(parametro[i])

        print("Los numeros primos de la lista son:", lista_nros_primos)


#---------------------------------------------------------------------    
    def valor_modal(self, lista, orden):  
        numero = 0
        repeticiones = 0
    
        for i in lista:
            repeticiones_nuevas = 0

            for n in lista:
                if i == n:
                    repeticiones_nuevas += 1

            if repeticiones_nuevas > repeticiones:
                repeticiones = repeticiones_nuevas
                numero = i

            elif repeticiones_nuevas == repeticiones:
                repeticiones = repeticiones_nuevas
                
                if orden == 'Menor':
                    minimo = min(numero, i)
                    numero = minimo
                elif orden == 'Mayor':
                    maximo = max(numero, i)
                    numero = maximo
                else:
                    continue

            else:
                continue   

        print("El numero", numero, "fue el más repetido de la lista. Se repitió", repeticiones, "veces.")

#---------------------------------------------------------------------
    def conversion_grados(self, valor, origen, destino):
        global resultado
    
        def c_a_f(valor):
            resultado = round((valor * 9/5) + 32, 2)
            print(valor, "°Celsius son", resultado, "°Farenheit")

        def c_a_k(valor):
            resultado = round(valor + 273.15, 2)
            print(valor, "°Celsius son", resultado, "°Kelvin")

        def f_a_c(valor):
            resultado = round((valor * (5/9)) - (160/9), 2)
            print(valor, "°Farenheit son", resultado, "°Celsius")

        def f_a_k(valor):
            resultado = round((valor * (5/9)) + 255.37, 2)
            print(valor, "°Farenheit son", resultado, "°Kelvin")

        def k_a_c(valor):
            resultado = round(valor - 273.15, 2)
            print(valor, "°Kelvin son", resultado, "°Celsius")

        def k_a_f(valor):
            resultado = round((valor * (9/5)) - 459.67, 2)
            print(valor, "°Kelvin son", resultado, "°Farenheit")
    
        if origen == 'C':
            if destino == 'F':
                c_a_f(valor)
            elif destino == 'K':
                c_a_k(valor)
            else:
                print("Destino incorrecto.")

        elif origen == 'F':
            if destino == 'C':
                f_a_c(valor)
            elif destino == 'K':
                f_a_k(valor)
            else:
                print("Destino incorrecto.")
    
        elif origen == 'K':
            if destino == 'C':
                k_a_c(valor)
            elif destino == 'F':
                k_a_f(valor)
            else:
                print("Destino incorrecto.")

        else:
            print("Origen incorrecto.")

#---------------------------------------------------------------------
    def factorial(self, numero):
        if type(numero) != int:
            return "Error. Por favor, ingrese un número entero."
        elif numero <= 0:
            return "Error. Por favor, ingrese un número positivo."
        else:
            resultado = 1
        
            for i in range (1, numero+1):
                resultado = resultado * i
        
        print("El factorial del numero", numero, "es igual a", resultado)
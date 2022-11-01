#Biblitecas
import math as math
import numpy as np
import streamlit as st

#Funcoes
def angulo_cosseno(x,y,z):
	cosseno = ((x*x)-(y*y)-(z*z))/-(2*x*y)
	angulo2 = np.degrees(math.acos(cosseno))
	angulo3 = math.acos(cosseno)
	st.write("O ângulo é(Em graus): ", angulo2)
	st.write("O ângulo é(Em Radianos): ", angulo3)
	
#Aparencia do Site
st.title("Cosseno")
st.info("Esse é um aplicativo que calcula o ângulo do cosseno.")

#Variaveis
a = st.number_input("Lado oposto ao ângulo: ")
b = st.number_input("Lado 2: ")
c = st.number_input("Lado 3: ")

if st.button("Calcular Cosseno"):
	angulo_cosseno(a, b, c)
	st.success("Achou o ângulo! Parabéns!")

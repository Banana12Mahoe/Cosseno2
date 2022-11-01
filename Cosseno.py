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

def angulo_seno(A, B, C):
	seno = (A * math.sin(B))/math.sin(C)
	seno2 = np.degrees(math.asin(seno))
	st.write("O ângulo é(Em graus): ", seno2)
	
	
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

st.title("Seno")
st.info("Esse é um aplicativo que calcula o ângulo do seno.")

d = st.number_input("Lado A: ")
e = st.number_input("Ângulo b: ")
f = st.number_input("Ângulo a: ")

if st.button("Calcular Seno"):
	angulo_seno(d, e, f)

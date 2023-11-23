import datetime 
import time
import pandas as pd
import streamlit as st
from PIL import Image

@st.cache
def run_fxn(n: int) -> list:
    return range(n)

"""Generación de la webapp con streamlit"""
# Definir titulo
st.title("Titulo: Analitica de Datos")
#Definir Header/SubHeader
st.header('Este es un header')
st.subheader("Este es un subheader")
#Definir en texto
st.text("Texto: Hola Streamlit")
#Definición de MarkDown
st.markdown("Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")
st.header("Colores de texto y mensajes de error")
st.success("Successful")
st.info("Información!")
st.warning("warning")
st.error("Error")
st.exception("NameError(no está definido)")
st.header("Obtener información de ayuda de Python")
st.help(range)
st.header("Widgets:")
st.subheader("Checkbox")

if st.checkbox("Show/Hide"):
    st.text("Mostrar u ocultar Widget")
    st.subheader("Radio buttons")

status = st.radio("Cual es su estatus", ("Activo", "Inactivo"))

if status == "Activo":
    st.success("Estás activo")
else: 
    st.warning("Inactivo")
    st.subheader("SelectBox")

occupation = st.selectbox(
    "Tu ocupación", ["Programador", "Científico de datos", "BI", "Ingeniero de Datos"]
)

st.write("Opción seleccionada:", occupation)
st.subheader("MultiSelect")

location = st.multiselect(
    "Donde trabajas?",
    ("México", "New York", "Guadalajara", "Monterrey", "Nepal", "Buenos Aires", "Caracas"),
)

st.write("Seleccionó:", len(location), "locaciones")
st.subheader("Slider")

level = st.slider("Cual es tu nivel?", 1, 5)
st.write("Nivel:", level)


st.subheader("Buttons")
#Buttons
if st.button("Acerca"):
    st.text("streamlit es cool")
else:
    st.text("")
st.header("Como recibir una entrada y procesarla con streamlit?")
st.subheader("Recibiendo texto")
#Recibiendo texto 
firstname= st.text_input("Escriba su nombre:")
if st.button("Aceptar"):
    result = firtname.title()
    st.success(result)
st.subheader("Area de texto")
#text Area 
message = st.text_area("Escriba un mensaje")
if st.button("Aceptar"):
    result = message.title()
    st.success(result)
st.subheader("Entrada de fecha:")
#Date input 
today = st.date_input("Hoy es", datetime.datetime.now())
st.text(f"{today}")
st.subheader("Entrada de tiempo")
#time 
the_time
the_time = st.time_input("La hora es:", datetime.time())
st.text(f"{the_time}")    
st.header("Trabajar con archivos de imagenes, audio o videos")
#images 
st.subheader("Archivo de imagen")
img = Image.open("")
st.image(img,width=300, caption="Simple Imagen")

st.header("Otras opciones que permite la función write")
#Writing text/super fxn 
st.subheader("texto con write")
st.write("Texto con write")
st.write(range(10))
st.header("Desplegando código puro y json")
st.subheader("codigo puro")
st.code("import numpy as np")
with st.echo():
    df=pd.DataFrame()
st.subheader("Desplegando json")
st.text("Mostrando JSON")
st.json({"nombre": "Jhon","apellido": "Doe", "genero": "masculino"})
st.header("Mostrar barra de progreso, spinner y ballons")
st.subheader("Barra de progreso")
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)
st.subheader("spinner")

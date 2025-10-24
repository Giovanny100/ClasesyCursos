import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ===============================
# CONFIGURACIÓN GENERAL
# ===============================
st.set_page_config(page_title="CATIA Learn Lab - Estudio de Mercado", page_icon="🎓", layout="centered")

st.title("📊 PLAN DE ESTUDIO DE MERCADO – CATIA LEARN LAB")
st.markdown("""
Este estudio busca conocer las preferencias y necesidades de los estudiantes para mejorar los servicios educativos de **Catia Learn Lab**.  
Tu participación es totalmente anónima y ayudará a crear cursos más útiles y divertidos.  
🎯 **Prioridad:** Publicidad en lona y volantes impresos.
""")

st.divider()

# ===============================
# FORMULARIO
# ===============================
with st.form("catia_form"):

    st.subheader("🧠 Datos generales")
    semestre = st.radio("¿En qué semestre estás?", ["1°", "2°", "3°", "4°", "5°", "6°"])
    genero = st.radio("¿Eres hombre, mujer o prefieres no decirlo?", ["Hombre", "Mujer", "Prefiero no decirlo"])
    turno = st.radio("¿En qué turno estudias?", ["Mañana", "Vespertino"])

    st.subheader("📚 Dificultades académicas")
    materias = st.multiselect(
        "¿Qué materias se te dificultan más?",
        ["Matemáticas / Física", "Química / Biología", "Historia / Sociales", "Artísticas", "Otro"],
    )

    razones = st.multiselect(
        "¿Por qué razones crees que tú o algún amig@ reprueban las materias?",
        ["Los profes no explican bien", "Son aburridas las clases", "Los alumnos no estudian", "La escuela no importa"],
    )

    st.subheader("💡 Comportamiento y preferencias")
    pasar = st.radio(
        "¿Para pasar una materia cuál de las siguientes opciones prefieres?",
        ["Estudiar mucho", "Pagar un curso extra", "Que resuelvan el examen por mí", "Ninguna de las anteriores"],
    )

    pagarias = st.radio(
        "¿Pagarías por que te hagan un examen o rúbrica para pasar una materia aburrida?",
        ["Sí", "No", "Depende del precio"],
    )

    curso = st.multiselect(
        "¿De cuál de los siguientes temas tomarías un curso?",
        ["Programación de videojuegos", "Trucos y secretos de la IA", "Diseño y Marketing", "Inversiones y manejo de dinero", "Otra"],
    )

    profesor = st.radio(
        "Prefieres que te dé clases:",
        ["Hombre", "Mujer", "Un personaje animado en videos", "Me da lo mismo mientras aprenda"],
    )

    pago = st.radio(
        "¿Cuánto te parece justo pagar por ayuda para pasar una materia difícil?",
        ["Menos de $200", "$200–$400", "$400–$600", "Más de $600"],
    )

    confianza = st.multiselect(
        "¿Qué te haría confiar en una escuela o persona que ofrece ese tipo de ayuda?",
        ["Recomendaciones de amigos", "Ver resultados o reseñas", "Que tenga un personaje animado que explique", "Que ofrezcan prueba gratuita"],
    )

    red = st.radio(
        "¿En qué red social pasas más tiempo?",
        ["TikTok", "Instagram", "WhatsApp", "YouTube", "Facebook"],
    )

    enviado = st.form_submit_button("🚀 Enviar respuestas")

# ===============================
# GUARDADO DE DATOS
# ===============================
if enviado:
    # Crear carpeta y archivo si no existen
    filename = "respuestas_catia.csv"
    existe = os.path.isfile(filename)

    # Crear registro de respuesta
    data = {
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "semestre": [semestre],
        "genero": [genero],
        "turno": [turno],
        "materias_dificiles": [", ".join(materias)],
        "razones_reprobacion": [", ".join(razones)],
        "preferencia_pasar": [pasar],
        "pagarias_rubrica": [pagarias],
        "curso_interes": [", ".join(curso)],
        "tipo_profesor": [profesor],
        "pago_justo": [pago],
        "confianza_en_ayuda": [", ".join(confianza)],
        "red_social": [red],
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, mode="a", header=not existe, index=False, encoding="utf-8-sig")

    # ===============================
    # ANIMACIÓN DE AGRADECIMIENTO
    # ===============================
    st.success("✅ ¡Gracias por participar en el estudio de mercado de CATIA Learn Lab!")
    st.balloons()
    st.toast("Tus respuestas han sido registradas correctamente 🎉")


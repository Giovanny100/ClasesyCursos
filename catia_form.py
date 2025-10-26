import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title="Encuesta Educativa",
    page_icon="📚",
    layout="centered"
)

# =========================
# ESTILOS PERSONALIZADOS
# =========================
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #fddde6, #d4f9f4);
            font-family: 'Poppins', sans-serif;
            color: #333;
        }
        .main {
            background-color: white;
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 {
            color: #ff69b4;
            text-align: center;
            font-weight: 700;
        }
        h3 {
            color: #009688;
            margin-top: 30px;
        }
        .stButton>button {
            background-color: #ff69b4;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.7rem 1.2rem;
            font-size: 1rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #009688;
            color: white;
            transform: scale(1.05);
        }
        .success {
            text-align: center;
            font-size: 1.1rem;
            color: #009688;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.markdown("<h1>📚 Encuesta Educativa</h1>", unsafe_allow_html=True)
st.markdown("Queremos conocer más sobre tus hábitos de estudio y tus preferencias académicas. Tu opinión es importante para mejorar los recursos educativos disponibles.")

# =========================
# FORMULARIO
# =========================
with st.form("encuesta_form"):
    st.markdown("<h3>Datos generales</h3>", unsafe_allow_html=True)
    semestre = st.selectbox("¿En qué semestre estás?", ["1°", "2°", "3°", "4°", "5°", "6°"])
    genero = st.radio("¿Eres hombre, mujer o prefieres no decirlo?", ["Hombre", "Mujer", "Prefiero no decirlo"])
    turno = st.radio("¿En qué turno estudias?", ["Mañana", "Vespertino"])

    st.markdown("<h3>Sobre tus materias</h3>", unsafe_allow_html=True)
    materias_dificiles = st.selectbox(
        "¿Qué materias se te dificultan más?",
        ["Matemáticas / Física", "Química / Biología", "Historia / Sociales", "Artísticas", "Otro"]
    )
    razon_reprobacion = st.radio(
        "¿Por qué razones crees que tú o algún amig@ reprueban las materias?",
        ["Los profes no explican bien", "Son aburridas las clases", "Los alumnos no estudian", "La escuela no importa"]
    )

    st.markdown("<h3>Preferencias de aprendizaje</h3>", unsafe_allow_html=True)
    metodo_estudio = st.radio(
        "¿Para pasar una materia cuál de las siguientes opciones prefieres?",
        ["Estudiar mucho", "Pagar un curso extra", "Que resuelvan el examen por mí", "Ninguna de las anteriores"]
    )
    pagaria = st.radio(
        "¿Pagarías por que te hagan un examen o rúbrica para pasar una materia aburrida?",
        ["Sí", "No", "Depende del precio"]
    )

    curso_interes = st.selectbox(
        "¿De cuál de los siguientes temas tomarías un curso?",
        ["Programación de videojuegos", "Trucos y secretos de la IA", "Diseño y Marketing", "Inversiones y manejo de dinero", "Otro"]
    )
    preferencia_profesor = st.radio(
        "Prefieres que te dé clases:",
        ["Hombre", "Mujer", "Un personaje animado en videos", "Me da lo mismo mientras aprenda"]
    )

    pago_justo = st.radio(
        "¿Cuánto te parece justo pagar por ayuda para pasar una materia difícil?",
        ["Menos de $200", "$200–$400", "$400–$600", "Más de $600"]
    )

    confianza = st.multiselect(
        "¿Qué te haría confiar en una escuela o persona que ofrece ese tipo de ayuda?",
        ["Recomendaciones de amigos", "Ver resultados o reseñas", "Que tenga un personaje animado que explique", "Que ofrezcan prueba gratuita"]
    )

    red_social = st.selectbox(
        "¿En qué red social pasas más tiempo?",
        ["TikTok", "Instagram", "WhatsApp", "YouTube", "Facebook"]
    )

    submit = st.form_submit_button("Enviar respuestas 📤")

# =========================
# GUARDADO EN CSV
# =========================
if submit:
    df = pd.DataFrame([{
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Semestre": semestre,
        "Género": genero,
        "Turno": turno,
        "Materias difíciles": materias_dificiles,
        "Razón reprobación": razon_reprobacion,
        "Método de estudio": metodo_estudio,
        "Pagaria": pagaria,
        "Curso interés": curso_interes,
        "Preferencia profesor": preferencia_profesor,
        "Pago justo": pago_justo,
        "Confianza": ", ".join(confianza),
        "Red social": red_social
    }])

    try:
        prev = pd.read_csv("respuestas.csv")
        df = pd.concat([prev, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv("respuestas.csv", index=False)
    st.markdown("<p class='success'>✅ ¡Gracias por participar! Tus respuestas fueron registradas correctamente.</p>", unsafe_allow_html=True)
    st.balloons()

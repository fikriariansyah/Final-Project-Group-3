import streamlit as st
import math
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import base64

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(
    page_title="Math Web App",
    page_icon="🧮",
    layout="wide"
)

# ============================
# LANGUAGE SELECTOR (NEW)
# ============================
language = st.sidebar.selectbox(
    "Language / Bahasa",
    ["English", "Indonesia"]
)

TEXT = {
    "English": {
        "navigate": "Navigate",
        "group": "Group Members",
        "function": "Function Tools",
        "optimization": "Optimization Solver",
        "story": "Story-Based Calculation",
        "enter_func": "Enter a function of x:",
        "derivative": "Derivative",
        "invalid_func": "Invalid function input.",
        "variable": "Variable(s)",
        "function_label": "Function",
        "opt_type": "Optimization Type",
        "maximize": "Maximize",
        "minimize": "Minimize",
        "category": "Select category:",
        "shape": "Select shape:",
        "area": "Area",
        "perimeter": "Perimeter",
        "volume": "Volume",
        "profit": "Profit",
        "price": "Price per unit",
        "cost": "Cost per unit",
        "fixed": "Fixed cost",
        "max_profit": "Maximum profit occurs at"
    },
    "Indonesia": {
        "navigate": "Navigasi",
        "group": "Anggota Kelompok",
        "function": "Alat Fungsi",
        "optimization": "Penyelesai Optimasi",
        "story": "Perhitungan Berbasis Cerita",
        "enter_func": "Masukkan fungsi dalam x:",
        "derivative": "Turunan",
        "invalid_func": "Input fungsi tidak valid.",
        "variable": "Variabel",
        "function_label": "Fungsi",
        "opt_type": "Jenis Optimasi",
        "maximize": "Maksimum",
        "minimize": "Minimum",
        "category": "Pilih kategori:",
        "shape": "Pilih bangun:",
        "area": "Luas",
        "perimeter": "Keliling",
        "volume": "Volume",
        "profit": "Keuntungan",
        "price": "Harga per unit",
        "cost": "Biaya per unit",
        "fixed": "Biaya tetap",
        "max_profit": "Keuntungan maksimum terjadi pada"
    }
}

SHAPES = {
    "English": {
        "Rectangle": "Rectangle",
        "Triangle": "Triangle",
        "Trapezoid": "Trapezoid",
        "Circle": "Circle",
        "Cuboid": "Cuboid",
        "Cylinder": "Cylinder",
        "Triangular Prism": "Triangular Prism",
        "Triangular Pyramid": "Triangular Pyramid"
    },
    "Indonesia": {
        "Rectangle": "Persegi Panjang",
        "Triangle": "Segitiga",
        "Trapezoid": "Trapesium",
        "Circle": "Lingkaran",
        "Cuboid": "Balok",
        "Cylinder": "Tabung",
        "Triangular Prism": "Prisma Segitiga",
        "Triangular Pyramid": "Limas Segitiga"
    }
}

t = TEXT[language]
shape_lang = SHAPES[language]

# ============================
# IMAGE TO BASE64 (ORIGINAL)
# ============================
def img_to_base64(filepath):
    try:
        with open(filepath, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# ============================
# CSS (ORIGINAL CARD)
# ============================
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 30px;
}
.member-card {
    background: linear-gradient(135deg, #002060, #C00000);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    text-align: center;
    border: 3px solid white;
    width: 280px;
    height: 380px;
    margin: auto;
    color: white;
}
.member-photo {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    border: 3px solid white;
    margin-bottom: 15px;
}
.member-name {
    font-size: 22px;
    font-weight: bold;
    color: #FFD700;
}
.member-role {
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR NAV (ORIGINAL + BILINGUAL)
# ============================
page = st.sidebar.radio(
    t["navigate"],
    [t["group"], t["function"], t["optimization"], t["story"]]
)

# ============================
# PAGE 1: GROUP MEMBERS (CARD RESTORED)
# ============================
if page == t["group"]:
    st.markdown(f"<div class='title'>{t['group']}</div>", unsafe_allow_html=True)

    members = [
        {
            "name": "Pardi Ihsan",
            "role": {
                "English": "Leader / Brainstorming and Project Execution",
                "Indonesia": "Ketua / Brainstorming dan Pelaksanaan Proyek"
            },
            "photo": "Pardi.jpeg"
        },
        {
            "name": "Fikri Ariansyah",
            "role": {
                "English": "Member / Brainstorming and Project Execution",
                "Indonesia": "Anggota / Brainstorming dan Pelaksanaan Proyek"
            },
            "photo": "Fikri.jpeg"
        },
        {
            "name": "Muhammad Adam Asyrofi",
            "role": {
                "English": "Member / Brainstorming and Project Execution",
                "Indonesia": "Anggota / Brainstorming dan Pelaksanaan Proyek"
            },
            "photo": "Adam.jpeg"
        },
        {
            "name": "Riska Dwi Ambarwati",
            "role": {
                "English": "Member / Brainstorming and Project Execution",
                "Indonesia": "Anggota / Brainstorming dan Pelaksanaan Proyek"
            },
            "photo": "Riska.jpeg"
        }
    ]

    cols = st.columns(2)
    for i, m in enumerate(members):
        with cols[i % 2]:
            img64 = img_to_base64(m["photo"])
            st.markdown(f"""
            <div class="member-card">
                <img src="data:image/jpeg;base64,{img64}" class="member-photo">
                <div class="member-name">{m["name"]}</div>
                <div class="member-role">{m["role"][language]}</div>
            </div>
            """, unsafe_allow_html=True)

# ============================
# PAGE 2: FUNCTION TOOLS (ORIGINAL)
# ============================
elif page == t["function"]:
    st.markdown(f"<div class='title'>{t['function']}</div>", unsafe_allow_html=True)

    func_input = st.text_input(t["enter_func"], "x**2")
    x = sp.symbols('x')

    try:
        expr = sp.sympify(func_input)
        f = sp.lambdify(x, expr, "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)
        st.pyplot(fig)

        derivative = sp.diff(expr, x)
        st.success(f"{t['derivative']}: {derivative}")

    except:
        st.error(t["invalid_func"])

# ============================
# PAGE 3: OPTIMIZATION SOLVER (ORIGINAL)
# ============================
elif page == t["optimization"]:
    st.markdown(f"<div class='title'>{t['optimization']}</div>", unsafe_allow_html=True)

    var_input = st.text_input(t["variable"], "x")
    func_input = st.text_input(t["function_label"], "-x**2 + 4*x")
    opt_type = st.radio(
        t["opt_type"],
        [t["maximize"], t["minimize"]]
    )

    try:
        vars_list = [sp.symbols(v.strip()) for v in var_input.split(",")]
        func = sp.sympify(func_input)

        derivs = [sp.diff(func, v) for v in vars_list]
        crit_points = sp.solve(derivs, vars_list, dict=True)

        if crit_points:
            best = max(crit_points, key=lambda p: func.subs(p)) \
                if opt_type == t["maximize"] \
                else min(crit_points, key=lambda p: func.subs(p))

            st.success(f"{opt_type}: {best}, value = {func.subs(best)}")
        else:
            st.warning("No critical points found")

    except Exception as e:
        st.error(e)

# ============================
# PAGE 4: STORY-BASED CALCULATION (ORIGINAL + BILINGUAL)
# ============================
elif page == t["story"]:
    st.markdown(f"<div class='title'>{t['story']}</div>", unsafe_allow_html=True)

    category = st.selectbox(
        t["category"],
        [t["area"], t["perimeter"], t["volume"], t["profit"]]
    )

    # AREA
    if category == t["area"]:
        shape = st.selectbox(
            t["shape"],
            ["Rectangle", "Triangle", "Trapezoid", "Circle"],
            format_func=lambda x: shape_lang[x]
        )

        if shape == "Rectangle":
            l = st.number_input("Length / Panjang", 10.0)
            w = st.number_input("Width / Lebar", 5.0)
            st.success(l * w)

        elif shape == "Triangle":
            b = st.number_input("Base / Alas", 8.0)
            h = st.number_input("Height / Tinggi", 5.0)
            st.success(0.5 * b * h)

        elif shape == "Trapezoid":
            a = st.number_input("Side a", 8.0)
            b = st.number_input("Side b", 5.0)
            h = st.number_input("Height / Tinggi", 4.0)
            st.success(0.5 * (a + b) * h)

        elif shape == "Circle":
            r = st.number_input("Radius / Jari-jari", 7.0)
            st.success(math.pi * r**2)

    # PERIMETER
    elif category == t["perimeter"]:
        shape = st.selectbox(
            t["shape"],
            ["Rectangle", "Triangle", "Trapezoid", "Circle"],
            format_func=lambda x: shape_lang[x]
        )

        if shape == "Rectangle":
            l = st.number_input("Length / Panjang", 10.0)
            w = st.number_input("Width / Lebar", 5.0)
            st.success(2 * (l + w))

        elif shape == "Triangle":
            a = st.number_input("Side a", 5.0)
            b = st.number_input("Side b", 6.0)
            c = st.number_input("Side c", 7.0)
            st.success(a + b + c)

        elif shape == "Trapezoid":
            a = st.number_input("Side a", 8.0)
            b = st.number_input("Side b", 5.0)
            c = st.number_input("Side c", 4.0)
            d = st.number_input("Side d", 3.0)
            st.success(a + b + c + d)

        elif shape == "Circle":
            r = st.number_input("Radius / Jari-jari", 7.0)
            st.success(2 * math.pi * r)

    # VOLUME
    elif category == t["volume"]:
        shape = st.selectbox(
            t["shape"],
            ["Cuboid", "Cylinder", "Triangular Prism", "Triangular Pyramid"],
            format_func=lambda x: shape_lang[x]
        )

        if shape == "Cuboid":
            l = st.number_input("Length / Panjang", 10.0)
            w = st.number_input("Width / Lebar", 5.0)
            h = st.number_input("Height / Tinggi", 4.0)
            st.success(l * w * h)

        elif shape == "Cylinder":
            r = st.number_input("Radius / Jari-jari", 7.0)
            h = st.number_input("Height / Tinggi", 10.0)
            st.success(math.pi * r**2 * h)

        elif shape == "Triangular Prism":
            b = st.number_input("Base / Alas", 6.0)
            h = st.number_input("Triangle height / Tinggi segitiga", 4.0)
            l = st.number_input("Length / Panjang", 10.0)
            st.success(0.5 * b * h * l)

        elif shape == "Triangular Pyramid":
            b = st.number_input("Base / Alas", 6.0)
            h = st.number_input("Triangle height / Tinggi segitiga", 4.0)
            H = st.number_input("Pyramid height / Tinggi limas", 10.0)
            st.success((1/3) * 0.5 * b * h * H)

    # PROFIT
    elif category == t["profit"]:
        price = st.number_input(t["price"], 50.0)
        cost = st.number_input(t["cost"], 20.0)
        fixed = st.number_input(t["fixed"], 100.0)

        q = sp.symbols('q')
        profit = price*q - (cost*q + fixed)
        crit = sp.solve(sp.diff(profit, q), q)

        if crit:
            st.success(f"{t['max_profit']}: q = {crit[0]}, P = {profit.subs(q, crit[0])}")

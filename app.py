import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a5f, #2563eb);
    min-height: 100vh;
}

/* Main calculator card */
.calculator-card {
    background: rgba(255, 255, 255, 0.10);
    padding: 35px;
    border-radius: 25px;
    max-width: 550px;
    margin: 50px auto;
    box-shadow: 0px 15px 40px rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

/* Title */
.title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 16px;
    margin-bottom: 30px;
}

/* Labels */
label {
    color: white !important;
    font-weight: 600 !important;
}

/* Result box */
.result-box {
    background: rgba(0, 0, 0, 0.30);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

.result-label {
    color: #cbd5e1;
    font-size: 16px;
}

.result-value {
    color: white;
    font-size: 36px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    color: #cbd5e1;
    margin-top: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# Calculator UI
st.markdown('<div class="calculator-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="title">🧮 Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Simple Calculator using Streamlit</div>',
    unsafe_allow_html=True
)

# Input numbers
num1 = st.number_input(
    "Enter first number",
    value=0.0,
    step=1.0
)

num2 = st.number_input(
    "Enter second number",
    value=0.0,
    step=1.0
)

# Operation
operation = st.selectbox(
    "Select Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    ]
)

# Calculate button
if st.button("Calculate", use_container_width=True):

    if operation == "Addition (+)":
        result = num1 + num2
        symbol = "+"

    elif operation == "Subtraction (-)":
        result = num1 - num2
        symbol = "-"

    elif operation == "Multiplication (×)":
        result = num1 * num2
        symbol = "×"

    else:
        symbol = "÷"

        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-label">
                    Result
                </div>
                <div class="result-value">
                    {num1:g} {symbol} {num2:g} = {result:g}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="footer">Calculator Project • C + Streamlit Interface</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


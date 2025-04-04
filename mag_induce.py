import streamlit as st
import json
import numpy as np

# Load the question data from the JSON file
with open("data/qs_3.5.json", "r") as f:
    questions = json.load(f)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Answer Checker", "Background Information"])

if page == "Background Information":
    st.title("Background Information")
    
# -----------------------------------------------------------    
    st.header("Magnetic Field Formulas and Explanations")
    st.markdown(r"""
    
    **Vacuum Permeability ($\mu_0$)**    
    The vacuum permeability ($\mu_0$) characterizes the ability of free space to support a magnetic field. Its standard value is:""")

    st.markdown(r"""  
    $
    \mu_0 = 1.25663706127 \times 10^{-6}\, \text{N/A}^2.
    $

**Long Straight Wire**  
A long straight wire carrying a current $I$ produces a magnetic field that encircles the wire and decreases with distance. The magnetic field at a distance $r$ is given by:""")

    # diagram_path = f"https://github.com/ZAKI1905/PHY132_Activity_3.4_Mag_Configs/main/data/figs/B_field_wire.jpg"
    st.image("data/figs/B_field_wire.jpg", caption="Magnetic Field Orientation: Long Straight Wire", use_container_width=True)
    st.markdown(r"""      
$$
B = \frac{\mu_0 I}{2 \pi r}
$$

where:  
- $I$ is the current in amperes (A).  
- $r$ is the distance from the wire in meters (m).  

This formula shows that the magnetic field is inversely proportional to the distance from the wire.

**Circular Loop**  
A circular loop of wire carrying a current $I$ produces a magnetic field at its center given by:""")
    # st.image("data/figs/B_field_loop.jpg", caption="Magnetic Field Orientation: Circular Loop", use_container_width=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("data/figs/B_field_loop.jpg", caption="Magnetic Field Orientation: Circular Loop")
    
    st.markdown(r"""
$$
B = \frac{\mu_0 I}{2R}
$$

where:  
- $R$ is the radius of the loop in meters (m).

This expression is valid when measuring the field at the center of the loop.

**Solenoid**  
For a solenoid with $N$ turns, a length $L$, and carrying a current $I$, the magnetic field inside (assuming an ideal, long solenoid) is approximately uniform and given by:""")
    st.image("data/figs/B_field_solenoid.jpg", caption="Magnetic Field Orientation: Solenoid", use_container_width=True)
    st.markdown(r"""
$$
B = \mu_0 \left(\frac{N}{L}\right) I
$$

where:  
- $\frac{N}{L}$ represents the number of turns per unit length (turns per meter).

This formula demonstrates that the field inside the solenoid increases with both the current and the turn density.
    """, unsafe_allow_html=True)

# -----------------------------------------------------------
    st.header("Electromagnetic Induction")
    st.markdown(r"""**Faraday’s Law of Induction**  
When the magnetic flux through a circuit changes, an electromotive force (EMF) is induced in the circuit. This is given by:""")
    st.markdown(r"""
$$
\varepsilon = -\frac{\Delta\Phi_B}{\Delta t}
$$
    """)
    st.markdown(r"""where:  
- $\varepsilon$ is the induced EMF,  
- $\Phi_B$ is the magnetic flux through the circuit.

The negative sign indicates the direction of the induced EMF as given by Lenz's Law.
    """, unsafe_allow_html=True)
    # st.image("data/figs/faraday_anim.gif")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("data/figs/faraday_anim.gif")
        
    st.markdown(r"""**Magnetic Flux ($\Phi_B$)**  
The magnetic flux through a loop of area $A$ is defined as:
    """)
    st.markdown(r"""
$$
\Phi_B = B \, A \, \cos\theta
$$
    """)
    st.markdown(r"""where:  
- $B$ is the magnetic field strength,  
- $A$ is the area of the loop,  
- $\theta$ is the angle between the magnetic field and the normal (perpendicular) to the loop's surface.
    """, unsafe_allow_html=True)
    st.image("data/figs/magnetic-flux.png", use_container_width=True)
    st.markdown(
        "<div style='text-align: center;'>Magnetic Flux: The magnetic field (<span style='color:green;'>green arrows</span>) passes through surfaces (<span style='color:salmon;'>salmon-colored areas</span>) with the surface normals indicated in <span style='color:red;'>red</span></div>",
        unsafe_allow_html=True
    )

    st.markdown(r"""**Lenz's Law**  
Lenz’s Law states that the induced current will flow in such a direction that its magnetic field opposes the change in the magnetic flux that produced it. This is why the negative sign appears in Faraday’s Law.
    """, unsafe_allow_html=True)
    
# -----------------------------------------------------------
    st.header("Centripetal Force")
    st.markdown(r"""When a particle moves in a circular path, a centripetal force is required to keep it in circular motion. This force is given by:""")
    st.markdown(r"""$F_c = \frac{mv^2}{r}$
    """, unsafe_allow_html=True)
    
    st.markdown(r"""where:  
- $m$ is the mass of the particle,  
- $v$ is the speed of the particle, and  
- $r$ is the radius of the circular path.

This force is always directed toward the center of the circle.
    """, unsafe_allow_html=True)
    
# -----------------------------------------------------------
    st.header("Ohm's Law and Power Dissipation")
    st.markdown(r"""
**Ohm's Law**  
Ohm's Law states that the voltage ($V$) across a resistor is directly proportional to the current ($I$) flowing through it:
    """)
    st.markdown(r"""
$$
V = IR
$$
    """)
    st.markdown(r"""
where:  
- $V$ is the voltage (in volts),  
- $I$ is the current (in amperes), and  
- $R$ is the resistance (in ohms, $\Omega$).
    """, unsafe_allow_html=True)
    st.markdown(r"""
**Power Dissipation in Resistors**  
The power dissipated by a resistor (i.e., the rate at which energy is converted to heat) can be calculated by:
    """)
    st.markdown(r"""
$$
P = I^2 R \quad \text{or} \quad P = \frac{V^2}{R}
$$
    """)
    st.markdown(r"""
where:  
- $P$ is the power (in watts, W).
    """, unsafe_allow_html=True)
    
# -----------------------------------------------------------
    st.header("Gravitational Force and Potential Energy")
    st.markdown(r"""
**Gravitational Force**  
The gravitational force on an object near the Earth's surface is given by:
    """)
    st.markdown(r"""
$$
F_g = mg
$$
    """)
    st.markdown(r"""
where:  
- $m$ is the mass of the object (in kilograms),  
- $g$ is the acceleration due to gravity (approximately $9.81\,\text{m/s}^2$).
    """, unsafe_allow_html=True)
    st.markdown(r"""
**Gravitational Potential Energy**  
The gravitational potential energy ($U$) of an object at a height $h$ above a reference point is:
    """)
    st.markdown(r"""
$$
U = mgh
$$
    """)
    st.markdown(r"""
where:  
- $U$ is the potential energy (in joules, J),  
- $h$ is the height (in meters),  
- $m$ is the mass, and  
- $g \approx 9.81\,\text{m/s}^2$.
    """, unsafe_allow_html=True)
    
# -----------------------------------------------------------
    st.header("Units")
    st.markdown(r"""
Magnetic field strength is commonly measured in **Gauss (G)** in the CGS system.  
$$
1\,\text{Gauss} = 10^{-4}\,\text{Tesla (T)}
$$  
The Tesla (T) is the SI unit for magnetic field strength.
    """, unsafe_allow_html=True)
    
 # -----------------------------------------------------------   
    st.header("Particle Properties")
    st.markdown(r"""
- **Electron:**  
  - Mass: $9.11 \times 10^{-31}\,\text{kg}$  
  - Charge: $-1.6 \times 10^{-19}\,\text{C}$
  
- **Proton:**  
  - Mass: $1.67 \times 10^{-27}\,\text{kg}$  
  - Charge: $+1.6 \times 10^{-19}\,\text{C}$
    """, unsafe_allow_html=True)
    
else:
    
    st.title("PHY 132 – Activity 3.5 - Magnetic Induction")
    st.write("This tool checks your final numerical answers (within 1% tolerance). Enter only the number(s) — no units.")
    
    # Dropdown to select a question
    question_ids = list(questions.keys())
    selected_id = st.selectbox("Choose a question:", question_ids)
    
    # Retrieve the selected question
    q = questions[selected_id]
    st.markdown(f"**{q['text']}**")
    
    # Check if the answer is a single number or a list (multiple parts)
    if isinstance(q['answer'], list):
        # For multiple answers, create a separate input for each part.
        user_answers = []
        num_parts = len(q['answer'])
        for i in range(num_parts):
            user_input = st.number_input(f"Enter answer part {i+1} in {q['unit']}:", format="%.6f", key=f"{selected_id}_{i}")
            user_answers.append(user_input)
        if st.button("Check Answer"):
            all_correct = True
            for user_ans, correct_ans in zip(user_answers, q['answer']):
                tolerance = 0.01 * abs(correct_ans)
                if abs(user_ans - correct_ans) > tolerance:
                    all_correct = False
                    break
            if all_correct:
                st.success("✅ Correct! Your answer is within 1% of the expected value.")
            else:
                st.error("❌ Not quite. Try again.")
    else:
        # Single numerical answer
        user_answer = st.number_input(f"Enter your answer in {q['unit']}:", format="%.6f")
        if st.button("Check Answer"):
            correct = float(q['answer'])
            tolerance = 0.01 * abs(correct)
            if abs(user_answer - correct) <= tolerance:
                st.success("✅ Correct! Your answer is within 1% of the expected value.")
            else:
                st.error("❌ Not quite. Try again.")

# Footer with contact info and EKU logo
footer = '''
---
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
        This tool was developed for <b>PHY 132 - College Physics II</b> at Eastern Kentucky University.<br>
        For questions, contact: <b>Professor Zakeri</b> (m.zakeri@eku.edu)
    </div>
    <div>
        <img src="https://raw.githubusercontent.com/ZAKI1905/phy132-kirchhoff-checker/main/img/PrimaryLogo_Maroon.png" width="150">
    </div>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)

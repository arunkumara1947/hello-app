# portfolio.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Arunkumar A Portfolio",
    page_icon=":computer:",
    layout="wide"
)

# Header
st.title("Arunkumar A")
st.subheader("Python Developer")
st.write("[LinkedIn Profile](https://www.linkedin.com/in/arunkumar-a-834113238)")
st.write("Email: kit.23.19bbm007@gmail.com | Phone: +91 9655909964")

# Objective
st.header("Objective")
st.write("""
To work in a challenging and dynamic environment and to keep adding value 
to the organization that I represent and serve, while also concurrently upgrading 
my skills and knowledge.
""")

# Education
st.header("Educational Qualification")
st.markdown("""
| Qualification | Institution | Board/University | Year | Percentage/CGPA |
|---------------|------------|----------------|------|----------------|
| BE–Bio Medical Engineering | KIT- Kalaignarkarunanidhi Institute of Technology (Autonomous) | Anna University| 2023 | 74.48% |
| HSC | St Xavier’s HR Sec School | State Board | 2019 | 69.6% |
| SSLC | St Xavier’s HR Sec School | State Board | 2017 | 93% |
""")

# Certifications
st.header("Certifications")
st.write("""
- NPTEL: Tissue Engineering 8-week course coordinated by IIT Madras  
- Python course completed in GUVI  
- HTML & CSS  
- GIT
""")

# Projects
st.header("Projects")
st.subheader("Handstaff Obstacle Avoidance System for Blind Pedestrians")
st.write("""
Enhances traditional white cane functionality by integrating sensors and feedback mechanisms 
that detect obstacles above ground level and at longer distances.
""")

st.subheader("Automated Level Detector and Alert System for Intravenous (IV) Drip")
st.write("""
Minimizes complications like air embolism, reverse flow of blood, and blood loss.  
Uses Micro-controller (UNO) Arduino board / Raspberry Pi and Relay module (Hx711).  
Replaces dedicated manpower with a fully automated unit.
""")

# Technical Skills
st.header("Technical Skills")
st.write("- Python")
st.write("- MySQL")
st.write("- HTML & CSS")

# Declaration
st.header("Declaration")
st.write("""
I hereby declare that the above information is correct to my best of my knowledge and belief.
""")

# Footer
st.markdown("---")

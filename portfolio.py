import streamlit as st
from PIL import Image

# --- Load Image ---
image = Image.open("Abhi .jpg")

# --- Sidebar ---
st.sidebar.title("📬 Contact Me")
st.sidebar.markdown("""
📧 abhishekkumardubey23022202@gmail.com  
📞 +91-9007947225  
🔗 [LinkedIn](https://www.linkedin.com/in/abhishek-dubey-a80736199)  
🐙 [GitHub](https://github.com/justabhishek23022002)
""")

# --- Main Profile Image and Name ---
st.image(image, width=200)
st.title("Abhishek Kumar Dubey")
st.subheader("Mathematics & Data Science Enthusiast")

st.markdown("""
I’m an analytically-minded, results-driven professional with a strong foundation in **Mathematics** and **Data Science**.  
Passionate about leveraging machine learning and data analysis to solve real-world problems.  
Currently pursuing **Master's in Mathematics with Data Science** at the *Institute of Mathematics & Applications*.
""")

# --- Skills ---
st.header("🛠️ Skills")
st.markdown("""
**Languages:** Python, R, C  
**Libraries/Tools:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Keras, TensorFlow, PyTorch, OpenCV, YOLO, Selenium, Airflow, PySpark  
**Data Analysis & Visualization:** Tableau, Power BI, Excel  
**Databases & Cloud:** SQL
""")

# --- Projects ---
st.header("📂 Projects")

st.subheader("🔧 [Tire Defect Detection using ML & DL](https://github.com/justabhishek23022002/Comparative-Analysis-of-Machine-Learning-and-Deep-Learning-Approaches-for-Tire-Defect-Detection)")
st.markdown("""
- Used SVM, KNN, Decision Trees, Random Forest for defect classification  
- Developed CNN model with 98.4% accuracy  
- Integrated YOLO for real-time object detection  
- Achieved 99% accuracy with optimized ML models
""")

st.subheader("📊 [Supervised & Unsupervised Learning Analysis](https://github.com/justabhishek23022002/On-some-applications-related-to-supervised-and-unsupervised-learning)")
st.markdown("""
- Analyzed economic mobility and gene expression datasets  
- Built predictive models  
- Used K-means for clustering feature groups
""")

st.subheader("🌿 [Leaf Disease Detection using Image Processing & SVM](https://github.com/justabhishek23022002/Leaf-disease-detection-project)")
st.markdown("""
- Converted RGB images to HSV for better color segmentation  
- Isolated infected areas using masking and image processing  
- Trained SVM for healthy/infected classification
""")

# --- Internships ---
st.header("💼 Internships")

st.subheader("🏛️ Presidency University, Kolkata — Data Science Intern")
st.markdown("""
- Worked on supervised and unsupervised learning techniques  
- Focused on economic and gene expression data analysis
""")

st.subheader("🌐 Oasis Infobyte — Data Science Intern")
st.markdown("""
- Sales forecasting  
- Unemployment analysis  
- Email spam detection
""")

st.subheader("🤖 Cognifyz Technologies — ML Intern")
st.markdown("""
- Stock price prediction  
- Handwritten digit recognition using CNN
""")

# --- Education ---
st.header("🎓 Education")
st.markdown("""
**Institute of Mathematics & Applications** — *Master’s in Mathematics with Data Science (2023 – 2025)*  
📍 Bhubaneswar, Odisha | CGPA: 7.7  

**University of Calcutta** — *B.Sc in Mathematics (2019 – 2022)*  
📍 Kolkata, West Bengal | CGPA: 7.8
""")

# --- Certifications ---
st.header("📜 Certifications")
st.markdown("""
**Winter School on Deep Learning & LLMs** — *CSI Kolkata Chapter*  
Advanced coursework in deep learning, generative AI, and large language models (Mar 2024 – May 2024)
""")

# --- Footer ---
st.markdown("---")
st.caption("Portfolio built with ❤️ using Streamlit.")

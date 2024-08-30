import streamlit as st

# Overall Styling (Mimicking React/HTML/CSS feel)
st.markdown("""
<style>
.project-container {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}
.project-title {
    font-size: 24px;
    color: #333;
    margin-bottom: 10px;
}
.project-description {
    color: #555;
}
.skill-section {
    display: flex;
    flex-wrap: wrap;
}
.skill-tag {
    background-color: #eee;
    color: #333;
    padding: 5px 10px;
    margin: 5px;
    border-radius: 3px;
}
.experience-item {
    margin-bottom: 15px;
}
.experience-title {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("Aaditya Gedhar")
st.subheader("Python Developer & Computer Vision Engineer")
st.write("""
Highly motivated and adaptable Python developer with 5+ years of experience in building and deploying AI-powered solutions. 
Proven track record in computer vision, machine learning, and cloud technologies. Passionate about leveraging technology to solve real-world problems.
""")

# Skills Section (with styling)
st.header("Skills")
st.write("<div class='skill-section'>", unsafe_allow_html=True)
all_skills = ["Python", "Generative AI", "Computer Vision", "NLP", "Machine Learning", 
              "Data Visualization", "DataDog", "Git", "Docker", "Raspberry Pi & Arduino", "RESTful APIs",
              "Django", "Flask", "TensorFlow", "PyTorch", "Keras", 
              "AWS", "Azure", "Linux/Unix Administration", "Bash", "PowerShell",
              "SQL/MySQL", "MongoDB"]
for skill in all_skills:
    st.write(f"<span class='skill-tag'>{skill}</span>", unsafe_allow_html=True)
st.write("</div>", unsafe_allow_html=True)

# Experience Section
st.header("Experience")

# Project Highlights (with detailed descriptions and styling)
st.subheader("Project Highlights")

# Project 1
with st.container():
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    st.markdown("<h3 class='project-title'>Generative AI Q&A Chatbot</h3>", unsafe_allow_html=True)
    # st.image("chatbot_image.jpg") 
    st.markdown("<p class='project-description'>Built a custom Generative AI Q&A chatbot that leverages OpenAI's GPT-4 and fine-tuned it on domain-specific data, stored in AWS S3 buckets, to provide accurate and contextually relevant responses to user queries. The chatbot utilizes sentence-transformers (all-MiniLM-L6-v2) for embedding and integrates with a database (MySQL/MongoDB) and Django for deployment.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Project 2
with st.container():
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    st.markdown("<h3 class='project-title'>AWS Application Rebuilding</h3>", unsafe_allow_html=True)
    # st.image("aws_image.jpg")
    st.markdown("<p class='project-description'>Designed and implemented a complete AWS architecture, encompassing VPC, LB, Lambda, EC2, RDS, Internet Gateway, Hosting, and CloudWatch. Migrated the operating system to the latest RHEL 9.2, upgraded the Python application from version 3.6 to 3.10, and configured Redis and ElasticSearch servers. Forwarded logs from CloudWatch to Datadog for monitoring.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Project 3
with st.container():
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    st.markdown("<h3 class='project-title'>Digital Signage Player</h3>", unsafe_allow_html=True)
    # st.image("signage_image.jpg")
    st.markdown("<p class='project-description'>Developed a versatile digital signage player capable of displaying diverse content (HTML pages, website URLs, images, videos, PDFs) based on scheduling. The player is platform-independent, running seamlessly on Windows, Raspberry Pi, Linux, and Mac-OS using Python. It interacts with a backend API to check for new schedules and content updates.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Project 4
with st.container():
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    st.markdown("<h3 class='project-title'>Footfall Analysis and Heatmap Generation</h3>", unsafe_allow_html=True)
    # st.image("heatmap_image.jpg")
    st.markdown("<p class='project-description'>Created a computer vision model to track footfall in stores or malls, generating heatmaps that visualize visitor pathways. The model provides valuable insights into customer behavior and was deployed using Django in production and Flask for testing.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Work History (with styling)
st.subheader("Work History")
st.markdown("""
<div class='experience-item'>
    <span class='experience-title'>Python Developer at TCS</span> (Mar 2022 - Present)
</div>
<div class='experience-item'>
    <span class='experience-title'>Computer Vision Engineer at Experiences Digital</span> (Mar 2020 - Feb 2022)
</div>
<div class='experience-item'>
    <span class='experience-title'>Computer Vision Engineer at Wobot AI</span> (Aug 2019 - Mar 2020)
</div>
<div class='experience-item'>
    <span class='experience-title'>Research Intern at Defense Research & Development Organization (DRDO)</span> (Jan 2019 - Jun 2019)
</div>
""", unsafe_allow_html=True)

# Education Section
st.header("Education")
st.write("B.Tech in Computer Science & Engineering from JECRC University")

# Mini-Projects Section
st.header("Mini-Projects")
mini_projects = ["Helmet Detector: Developed a custom object detector using YOLO to accurately identify helmets in images or video streams.",
                 "Optical Character Recognition (OCR): Designed an OCR system to extract timestamp information from video streams, enabling efficient data collection and analysis.",
                 "Motion Detection Model: Created a motion detection model to identify movement in video streams, triggering subsequent code execution and optimizing resource utilization.",
                 "Region of Interest (ROI) Visualization: Developed ROI code to focus on specific areas of interest, improving result accuracy and reducing processing overhead.",
                 "Custom Face Detector: Gained hands-on experience with building a custom face detector using the TensorFlow Object Detection API.",
                 "SAM2 and CatVTON for clothes detection.",
                 "Tested llama 3.1 and Gemini model at local server on GPU."]
for project in mini_projects:
    st.write(f"* {project}")

# Contact Section
st.header("Contact")
st.write("Email: your_email@example.com") 
st.write("LinkedIn: your_linkedin_profile_link")

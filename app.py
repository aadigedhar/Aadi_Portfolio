import streamlit as st

# Overall Styling (Mimicking React/HTML/CSS feel)
st.markdown("""
<style>
/* ... (rest of your existing CSS) ... */
.skill-group {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 10px;
}
.skill-tag {
    background-color: #007bff; 
    color: white;
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
.main-title {
    text-align: center;
    color: #007bff; 
    margin-bottom: 30px;
}
.subheader {
    color: #333;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
    margin-bottom: 20px;
}
.two-column-layout {
    display: flex;
    justify-content: space-between;
}
.column {
    width: 48%; /* Adjust as needed for desired column width */
}
</style>
""", unsafe_allow_html=True)

# Title and Introduction (centered and styled)
st.markdown(f"<h1 class='main-title'>Aaditya Gedhar</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subheader'>Python Developer & Computer Vision Engineer</h2>", unsafe_allow_html=True)
st.write("""
Highly motivated and adaptable Python developer with 5+ years of experience in building and deploying AI-powered solutions. 
Proven track record in computer vision, machine learning, and cloud technologies. Passionate about leveraging technology to solve real-world problems.
""")

# Skills Section (with improved grouping and styling)
st.header("Skills")

# Grouped Skills (using columns for better space utilization)
skill_groups = {
    "Programming & Frameworks": ["Python", "Django", "Flask", "TensorFlow", "PyTorch", "Keras"],
    "AI & ML": ["Generative AI", "Computer Vision", "NLP", "Machine Learning"],
    "Cloud & DevOps": ["AWS", "Azure", "Docker", "Git", "DataDog"],
    "Databases & Tools": ["SQL/MySQL", "MongoDB", "Raspberry Pi & Arduino", "RESTful APIs", "Linux/Unix Administration", "Bash", "PowerShell", "Data Visualization"]
}

# Create two columns for skill groups
col1, col2 = st.columns(2)

# Display skill groups in columns
with col1:
    for group_name, skills in list(skill_groups.items())[:2]:  # First two groups in the first column
        st.write(f"**{group_name}**")
        st.write("<div class='skill-group'>", unsafe_allow_html=True)
        for skill in skills:
            st.write(f"<span class='skill-tag'>{skill}</span>", unsafe_allow_html=True)
        st.write("</div>", unsafe_allow_html=True)

with col2:
    for group_name, skills in list(skill_groups.items())[2:]:  # Remaining groups in the second column
        st.write(f"**{group_name}**")
        st.write("<div class='skill-group'>", unsafe_allow_html=True)
        for skill in skills:
            st.write(f"<span class='skill-tag'>{skill}</span>", unsafe_allow_html=True)
        st.write("</div>", unsafe_allow_html=True)

# ... (rest of your code - Experience, Education, Mini-Projects, Contact) ...

# Experience Section
st.header("Experience")

# Project Highlights (with detailed descriptions, styling, and expanders)
st.subheader("Project Highlights")

# Project 1
with st.expander("Generative AI Q&A Chatbot"):  # Use expander for better organization
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    # st.image("chatbot_image.jpg") 
    st.markdown("<p class='project-description'>Built a custom Generative AI Q&A chatbot that leverages OpenAI's GPT-4 and fine-tuned it on domain-specific data, stored in AWS S3 buckets, to provide accurate and contextually relevant responses to user queries. The chatbot utilizes sentence-transformers (all-MiniLM-L6-v2) for embedding and integrates with a database (MySQL/MongoDB) and Django for deployment.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Project 2
with st.expander("AWS Application Rebuilding"):
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    # st.image("aws_image.jpg")
    st.markdown("<p class='project-description'>Designed and implemented a complete AWS architecture, encompassing VPC, LB, Lambda, EC2, RDS, Internet Gateway, Hosting, and CloudWatch. Migrated the operating system to the latest RHEL 9.2, upgraded the Python application from version 3.6 to 3.10, and configured Redis and ElasticSearch servers. Forwarded logs from CloudWatch to Datadog for monitoring.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Project 3
with st.expander("Digital Signage Player"):
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
    # st.image("signage_image.jpg")
    st.markdown("<p class='project-description'>Developed a versatile digital signage player capable of displaying diverse content (HTML pages, website URLs, images, videos, PDFs) based on scheduling. The player is platform-independent, running seamlessly on Windows, Raspberry Pi, Linux, and Mac-OS using Python. It interacts with a backend API to check for new schedules and content updates.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Project 4
with st.expander("Footfall Analysis and Heatmap Generation"):
    st.markdown("<div class='project-container'>", unsafe_allow_html=True)
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

import streamlit as st

# Title and Introduction
st.title("Aaditya Gedhar - Python Developer & Computer Vision Engineer")
st.write("""
Highly motivated and adaptable Python developer with 5+ years of experience in building and deploying AI-powered solutions. 
Proven track record in computer vision, machine learning, and cloud technologies. Passionate about leveraging technology to solve real-world problems.
""")

# Skills Section
st.header("Skills")

# Core Technical Skills
st.subheader("Core Technical Skills")
core_skills = ["Python", "Generative AI", "Computer Vision", "NLP", "Machine Learning"]
st.write(", ".join(core_skills))  # Display skills as comma-separated list

# Additional Skills
st.subheader("Additional Skills")
additional_skills = ["Data Visualization", "DataDog", "Git", "Docker", "Raspberry Pi & Arduino", "RESTful APIs"]
st.write(", ".join(additional_skills))

# Experience Section
st.header("Experience")

# Project Highlights
st.subheader("Project Highlights")

# Project 1: Generative AI Q&A Chatbot
st.write("**Generative AI Q&A Chatbot**")
# st.image("chatbot_image.jpg")  # Add an image if available
st.write("Developed a custom chatbot using OpenAI's GPT-4 and fine-tuned it on domain-specific data for accurate and context-aware responses.")

# Project 2: AWS Application Rebuilding
st.write("**AWS Application Rebuilding**")
# st.image("aws_image.jpg")
st.write("Designed and implemented a complete AWS architecture, migrating and optimizing an existing application for improved performance and scalability.")

# Project 3: Digital Signage Player
st.write("**Digital Signage Player**")
# st.image("signage_image.jpg")
st.write("Built a versatile, platform-independent digital signage solution using Python, enabling dynamic content scheduling and display.")

# Project 4: Footfall Analysis & Heatmap Generation
st.write("**Footfall Analysis & Heatmap Generation**")
# st.image("heatmap_image.jpg")
st.write("Created a computer vision model to track customer movement in retail spaces, generating heatmaps for valuable insights into customer behavior.")

# Work History
st.subheader("Work History")
st.write("""
* Python Developer at TCS (Mar 2022 - Present)
* Computer Vision Engineer at Experiences Digital (Mar 2020 - Feb 2022)
* Computer Vision Engineer at Wobot AI (Aug 2019 - Mar 2020)
* Research Intern at Defense Research & Development Organization (DRDO) (Jan 2019 - Jun 2019)
""")

# Education Section
st.header("Education")
st.write("B.Tech in Computer Science & Engineering from JECRC University")

# Projects Section
st.header("Projects")
projects = ["Helmet Detector", "Optical Character Recognition (OCR)", "Motion Detection Model", "Custom Face Detector"]
st.write("\n".join(f"* {project}" for project in projects))  # Display projects as a bulleted list

# Contact Section
st.header("Contact")
st.write("Email: your_email@example.com")  # Replace with your actual email
st.write("LinkedIn: your_linkedin_profile_link")  # Replace with your LinkedIn profile link

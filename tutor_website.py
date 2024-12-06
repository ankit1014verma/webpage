import streamlit as st
import csv


# Set page title
st.set_page_config(page_title="Home Tutor Website", page_icon="📚")

# Inject custom CSS for vibrant background
# st.markdown("""
#     <style>
#         body {
#             background-color: #ffebcd;  # Light color for the background (like Blanched Almond)
#             color: #333;  # Dark text color for contrast
#         }
#         .stButton button {
#             background-color: #32CD32;  # Vibrant green button color
#             color: white;
#             font-weight: bold;
#         }
#         .stTextInput input {
#             background-color: #fff;  # Light background for input fields
#             color: #333;  # Text color inside input fields
#         }
#         .stTextArea textarea {
#             background-color: #fff;  # Light background for text area
#             color: #333;  # Text color inside text area
#         }
#         .stForm label {
#             color: #4B0082;  # Purple color for form labels
#         }
#         h1, h2, h3 {
#             color: #ff6347;  # Tomato red for headers (vibrant)
#         }
#         .stMarkdown {
#             color: #5f5f5f;  # Slightly grey color for text sections
#         }
#         .stWrite {
#             font-size: 16px;
#         }
#         .stSelectbox select, .stTextInput input, .stTextArea textarea {
#             border-radius: 8px;  # Rounded corners for input fields
#         }
#         .stTextInput label, .stTextArea label {
#             font-weight: bold;
#         }
#     </style>
# """, unsafe_allow_html=True)



# Header
st.title("Welcome to Home Tutoring Services 📚")

# About Section
st.write("""
Hi! we are a team of passionate and dedicated home tutor with 6+ years of experience in teaching Science and Maths.  
I specialize in helping students improve their academic performance, build confidence, and develop a love for learning.  

Our approach is personalized and focused on addressing the individual learning needs of each student. I offer tutoring in the following subjects:
- Mathematics
- Physics
- Chemistry
- Problem Solving Techniques
""")

# Services Section
st.header("My Services")
st.write("""
We offer the following tutoring services:
- One-on-one in-person tutoring
- Online tutoring sessions (via Zoom, Google Meet, etc.)
- Homework assistance and exam preparation
- Customized lesson plans based on student's needs
- Flexible schedule and location options
""")

# Inquiry Section - Form
st.header("Inquiry Form")
st.write("Please fill out the form below to get in touch with me or ask any questions.")

# Contact Form
with st.form(key='inquiry_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email Address")
    phone = st.text_input("Your Phone Number")
    subject = st.text_input("Subject of Inquiry")
    message = st.text_area("Message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if name and email and message:
            # Save to CSV file
            with open('inquiries.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, email, phone, subject, message])
            st.success("Thank you for your inquiry. I will get back to you as soon as possible.")
        else:
            st.error("Please fill in all the required fields.")

# Footer Section
st.header("Contact Information")
st.write("""
You can reach me via phone:
- Phone: 8707397354
""")
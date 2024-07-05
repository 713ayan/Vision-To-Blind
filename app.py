import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from module import page2
import os
def main():
    st.set_page_config(page_title="Vision_To_Blind", page_icon=Image.open("assets/logo.jpeg"), layout="wide")
    
    if st.session_state.page == "About":
        col1, col2, col3,col4,col5 = st.columns([1, 1, 1,1,1])  # Create columns to adjust centering
        with col3:
            st.image('assets/image 1.jpeg', width=300, use_column_width=False)  # Adjust the width as needed        
        selected =option_menu(menu_title=None,options=["Home","About Us"],orientation="horizontal",)      
        if selected=="Home":
            st.markdown("""<h1 style='text-align: center;'>Welcome to Vision_To_Blind</h1>""", unsafe_allow_html=True)
            col1, col2= st.columns([1, 1])
            with col1:
                st.header("What is Vision_To_Blind?")
                st.markdown("""
                Vision_To_Blind is a specialized application developed to aid visually impaired individuals in understanding and navigating their environment. It utilizes advanced technology to detect and recognize objects in real-time using a computer vision library.
                """)
                st.header("How Does Vision_To_Blind?")
                st.markdown("""
              Vision_To_Blind works by capturing live video input from a camera, which is then processed through computer vision algorithms. These algorithms analyze the visual data to identify objects such as people, furniture, vehicles, and other items commonly found in everyday surroundings. The application then provides auditory feedback or tactile notifications to the user, conveying information about the objects detected.
                """)
    
                st.header("Importance of Vision_To_Blind")
                st.markdown("""
              The importance of Vision_To_Blind lies in its ability to enhance independence and safety for visually impaired individuals. By leveraging technology to interpret their surroundings, the application empowers users to navigate unfamiliar places, avoid obstacles, and interact more confidently with their environment. This innovative tool promotes inclusivity and accessibility by bridging the gap between visual impairment and everyday activities.
                """)
              
            with col2:
                st.image('assets/image 2.jpeg', width=600, use_column_width=False)
           

            if st.button("Test Vision_To_Blind"):
                st.session_state.page = "Page 2"




        
        if selected=="About Us":
            # Function to display team member information
            def display_team_member(image_filename, name, roll_number, email):
                st.markdown(
                    f"## {name}",
                    unsafe_allow_html=True
                )
                st.image(f"assets/{image_filename}")
                st.write(f"Roll Number: {roll_number}")
                st.write(f"Email: {email}")   
            # Function to display mentor information
            def display_mentor(image_filename, name, linkedin_profile):
                st.markdown(f"## {name}", unsafe_allow_html=True)
                st.image(f"assets/{image_filename}")
                st.write(f"LinkedIn Profile: [{name}]({linkedin_profile})")      
            col1, col2,col3,col4,col5 = st.columns(5)
            with col3:
                # Bolder text using HTML and CSS
                st.markdown("<p style='font-size: 34px; font-weight: bold; color: red;'>MENTOR</p>", unsafe_allow_html=True)
                # Example usage
                display_mentor("m.jpg", "Dr. Mayur Gaikwad", "https://www.linkedin.com/in/mayur-gaikwad-9047b0249/")
            col1, col2,col3,col4,col5 = st.columns(5)
            with col3:
                # Bolder text using HTML and CSS
                st.markdown("<p style='font-size: 40px; font-weight: bold; color: red;'>TEAM</p>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            # Display team members' information in each column
            with col1:
                display_team_member("3.jpg", "Kanika Thombre", "22070126052", "Kanika.Thombre.btech2022@sitpune.edu.in")
            with col2:
                display_team_member("1.jpg", "PratyushAgrawal", "22070126077", "Pratyush.Agrawal.btech2022@sitpune.edu.in")
            with col3:
                display_team_member("2.jpg", "Palak Kochey", "22070126070", "Palak.Kochey.btech2022@sitpune.edu.in")   
    elif st.session_state.page == "Page 2":
        page2()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "About"
    main()
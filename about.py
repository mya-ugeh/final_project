import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
import home, about, contact, dashboard, predict, logout, mimo

def about_us_page():
    
    # to import css file into streamlit
    with open('css\more.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.logo("img\INSIGHT-removebg-preview.png")
    
    #front header
    
    with stylable_container(
        key="header_container",
        css_styles="""
            {
                background-color: #012034;
                width: 78pc;
                margin-top: -6.1pc;
                margin-left: -13pc;
            }
        """,
    ):
        colored_header(
            label="ABOUT CARDIO INSIGHT",
            description="CardioInsight: Empowering Early Detection for a Healthier Heart",
            color_name='red-70'
        )
        col1,col2 = st.columns(2)
        with col2:
            st.markdown("<img src='https://github.com/mya-ugeh/siwes-presentation/blob/master/dub-removebg-preview.png?raw=true' style='width:408px;margin-top:-6pc; margin-left:-3pc;'>",unsafe_allow_html=True)
        with col1:
            st.markdown("<p style=' color:white; width:500px; text-align:justify;'>CardioInsight is dedicated to transforming cardiovascular health management through \
                cutting-edge technology. We leverage advanced machine learning and a user-friendly interface to \
                facilitate early detection and personalized insights for cardiovascular diseases (CVDs). Our \
                platform serves patients, healthcare professionals, and medical researchers, providing tools \
                for prediction, analysis, and interaction to improve overall health outcomes and reduce the \
                burden on healthcare systems</p>", unsafe_allow_html=True)
            
        
    with stylable_container(
        key="tab_container",
        css_styles="""
            {
                width: 76pc;
                background: rgba(0,0,0,0.5);
                margin-left: -13pc;
                margin-top: -1pc;
            }
        """
    ):
        tab1, tab2, tab3, tab4 = st.tabs(["Our Vision", "Our Mission", "Our Core Values", "Technologies"])
        with tab1:
            eye1, eye2 = st.columns(2)
            with eye1:
                st.markdown("<img src = 'https://github.com/mya-ugeh/siwes-presentation/blob/master/vision2.png?raw=true' style = 'margin-left: -5pc; width:200px; margin-top:7px;'>", unsafe_allow_html=True)
            with eye2:
                st.markdown("<p style = 'color:white; width:500px; text-align:justify;'>Our vision is to revolutionize the landscape of cardiovascular healthcare by harnessing the power of advanced technologies and data-driven insights. We strive to create a future where cardiovascular diseases are detected and managed proactively, significantly reducing the global burden of these conditions. By fostering innovation, collaboration, and accessibility, we envision a world where everyone has the tools and knowledge to maintain optimal cardiovascular health and prevent premature deaths caused by heart diseases.</p>",unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
        
        with tab2:
            mis1,mis2 = st.columns(2)
            with mis1:
                st.markdown("<img src = 'https://github.com/mya-ugeh/siwes-presentation/blob/master/target1.png?raw=true' style = 'margin-left: -5pc; width:250px; margin-top:-1.5pc;'>", unsafe_allow_html=True)
            with mis2:
                st.markdown("<p style = 'color:white; width:500px; text-align:justify'>Our mission is to deliver an intuitive and accurate cardiovascular disease prediction system that empowers users with critical health insights. We are committed to leveraging the latest advancements in machine learning and artificial intelligence to provide actionable predictions and analyses. Through continuous innovation and collaboration with medical experts, we aim to enhance the quality of healthcare and support informed decision-making for patients, healthcare providers, and researchers.</p>", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            
        with tab3:
            v1,v2 = st.columns(2)
            with v1:
                st.markdown("<img src = 'https://github.com/mya-ugeh/siwes-presentation/blob/master/diamond.png?raw=true' style = 'margin-left: -5pc; width:200px; margin-top:7px;'>", unsafe_allow_html=True)
            with v2:
                st.markdown("""
                    <style>
                        .stMarkdown li {
                            color: white;
                            width: 500px;
                            text-align: justify;
                        }
                    </style>
                    <ol>
                        <li><strong>Innovation</strong>: We continuously seek to improve and integrate the latest technologies to advance cardiovascular health management.</li>
                        <li><strong>Accuracy</strong>: We are committed to providing reliable and precise predictions and analyses to support informed health decisions.</li>
                        <li><strong>Accessibility</strong>: We strive to make our platform easy to use and accessible to patients, healthcare professionals, and researchers.</li>
                        <li><strong>Collaboration</strong>: We believe in the power of collaboration and work closely with medical experts and researchers to enhance our system's capabilities.</li>
                        <li><strong>Compassion</strong>: We prioritize the well-being of our users, ensuring our solutions are user-centric and focused on improving health outcomes.</li>
                    </ol>
                """, unsafe_allow_html=True)
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            
        with tab4:
            t1,t2 = st.columns(2)
            with t1:
                st.markdown("<img src = 'https://github.com/mya-ugeh/siwes-presentation/blob/master/tech.png?raw=true' style = 'margin-left: -5pc; width:200px; margin-top:7px; border:none;'>", unsafe_allow_html=True)
            with t2:
                st.markdown("<p><strong>Machine Learning</strong>: Utilized for predictive modeling and risk assessment.</p", unsafe_allow_html= True)
                st.markdown("<p><strong>Natural Language</strong> Processing: Powers the interactive chatbot for user engagement.</p>", unsafe_allow_html= True)
                st.markdown("<p><strong>Web Development</strong> Frameworks: Django and Streamlit for building the user interface.</p>", unsafe_allow_html= True)
                st.markdown("<p><strong>Cloud Computing</strong>: Deployment on cloud servers for scalability and accessibility.</p>", unsafe_allow_html= True)

            st.markdown("<br><br>", unsafe_allow_html=True)

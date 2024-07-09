import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
import base64
import time
import logout,about, predict, contact, dashboard, mimo



def home_page():
    # Add custom CSS
    with open('css\home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
            
    a,b = st.columns(2)
    with a:
        st.markdown("<p style='color:#1898BA;font-weight:bold;font-family:sans-serif;letter-spacing:2px;text-shadow:14px 20px 8px black'>CARDIOVASCULAR</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='color:white;margin-top:-45px; letter-spacing:2px; font-size:60px; text-shadow:14px 20px 8px black'>DISEASES</h1>",unsafe_allow_html=True)
        st.markdown("<hr style = 'border-weight:20px; color:white; width:160px; margin-block-start:auto'/>",unsafe_allow_html=True)
        words = """
            <p style= 'text-align:justify; font-weight:bold; color:azure; position:absolute; overflow:hidden'>
                Discover Your Heart's Health: Welcome to our Cardiovascular Disease Prediction Platform!
                With cutting-edge technology and a friendly chatbot, we're revolutionizing heart health. 
                Get personalized risk assessments, proactive tips, and expert guidance—all at your fingertips. 
                Take charge of your heart's future today!
            </p>
        """
        st.markdown(words, unsafe_allow_html=True)
        
    with b:
        with stylable_container(
            key="video",
            css_styles="""
                {
                  margin-left: 16pc;  
                }
            """
        ):
            from streamlit_player import st_player
            videos =  "https://www.youtube.com/watch?v=h413NHcx7eo&t=57s"
            

            # Get video path based on selection
            video_path = videos

            # Display video on main page
            st_player(video_path)
    
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    #machine learning
    with stylable_container(
        key="ml_container",
        css_styles="""
            {
                margin-left: 4pc;
                background-image: url('https://raw.githubusercontent.com/mya-ugeh/siwes-presentation/master/ml.png');
                background-size: cover;
                width: 65pc;
            }
            """,
    ):
        colored_header(
        label="WHAT IS MACHINE LEARNING?",
        description="Find out about machine learning",
        color_name="red-70",
        )
        st.markdown("<p style = 'width:800px; text-align: justify; font-weight: 300;'>Machine learning (ML) is a branch of \
            artificial intelligence (AI) focused on building systems that learn from data and improve over time without explicit \
            programming. It includes supervised learning (with labeled data), unsupervised learning (finding patterns in unlabeled \
            data), and reinforcement learning (learning through interaction with an environment). ML is widely used in fields such \
            as NLP, computer vision, and recommendation systems. Common tools include Python, TensorFlow, \
            and Scikit-learn, with key steps involving data collection, model training, and evaluation.</p><br>", unsafe_allow_html=True)
        
    st.markdown("<br>",unsafe_allow_html=True)
    
    #artificial intelligence
    with stylable_container(
        key="ai_container",
        css_styles="""
            {
                margin-left: 4pc;
                background-image: url('https://github.com/mya-ugeh/siwes-presentation/blob/master/ai.PNG?raw=true');
                background-size: cover;
                width: 65pc;
            }
            """,
    ):
        colored_header(
        label="WHAT IS ARTIFICIAL INTELLIGENCE?",
        description="Find out about artificial intelligence",
        color_name="blue-70",
        )
        st.markdown("<p style = 'width:800px; text-align: justify; font-weight: 300;'>Artificial Intelligence (AI) is a field of \
            computer science focused on creating systems that mimic human intelligence. Through techniques like machine learning \
            and natural language processing, AI enables computers to understand language, recognize patterns, and make decisions \
            autonomously. Its applications span various industries, from healthcare to finance, revolutionizing processes and \
            augmenting human capabilities. As AI continues to evolve, ongoing research and development drive innovation, promising \
            new possibilities for the future.</p><br>", unsafe_allow_html=True)
        
        
    st.markdown("<br>",unsafe_allow_html=True)
    
    
    #causes and prevention
    with stylable_container(
        key="cp_container",
        css_styles="""
            {
                margin-left: 4pc;
                background-image: url('https://github.com/mya-ugeh/siwes-presentation/blob/master/cause.PNG?raw=true');
                background-size: cover;
                width: 65pc;
            }
            """,
    ):
        colored_header(
        label="CAUSES, TREATMENT & PREVENTION",
        description="Find out more about cardiovascular disease",
        color_name="violet-70",
        )
        st.markdown("<p style = 'width:800px; text-align: justify; font-weight: 300;'>Cardiovascular disease (CVD) encompasses \
            heart and blood vessel conditions, including heart attack and stroke. Causes include lifestyle factors like smoking, \
            poor diet, and genetics. Treatment involves lifestyle changes, medication, and sometimes surgery. Prevention includes \
            healthy habits like exercise, a balanced diet, managing blood pressure and cholesterol, and avoiding tobacco. Regular \
            medical check-ups are crucial for early detection and management.</p>", unsafe_allow_html=True)
        
        link_url = "https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)?gad_source=1&gclid=CjwKCAjw34qzBhBmEiwAOUQcF6Vkxd1YnCEL3O3_oOM4ee4obMu-ecd7FOC02V97ec7H1VWMsfIITRoCERwQAvD_BwE"
        button_text = "Read More"
        button_style = """
            background-color: black;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            border-radius: 4px;
            margin-top: -2pc;
        """

        # Generate the HTML code for the button with a hyperlink
        button_html = f'<a href="{link_url}" style="{button_style}">{button_text}</a>'

        # Display the button using st.markdown
        st.markdown(button_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
        
    #app
    with stylable_container(
        key="app_container",
        css_styles="""
            {
                margin-left: 4pc;
                background-image: url('https://github.com/mya-ugeh/siwes-presentation/blob/master/app1.PNG?raw=true');
                background-size: cover;
                width: 65pc;
            }
            """,
    ):
        colored_header(
        label="HOW THE APP WORKS",
        description="Find out how the application works",
        color_name="yellow-80",
        )
        st.markdown("<p style = 'width:800px; text-align: justify; font-weight: 300;'>This application caters to patients, healthcare \
            professionals, and medical researchers, each with their unique benefits. Users can unlock predictive insights for \
            proactive health management. Researchers delve into detailed analytics with tools like pandas profiling, uncovering \
            hidden patterns. And for everyone, there's the dynamic chatbot, ready to engage and assist with personalized guidance.\
            </p><br>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    #chatbot
    with stylable_container(
        key="chatbot_container",
        css_styles="""
            {
                margin-left: 4pc;
                background-image: url('https://github.com/mya-ugeh/siwes-presentation/blob/master/mimo.PNG?raw=true');
                background-size: cover;
                width: 65pc;
            }
            """,
    ):
        colored_header(
        label="MIMO",
        description="Find out about Mimo",
        color_name="blue-70",
        )
        st.markdown("<p style = 'width:700px; text-align: justify; font-weight: 300;'>Our app features Mimo, an intelligent \
            chatbot powered by cutting-edge Ollama and Llama technologies. Mimo engages users with personalized health guidance \
            and support, making complex information easy to understand. Whether you're a patient seeking advice, a healthcare \
            professional needing quick insights, or a researcher exploring data, Mimo provides a seamless and interactive \
            experience, ensuring you get the most out of the app's features.</p><br>", unsafe_allow_html=True)
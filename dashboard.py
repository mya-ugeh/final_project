import streamlit as st
import about, contact, dashboard, predict, mimo, logout
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import numpy as np




def dashboard_page():
    with open('css\dashboard.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    data = pd.read_csv('new_cardio.csv', sep=',')
    samp = data.sample(10)
    samp.reset_index(inplace=True)
    samp.drop('Unnamed: 0',axis=1,inplace=True)
    samp.drop('index', axis=1, inplace=True)
    
    col = samp.columns.tolist()
    
    st.title(":red[Cardiovascular] Disease Dataset :red[Analysis] :coffee::bar_chart::stethoscope:")
    with stylable_container(
        key='sample_data',
        css_styles="""
            margin-left: 70pc
        """
    ):
        st.markdown("<h5>Sample Data<h5>", unsafe_allow_html=True)
        st.markdown("<marquee>The dataset consists of 70 000 records of patients data, 11 features + target. All of the dataset values were collected at the moment of medical examination.</marquee>", unsafe_allow_html=True)
        st.dataframe(data=samp, width= 900)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        
    #SCATTER PLOT    
    with stylable_container(
        key="scatterplot",
        css_styles="""
            {
                
            }
        """
    ):
        colored_header(
            label="ScatterPlot",
            description="The scatter plot shows relationship between two measurements where each point of scatter point is colored to represent cvd type (present or not).",
            color_name="blue-70"
        )
        x_axis = st.selectbox(
            "Select x-axis",
            col,
            help="Choose a variable for the x-axis"
        )
        y_axis = st.selectbox(
            "Select y-axis",
            col,
            help="Choose a variable for the y-axis"
        )       
        if x_axis and y_axis:
            fig = px.scatter(
                samp,
                x = x_axis,
                y = y_axis,
                color = "cardio",
                title = f"Scatter plot of {x_axis} vs {y_axis}",
                labels = {"cardio": "Cardiovascular Disease"}
            )
            st.plotly_chart(fig)
               
                
    st.markdown("<br>", unsafe_allow_html=True)
        
    
    #CVD BAR CHART    
    with stylable_container(
        key="bar_chart",
        css_styles="""
            {
                
            }
        """
    ):
        colored_header(
        label=" CVDs Bar Chart",
        description="Bar chart showing the count of cardiovascular diseases.",
        color_name="blue-70"
    )
        # Calculate counts of cardiovascular diseases
        disease_counts = data['cardio'].value_counts().reset_index()
        disease_counts.columns = ['Cardiovascular Disease', 'Count']  
        # Create the bar plot using Plotly
        fig = px.bar(disease_counts, x='Cardiovascular Disease', y='Count', 
                    labels={'Cardiovascular Disease': 'Presence of Cardiovascular Disease', 'Count': 'Number of Cases'},
                    title='Distribution of Cardiovascular Diseases')
        # Display the plot in Streamlit
        st.plotly_chart(fig)
    
    
    # HEATMAP
    with stylable_container(
        key="heatmap",
        css_styles="""
            {
                     
            }
        """
    ):
        colored_header(
        label="HeatMap",
        description="Visualize the correlation matrix of variables in the dataset using a heatmap. Each cell's color intensity represents the strength and direction of the correlation between two variables, providing insights into relationships and dependencies.",
        color_name="blue-70"
    )
        corr_matrix = data.corr()
        fig2 = px.imshow(corr_matrix,
                         text_auto=True,
                            color_continuous_scale='Viridis',
                         title='Correlation Heatmap of Variables'
                        )
        fig2.update_layout(
            autosize=False,
            width=1200,
            height=800,
            margin=dict(l=50,r=50,b=100,t=100,pad=4)
        )
        st.plotly_chart(fig2)
          
            
    #AGE ANALYSIS 
    st.markdown("<h1 style='margin-left:1pc;'>Feature Analysis</h1><br>", unsafe_allow_html=True)
    with stylable_container(
        key="age_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Age Analysis",
            description="Explore the distribution and statistical insights related to age in the dataset. This analysis highlights trends, patterns, and correlations involving age as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t1,t2,t3,t4 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t1:
            age_counts = data['age'].value_counts()
            fig3 = px.pie(age_counts, values=age_counts.values, names=age_counts.index, title='Age Distribution')
            st.plotly_chart(fig3)
        with t2:
            data.loc[(data['age'] < 40), 'age_range'] = '30-39'
            data.loc[(data['age'] >= 40) & (data['age'] < 50), 'age_range'] = '40-49'
            data.loc[(data['age'] >= 50) & (data['age'] < 60), 'age_range'] = '50-59'
            data.loc[(data['age'] >= 60) & (data['age'] < 70), 'age_range'] = '60-69'
                
            # Create a countplot using Plotly Express
            fig4 = px.histogram(data, x='age_range', color='cardio', barmode='group',
                            title='Age Ranges and Cardiovascular Disease Count',
                            labels={'age_range': 'Age Range', 'cardio': 'Cardiovascular Disease', 'count': 'Patients'},
                            category_orders={'age_range': ['30-39', '40-49', '50-59', '60-69']},
                            )  # Customize colors for 0 and 1
            
            # Display the plotly chart using Streamlit
            st.plotly_chart(fig4)
        with t3:
            age_matrix = data[['age','cardio']].corr()
            fig5 = px.imshow(age_matrix,
                             labels=dict(color="correlation"),
                             color_continuous_scale='Viridis',
                            title='Age Correlation Heatmap'
                            )
            st.plotly_chart(fig5)
        with t4:
            x1_axis = data['age']
            y1_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis")
            plot1 = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram")
            if y1_axis and plot1:
                if plot1 == 'bar':
                    fig6 = px.bar(data, x=x1_axis, y=y1_axis, title=f'Age vs {y1_axis} {plot1} Chart')
                elif plot1 == 'scatterplot':
                    fig6 = px.scatter(data, x=x1_axis, y=y1_axis, title=f'Age vs {y1_axis} {plot1} Chart')
                elif plot1 == 'boxplot':
                    fig6 = px.box(data, x=x1_axis, y=y1_axis, title=f'Age vs {y1_axis} {plot1} Chart')
                elif plot1 == 'area':
                    fig6 = px.area(data, x=x1_axis, y=y1_axis, title=f'Age vs {y1_axis} {plot1} Chart')
                st.plotly_chart(fig6)
               
    
    #GENDER ANALYSIS            
    with stylable_container(
        key="gender_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Gender Analysis",
            description="Explore the distribution and statistical insights related to Gender in the dataset. This analysis highlights trends, patterns, and correlations involving Gender as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t5,t6,t7,t8 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t5:
            df1 = data.copy()
            df1['gender'] = df1['gender'].map({0:'Female',1:'Male'})
            df1['cardio'] = df1['cardio'].map({0:'Absence of CVD',1:'Presence of CVD'})
            gender_counts = df1['gender'].value_counts()
            fig_gen = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index, title='Gender Distribution', labels={'female','male'})
            st.plotly_chart(fig_gen)
        with t6:
            # Create a countplot using Plotly Express
            fig_gen1 = px.histogram(df1, x='gender', color='cardio', barmode='group',
                            title='Count of Male and Females with and without Cardio Disease',
                            labels={'gender': 'Gender', 'cardio': 'Cardiovascular Disease'},
                            )  # Customize colors for 0 and 1
            
            # Display the plotly chart using Streamlit
            st.plotly_chart(fig_gen1)
        with t7:
            gender_matrix = data[['gender','cardio']].corr()
            fig_gen2 = px.imshow(gender_matrix,
                             labels=dict(color="correlation"),
                             color_continuous_scale='Viridis',
                            title='Gender Correlation Heatmap'
                            )
            st.plotly_chart(fig_gen2)
        with t8:
            x2_axis = data['gender']
            y2_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='gender')
            plot2 = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='gender_ana')
            if y2_axis and plot2:
                if plot2 == 'bar':
                    fig_gen3 = px.bar(data, x=x2_axis, y=y2_axis, title=f'Gender vs {y1_axis} {plot1} Chart')
                elif plot2 == 'scatterplot':
                    fig_gen3 = px.scatter(data, x=x2_axis, y=y2_axis, title=f'Gender vs {y1_axis} {plot1} Chart')
                elif plot2 == 'boxplot':
                    fig_gen3 = px.box(data, x=x2_axis, y=y2_axis, title=f'Gender vs {y1_axis} {plot1} Chart')
                elif plot2 == 'area':
                    fig_gen3 = px.area(data, x=x2_axis, y=y2_axis, title=f'Gender vs {y1_axis} {plot1} Chart')
                st.plotly_chart(fig_gen3)
        
             
             
    #HEIGHT ANALYSIS
    with stylable_container(
        key="height_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Heights Analysis",
            description="Explore the distribution and statistical insights related to Height in the dataset. This analysis highlights trends, patterns, and correlations involving Height as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t9,t10,t11,t12 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t9:
            bins = list(range(150, 181, 5))
            labels = [f'{b}-{b+4}' for b in bins[:-1]]
            data['height_range'] = pd.cut(data['height'], bins=bins, labels=labels, include_lowest=True)
            # Count the occurrences of each height range
            height_counts = data['height_range'].value_counts().reset_index()
            height_counts.columns = ['height_range', 'count']
            category_order = labels
            # Create the pie chart for height distribution
            fig_hei = px.pie(
                height_counts,
                values='count',
                names='height_range',
                title='Heights Distribution',
                category_orders={'height_range': category_order}
            )
            # Display the pie chart in Streamlit
            st.plotly_chart(fig_hei)
        with t10:
            # Create a countplot using Plotly Express
            fig_hei1 = px.histogram(data, x='height_range', color='cardio', barmode='group',
                            title='Count of Ranges of Height with and without Cardio Disease',
                            labels={'height': 'Height', 'cardio': 'Cardiovascular Disease'},
                            category_orders={'height_range': category_order})  # Customize colors for 0 and 1
            # Display the plotly chart using Streamlit
            st.plotly_chart(fig_hei1)
        with t11:
            height_matrix = data[['height','cardio']].corr()
            fig_hei2 = px.imshow(height_matrix,
                             labels=dict(color="correlation"),
                             color_continuous_scale='Viridis',
                            title='Height Correlation Heatmap'
                            )
            st.plotly_chart(fig_hei2)
        with t12:
            x3_axis = data['height']
            y3_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='height')
            plot3 = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='height_ana')
            if y3_axis and plot3:
                if plot3 == 'bar':
                    fig_hei3 = px.bar(data, x=x3_axis, y=y3_axis, title=f'Gender vs {y3_axis} {plot3} Chart')
                elif plot3 == 'scatterplot':
                    fig_hei3 = px.scatter(data, x=x3_axis, y=y3_axis, title=f'Gender vs {y3_axis} {plot3} Chart')
                elif plot3 == 'boxplot':
                    fig_hei3 = px.box(data, x=x3_axis, y=y3_axis, title=f'Gender vs {y3_axis} {plot3} Chart')
                elif plot3 == 'area':
                    fig_hei3 = px.area(data, x=x3_axis, y=y3_axis, title=f'Gender vs {y3_axis} {plot3} Chart')
                st.plotly_chart(fig_hei3)
             
       
    #WEIGHT ANALYSIS
    with stylable_container(
        key="weight_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Weight Analysis",
            description="Explore the distribution and statistical insights related to weight in the dataset. This analysis highlights trends, patterns, and correlations involving weight as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t13,t14,t15,t16 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t13:
            df2 = data.copy()
            bins = list(range(50, 111, 10))
            labels = [f'{b}-{b+4}' for b in bins[:-1]]
            df2['weight_range'] = pd.cut(df2['weight'], bins=bins, labels=labels, include_lowest=True)
            # Count the occurrences of each weight range
            weight_counts = df2['weight_range'].value_counts().reset_index()
            weight_counts.columns = ['weight_range', 'count']
            category_order = labels
            # Create the pie chart for weight distribution
            fig_weight1 = px.pie(
                weight_counts,
                values='count',
                names='weight_range',
                title='weights Distribution',
                category_orders={'weight_range': category_order}
            )
            # Display the pie chart in Streamlit
            st.plotly_chart(fig_weight1)
        with t14:
            # Create a countplot using Plotly Express
            fig_weight2 = px.histogram(df2, x='weight_range', color='cardio', barmode='group',
                            title='Count of Ranges of weight with and without Cardio Disease',
                            labels={'weight': 'weight', 'cardio': 'Cardiovascular Disease'},
                            category_orders={'weight_range': category_order})  # Customize colors for 0 and 1
            # Display the plotly chart using Streamlit
            st.plotly_chart(fig_weight2)
        with t15:
            weight_matrix = data[['weight','cardio']].corr()
            fig_weight3 = px.imshow(weight_matrix,
                             labels=dict(color="correlation"),
                             color_continuous_scale='Viridis',
                            title='weight Correlation Heatmap'
                            )
            st.plotly_chart(fig_weight3)
        with t16:
            x4_axis = data['weight']
            y4_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='weight')
            plot4 = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='weight_ana')
            if y4_axis and plot4:
                if plot4 == 'bar':
                    fig_weight4 = px.bar(data, x=x4_axis, y=y4_axis, title=f'Gender vs {y4_axis} {plot4} Chart')
                elif plot4 == 'scatterplot':
                    fig_weight4 = px.scatter(data, x=x4_axis, y=y4_axis, title=f'Gender vs {y4_axis} {plot4} Chart')
                elif plot4 == 'boxplot':
                    fig_weight4 = px.box(data, x=x4_axis, y=y4_axis, title=f'Gender vs {y4_axis} {plot4} Chart')
                elif plot4 == 'area':
                    fig_weight4 = px.area(data, x=x4_axis, y=y4_axis, title=f'Gender vs {y4_axis} {plot4} Chart')
                st.plotly_chart(fig_weight4)
            
    
    #BLOOD PRESSURE ANALYSIS
    with stylable_container(
        key="blood_pressure_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Blood Pressure Analysis",
            description="Explore the distribution and statistical insights related to Blood Pressure in the dataset. This analysis highlights trends, patterns, and correlations involving Blood Pressure as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t17,t18,t19,t20 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t17:
            df3 = data.copy()
            df3['cardio'] = df3['cardio'].replace({0:'No disease', 1:'Disease Present'})
            def categorize_blood_pressure(df):
                df["BP_Category"] = np.select(
                    [
                        (df["systolic bp"] < 120) & (df["diastolic bp"] < 80),
                        (df["systolic bp"] <= 129) & (df["diastolic bp"] < 80),
                        (df["systolic bp"] <= 139) & (df["diastolic bp"] <= 89),
                        (df["systolic bp"] >= 140) | (df["diastolic bp"] >= 90),
                    ],
                    ["Normal", "Elevated", "Hypertension Stage 1", "Hypertension Stage 2"],
                    default="Unknown"
                )
                return df
            df3 = categorize_blood_pressure(df3)
            bp_counts = df3['BP_Category'].value_counts().reset_index()
            bp_counts.columns = ['BP_Category', 'count']
            category_order1 = ['Normal', 'Elevated', 'Hypertension Stage 1', 'Hypertension Stage 2']
            # Create pie chart for blood pressure distribution
            fig_bp = px.pie(bp_counts, values='count', names='BP_Category', title='Blood Pressure Distribution',category_orders={'BP_Category': category_order1})
            # Display the pie chart in Streamlit
            st.plotly_chart(fig_bp)   
        with t18:
            # Create a countplot using Plotly Express
            fig_bp2 = px.histogram(df3, x='BP_Category', color='cardio', barmode='group',
                            title='Blood Pressure Categories and Presence of Cardiovascular Disease',
                            labels={'BP_Category': 'BP Category', 'cardio': 'Cardiovascular Disease'},
                            category_orders={'BP_Category': category_order1})  # Customize colors for 0 and 1
            # Display the plotly chart using Streamlit
            st.plotly_chart(fig_bp2)
        with t19:
            col1, col2 = st.columns(2)
            with col1:
                bp_matrix = data[['systolic bp','cardio']].corr()
                fig_bp3 = px.imshow(bp_matrix,
                                labels=dict(color="correlation"),
                                color_continuous_scale='Viridis',
                                title='Systolic BP Correlation Heatmap'
                                )
                st.plotly_chart(fig_bp3)
            with col2:
                bp_matrix1 = data[['diastolic bp','cardio']].corr()
                fig_bp4 = px.imshow(bp_matrix1,
                                labels=dict(color="correlation"),
                                color_continuous_scale='Viridis',
                                title='Diastolic BP Correlation Heatmap'
                                )
                st.plotly_chart(fig_bp4)
        with t20:
            with st.expander("Systolic BP / Diastolic BP Analysis"):
                if st.checkbox('Analyze Systolic BP', key='sys_toggle'):
                    bp_axis = 'systolic bp'
                else:
                    bp_axis = 'diastolic bp'

                y_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis", key='bpp')
                plot_type = st.selectbox("Select Chart", ['bar', 'scatterplot', 'boxplot', 'area'], help="Select your preferred chart diagram", key="bp")

                if y_axis and plot_type:
                    if plot_type == 'bar':
                        fig = px.bar(data, x=bp_axis, y=y_axis, title=f'{bp_axis} vs {y_axis} {plot_type} Chart')
                    elif plot_type == 'scatterplot':
                        fig = px.scatter(data, x=bp_axis, y=y_axis, title=f'{bp_axis} vs {y_axis} {plot_type} Chart')
                    elif plot_type == 'boxplot':
                        fig = px.box(data, x=bp_axis, y=y_axis, title=f'{bp_axis} vs {y_axis} {plot_type} Chart')
                    elif plot_type == 'area':
                        fig = px.area(data, x=bp_axis, y=y_axis, title=f'{bp_axis} vs {y_axis} {plot_type} Chart')

                    st.plotly_chart(fig)
        

    
    #CHOLESTEROL ANALYSIS
    with stylable_container(
        key="chol_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Cholesterol Analysis",
            description="Explore the distribution and statistical insights related to Cholesterol in the dataset. This analysis highlights trends, patterns, and correlations involving Cholesterol as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t21,t22,t23,t24 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t21:
            df4 = data.copy()
            df4['cholesterol'] = df4['cholesterol'].map({1:'Normal',2:'Above Normal',3:'Well Above Normal'}) 
            df4['cardio'] = df4['cardio'].map({0:'No Disease', 1:'Disease Present'})
            chol_counts = df4['cholesterol'].value_counts()
            fig_chol = px.pie(chol_counts, values=chol_counts.values, names=chol_counts.index, title='Cholesterol Distribution')
            st.plotly_chart(fig_chol)
        with t22:
            fig_chol1 = px.histogram(df4, x='cholesterol', color='cardio', barmode='group',
                            title='Cholesterol and Disease',
                            labels={'cholesterol': 'Cholesterol Rank', 'cardio': 'Cardiovascular Disease'},
                            ) 
            st.plotly_chart(fig_chol1)
        with t23:
            chol_matrix = data[['cholesterol','cardio']].corr()
            fig_chol2 = px.imshow(chol_matrix,
                            labels=dict(color="correlation"),
                            color_continuous_scale='Viridis',
                            title='Cholesterol Correlation Heatmap'
                            )
            st.plotly_chart(fig_chol2)
        with t24:
            chol_axis = df4['cholesterol']
            chol_y_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='chol')
            plot7 = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='chol_ana')
            if chol_y_axis and plot7:
                if plot7 == 'bar':
                    fig_chol5 = px.bar(data, x=chol_axis, y=chol_y_axis, title=f'Cholesterol vs {chol_y_axis} {plot7} Chart')
                elif plot7 == 'scatterplot':
                    fig_chol5 = px.scatter(data, x=chol_axis, y=chol_y_axis, title=f'Cholesterol vs {chol_y_axis} {plot7} Chart')
                elif plot7 == 'boxplot':
                    fig_chol5 = px.box(data, x=chol_axis, y=chol_y_axis, title=f'Cholesterol vs {chol_y_axis} {plot7} Chart')
                elif plot7 == 'area':
                    fig_chol5 = px.area(data, x=chol_axis, y=chol_y_axis, title=f'Cholesterol vs {chol_y_axis} {plot7} Chart')
                st.plotly_chart(fig_chol5)
                
                
    #GLUCOSE ANALYSIS
    with stylable_container(
        key="gluc_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Glucose Analysis",
            description="Explore the distribution and statistical insights related to Glucose in the dataset. This analysis highlights trends, patterns, and correlations involving Glucose as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t25,t26,t27,t28 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t25:
            df4['glucose'] = df4['glucose'].map({1:'Normal',2:'Above Normal',3:'Well Above Normal'}) 
            gluc_counts = df4['glucose'].value_counts()
            fig_gluc = px.pie(gluc_counts, values=gluc_counts.values, names=gluc_counts.index, title='Glucose Distribution')
            st.plotly_chart(fig_gluc)
        with t26:
            fig_gluc1 = px.histogram(df4, x='glucose', color='cardio', barmode='group',
                            title='Glucose and Disease',
                            labels={'glucose': 'glucose Rank', 'cardio': 'Cardiovascular Disease'},
                            ) 
            st.plotly_chart(fig_gluc1)
        with t27:
            gluc_matrix = data[['glucose','cardio']].corr()
            fig_gluc2 = px.imshow(gluc_matrix,
                            labels=dict(color="correlation"),
                            color_continuous_scale='Viridis',
                            title='glucose Correlation Heatmap'
                            )
            st.plotly_chart(fig_gluc2)
        with t28:
            gluc_axis = df4['glucose']
            gluc_y_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='gluc')
            plot8 = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='gluc_ana')
            if gluc_y_axis and plot8:
                if plot8 == 'bar':
                    fig_gluc5 = px.bar(data, x=gluc_axis, y=gluc_y_axis, title=f'glucose vs {gluc_y_axis} {plot8} Chart')
                elif plot8 == 'scatterplot':
                    fig_gluc5 = px.scatter(data, x=gluc_axis, y=gluc_y_axis, title=f'glucose vs {gluc_y_axis} {plot8} Chart')
                elif plot8 == 'boxplot':
                    fig_gluc5 = px.box(data, x=gluc_axis, y=gluc_y_axis, title=f'glucose vs {gluc_y_axis} {plot8} Chart')
                elif plot8 == 'area':
                    fig_gluc5 = px.area(data, x=gluc_axis, y=gluc_y_axis, title=f'glucose vs {gluc_y_axis} {plot8} Chart')
                st.plotly_chart(fig_gluc5)
    
    
    #ACTIVITY ANALYSIS
    with stylable_container(
        key="act_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Active Analysis",
            description="Explore the distribution and statistical insights related to Activity in the dataset. This analysis highlights trends, patterns, and correlations involving Activity as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t29,t30,t31,t32 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t29:
            df4['active'] = df4['active'].map({0:'Not Active',1:'Active'}) 
            act_counts = df4['active'].value_counts()
            fig_act = px.pie(act_counts, values=act_counts.values, names=act_counts.index, title='Activity Distribution')
            st.plotly_chart(fig_act)
        with t30:
            fig_act1 = px.histogram(df4, x='active', color='cardio', barmode='group',
                            title='Activity and Disease',
                            labels={'active': 'Active', 'cardio': 'Cardiovascular Disease'},
                            ) 
            st.plotly_chart(fig_act1)
        with t31:
            act_matrix = data[['active','cardio']].corr()
            fig_act2 = px.imshow(act_matrix,
                            labels=dict(color="correlation"),
                            color_continuous_scale='Viridis',
                            title='Activity Correlation Heatmap'
                            )
            st.plotly_chart(fig_act2)
        with t32:
            act_axis = df4['active']
            act_y_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='act')
            act_plot = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='act_ana')
            if act_y_axis and act_plot:
                if act_plot == 'bar':
                    fig_act5 = px.bar(data, x=act_axis, y=act_y_axis, title=f'activity vs {act_y_axis} {act_plot} Chart')
                elif act_plot == 'scatterplot':
                    fig_act5 = px.scatter(data, x=act_axis, y=act_y_axis, title=f'activity vs {act_y_axis} {act_plot} Chart')
                elif act_plot == 'boxplot':
                    fig_act5 = px.box(data, x=act_axis, y=act_y_axis, title=f'activity vs {act_y_axis} {act_plot} Chart')
                elif act_plot == 'area':
                    fig_act5 = px.area(data, x=act_axis, y=act_y_axis, title=f'activity vs {act_y_axis} {act_plot} Chart')
                st.plotly_chart(fig_act5)
    
    
    #ALCOHOL ANALYSIS
    with stylable_container(
        key="alh_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Alcohol Analysis",
            description="Explore the distribution and statistical insights related to Alcohol in the dataset. This analysis highlights trends, patterns, and correlations involving Alcohol as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t33,t34,t35,t36 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t33:
            df4['alcohol'] = df4['alcohol'].map({0:'No Alcohol intake',1:'Alcohol intake'}) 
            alh_counts = df4['alcohol'].value_counts()
            fig_alh = px.pie(alh_counts, values=alh_counts.values, names=alh_counts.index, title='Alcohol Distribution')
            st.plotly_chart(fig_alh)
        with t34:
            fig_alh1 = px.histogram(df4, x='alcohol', color='cardio', barmode='group',
                            title='alcohol and Disease',
                            labels={'alcohol': 'Alcohol', 'cardio': 'Cardiovascular Disease'},
                            ) 
            st.plotly_chart(fig_alh1)
        with t35:
            alh_matrix = data[['alcohol','cardio']].corr()
            fig_alh2 = px.imshow(alh_matrix,
                            labels=dict(color="correlation"),
                            color_continuous_scale='Viridis',
                            title='alcohol Correlation Heatmap'
                            )
            st.plotly_chart(fig_alh2)
        with t36:
            alh_axis = df4['alcohol']
            alh_y_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='alh')
            alh_plot = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='alh_ana')
            if alh_y_axis and alh_plot:
                if alh_plot == 'bar':
                    fig_alh5 = px.bar(data, x=alh_axis, y=alh_y_axis, title=f'alcohol vs {alh_y_axis} {alh_plot} Chart')
                elif alh_plot == 'scatterplot':
                    fig_alh5 = px.scatter(data, x=alh_axis, y=alh_y_axis, title=f'alcohol vs {alh_y_axis} {alh_plot} Chart')
                elif alh_plot == 'boxplot':
                    fig_alh5 = px.box(data, x=alh_axis, y=alh_y_axis, title=f'alcohol vs {alh_y_axis} {alh_plot} Chart')
                elif alh_plot == 'area':
                    fig_alh5 = px.area(data, x=alh_axis, y=alh_y_axis, title=f'alcohol vs {alh_y_axis} {alh_plot} Chart')
                st.plotly_chart(fig_alh5)
    
    
    #SMOKE ANALYSIS
    with stylable_container(
        key="smo_analysis",
        css_styles="""
            {
             
            }
        """
    ):
        colored_header(
            label="Smoke Analysis",
            description="Explore the distribution and statistical insights related to Smoke in the dataset. This analysis highlights trends, patterns, and correlations involving Smoke as a factor in cardiovascular disease prediction.",
            color_name="blue-green-70"
        )
        t37,t38,t39,t40 = st.tabs(['Pie Chart','Histogram','Correlation','Plots'])
        with t37:
            df4['smoke'] = df4['smoke'].map({0:'Non-Smoker',1:'Smoker'}) 
            smo_counts = df4['smoke'].value_counts()
            fig_smo = px.pie(smo_counts, values=smo_counts.values, names=smo_counts.index, title='smoke Distribution')
            st.plotly_chart(fig_smo)
        with t38:
            fig_smo1 = px.histogram(df4, x='smoke', color='cardio', barmode='group',
                            title='Smoke and Disease',
                            labels={'smoke': 'Smoke', 'cardio': 'Cardiovascular Disease'},
                            ) 
            st.plotly_chart(fig_smo1)
        with t39:
            smo_matrix = data[['smoke','cardio']].corr()
            fig_smo2 = px.imshow(smo_matrix,
                            labels=dict(color="correlation"),
                            color_continuous_scale='Viridis',
                            title='Smoke Correlation Heatmap'
                            )
            st.plotly_chart(fig_smo2)
        with t40:
            smo_axis = df4['smoke']
            smo_y_axis = st.selectbox("Select y-axis", col, help="Choose a variable for y-axis",key='smo')
            smo_plot = st.selectbox("Select Chart",['bar', 'scatterplot','boxplot','area'], help="Select your preferred chart diagram", key='smo_ana')
            if smo_y_axis and smo_plot:
                if smo_plot == 'bar':
                    fig_smo5 = px.bar(data, x=smo_axis, y=smo_y_axis, title=f'smoke vs {smo_y_axis} {smo_plot} Chart')
                elif smo_plot == 'scatterplot':
                    fig_smo5 = px.scatter(data, x=smo_axis, y=smo_y_axis, title=f'smoke vs {smo_y_axis} {smo_plot} Chart')
                elif smo_plot == 'boxplot':
                    fig_smo5 = px.box(data, x=smo_axis, y=smo_y_axis, title=f'smoke vs {smo_y_axis} {smo_plot} Chart')
                elif smo_plot == 'area':
                    fig_smo5 = px.area(data, x=smo_axis, y=smo_y_axis, title=f'smoke vs {smo_y_axis} {smo_plot} Chart')
                st.plotly_chart(fig_smo5)
    
    colored_header(
            label="Pandas Profiling",
            description=" ",
            color_name="red-70"
        )
    download,view = st.columns(2)
    profile = ProfileReport(data, title="Cardiovascular Disease Dataset Report", explorative=True, dark_mode=True)
    with download:
        profile.to_file("cardio_profile_report.html")
        with open("cardio_profile_report.html", "rb") as file:
            btn = st.download_button(
                label="Download Pandas Profile",
                data=file,
                file_name="cardio_profile_report.html",
                mime="text/html"
            )
    with view:
        with st.popover("View Pandas Profiling"):
            st_profile_report(profile)
        
        
                        
            
            
            
            

    

        
    
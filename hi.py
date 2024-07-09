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
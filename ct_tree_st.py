# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from streamlit_plotly_events import plotly_events

# # Load data
# fname = 'ct_treemap_data.csv'
# df = pd.read_csv(fname)

# # Set page config
# st.set_page_config(layout="wide")

# # Title
# st.title('Interactive Treemap')

# # Initialize session state
# if 'current_path' not in st.session_state:
#     st.session_state.current_path = ['sector', 'subsector']
# if 'df_chart' not in st.session_state:
#     st.session_state.df_chart = df.copy()

# # Define all levels
# all_levels = ['sector', 'subsector', 'iso3_country']

# # Function to update treemap
# def update_treemap(clicked_label):
#     new_path = st.session_state.current_path.copy()
#     df_chart = st.session_state.df_chart.copy()
    
#     if clicked_label:
#         for idx, p in enumerate(all_levels):
#             if clicked_label in df[p].unique():
#                 clicked_level = p
#                 break
        
#         clicked_index = all_levels.index(clicked_level)
#         current_index = all_levels.index(st.session_state.current_path[-1])
        
#         if clicked_index == current_index:
#             if clicked_index == 0:
#                 new_path = all_levels[clicked_index:clicked_index + 2]
#             elif clicked_index == len(all_levels) - 1:
#                 new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#             else:
#                 new_path = all_levels[clicked_index:clicked_index + 2]
#         elif clicked_index < current_index:
#             if clicked_index == 0:
#                 new_path = all_levels[clicked_index:clicked_index + 2]
#             else:
#                 new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#         else:
#             if clicked_index == len(all_levels) - 1:
#                 new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#             else:
#                 new_path = all_levels[clicked_index:clicked_index + 2]
        
#         new_path = new_path[:2]
        
#         if clicked_index == 0:
#             pass
#         elif clicked_index == len(all_levels) - 1:
#             clicked_label_parent = df[df[clicked_level] == clicked_label][new_path[0]].iloc[0]
#             df_chart = df_chart[df_chart[new_path[0]] == clicked_label_parent]
#         else:
#             df_chart = df_chart[df_chart[all_levels[clicked_index]] == clicked_label]
    
#     st.session_state.current_path = new_path
#     st.session_state.df_chart = df_chart

# # Create treemap
# fig = px.treemap(st.session_state.df_chart, path=st.session_state.current_path, values='co2e_100yr', color='continent_ct')

# fig.update_layout(
#     margin=dict(t=0, l=0, b=0, r=0),
#     paper_bgcolor='white',
#     uniformtext_minsize=10,
#     uniformtext_mode='hide',
#     clickmode='event+select'  # Ensure click events are enabled
# )

# fig.update_traces(
#     hovertemplate='%{label}<br>Value: %{value}<br>Percent of Total: %{percent.entry:.2%}',
#     textinfo='label+percent entry+value',
#     textfont_size=10,
#     marker=dict(line=dict(width=0))
# )

# # Display the plot
# st.plotly_chart(fig, use_container_width=True)

# # Capture click events
# selected_points = plotly_events(fig, click_event=True)

# # Process click data
# if selected_points:
#     click_info = selected_points[0]
    
#     # Extract label
#     clicked_label = click_info.get('label')
    
#     if clicked_label:
#         st.write("Clicked Label:", clicked_label)
        
#         # Update treemap based on the clicked label
#         update_treemap(clicked_label)

#         # Display the updated treemap
#         fig = px.treemap(st.session_state.df_chart, path=st.session_state.current_path, values='co2e_100yr', color='continent_ct')
#         st.plotly_chart(fig, use_container_width=True)





# import streamlit as st
# import plotly.express as px
# import pandas as pd
# from streamlit_plotly_events import plotly_events
# from streamlit.components.v1 import html


# # Load your DataFrame
# fname = 'ct_treemap_data.csv'
# df = pd.read_csv(fname)

# # Define all levels
# all_levels = ['sector', 'subsector', 'iso3_country']

# # Initialize session state
# if 'current_path' not in st.session_state:
#     st.session_state.current_path = ['sector', 'subsector']
# if 'selected_label' not in st.session_state:
#     st.session_state.selected_label = None

# # Function to generate the treemap figure
# def generate_treemap(df, path):
#     fig = px.treemap(df, path=path, values='co2e_100yr', color='continent_ct',
#                      title='Interactive Treemap with Two Levels Displayed')
#     fig.update_layout(
#         margin=dict(t=0, l=0, b=0, r=0),  # Remove margins around the treemap
#         paper_bgcolor='white',  # Background color of the paper
#         uniformtext_minsize=10,  # Minimum text size for labels
#         uniformtext_mode='hide',  # Hide text if it doesn't fit
#         clickmode='event+select'
#     )
#     fig.update_traces(
#         hovertemplate='%{label}<br>Value: %{value}<br>Percent of Total: %{percent.entry:.2%}',
#         textinfo='label+percent entry+value',
#         textfont_size=10,
#         marker=dict(
#             line=dict(width=0)  # Reduce outline width
#         )
#     )
#     st.session_state.fig = fig 
#     st.plotly_chart(fig, use_container_width=True)
#     return fig

# # Function to update the treemap based on selected label
# def update_treemap(selected_label):
#     # Determine the new path based on user clicks
#     clicked_level = None
#     for idx, p in enumerate(all_levels):
#         if selected_label in df[p].unique():
#             clicked_level = p
#             break

#     clicked_index = all_levels.index(clicked_level)
#     current_index = all_levels.index(st.session_state.current_path[-1]) if st.session_state.current_path else 0

#     if clicked_index == current_index:
#         if clicked_index == 0:
#             new_path = all_levels[clicked_index:clicked_index + 2]
#         elif clicked_index == len(all_levels) - 1:
#             new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#         else:
#             new_path = all_levels[clicked_index:clicked_index + 2]
#     elif clicked_index < current_index:  # Clicked on a higher level
#         if clicked_index == 0:
#             new_path = all_levels[clicked_index:clicked_index + 2]
#         else:
#             new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#     else:  # Clicked on a lower level
#         if clicked_index == len(all_levels) - 1:
#             new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#         else:
#             new_path = all_levels[clicked_index:clicked_index + 2]

#     new_path = new_path[:2]

#     # Filter DataFrame based on the selected level
#     df_chart = df.copy()
#     if clicked_index == 0:
#         pass
#     elif clicked_index == len(all_levels) - 1:
#         clicked_label_parent = df_chart[df_chart[st.session_state.current_path[-1]] == selected_label].iloc[0]['parent']
#         df_chart = df_chart[df_chart[new_path[0]] == clicked_label_parent]
#     else:
#         df_chart = df_chart[df_chart[all_levels[clicked_index]] == selected_label]

#     # Update session state with new path
#     st.session_state.current_path = new_path

#     # Generate and display the updated treemap
#     return generate_treemap(df_chart, new_path)

# # Display initial treemap
# fig = generate_treemap(df, st.session_state.current_path)

# selected_points = plotly_events(st.session_state.fig, click_event=True)
# if selected_points:
#     click_info = selected_points[0]
#     clicked_label = click_info.get('label')
#     st.session_state.selected_label = clicked_label

#     st.write("Selected Label:", click_info)

#     # Update treemap based on the clicked label
#     if clicked_label:
#         fig = update_treemap(clicked_label)
#         st.plotly_chart(fig, use_container_width=True)



# import streamlit as st
# import plotly.express as px
# import pandas as pd
# from streamlit_plotly_events import plotly_events
# from streamlit.components.v1 import html

# # Load your DataFrame
# fname = 'ct_treemap_data.csv'
# df = pd.read_csv(fname)

# # Define all levels
# all_levels = ['sector', 'subsector', 'iso3_country']

# # Initialize session state
# if 'current_path' not in st.session_state:
#     st.session_state.current_path = ['sector', 'subsector']
# if 'selected_label' not in st.session_state:
#     st.session_state.selected_label = None
# if 'fig' not in st.session_state:
#     st.session_state.fig = None

# # Function to generate the treemap figure
# def generate_treemap(df, path):
#     fig = px.treemap(df, path=path, values='co2e_100yr', color='continent_ct',
#                      title='Interactive Treemap with Two Levels Displayed')
#     fig.update_layout(
#         margin=dict(t=0, l=0, b=0, r=0),  # Remove margins around the treemap
#         paper_bgcolor='white',  # Background color of the paper
#         uniformtext_minsize=10,  # Minimum text size for labels
#         uniformtext_mode='hide',  # Hide text if it doesn't fit
#         clickmode='event+select'
#     )
#     fig.update_traces(
#         hovertemplate='%{label}<br>Value: %{value}<br>Percent of Total: %{percent.entry:.2%}',
#         textinfo='label+percent entry+value',
#         textfont_size=10,
#         marker=dict(
#             line=dict(width=0)  # Reduce outline width
#         )
#     )
#     return fig

# # Function to update the treemap based on selected label
# def update_treemap(selected_label):
#     # Determine the new path based on user clicks
#     clicked_level = None
#     for idx, p in enumerate(all_levels):
#         if selected_label in df[p].unique():
#             clicked_level = p
#             break

#     clicked_index = all_levels.index(clicked_level)
#     current_index = all_levels.index(st.session_state.current_path[-1]) if st.session_state.current_path else 0

#     if clicked_index == current_index:
#         if clicked_index == 0:
#             new_path = all_levels[clicked_index:clicked_index + 2]
#         elif clicked_index == len(all_levels) - 1:
#             new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#         else:
#             new_path = all_levels[clicked_index:clicked_index + 2]
#     elif clicked_index < current_index:  # Clicked on a higher level
#         if clicked_index == 0:
#             new_path = all_levels[clicked_index:clicked_index + 2]
#         else:
#             new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#     else:  # Clicked on a lower level
#         if clicked_index == len(all_levels) - 1:
#             new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
#         else:
#             new_path = all_levels[clicked_index:clicked_index + 2]

#     new_path = new_path[:2]

#     # Filter DataFrame based on the selected level
#     df_chart = df.copy()
#     if clicked_index == 0:
#         pass
#     elif clicked_index == len(all_levels) - 1:
#         clicked_label_parent = df_chart[df_chart[st.session_state.current_path[-1]] == selected_label].iloc[0]['parent']
#         df_chart = df_chart[df_chart[new_path[0]] == clicked_label_parent]
#     else:
#         df_chart = df_chart[df_chart[all_levels[clicked_index]] == selected_label]

#     # Update session state with new path
#     st.session_state.current_path = new_path

#     # Generate and return the updated treemap
#     return generate_treemap(df_chart, new_path)

# # Display initial or updated treemap
# if st.session_state.fig is None:
#     st.session_state.fig = generate_treemap(df, st.session_state.current_path)

# fig = st.session_state.fig
# # st.plotly_chart(fig, use_container_width=True)

# fig_json = fig.to_json()

# # clicked_label = st.components.v1.html(f"""
# # <div id="plotly-div"></div>
# # <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
# # <script>
# #     var plotly_data = {fig_json};
# #     var plotly_div = document.getElementById('plotly-div');
# #     Plotly.newPlot(plotly_div, plotly_data.data, plotly_data.layout);

# #     plotly_div.on('plotly_click', function(data) {{
# #         var clicked_label = data.points[0].label;
# #         document.getElementById('click-output').innerText = "You clicked on: " + clicked_label;

# #         // Send the clicked label back to Streamlit
# #         window.parent.postMessage({{
# #             type: "streamlit:setComponentValue",
# #             value: clicked_label
# #         }}, "*");
# #     }});
# # </script>
# # <div id="click-output">Click on a segment to see the label</div>
# # """, height=600)

# # # st.write("Last clicked label:", clicked_label)
# # clicked_label = st.text_input("Last clicked label:", clicked_label)

# html(f"""
#     <div id="plotly-div"></div>
#     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
#     <script>
#         var plotly_data = {fig_json};
#         var plotly_div = document.getElementById('plotly-div');
#         Plotly.newPlot(plotly_div, plotly_data.data, plotly_data.layout);

#         plotly_div.on('plotly_click', function(data) {{
#             var clicked_label = data.points[0].label;
#             document.getElementById('click-output').innerText = "You clicked on: " + clicked_label;

#             // Send the clicked label back to Streamlit
#             const message = {{
#                 type: "streamlit:setComponentValue",
#                 value: clicked_label
#             }};
#             window.parent.postMessage(message, "*");
#         }});
#     </script>
#     <div id="click-output">Click on a segment to see the label</div>
# """, height=600)

# clicked_label = st.text_input("Last clicked label:", "")
# st.write("You clicked on:", clicked_label)

# Display the clicked label in Streamlit
# clicked_label = st.text_input("Last clicked label:", clicked_label)

# import streamlit as st
# import plotly.express as px
# import pandas as pd

# # # Sample DataFrame
# fname = 'ct_treemap_data.csv'
# df = pd.read_csv(fname)

# # Create a Plotly treemap
# # fig = px.treemap(df, path=['sector', 'subsector'], values='co2e_100yr')
# fig = px.treemap(df, path=['sector', 'subsector'], values='co2e_100yr', color='continent_ct',
#                     title='Interactive Treemap with Two Levels Displayed')
# fig.update_layout(
#     margin=dict(t=0, l=0, b=0, r=0),  # Remove margins around the treemap
#     paper_bgcolor='white',  # Background color of the paper
#     uniformtext_minsize=10,  # Minimum text size for labels
#     uniformtext_mode='hide',  # Hide text if it doesn't fit
#     clickmode='event+select'
# )
# fig.update_traces(
#     hovertemplate='%{label}<br>Value: %{value}<br>Percent of Total: %{percent.entry:.2%}',
#     textinfo='label+percent entry+value',
#     textfont_size=10,
#     marker=dict(
#         line=dict(width=0)  # Reduce outline width
#     )
# )
# # Convert the figure to JSON
# fig_json = fig.to_json()

# # Embed Plotly chart with custom JavaScript to capture click events
# clicked_label = st.components.v1.html(f"""
# <div id="plotly-div"></div>
# <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
# <script>
#     var plotly_data = {fig_json};
#     var plotly_div = document.getElementById('plotly-div');
#     Plotly.newPlot(plotly_div, plotly_data.data, plotly_data.layout);

#     plotly_div.on('plotly_click', function(data) {{
#         var clicked_label = data.points[0].label;
#         document.getElementById('click-output').innerText = "You clicked on: " + clicked_label;
#         window.parent.postMessage(clicked_label, "*");
#     }});
# </script>
# <div id="click-output">Click on a segment to see the label</div>
# """, height=600)

# # Capture and display the clicked label in Streamlit
# clicked_label = st.text_input("Last clicked label:", clicked_label)



# import streamlit as st
# import plotly.express as px
# import pandas as pd
# from streamlit.components.v1 import html

# # Sample DataFrame
# df = pd.DataFrame({
#     "Category": ["A", "B", "C", "A", "B", "C"],
#     "Subcategory": ["X", "X", "X", "Y", "Y", "Y"],
#     "Value": [10, 20, 30, 40, 50, 60]
# })

# # Create a Plotly treemap
# fig = px.treemap(df, path=['Category', 'Subcategory'], values='Value')

# # Convert the figure to JSON
# fig_json = fig.to_json()

# # HTML/JS for Plotly and communication
# clicked_label = st.components.v1.html(f"""
#     <div id="plotly-div"></div>
#     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
#     <script>
#         var plotly_data = {fig_json};
#         var plotly_div = document.getElementById('plotly-div');
#         Plotly.newPlot(plotly_div, plotly_data.data, plotly_data.layout);

#         plotly_div.on('plotly_click', function(data) {{
#             var clicked_label = data.points[0].label;
#             document.getElementById('click-output').innerText = "You clicked on: " + clicked_label;

#             // Send the clicked label back to Streamlit
#             const message = {{
#                 type: "streamlit:setComponentValue",
#                 value: clicked_label
#             }};
#             window.parent.postMessage(message, "*");
#         }});
#     </script>
#     <div id="click-output">Click on a segment to see the label</div>
# """, height=600)

# # Display the clicked label
# st.write("Last clicked label:", clicked_label)

import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit.components.v1 import html

# Sample DataFrame
df = pd.DataFrame({
    "Category": ["A", "B", "C", "A", "B", "C"],
    "Subcategory": ["X", "X", "X", "Y", "Y", "Y"],
    "Value": [10, 20, 30, 40, 50, 60]
})

# Create a Plotly treemap
fig = px.treemap(df, path=['Category', 'Subcategory'], values='Value')

# Convert the figure to JSON
fig_json = fig.to_json()

# Initialize session state for clicked label if it doesn't exist
if 'clicked_label' not in st.session_state:
    st.session_state.clicked_label = "No label clicked yet"

# HTML/JS for Plotly and communication
html(f"""
    <div id="plotly-div"></div>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script>
        var plotly_data = {fig_json};
        var plotly_div = document.getElementById('plotly-div');
        Plotly.newPlot(plotly_div, plotly_data.data, plotly_data.layout);

        plotly_div.on('plotly_click', function(data) {{
            var clicked_label = data.points[0].label;
            document.getElementById('click-output').innerText = "You clicked on: " + clicked_label;

            // Send the clicked label back to Streamlit
            window.parent.Streamlit.setComponentValue(clicked_label);
        }});
    </script>
    <div id="click-output">Click on a segment to see the label</div>
""", height=600)

# Display the clicked label
st.write("Last clicked label:", st.session_state.clicked_label)

# Update session state when a new value is received
if st.session_state.get('component_value'):
    st.session_state.clicked_label = st.session_state.component_value

# Rerun the app to update the display
if st.session_state.clicked_label != "No label clicked yet":
    st.experimental_rerun()
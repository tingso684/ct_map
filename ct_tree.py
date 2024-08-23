import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px

fname = 'ct_treemap_data.csv'

df = pd.read_csv(fname)

# Initialize Dash app
app = dash.Dash(__name__)

# Initial figure with only two levels
fig = px.treemap(df, path=['sector', 'subsector'], values='co2e_100yr',color='continent_ct', title='Treemap with Two Levels Displayed')

fig.update_layout(
    margin=dict(t=0, l=0, b=0, r=0),  # Remove margins around the treemap
    paper_bgcolor='white',  # Background color of the paper
    uniformtext_minsize=10,  # Minimum text size for labels
    uniformtext_mode='hide'  # Hide text if it doesn't fit
)

fig.update_traces(
    hovertemplate='%{label}<br>Value: %{value}',
    textinfo='label+percent entry',

    # textinfo='label+percent entry',  # Show labels and percentage
    textfont_size=10,    
    marker=dict(
        line=dict(
            width=0  # Reduce outline width
        )
    )
)

app.layout = html.Div([
    dcc.Graph(
        id='treemap',
        figure=fig
    ),
    dcc.Store(id='current-path', data=['sector', 'subsector'])
])

@app.callback(
    [Output('treemap', 'figure'),
     Output('current-path', 'data')],
    [Input('treemap', 'clickData')],
    [State('current-path', 'data')]
)

def update_treemap(clickData, current_path):
    # Define possible paths
    all_levels = ['sector', 'subsector', 'iso3_country']
    
    # Determine the new path based on user clicks
    df_chart = df.copy()
    new_path = current_path
    clicked_label = None

    print("clicked")
    if clickData:
        print(clickData['points'])
        if 'label' in clickData['points'][0]:
            clicked_label = clickData['points'][0]['label']

            for idx, p in enumerate(all_levels):
                if clicked_label in df[p].unique():
                    clicked_level = p
                    break

            # Determine which level is clicked
            clicked_index = all_levels.index(clicked_level)
            current_index = all_levels.index(current_path[-1]) if current_path else 0
            
            if clicked_index == current_index: 
                if clicked_index == 0:
                    new_path = all_levels[clicked_index:clicked_index + 2]

                elif clicked_index == len(all_levels)-1:
                    new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]

                else:
                    new_path = all_levels[clicked_index:clicked_index + 2]


            elif clicked_index < current_index:  # Clicked on a higher level
                if clicked_index == 0:
                    new_path = all_levels[clicked_index:clicked_index + 2]
                else:
                    new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
            
            else:  # Clicked on a lower level
                if clicked_index == len(all_levels)-1:
                    new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
                else:
                    new_path = all_levels[clicked_index:clicked_index + 2]
                
            # Ensure new path does not exceed available levels
            new_path = new_path[:2]
            print(new_path)

    if clicked_label:
        print("clicked label", clicked_label)
        print("clicked index", clicked_index, current_index)
        print("Current path", current_path)
        print("New path", new_path)
        
        if clicked_index == 0:
            pass
        elif clicked_index == len(all_levels)-1:
            clicked_label_parent = clickData['points'][0]['parent']
            df_chart = df_chart[df_chart[new_path[0]] == clicked_label_parent]
            print('getting parent', clicked_label_parent, df_chart.shape)
        else:
            df_chart = df_chart[df_chart[all_levels[clicked_index]] == clicked_label]

        print(df_chart.shape)


    fig = px.treemap(df_chart, path=new_path, values='co2e_100yr',color='continent_ct', title='Interactive Treemap with Two Levels Displayed')    

    colors = {
        'sector': 'blue',
        'subsector': 'green',
        'iso3_country': 'red'
    }
    if new_path[-1] == all_levels[-1]:
        fig = px.treemap(df_chart, path=new_path, values='co2e_100yr',color='continent_ct', title='Interactive Treemap with Two Levels Displayed')    
    else:
        fig = px.treemap(df_chart, path=new_path, values='co2e_100yr',color_continuous_scale=[colors.get(p, 'grey') for p in new_path], title='Interactive Treemap with Two Levels Displayed')
        
    # Create new figure with updated path
    fig.update_layout(
        margin=dict(t=0, l=0, b=0, r=0),  # Remove margins around the treemap
        paper_bgcolor='white',  # Background color of the paper
        uniformtext_minsize=10,  # Minimum text size for labels
        uniformtext_mode='hide',  # Hide text if it doesn't fit
    )

    fig.update_traces(
        hovertemplate='%{label}<br>Value: %{value}<br>Percent of Total: %{percent.entry:.2%}',#'%{label}<br>Value: %{value}',
        textinfo='label+percent entry+value',
        textfont_size=10,    
        marker=dict(
            line=dict(
                width=0,  # Reduce outline width
            ),
        )
    )
    return fig, new_path

if __name__ == '__main__':
    app.run_server(debug=True)
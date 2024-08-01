import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from categories import APP_CATEGORIES, COLOR_MAP  # Import updated categories and color mapping

# Load and prepare the data
df = pd.read_csv("curated_crime.csv").dropna().reset_index()
# Create a list of unique times and holidays for dropdown options
times = sorted(df['Time Rounded'].unique())
holidays = sorted(df['Holiday'].unique())

# Initialize the Dash app
app = Dash(__name__)

# Set default map view to Cambridge MA
INITIAL_LAT = 42.3736
INITIAL_LON = -71.1097
INITIAL_ZOOM = 13

# Layout: This dictates all the interactables: including dropdowns checklists, sliders, and graphs
app.layout = html.Div([
    dcc.Dropdown( # category dropdwn
        id='category-dropdown',
        options=[{'label': cat, 'value': cat} for cat in APP_CATEGORIES.keys()],
        value='All Crimes',  # Default value
        placeholder="Select a crime category"  # Placeholder text
    ),
    dcc.Dropdown( #Holiday dropdown
        id='holiday-dropdown',
        options=[{'label': holiday, 'value': holiday} for holiday in holidays],
        value='Nonholiday',  # Default value
        placeholder="Filter by a holiday..."  # Placeholder text
    ),
    dcc.Checklist( # Buttons to enable or disable filters, for easily turning off filters
        id='filter-options',
        options=[
            {'label': 'Enable Holiday Filter', 'value': 'holiday'},
            {'label': 'Enable Time Filter', 'value': 'time'},
            {'label': 'Enable Year Filter', 'value': 'year'}
        ],
        value=['year'],  # Default values - Holiday and Time filters OFF and year ON
        inline=True
    ),
    dcc.Slider( #the time slider, to filter the data based on Year paramaters
        id='year-slider',
        min=2009,  # hard coded in 2009 because earlier data is too sparse
        max=df['Year Reported'].max(),
        value=df['Year Reported'].min(),
        marks={str(year): str(year) for year in df['Year Reported'].unique()},
        step=None
    ),
    dcc.Slider( #the time slider, to filter the data based on hourly paramaters
        id='time-slider',
        min=0,
        max=len(times) - 1,
        value=0,
        marks={i: time for i, time in enumerate(times)},
        step=1
    ),
    dcc.Graph(id='mapbox-graph'),
    dcc.Graph(id='bar-graph'),
    dcc.Markdown(id='crime-counts-list', style={'width': '30%', 'display': 'inline-block'})
])

# Callback decorator: to update the map and other elements based on dropdown and slider selections
@app.callback(
    [Output('mapbox-graph', 'figure'),
     Output('bar-graph', 'figure'),
     Output('crime-counts-list', 'children')],
    [Input('year-slider', 'value'),
     Input('category-dropdown', 'value'),
     Input('holiday-dropdown', 'value'),
     Input('time-slider', 'value'),
     Input('filter-options', 'value')]
)
# Update content is what drives filtered_df, where all mapbox and bargraph data is derived from
def update_content(selected_year, selected_category, selected_holiday, selected_time_index, filter_options):
    # Get the selected time based on the slider index
    selected_time = times[selected_time_index]

    if selected_category in APP_CATEGORIES:
        category_crimes = APP_CATEGORIES[selected_category]
        filtered_df = df[df['Crime'].isin(category_crimes)]
    else:
        filtered_df = df

    if 'year' in filter_options: #Based on year reported, not year of crime 
        filtered_df = filtered_df[filtered_df['Year Reported'] == selected_year]

    if 'holiday' in filter_options:
        filtered_df = filtered_df[filtered_df['Holiday'] == selected_holiday]

    if 'time' in filter_options:
        filtered_df = filtered_df[filtered_df['Time Rounded'] == selected_time]

    # Create the map figure
    map_title = f"{selected_category} - Interactive Map"
    if 'year' in filter_options:
        map_title += f" - {selected_year}"

    map_fig = px.scatter_mapbox(
    filtered_df,
    lon='Longitude',
    lat='Latitude',
    color='Crime',
    color_discrete_map=COLOR_MAP,
    zoom=INITIAL_ZOOM,
    width=1200,
    height=800,
    title=f"{selected_category if selected_category else 'All Crimes'}" +
          (f" - {selected_year}" if 'year' in filter_options and selected_year else ''),
    hover_name='Crime', # the title of the hover marker
    hover_data={
        'Latitude': True, 
        'Longitude': True, 
        'Crime': False,        # Exclude 'Crime' from hover data, it is already the name of the marker
        'Reporting Area' : True
    }
)   # locks the map even when filtered_df changes (because of uirevision) - not sure if this works
    map_fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_center={"lat": INITIAL_LAT, "lon": INITIAL_LON},
        uirevision='constant'
    )

    # Update the bar graph based on filtered data
    crime_counts = filtered_df['Crime'].value_counts().reset_index()
    crime_counts.columns = ['Crime', 'Count']
    bar_fig = px.bar(crime_counts,
                     x='Crime', y='Count',
                     color='Crime',
                     color_discrete_map=COLOR_MAP,
                     labels={'Crime': 'Crime', 'Count': 'Count'},
                     title=f"Crime Counts for {selected_category} - {selected_year}")

    # Create a Markdown list of crime counts
    crime_counts_list = "\n".join([f"{i + 1}. {count} counts of {crime}" for i, (crime, count) in enumerate(crime_counts.values)])
    
    return map_fig, bar_fig, crime_counts_list

# Run the Dash server
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

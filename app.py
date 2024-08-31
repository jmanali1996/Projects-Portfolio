import dash_mantine_components as dmc
from dash import Dash, html
from dash_iconify import DashIconify
from dash import html, Output, Input, callback

# INTRODUCTION
intro_div = html.Div([
    dmc.Image(src="https://i.postimg.cc/Pf9tTKxS/intro-pic.jpg", alt="intro pic", style={'width': '50%', 'max-width': '750px', 'marginLeft': 'auto', 'marginRight': 'auto'}),
    html.Br(),
    dmc.Text(children=[
        html.B("Greetings! I'm Manali Jain"), ", hailing from the vibrant city of Mumbai, Maharashtra, India. My academic journey "
        "led me through the realms of Psychology for my graduation, followed by a deep dive into the field of Health "
        "Data Science for my master's degree. With a professional trajectory spanning over three years, I've donned "
        "various hats, serving as a Business Data Analyst, Data Engineer, and Student Researcher."],
    size="sm",
    style={'color': 'white'},
    ),
    dmc.Text(
        "My passion lies in leveraging data science and analytics to catalyze transformative discoveries that resonate with "
        "the betterment of humanity. Beyond the world of data, I find solace and creativity in the art of crocheting. Much "
        "like life itself, crocheting starts as a jumble of yarn, but with patience and skill, transforms into a masterpiece. "
        "Indeed, life and work are akin to crafting intricate pieces of art, each with its unique beauty waiting to be unveiled.",
    size="sm",
    style={'color': 'white'},
    ),
    dmc.Text(
        "Feel free to peruse my resume, explore the diverse projects I've undertaken, and review reference letters from colleagues.",
    size="sm",
    style={'color': 'white'},
    ),
    html.Br(),
    dmc.Text(
        [
            "If you'd like to get in touch, drop me an email at ",
            html.A("jmanali1996@gmail.com", href='mailto:jmanali1996@gmail.com', target="_blank")
        ],
        size="sm",
        style={'color': 'white', 'italic': True, 'weight': 900},
    ),
    dmc.Text(
        "Socially, I'm active on:",
    size="sm",
    style={'color': 'white', 'italic': True, 'weight': 900},
    ),
    dmc.Group(
        justify="center", 
        children=[
            dmc.Group([
                html.A(
                    children=[
                        DashIconify(icon="mdi:linkedin", width=25), 
                        dmc.Text("LinkedIn", size='sm')
                    ],
                    href='https://www.linkedin.com/in/manalijain09',
                    target="_blank"
                )
            ],
                mt="md",
                mb="xs",
            ),
            dmc.Group([
                html.A(
                    children=[
                        DashIconify(icon="ion:logo-github", width=25), 
                        dmc.Text("GitHub", size='sm')
                    ],
                    href='https://github.com/jmanali1996',
                    target="_blank"
                )
            ],
            mt="md",
            mb="xs",
            ),
            dmc.Group([
                html.A(
                    children=[
                        DashIconify(icon="mdi:instagram", width=25), 
                        dmc.Text("Instagram", size='sm')
                    ],
                    href='https://instagram.com/mjain09',
                    target="_blank"
                )
            ],
            mt="md",
            mb="xs",
            ),
        ]
    ),
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20, 'text-align': 'center'}
)

# RESUME
resume_div = html.Div([
    html.Iframe(src="https://drive.google.com/file/d/1tafly6mUwfamh_-T_OovhCFQzV1RVo_K/preview",
                width="1000", height="1200")
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20, 'text-align': 'center'}
)

# PROJECTS 
pjcard1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/gJ73Mfcw/Stop-war.png",
                    alt="Civilian Conflicts",
                    style={'height': '250px', 'width': '100%', 'max-width': '400px'}
                ),
                href="https://drive.google.com/file/d/1CEVdcJOXywkzH2fslff8S4SqcMtHJuJL/preview",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Civilian Conflicts", size='xl', style={'color': 'white', 'weight': 500}),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/Civilian-Conflicts.git',
                    target="_blank"
                )
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "A multi-page dashboard visualizing global conflict-related fatalities. It highlights conflict details, causation, "
            "distribution, and overall impact. Data sourced from the Uppsala Conflict Data Program (UCDP).",
            size="sm",
            style={'color': 'white'}
        ),
        dmc.Text(
            children=[
                html.I("*Tap the image to view the walkthrough video")
            ],
            size="xs",
            style={'color': "white", "paddingTop": 5}
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '100%', 'max-width': '400px'}
)

pjcard2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/vmJttstq/artistvsart.webp",
                    alt="ARTISTvsAI",
                    style={'height': '250px', 'width': '100%', 'max-width': '400px'}
                ),
                href="https://drive.google.com/file/d/1GfFte2bt-sWwY6nz-j8ATkhNgm62Emy3/preview",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("ARTISTvsAI", size='xl', style={'color': 'white', 'weight': 500}),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/ARTISTvsAI.git',
                    target="_blank"
                )
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "This app supports the ARTIST vs AI campaign using neural style transfer principles by Mr. Shafik Quoraishee and "
            "frontend design by Ms. Manali Jain to stylize images and compare similarities.",
            size="sm",
            style={'color': 'white'}
        ),
        dmc.Text(
            children=[
                html.I("*Tap the image to view the walkthrough video")
            ],
            size="xs",
            style={'color': "white", "paddingTop": 5}
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '100%', 'max-width': '400px'}
)

pjcard3 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/cC8dcbns/columbia-wildfires.webp",
                    alt="Colombian Wildfires",
                    style={'height': '250px', 'width': '100%', 'max-width': '400px'}
                ),
                href="https://drive.google.com/file/d/1Bso3ZRwID-yydYzEs8V59fSDxu5fFunx/preview",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Colombian Wildfires", size='xl', style={'color': 'white', 'weight': 500}),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/Colombian-Wildfires.git',
                    target="_blank"
                )
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "A dashboard visualizes fire incidents in Colombia from 2000 to 2024, with filters, bar graphs, and an animated map. It helps "
            "users explore trends, identify high-risk areas, and understand the distribution of fires.",
            size="sm",
            style={'color': 'white'}
        ),
        dmc.Text(
            children=[
                html.I("*Tap the image to view the walkthrough video")
            ],
            size="xs",
            style={'color': "white", "paddingTop": 5}
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '100%', 'max-width': '400px'}
)

pjcard4 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/qvRkYh2x/chatbot.jpg",
                    alt="Wild Bird Fund Chatbot",
                    style={'height': '250px', 'width': '100%', 'max-width': '400px'}
                ),
                href="https://drive.google.com/file/d/1eRbEroHlh76xWbo9j1VjMxorANPhGr6K/preview",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Wild Bird Fund Chatbot", size='xl', style={'color': 'white', 'weight': 500}),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/WBF-Chatbot.git',
                    target="_blank"
                )
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "An AI chatbot built for the Wildbirdfund Nyc that can help save the lives of thousands of birds annually and can be used to "
            "reduce bird-glass collisions and offer help to injured birds.",
            size="sm",
            style={'color': 'white'}
        ),
        dmc.Text(
            children=[
                html.I("*Tap the image to view the walkthrough video")
            ],
            size="xs",
            style={'color': "white", "paddingTop": 5}
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '100%', 'max-width': '400px'}
)

pjcard5 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/SKCBhGbv/mmm.png",
                    alt="Multimorbidity Multistate Model",
                    style={'height': '250px', 'width': '100%', 'max-width': '400px'}
                ),
                href="https://www.slideshare.net/slideshows/multimorbidity-multistate-model/265530051",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Multimorbidity Multistate Model", size='xl', style={'color': 'white', 'weight': 500}),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/Multimorbidity-Multistate-Model.git',
                    target="_blank"
                )
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "My research focused on developing and validating a multi-state model to predict multimorbidity of cardiovascular disease, "
            "type 2 diabetes, and chronic kidney diseases.",
            size="sm",
            style={'color': 'white'}
        ),
        dmc.Text(
            children=[
                html.I("*Tap the image to view the presentation")
            ],
            size="xs",
            style={'color': "white", "paddingTop": 5}
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '100%', 'max-width': '400px'}
)

all_pjcards = html.Div(
    [
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(html.Div(pjcard1), span=4),
                dmc.GridCol(html.Div(pjcard2), span=4),
                dmc.GridCol(html.Div(pjcard3), span=4),
                dmc.GridCol(html.Div(pjcard4), span=4),
                dmc.GridCol(html.Div(pjcard5), span=4)
            ]
        )
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20, 'width': '90%', 'marginLeft': 'auto', 'marginRight': 'auto'}
)

# CERTIFICATES
head = dmc.TableThead(
    dmc.TableTr(
        [
            dmc.TableTh("Title"),
            dmc.TableTh("Organization"),
            dmc.TableTh("Year"),
            dmc.TableTh("Digital copy"),
        ]
    )
)

row1 = dmc.TableTr([
    dmc.TableTd("CPRD resource module training test"),
    dmc.TableTd("Clinical Practice Research Datalink (CPRD)"),
    dmc.TableTd("2023"),
    dmc.TableTd([
        dmc.Button("View", color = "gray", id = "CPRD-button"),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1N2x9ZjaFxlx1HJsCBGw6R3hfBfW3-Fas/preview", style={'height': '450px', 'width': '1400px'}),
            id = "CPRD-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])
row2 = dmc.TableTr([
    dmc.TableTd("Data Science & Business Analytics Core Module"),
    dmc.TableTd("Boston Institute of Analytics (BIA)"),
    dmc.TableTd("2019"),
    dmc.TableTd([
        dmc.Button("View", color = "gray", id = "BIA-button"),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1c5m_jOSt5l-Mou1GAme4D4BbunrhflhJ/preview", style={'height': '450px', 'width': '1400px'}),
            id = "BIA-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])
row3 = dmc.TableTr([
    dmc.TableTd("PH125.1x: Data Science: R Basics"),
    dmc.TableTd("HarvardX"),
    dmc.TableTd("2019"),
    dmc.TableTd([
        dmc.Button("View", color = "gray", id = "R-button"),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1Xs14mvQaM9pLYoNlmOHiRQ0Ecy9lu9PN/preview", style={'height': '450px', 'width': '1400px'}),
            id = "R-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])

body = dmc.TableTbody([row1, row2, row3]) 

cert_div = html.Div(
    [
        dmc.Table([head, body], verticalSpacing="md", highlightOnHover=True, style={"fontSize": 18})
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20}
)

# REFERENCES
refcard1 = dmc.Card(
    children=[
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(
                    dmc.CardSection(
                        dmc.Anchor(
                            dmc.Image(
                                src="https://i.postimg.cc/X75hLWmz/Charming-Data.webp",
                                alt="Charming Data Community",
                                style={'height': '200px', 'width':'400px'}
                            ),
                            href="https://charming-data.circle.so",
                            target="_blank"
                        )
                    ),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Stack([
                        dmc.Text("Mr. Adam Schroeder", size='xl', style={'color': 'white', 'weight': 500}),
                        dmc.Text(
                            "Founder",
                            size="md",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            children=[
                                html.I("*Tap the logo to visit the website")
                            ],
                            size="sm",
                            style={'color': "white"}
                        ),
                    ]),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Button(
                        dmc.Anchor(
                            "Recommendation Letter", 
                            href="https://drive.google.com/file/d/1odmD1v547BzKomPq7wBrhmAQjuvBWQR6/preview",
                            target="_blank"
                        ),
                        color = "gray",
                        style = {"position": "absolute", "bottom": 20}
                    ),
                    span=4
                )
            ]
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '1230px'}
)

refcard2 = dmc.Card(
    children=[
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(
                    dmc.CardSection(
                        dmc.Anchor(
                            dmc.Image(
                                src="https://i.postimg.cc/kgq0PZsM/uom.gif",
                                alt="The University of Manchester",
                                style={'height': '200px', 'width': '400px'}
                            ),
                            href="https://www.manchester.ac.uk",
                            target="_blank"
                        )
                    ),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Stack([
                        dmc.Text("Dr. David Jenkins", size='xl', style={'color': 'white', 'weight': 500}),
                        dmc.Text(
                            "Lecturer in Health Data Sciences",
                            size="md",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            "Examiner No. 2",
                            size="md",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            children=[
                                html.I("*Tap the logo to visit the website")
                            ],
                            size="sm",
                            style={'color': "white"}
                        )
                    ]),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Button(
                        dmc.Anchor(
                            "Dissertation Review", 
                            href="https://drive.google.com/file/d/1-JSS0bZw5AhBz7097LmVeORylKDizQQM/preview",
                            target="_blank"
                        ),
                        color = "gray",
                        style = {"position": "absolute", "bottom": 20}
                    ),
                    span=4
                )
            ]
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '1230px'}
)

refcard3 = dmc.Card(
    children=[
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(
                    dmc.CardSection(
                        dmc.Anchor(
                            dmc.Image(
                                src="https://i.postimg.cc/kgq0PZsM/uom.gif",
                                alt="The University of Manchester",
                                style={'height': '200px', 'width': '400px'}
                            ),
                            href="https://www.manchester.ac.uk",
                            target="_blank"
                        )
                    ),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Stack([
                        dmc.Text("Dr. Glen Martin", size='xl', style={'color': 'white', 'weight': 500}),
                        dmc.Text(
                            "Senior Lecturer in Health Data Sciences",
                            size="sm",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            "Examiner No. 1",
                            size="sm",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            "Supervisor",
                            size="sm",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            children=[
                                html.I("*Tap the logo to visit the website")
                            ],
                            size="xs",
                            style={'color': "white"}
                        )
                    ]),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Button(
                        dmc.Anchor(
                            "Dissertation Review", 
                            href="https://drive.google.com/file/d/1dYuKRtgVVY8FOvKf9cAZznKv5u-ytazD/preview",
                            target="_blank"
                        ),
                        color = "gray",
                        style = {"position": "absolute", "bottom": 20}
                    ),
                    span=4
                )
            ]
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '1230px'}
)

refcard4 = dmc.Card(
    children=[
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(
                    dmc.CardSection(
                        dmc.Anchor(
                            dmc.Image(
                                src="https://i.postimg.cc/d1knGfhS/Chistats.jpg",
                                alt="Chistats Labs Pvt. Ltd.",
                                style={'height': '200px', 'width': '400px'}
                            ),
                            href="https://chistats.ai",
                            target="_blank"
                        )
                    ),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Stack([
                        dmc.Text("Dr. Yogesh Karpate", size='xl', style={'color': 'white', 'weight': 500}),
                        dmc.Text(
                            "Founder",
                            size="md",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            "Chief Technology Officer",
                            size="md",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            children=[
                                html.I("*Tap the logo to visit the website")
                            ],
                            size="sm",
                            style={'color': "white"}
                        )
                    ]),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Button(
                        dmc.Anchor(
                            "Recommendation Letter", 
                            href="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview",
                            target="_blank"
                        ),
                        color = "gray",
                        style = {"position": "absolute", "bottom": 20}
                    ),
                    span=4
                )
                    
            ]
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '1230px'}
)

refcard5 = dmc.Card(
    children=[
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(
                    dmc.CardSection(
                        dmc.Anchor(
                            dmc.Image(
                                src="https://i.postimg.cc/rwRcxjCS/Hotmuggs.jpg",
                                alt="Hot Stuffs Pvt. Ltd.",
                                style={'height': '200px', 'width': '400px'}
                            ),
                            href="https://hotmuggs.com",
                            target="_blank"
                        )
                    ),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Stack([
                        dmc.Text("Mr. Rishi Jain", size='xl', style={'color': 'white', 'weight': 500}),
                        dmc.Text(
                            "Chief Marketing Officer",
                            size="sm",
                            style={'color': "white"},
                        ),
                        dmc.Text(
                            children=[
                                html.I("*Tap the logo to visit the website")
                            ],
                            size="xs",
                            style={'color': "white"}
                        )
                    ]),
                    span=4
                ),
                dmc.GridCol(
                    dmc.Button(
                        dmc.Anchor(
                            "Recommendation Letter", 
                            href="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview",
                            target="_blank"
                        ),
                        color = "gray",
                        style = {"position": "absolute", "bottom": 20}
                    ),
                    span=4
                )
                    
            ]
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={'width': '1230px'}
)

all_refcards = html.Div(
    [
        dmc.Grid(
            gutter="sm",
            children=[
                dmc.GridCol(html.Div(refcard1)),
                dmc.GridCol(html.Div(refcard2)),
                dmc.GridCol(html.Div(refcard3)),
                dmc.GridCol(html.Div(refcard4)),
                dmc.GridCol(html.Div(refcard5))
            ]
        )
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20, 'width': '90%', 'marginLeft': 'auto', 'marginRight': 'auto'}
)

# LAYOUT
app = Dash(__name__)
server = app.server
app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    withGlobalClasses=True,
    children=[
        dmc.Tabs(
            children=[
            dmc.TabsList(
                grow=True,
                children=[
                    dmc.TabsTab(dmc.Text([(html.B(html.I("Get to know me")))], size="md", style={'color': 'white'}), value="introduction"),
                    dmc.TabsTab(dmc.Text([(html.B(html.I("Resumé")))], size="md", style={'color': 'white'}), value="resume"),
                    dmc.TabsTab(dmc.Text([(html.B(html.I("Projects")))], size="md", style={'color': 'white'}), value="projects"),
                    dmc.TabsTab(dmc.Text([(html.B(html.I("Certificates")))], size="md", style={'color': 'white'}), value="certificates"),
                    dmc.TabsTab(dmc.Text([(html.B(html.I("Testimonials")))], size="md", style={'color': 'white'}), value="references"),
                ], style={"paddingTop": 5}
            ),
            dmc.TabsPanel(intro_div, value="introduction", pb="xs"),
            dmc.TabsPanel(resume_div, value="resume", pb="xs"),
            dmc.TabsPanel(children=all_pjcards, value="projects", pb="xs"),
            dmc.TabsPanel(cert_div, value="certificates", pb="xs"),
            dmc.TabsPanel(children=all_refcards, value="references", pb="xs"),
            ],
        value="introduction",
        color="white"
        )
    ]
)

# CPRD DRAWER CALLBACK
@callback(
    Output("CPRD-drawer", "opened"),
    Input("CPRD-button", "n_clicks"),
    prevent_initial_call=True,
)
def cprd_drawer(n_clicks):
    return True

# BIA DRAWER CALLBACK
@callback(
    Output("BIA-drawer", "opened"),
    Input("BIA-button", "n_clicks"),
    prevent_initial_call=True,
)
def bia_drawer(n_clicks):
    return True

# R DRAWER CALLBACK
@callback(
    Output("R-drawer", "opened"),
    Input("R-button", "n_clicks"),
    prevent_initial_call=True,
)
def r_drawer(n_clicks):
    return True

if __name__=='__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)

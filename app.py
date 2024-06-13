import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash, html
from dash_iconify import DashIconify

#INTRODUCTION
intro_div = html.Div([
    dmc.Image(src="https://i.postimg.cc/Pf9tTKxS/intro-pic.jpg", alt="intro pic", style={'width': '750px'}),
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
    dmc.Group(children=[
        dmc.Group(
                [
                    html.A(children=[
                        DashIconify(icon="mdi:linkedin", width=25), dmc.Text("LinkedIn", size='sm')],
                        href='www.linkedin.com/in/manalijain09',
                        target="_blank"
                    )
                ],
                align="left",
                mt="md",
                mb="xs",
        ),
        dmc.Group(
                [
                    html.A(children=[
                        DashIconify(icon="ion:logo-github", width=25), dmc.Text("GitHub", size='sm')],
                        href='https://github.com/jmanali1996',
                        target="_blank"
                    )
                ],
                align="left",
                mt="md",
                mb="xs",
        ),
        dmc.Group(
                [
                    html.A(children=[
                        DashIconify(icon="mdi:instagram", width=25), dmc.Text("Instagram", size='sm')],
                        href='https://instagram.com/mjain09',
                        target="_blank"
                    )
                ],
                align="left",
                mt="md",
                mb="xs",
        ),
        ]
    ),
    ],
    style={"paddingTop": 10, "paddingRight": 20}
)

#RESUME
resume_div = html.Div([
    html.Iframe(src="https://drive.google.com/file/d/1MtSStFAzQuNVBn1RAJfW4xmp8AiAsuD4/preview",
                width="1000", height="1200")
    ],
    style={"paddingTop": 20}
)

#PROJECTS
pjcard1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/qvRkYh2x/chatbot.jpg",
                    alt="Wild Bird Fund Chatbot",
                    style={'width': 350}
                ),
                href="https://wbf-chatbot.onrender.com",
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
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "A chatbot built for the Wildbirdfund Nyc that can help save the lives of thousands of birds annually and can be used to "
            "reduce bird-glass collisions and offer help to injured birds.",
            size="sm",
            style={'color': 'white'},
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

pjcard2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/SKCBhGbv/mmm.png",
                    alt="Multimorbidity Multistate Model",
                    style={'width': '350px'}
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
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "My research focused on developing and validating a multi-state model to predict multimorbidity of cardiovascular disease, "
            "type 2 diabetes, and chronic kidney diseases.",
            size="sm",
            style={'color': 'white'},
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

all_pjcards = [
    dmc.Text(
        "Data Analysis and AI Projects",
        style={'height': 80, "fontSize": 40, "color": "white"},
#        children=[dmc.Text("Data Analysis and AI Projects",
#                           style={"fontSize": 40, "color": "white"})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        style=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(pjcard1),
            html.Div(pjcard2)
        ],
    )
]

#CERTIFICATES
header = [
    html.Thead(
        html.Tr(
            [
                html.Th("Title"),
                html.Th("Organization"),
                html.Th("Year"),
                html.Th("Digital copy"),
            ]
        )
    )
]

row1 = html.Tr([
    html.Td("CPRD resource module training test"),
    html.Td("Clinical Practice Research Datalink (CPRD)"),
    html.Td("2023"),
    html.Td(
        dbc.Button("View", href="https://drive.google.com/file/d/1N2x9ZjaFxlx1HJsCBGw6R3hfBfW3-Fas/preview", target="_blank")
    )
])
row2 = html.Tr([
    html.Td("Data Science & Business Analytics Core Module"),
    html.Td("Boston Institute of Analytics (BIA)"),
    html.Td("2019"),
    html.Td(
        dbc.Button("View", href="https://drive.google.com/file/d/1c5m_jOSt5l-Mou1GAme4D4BbunrhflhJ/preview", target="_blank")
    )
])
row3 = html.Tr([
    html.Td("PH125.1x: Data Science: R Basics"),
    html.Td("HarvardX"),
    html.Td("2019"),
    html.Td(
        dbc.Button("View", href="https://drive.google.com/file/d/1Xs14mvQaM9pLYoNlmOHiRQ0Ecy9lu9PN/preview", target="_blank")
    )
])

body = [html.Tbody([row1, row2, row3])]

cert_div = html.Div([
    dmc.Table(header + body)
    ],
    style={"paddingTop": 40, "paddingRight": 40}
)

#REFERENCES
refcard1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/X75hLWmz/Charming-Data.webp",
                alt="Charming Data Community",
                style={'width':'350px'}
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Mr. Adam Schroeder", size='xl', style={'color': 'white', 'weight': 500})
            ],
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Founder",
            size="sm",
            style={'color': "white"},
        ),
        html.Br(),
        dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1odmD1v547BzKomPq7wBrhmAQjuvBWQR6/preview",
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

refcard2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/kgq0PZsM/uom.gif",
                alt="The University of Manchester",
                style={'width': '350px'}
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Dr. David Jenkins", size='xl', style={'color': 'white', 'weight': 500})
            ],
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Lecturer in Health Data Sciences/Examiner No. 2",
            size="sm",
            style={'color': 'white'},
        ),
        html.Br(),
        dbc.Button("Dissertation Review", href="https://drive.google.com/file/d/1-JSS0bZw5AhBz7097LmVeORylKDizQQM/preview",
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

refcard3 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/kgq0PZsM/uom.gif",
                alt="The University of Manchester",
                style={'width': '350px'}
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Dr. Glen Martin", size='xl', style={'color': 'white', 'weight': 500})
            ],
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Senior Lecturer in Health Data Sciences/Examiner No. 1/Supervisor",
            size="sm",
            style={'color': 'white'},
        ),
        html.Br(),
        dbc.Button("Dissertation Review", href="https://drive.google.com/file/d/1dYuKRtgVVY8FOvKf9cAZznKv5u-ytazD/preview",
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

refcard4 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/BnBP9JkY/Chistats.jpg",
                alt="Chistats Labs Pvt. Ltd.",
                style={'width': '350px'}
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Dr. Yogesh Karpate", size='xl', style={'color': 'white', 'weight': 500})
            ],
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Founder/Chief Technology Officer",
            size="sm",
            style={'color': 'white'},
        ),
        html.Br(),
        dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview",
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

refcard5 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/rwRcxjCS/Hotmuggs.jpg",
                alt="Hot Stuffs Pvt. Ltd.",
                style={'width': '350px'}
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Mr. Rishi Jain", size='xl', style={'color': 'white', 'weight': 500})
            ],
            align="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Chief Marketing Officer",
            size="sm",
            style={'color': 'white'},
        ),
        html.Br(),
        dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview",
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

all_refcards = [
    dmc.Text(
        "Recommendation notes and letters",
        style={'height': 80, "fontSize": 40, "color": "white"},
#        children=[dmc.Text("Recommendation notes and letters",
#                           style={"fontSize": 40, 'color': 'white'})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        style=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(refcard1),
            html.Div(refcard2),
            html.Div(refcard3),
            html.Div(refcard4),
            html.Div(refcard5)
        ],
    )
]

#LAYOUT
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])
server = app.server
ct = {"colorScheme": "dark"}
app.layout = dmc.MantineProvider(
    theme=ct,
    withGlobalClasses=True,
    children=[
            dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.TabsTab("Get to know me", value="introduction"),
                    dmc.TabsTab("Resumé", value="resume"),
                    dmc.TabsTab("Projects", value="projects"),
                    dmc.TabsTab("Certificates", value="certificates"),
                    dmc.TabsTab("Testimonials", value="references"),
                ], style={"paddingRight": 50, "paddingTop": 15}
            ),
            dmc.TabsPanel(intro_div, value="introduction", pb="xs"),
            dmc.TabsPanel(resume_div, value="resume", pb="xs"),
            dmc.TabsPanel(children=all_pjcards, value="projects", pb="xs"),
            dmc.TabsPanel(cert_div, value="certificates", pb="xs"),
            dmc.TabsPanel(children=all_refcards, value="references", pb="xs"),
        ],
        value="introduction",
        orientation='vertical',
        variant='pills',
    )
])


if __name__=='__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)

# These first 3 lines of code are needed when running the app in https://wasmdash.vercel.app/
# import micropip
# await micropip.install('dash-mantine-components')
# await micropip.install('dash-iconify')
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash_iconify import DashIconify

intro_div = html.Div([
    html.Iframe(src="https://i.postimg.cc/hvXX5kRm/IMG-20230921-WA0002.jpg",
                width="1400", height="700")
    ],
    style={"paddingTop": 40}                
)

resume_div = html.Div([
    html.Iframe(src="https://drive.google.com/file/d/1u90zM7WbGaVLAl6sdr3tnKaX-CUrVzIw/preview",
                width="1000", height="1200")
    ],
    style={"paddingTop": 40}
)

pjcard1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/gkX18svb/chatbot.jpg",
                    alt="Wild Bird Fund Chatbot",
                ),
                href="https://wbf-chatbot.onrender.com",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Wild Bird Fund Chatbot", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/WBF-Chatbot.git',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "A chatbot built for the Wildbirdfund Nyc that can help save the lives of thousands of birds annually and can be used to reduce bird-glass collisions and offer help to injured birds.",
            size="sm",
            color="dimmed",
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
                    src="https://i.postimg.cc/CL3VdXnq/mmm.png",
                    alt="Multimorbidity Multistate Model",
                ),
                href="https://www.slideshare.net/slideshows/multimorbidity-multistate-model/265530051",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Multimorbidity Multistate Model", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996/Multimorbidity-Multistate-Model.git',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "The study focused on developing and validating a multi-state model to predict multimorbidity of cardiovascular disease, type 2 diabetes, and chronic kidney diseases.",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

#card3 = dmc.Card(
#    children=[
#        dmc.CardSection(
#            dmc.Anchor(
#                dmc.Image(
#                    src="https://i.im.ge/2024/01/11/3xar3p.your-project-filler.png",
#                    alt="dash-app",
#                ),
#                href="https://charming-data.com/",
#                target="_blank"
#            ),
#        ),
#        dmc.Group(
#            [
#                dmc.Text("Your Project Title", weight=500, size='xl'),
#                html.A(
#                    DashIconify(icon="skill-icons:linkedin", width=30),
#                    href='https://www.linkedin.com/in/adam-schroeder-17b5a819/',
#                    target="_blank"
#                )
#            ],
#            position="apart",
#            mt="md",
#            mb="xs",
#        ),
#        dmc.Text(
#            "Your project description to share with the viewers of your portfolio.",
#            size="sm",
#            color="dimmed",
#        ),
#    ],
#    withBorder=True,
#    shadow="sm",
#    radius="md",
#    style={"width": 350},
#)

all_pjcards = [
    dmc.Header(
        height=80,
        children=[dmc.Text("Data Analysis and AI Projects",
                           style={"fontSize": 40})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        breakpoints=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(pjcard1),
            html.Div(pjcard2)
            #html.Div(card3),
        ],
    )
]

cs_field = "https://www.f6s.com/content-resource/profiles/2595505_original.jpg"
refcard1 = dbc.Card(
    [
        dbc.CardImg(src=cs_field),
        dbc.CardImgOverlay([
            html.H2("Dr. Yogesh Karpate"),
            html.H3("Founder/Chief Technology Officer"),
            dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview"),
        ])

    ],
    style={"maxWidth": 500},
    className="my-4 text-center text-black"
)

hm_field = "https://hotmuggs.com/cdn/shop/files/Hot_Muggs_3D_Wall_Gold_Logo.jpg?v=1641220143"
refcard2 = dbc.Card(
    [
        dbc.CardImg(src=cs_field),
        dbc.CardImgOverlay([
            html.H2("Mr. Rishi Jain"),
            html.H3("Chief Marketing Officer"),
            dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview"),
        ])

    ],
    style={"maxWidth": 500},
    className="my-4 text-center text-black"
)


#refcard1 = dmc.Card(
#    children=[
#        dmc.CardSection(
#            dmc.Anchor(
#                dmc.Image(
#                    src="https://www.f6s.com/content-resource/profiles/2595505_original.jpg",
#                    alt="Chistats Labs Pvt. Ltd.",
#                ),
#                href="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview",
#                target="_blank"
#            ),
#        ),
#        dmc.Group(
#            [
#                dmc.Text("Dr. Yogesh Karpate", weight=500, size='xl')
#            ],
#            position="apart",
#            mt="md",
#            mb="xs",
#        ),
#        dmc.Text(
#            "Founder/Chief Technology Officer",
#            size="sm",
#            color="dimmed",
#        ),
#    ],
#    withBorder=True,
#    shadow="sm",
#    radius="md",
#    style={"width": 350},
#)

#refcard2 = dmc.Card(
#    children=[
#        dmc.CardSection(
#            dmc.Anchor(
#                dmc.Image(
#                    src="https://hotmuggs.com/cdn/shop/files/Hot_Muggs_3D_Wall_Gold_Logo.jpg?v=1641220143",
#                    alt="Hot Stuffs Pvt. Ltd.",
#                ),
#                href="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview",
#                target="_blank"
#            ),
#        ),
#        dmc.Group(
#            [
#                dmc.Text("Mr. Rishi Jain", weight=500, size='xl')
#            ],
#            position="apart",
#            mt="md",
#            mb="xs",
#        ),
#        dmc.Text(
#            "Chief Marketing Officer",
#            size="sm",
#            color="dimmed",
#        ),
#    ],
#    withBorder=True,
#    shadow="sm",
#    radius="md",
#    style={"width": 350},
#)

#reference_card = html.Div([
#    dmc.Card(
#        children=[
#            dmc.Text("Marge Simpson", weight=500, size='xl'),
#            dmc.Text(
#                "Pretzel business Owner",
#                size="md",
#                mb="xs",
#            ),
#            dmc.Text(
#                "when a man's biggest dreams include seconds on dessert, occasional snuggling and sleeping in til noon on weekends, no one man can destroy them.",
#                size="sm",
#                color="dimmed",
#            ),
#        ],
#        withBorder=True,
#        shadow="sm",
#        radius="md",
#        style={"width": 350})
#    ],
#    style={"paddingTop": 40}
#)

all_refcards = [
    dmc.Header(
        height=80,
        children=[dmc.Text("Former employers' reference letters",
                           style={"fontSize": 40})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        breakpoints=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(refcard1),
            html.Div(refcard2)
        ],
    )
]

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])
server = app.server
app.layout = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    children=[
            dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.Tab("Introduction", value="introduction"),
                    dmc.Tab("Resumé", value="resume"),
                    dmc.Tab("Projects", value="projects"),
                    dmc.Tab("References", value="references"),
                ], style={"paddingRight": 50, "paddingTop": 15}
            ),
            dmc.TabsPanel(intro_div, value="introduction", pb="xs"),
            dmc.TabsPanel(resume_div, value="resume", pb="xs"),
            dmc.TabsPanel(children=all_pjcards, value="projects", pb="xs"),
            dmc.TabsPanel(children=all_refcards, value="references", pb="xs"),
        ],
        value="projects",
        orientation='vertical',
        variant='pills',
    )
])


if __name__=='__main__':
    app.run_server(debug=False)

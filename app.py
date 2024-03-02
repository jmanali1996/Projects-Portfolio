# These first 3 lines of code are needed when running the app in https://wasmdash.vercel.app/
# import micropip
# await micropip.install('dash-mantine-components')
# await micropip.install('dash-iconify')
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash_iconify import DashIconify

intro_div = html.Div([
    dmc.Image(src="https://i.postimg.cc/Pf9tTKxS/intro-pic.jpg", alt="intro pic", width=650),
    html.Br(),
    dmc.Text(
        "Greetings! I'm Manali Jain, hailing from the vibrant city of Mumbai, Maharashtra, India. My academic journey "
        "led me through the realms of Psychology for my graduation, followed by a deep dive into the field of Health "
        "Data Science for my master's degree. With a professional trajectory spanning over three years, I've donned "
        "various hats, serving as a Business Data Analyst, Data Engineer, and Student Researcher.",
    size="sm",
    color="white",
    ),
    dmc.Text(
        "My passion lies in leveraging data science and analytics to catalyze transformative discoveries that resonate with "
        "the betterment of humanity. Beyond the world of data, I find solace and creativity in the art of crocheting. Much "
        "like life itself, crocheting starts as a jumble of yarn, but with patience and skill, transforms into a masterpiece. "
        "Indeed, life and work are akin to crafting intricate pieces of art, each with its unique beauty waiting to be unveiled.",
    size="sm",
    color="white",
    ),
    dmc.Text(
        "Feel free to peruse my resume, explore the diverse projects I've undertaken, and review reference letters from colleagues.",
    size="sm",
    color="white",
    ),
    dmc.Text(
        "If you'd like to get in touch, drop me an email at ",
        html.A("jmanali1996@gmail.com", href='mailto:jmanali1996@gmail.com', target="_blank"),
    size="sm",
    color="white",
    weight=900,
    ),
    dmc.Text(
        "Socially, I'm active on:",
    size="sm",
    color="white",
    ),
    dmc.Group(
            [
                html.A(
                    DashIconify(icon="mdi:linkedin", width=30),
                    href='www.linkedin.com/in/manalijain09',
                    target="_blank"
                ),
                dmc.Text("LinkedIn", size='sm')
            ],
            position="left",
            mt="md",
            mb="xs",
    ),
    dmc.Group(
            [
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/jmanali1996',
                    target="_blank"
                ),
                dmc.Text("GitHub", size='sm')
            ],
            position="left",
            mt="md",
            mb="xs",
    ),
    dmc.Group(
            [
                html.A(
                    DashIconify(icon="mdi:instagram", width=30),
                    href='https://instagram.com/mjain09',
                    target="_blank"
                ),
                dmc.Text("Instagram", size='sm')
            ],
            position="left",
            mt="md",
            mb="xs",
    ),
    ],
    style={"paddingTop": 10, "paddingRight": 20}                
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
                    src="https://i.postimg.cc/qvRkYh2x/chatbot.jpg",
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
            "A chatbot built for the Wildbirdfund Nyc that can help save the lives of thousands of birds annually and can be used to " 
            "reduce bird-glass collisions and offer help to injured birds.",
            size="sm",
            color="white",
        ),
        dmc.Text(
            "Please be patient while the app loads as it uses a free server and advanced AI integrations.",
            size="sm",
            color="white",
            italic=True,
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    color="white",
    style={"width": 350},
)

pjcard2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.postimg.cc/SKCBhGbv/mmm.png",
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
            "My research focused on developing and validating a multi-state model to predict multimorbidity of cardiovascular disease, " 
            "type 2 diabetes, and chronic kidney diseases.",
            size="sm",
            color="white",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    color="white",
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
#            color="white",
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

#cs_field = "https://www.f6s.com/content-resource/profiles/2595505_original.jpg"
#refcard1 = dbc.Card(
#    [
#        dbc.CardImg(src=cs_field),
#        dbc.CardImgOverlay([
#            html.H2("Dr. Yogesh Karpate"),
#            html.H3("Founder/Chief Technology Officer"),
#            dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview", target="_blank"),
#        ])
#    ],
#    style={"maxWidth": 500},
#    className="my-4 text-center text-black"
#)

#hm_field = "https://hotmuggs.com/cdn/shop/files/Hot_Muggs_3D_Wall_Gold_Logo.jpg?v=1641220143"
#refcard2 = dbc.Card(
#    [
#        dbc.CardImg(src=hm_field),
#        dbc.CardImgOverlay([
#            html.H2("Mr. Rishi Jain"),
#            html.H3("Chief Marketing Officer"),
#            dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview", target="_blank"),
#        ])
#    ],
#    style={"maxWidth": 500},
#    className="my-4 text-center text-black"
#)

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
    color="white",
    style={"paddingTop": 40}             
)

refcard1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/q75JbvT1/uom.png",
                alt="The University of Manchester"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Dr. David Jenkins", weight=500, size='xl')
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Lecturer in Health Data Sciences/Examiner No. 2",
            size="sm",
            color="white",
        ),
        html.Br(),
        dbc.Button("Dissertation Review", href="https://drive.google.com/file/d/1-JSS0bZw5AhBz7097LmVeORylKDizQQM/preview", 
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    color="white",
    style={"width": 350},
)

refcard2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/q75JbvT1/uom.png",
                alt="The University of Manchester"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Dr. Glen Martin", weight=500, size='xl')
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Senior Lecturer in Health Data Sciences/Examiner No. 1/Supervisor",
            size="sm",
            color="white",
        ),
        html.Br(),
        dbc.Button("Dissertation Review", href="https://drive.google.com/file/d/1dYuKRtgVVY8FOvKf9cAZznKv5u-ytazD/preview", 
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    color="white",
    style={"width": 350},
)

refcard3 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/XJLR7kCP/Chistats.png",
                alt="Chistats Labs Pvt. Ltd."
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Dr. Yogesh Karpate", weight=500, size='xl')
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Founder/Chief Technology Officer",
            size="sm",
            color="white",
        ),
        html.Br(),
        dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview", 
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    color="white",
    style={"width": 350},
)

refcard4 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://i.postimg.cc/L8swN1Gk/Hotmuggs.png",
                alt="Hot Stuffs Pvt. Ltd."
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Mr. Rishi Jain", weight=500, size='xl')
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Chief Marketing Officer",
            size="sm",
            color="white",
        ),
        html.Br(),
        dbc.Button("Reference Letter", href="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview", 
                   target="_blank")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    color="white",
    style={"width": 350},
)

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
#                color="white",
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
        children=[dmc.Text("Recommendation notes and letters",
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
            html.Div(refcard2),
            html.Div(refcard3),
            html.Div(refcard4)
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
                    dmc.Tab("Get to know me", value="introduction"),
                    dmc.Tab("Resumé", value="resume"),
                    dmc.Tab("Projects", value="projects"),
                    dmc.Tab("Certificates", value="certificates"),
                    dmc.Tab("Testimonials", value="references"),
                ], color="white", style={"paddingRight": 50, "paddingTop": 15}
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
    app.run_server(debug=False)

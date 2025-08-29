import dash_mantine_components as dmc
from dash import Dash, html, dcc, Output, Input, callback
from dash_iconify import DashIconify

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
    dcc.Download(id="download-cv"),  
    dmc.Button(
        "Download CV",
        id="download-button",
        variant="filled",
        style={"position": "fixed", "left": "80%", "transform": "translateX(-50%)", "backgroundColor": "white", "color": "black"}
    ),
    dmc.Text(
        children=[html.U(html.B("Skills"))],
        size="xl",
        style={'color': 'white'}
    ),
    dmc.Text(
        children=[html.B("Data Analysis - Data Management - Data Visualization - Machine Learning and AI - Microsoft Office - Microsoft Power BI - Tableau - R programming - Python - SQL")],
        size="md",
        style={'color': 'white', 'marginBottom': 20}
    ),
    dmc.Text(
        children=[html.U(html.B("Work experience"))],
        size="xl",
        style={'color': 'white'}
    ),
    dmc.Accordion(
        children=[
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Text(
                            children=[html.B("Clinical Data Analyst: "), html.A("Umbizo, Manchester, England, UK", href="https://www.umbizo.co.uk/", target="_blank"), html.I(" (July 2025 - Present)")],
                            size="md",
                            style={'color': 'white'}
                        )
                    ),
                    dmc.AccordionPanel(
                        [
                            dmc.Text(
                                "> Completed project-based assessment to demonstrate ability to understand and execute clinical data analysis tasks effectively and efficiently.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Applied core bioinformatics and data analysis skills on real-world datasets, showcasing aptitude for species identification research and data interpretation.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Gained exposure to clinical data workflows and contributed to project deliverables aligned with organizational expectations.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                        ]
                    )
                ],
                value="umbizo"
            ),
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Text(
                            children=[html.B("Cochrane Member (Health Data Analyst): "), html.A("Cochrane, Global", href="https://www.cochrane.org/", target="_blank"), html.I(" (October 2024 - Present)")],
                            size="md",
                            style={'color': 'white'}
                        )
                    ),
                    dmc.AccordionPanel(
                        [
                            dmc.Text(
                                "> Led screening of over 2,000 research records, improving systematic review processes.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Developed blogshots translating complex medical research into accessible summaries for wider audiences.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Assisted in early-stage classification of randomized controlled trials, enhancing evidence synthesis quality.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Contributed to global initiatives fostering reliable, evidence-based healthcare decision-making.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                        ]
                    )
                ],
                value="cochrane"
            ),
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Text(
                            children=[html.B("Community Moderator (Data Analyst): "), html.A("Charming Data Community, Global", href="https://charming-data.circle.so/", target="_blank"), html.I(" (January 2024 — September 2024)")],
                            size="md",
                            style={'color': 'white'}
                        )
                    ),
                    dmc.AccordionPanel(
                        [
                            dmc.Text(
                                "> Managed and resolved 500+ data analysis inquiries, fostering knowledge exchange.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Enforced community guidelines, reducing spam and irrelevant content by 20%.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                            dmc.Text(
                                "> Analyzed user data to implement 3 new engagement features, increasing activity by 30%.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                            dmc.Text(
                                "> Facilitated communication between users and data teams, integrating 5 requested features.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                        ]
                    )
                ],
                value="charmingdata"
            ),
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Text(
                            children=[html.B("Disability Student Researcher: "), html.A("The University of Manchester Student's Union, Manchester, England, UK", href="https://manchesterstudentsunion.com/", target="_blank"), html.I(" (April 2023 — June 2023)")],
                            size="md",
                            style={'color': 'white'}
                        )
                    ),
                    dmc.AccordionPanel(
                        [
                            dmc.Text(
                                "> Analyzed survey data to identify challenges for disabled students.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Presented research findings at a major university conference.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                        ]
                    )
                ],
                value="manchester"
            ),
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Text(
                            children=[html.B("Data Engineer: "), html.A("Chistats Labs Pvt. Ltd., Pune, Maharashtra, India", href="https://chistats.ai/", target="_blank"), html.I(" (August 2020 — July 2022)")],
                            size="md",
                            style={'color': 'white'}
                        )
                    ),
                    dmc.AccordionPanel(
                        [
                            dmc.Text(
                                "> Led machine learning model deployments, improving process efficiency by 30%.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Enhanced project completion rates by approximately 25% through improved workflows.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                            dmc.Text(
                                "> Provided timely project updates, reducing deadline risks by 20%.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                            dmc.Text(
                                "> Ensured data selection met client specifications for diverse operational needs.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                        ]
                    )
                ],
                value="chistats"
            ),
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(
                        dmc.Text(
                            children=[html.B("Business Data Analyst: "), html.A("Hot Stuffs Pvt. Ltd., Mumbai, Maharashtra, India", href="https://hotmuggs.com/", target="_blank"), html.I(" (November 2019 — July 2020)")],
                            size="md",
                            style={'color': 'white'}
                        )
                    ),
                    dmc.AccordionPanel(
                        [
                            dmc.Text(
                                "> Designed visual dashboards to support data-driven decision-making.",
                                size="sm",
                                style={'color': 'white'}        
                            ),
                            dmc.Text(
                                "> Conducted training for business users, enhancing data-informed actions by 15%.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                            dmc.Text(
                                "> Managed social media accounts, increasing engagement by 10%.",
                                size="sm",
                                style={'color': 'white'}
                            ),
                        ]
                    )
                ],
                value="hotstuffs"
            ),
        ],
        variant="contained",
        radius="md",
        style={"marginBottom": 20}
    ),
    dmc.Text(
        children=[html.U(html.B("Education"))],
        size="xl",
        style={'color': 'white'}
    ),
    dmc.List(
        spacing="md",
        size="sm",
        center=False,
        icon=DashIconify(icon="mdi:school", width=24, color="white"),
        children=[
            dmc.ListItem(
                [
                    dmc.Text(
                        children=[html.B("MSc Health Data Science — The University of Manchester, Manchester, England, UK")],
                        size="md",
                        style={'color': 'white'}
                    ),
                    dmc.Text(
                        children=[html.I("December 2023")],
                        size="sm",
                        style={'color': 'white'}
                    ),
                    dmc.Text(
                        "Thesis topic: Multi-state multimorbidity prediction model, focused on cardiovascular disease, type 2 diabetes, and chronic kidney diseases.",
                        size="sm",
                        style={'color': 'white'}        
                    ),
                    dmc.Text(
                        "Supervisors: Dr Alexander Pate and Dr Glen P Martin",
                        size="sm",
                        style={'color': 'white'}
                    ),
                ]
            ),
            dmc.ListItem(
                [
                    dmc.Text(
                        children=[html.B("BA Psychology — Mithibai College of Arts, Mumbai University, Mumbai, Maharashtra, India")],
                        size="md",
                        style={'color': 'white'}
                    ),
                    dmc.Text(
                        children=[html.I("March 2018")],
                        size="sm",
                        style={'color': 'white'}
                    ),
                ]
            ),
        ],
        style={'marginBottom': 20}
    ),
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20}
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
        dmc.Flex(
            [
                html.Div(pjcard1),
                html.Div(pjcard2),
                html.Div(pjcard3)
            ],
            direction={"base": "column", "sm": "row"},
            gap={"base": "sm", "sm": "lg"},
            justify={"sm": "center"},
            style={"paddingBottom": 10}
        ),
        dmc.Flex(
            [
                html.Div(pjcard4),
                html.Div(pjcard5)
            ],
            direction={"base": "column", "sm": "row"},
            gap={"base": "sm", "sm": "lg"},
            justify={"sm": "center"},
            style={"paddingBottom": 10}
        )
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20}
)

# CERTIFICATES
head = dmc.TableThead(
    dmc.TableTr(
        [
            dmc.TableTh(html.U("Title")),
            dmc.TableTh(html.U("Organization")),
            dmc.TableTh(html.U("Year")),
            dmc.TableTh(html.U("Digital copy")),
        ]
    )
)

row1 = dmc.TableTr([
    dmc.TableTd("Data Science using Gen AI and Python"),
    dmc.TableTd("Scaler"),
    dmc.TableTd("2024"),
    dmc.TableTd([
        dmc.Button("View", id = "GenAI-button", variant="filled", style={"backgroundColor": "white", "color": "black"}),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1GsU1rtCAGo1F1hX1uY6BCxAt-vPOz8JL/preview", style={'height': '450px', 'width': '100%', 'max-width': '1400px'}),
            id = "GenAI-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])
row2 = dmc.TableTr([
    dmc.TableTd("CPRD resource module training test"),
    dmc.TableTd("Clinical Practice Research Datalink (CPRD)"),
    dmc.TableTd("2023"),
    dmc.TableTd([
        dmc.Button("View", id = "CPRD-button", variant="filled", style={"backgroundColor": "white", "color": "black"}),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1N2x9ZjaFxlx1HJsCBGw6R3hfBfW3-Fas/preview", style={'height': '450px', 'width': '100%', 'max-width': '1400px'}),
            id = "CPRD-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])
row3 = dmc.TableTr([
    dmc.TableTd("Data Science & Business Analytics Core Module"),
    dmc.TableTd("Boston Institute of Analytics (BIA)"),
    dmc.TableTd("2019"),
    dmc.TableTd([
        dmc.Button("View", id = "BIA-button", variant="filled", style={"backgroundColor": "white", "color": "black"}),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1c5m_jOSt5l-Mou1GAme4D4BbunrhflhJ/preview", style={'height': '450px', 'width': '100%', 'max-width': '1400px'}),
            id = "BIA-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])
row4 = dmc.TableTr([
    dmc.TableTd("PH125.1x: Data Science: R Basics"),
    dmc.TableTd("HarvardX"),
    dmc.TableTd("2019"),
    dmc.TableTd([
        dmc.Button("View", id = "R-button", variant="filled", style={"backgroundColor": "white", "color": "black"}),
        dmc.Drawer(
            html.Iframe(src="https://drive.google.com/file/d/1Xs14mvQaM9pLYoNlmOHiRQ0Ecy9lu9PN/preview", style={'height': '450px', 'width': '100%', 'max-width': '1400px'}),
            id = "R-drawer",
            padding = "md",
            size = "70%",
            position = "bottom",
            zIndex = 10000,
        )    
    ])
])

body = dmc.TableTbody([row1, row2, row3, row4]) 

cert_div = html.Div(
    [
        dmc.Table([head, body], verticalSpacing="md", highlightOnHover=True, style={"fontSize": 18, "color": "white"})
    ],
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20}
)

# TESTIMONIALS
tml_carousel = dmc.Carousel(
    children=[
        dmc.CarouselSlide(html.Iframe(src="https://drive.google.com/file/d/1odmD1v547BzKomPq7wBrhmAQjuvBWQR6/preview", style={"width": "100%", "max-width": "1330px", "height": "700px"})),
        dmc.CarouselSlide(html.Iframe(src="https://drive.google.com/file/d/1-JSS0bZw5AhBz7097LmVeORylKDizQQM/preview", style={"width": "100%", "max-width": "1330px", "height": "700px"})),
        dmc.CarouselSlide(html.Iframe(src="https://drive.google.com/file/d/1dYuKRtgVVY8FOvKf9cAZznKv5u-ytazD/preview", style={"width": "100%", "max-width": "1330px", "height": "700px"})),
        dmc.CarouselSlide(html.Iframe(src="https://drive.google.com/file/d/1buW94xKyB-Dt4S1a9JUWFESDbEnUcrla/preview", style={"width": "100%", "max-width": "1330px", "height": "700px"})),
        dmc.CarouselSlide(html.Iframe(src="https://drive.google.com/file/d/1IS4TX0uwcIlPEa9dkC5Mbs2rqlnYs6sM/preview", style={"width": "100%", "max-width": "1330px", "height": "700px"}))
    ],
    withControls=True,
    loop=True,
    style={"paddingTop": 10, "paddingRight": 20, "paddingLeft": 20, 'width': '100%', 'max-width': '1330px', 'marginLeft': 'auto', 'marginRight': 'auto'}
)

# LAYOUT
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dmc.styles.CAROUSEL])
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
                        dmc.TabsTab(dmc.Text([(html.B(html.I("Testimonials")))], size="md", style={'color': 'white'}), value="testimonials"),
                    ], style={"paddingTop": 5}
                )
            ],
            id="tabs",
            value="introduction",
            color="white"
        ),
        html.Div(id="tabs-content")
    ]
)

# TABS CALLBACK
@callback(
    Output("tabs-content", "children"),
    Input("tabs", "value")
)
def render_content(active):
    if active == "introduction":
        return [intro_div]
    elif active == "resume":
        return [resume_div]
    elif active == "projects":
        return [all_pjcards]
    elif active == "certificates":
        return [cert_div]
    else:
        return [tml_carousel]

# DOWNLOAD CV CALLBACK
@callback(
    Output("download-cv", "data"),
    Input("download-button", "n_clicks"),
    prevent_initial_call=True
)
def download_cv(n_clicks):
    return dcc.send_file("assets/Manali_Jain_CV.pdf")

# GENAI DRAWER CALLBACK
@callback(
    Output("GenAI-drawer", "opened"),
    Input("GenAI-button", "n_clicks"),
    prevent_initial_call=True
)
def genai_drawer(n_clicks):
    return True

# CPRD DRAWER CALLBACK
@callback(
    Output("CPRD-drawer", "opened"),
    Input("CPRD-button", "n_clicks"),
    prevent_initial_call=True
)
def cprd_drawer(n_clicks):
    return True

# BIA DRAWER CALLBACK
@callback(
    Output("BIA-drawer", "opened"),
    Input("BIA-button", "n_clicks"),
    prevent_initial_call=True
)
def bia_drawer(n_clicks):
    return True

# R DRAWER CALLBACK
@callback(
    Output("R-drawer", "opened"),
    Input("R-button", "n_clicks"),
    prevent_initial_call=True
)
def r_drawer(n_clicks):
    return True

if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0', port=8050)

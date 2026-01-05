#!/usr/bin/env python3
"""
Functiegroep Taxonomie Database

Contains the complete database of function groups used for boolean search generation.
This includes all job titles, synonyms, skills, certifications, and related data
for various technical recruitment categories.
"""

from typing import Dict
from .functiegroep import FunctieGroep


# Uitgebreide functiegroep database
FUNCTIEGROEPEN: Dict[str, FunctieGroep] = {
    # === WERKVOORBEREIDING & CALCULATIE ===
    "werkvoorbereider_elektro": FunctieGroep(
        id="werkvoorbereider_elektro",
        naam="Werkvoorbereider Elektrotechniek",
        categorie="werkvoorbereiding",
        titels=[
            "Werkvoorbereider",
            "Calculator",
            "Technisch Planner",
            "Tekenaar-Werkvoorbereider",
        ],
        synoniemen=[
            "Werkvoorbereider Elektrotechniek",
            "Calculator E-techniek",
            "Technisch Werkvoorbereider",
            "Project Planner Elektro",
            "Werkvoorbereider Electrical",
            "E-Werkvoorbereider",
            "Werkvoorbereider E&I",
            "WVB Elektro",
            "Werkvoorbereider Sterkstroom",
            "Werkvoorbereider Zwakstroom",
            "Werkvoorbereider Industriële Automatisering",
            "Tekenaar Werkvoorbereider Elektro",
            "Senior Werkvoorbereider E-techniek",
            "Junior Werkvoorbereider Elektro",
            "Medior Werkvoorbereider Elektrotechniek",
            "Werkvoorbereider Laagspanning",
            "Werkvoorbereider Middenspanning",
            "Werkvoorbereider Utiliteit",
            "Technisch Calculator Elektro",
            "Elektrotechnisch Werkvoorbereider",
            "Coördinator Werkvoorbereiding Elektro",
        ],
        english_titles=[
            "Work Planner",
            "Technical Planner",
            "Project Calculator",
            "Electrical Planner",
            "Construction Planner",
            "Electrical Work Preparer",
            "E&I Work Preparer",
            "MEP Work Planner",
            "Electrical Estimator",
            "Technical Coordinator Electrical",
            "Design Coordinator Electrical",
        ],
        skills=[
            "AutoCAD",
            "Revit",
            "E-Plan",
            "EPLAN",
            "EPLAN Electric P8",
            "EPLAN Pro Panel",
            "BIM",
            "NEN1010",
            "NEN3140",
            "calculatie",
            "werkvoorbereiding",
            "3D tekenen",
            "elektrotechniek",
            "MS Project",
            "Primavera",
            "SAP",
            "Navisworks",
            "Dialux",
            "Relux",
            "Caneco",
            "Desigo CC",
            "See Electrical",
            "NEN-EN-IEC 61439",
            "materiaalbegrotingen",
            "installatietekeningen",
            "PLC schema's",
            "laagspanningsinstallaties",
            "middenspanningsinstallaties",
            "E&I engineering",
            "schema lezen",
            "tekening lezen",
            "uittrekstaten",
        ],
        certificeringen=[
            "VCA",
            "VCA VOL",
            "VCA Basis",
            "NEN1010",
            "NEN3140",
            "BIM certificaat",
            "MBO Elektrotechniek niveau 4",
            "HBO Elektrotechniek",
            "MBO Middenkaderfunctionaris Elektrotechnische Installaties",
            "EPLAN gecertificeerd",
            "Revit MEP certificaat",
            "AutoCAD certificaat",
        ],
        look_alikes=[
            "werkvoorbereider_installatie",
            "calculator_bouw",
            "projectleider_elektro",
        ],
        typische_werkgevers=[
            "Unica",
            "Croonwolter&dros",
            "Hoppenbrouwers",
            "Kuijpers",
            "Breman",
            "Spie",
            "Engie",
            "Imtech",
            "Equans",
        ],
        concurrenten=[
            "Strukton",
            "Heijmans",
            "BAM",
            "VolkerWessels",
            "Dura Vermeer",
            "TBI",
            "GMB",
            "Van Gelder",
        ],
        sector_keywords=[
            "elektrotechniek",
            "E-techniek",
            "electrical",
            "elektro",
            "laagspanning",
            "hoogspanning",
            "middenspanning",
            "sterkstroom",
            "zwakstroom",
            "utiliteit",
            "E&I",
        ],
    ),
    "werkvoorbereider_installatie": FunctieGroep(
        id="werkvoorbereider_installatie",
        naam="Werkvoorbereider Installatietechniek",
        categorie="werkvoorbereiding",
        titels=[
            "Werkvoorbereider",
            "Calculator",
            "Technisch Planner",
            "Tekenaar-Werkvoorbereider",
        ],
        synoniemen=[
            "Werkvoorbereider Installatietechniek",
            "Calculator Installatie",
            "Werkvoorbereider W-techniek",
            "Calculator HVAC",
            "Werkvoorbereider Klimaat",
            "W-Werkvoorbereider",
            "Werkvoorbereider Klimaattechniek",
            "Werkvoorbereider Sanitair",
            "Werkvoorbereider Koeltechniek",
            "WVB Installatie",
            "WVB W-techniek",
            "Tekenaar Werkvoorbereider Installatie",
            "Senior Werkvoorbereider W-techniek",
            "Junior Werkvoorbereider Installatietechniek",
            "Medior Werkvoorbereider HVAC",
            "Werkvoorbereider Utiliteit",
            "Werkvoorbereider Sprinkler",
            "Werkvoorbereider Luchtbehandeling",
            "Technisch Calculator Installatie",
            "Coördinator Werkvoorbereiding Installatie",
            "Werkvoorbereider CV",
            "Werkvoorbereider Verwarming",
            "Werkvoorbereider Gebouwgebonden Installaties",
        ],
        english_titles=[
            "HVAC Planner",
            "Installation Planner",
            "MEP Calculator",
            "MEP Work Preparer",
            "Mechanical Work Planner",
            "HVAC Estimator",
            "Plumbing Work Preparer",
            "MEP Coordinator",
            "Technical Planner HVAC",
        ],
        skills=[
            "BIM",
            "Revit",
            "Revit MEP",
            "AutoCAD",
            "AutoCAD MEP",
            "calculatie",
            "HVAC",
            "klimaattechniek",
            "sanitair",
            "werktuigbouw",
            "MS Project",
            "Primavera",
            "SAP",
            "Navisworks",
            "Stabicad",
            "DDS-CAD",
            "Trimble",
            "Plancal Nova",
            "VABI",
            "Vabi Elements",
            "warmtepompen",
            "koelmachines",
            "luchtbehandeling",
            "materiaalbegrotingen",
            "installatietekeningen",
            "isometrieën",
            "leidingschema's",
            "P&ID",
            "CV-installaties",
            "sprinklerinstallaties",
            "tekening lezen",
            "uittrekstaten",
            "gebouwgebonden installaties",
        ],
        certificeringen=[
            "VCA",
            "VCA VOL",
            "VCA Basis",
            "F-gassen",
            "BIM certificaat",
            "MBO Installatie- en Koudetechniek niveau 4",
            "HBO Werktuigbouwkunde",
            "MBO Middenkaderfunctionaris Installaties",
            "Revit MEP certificaat",
            "ISSO gecertificeerd",
            "STEK certificaat",
            "AutoCAD certificaat",
        ],
        look_alikes=[
            "werkvoorbereider_elektro",
            "calculator_bouw",
            "projectleider_installatie",
        ],
        typische_werkgevers=[
            "Unica",
            "Kuijpers",
            "Breman",
            "Aalberts",
            "Engie",
            "Equans",
        ],
        concurrenten=["Strukton", "Heijmans", "BAM", "Croonwolter&dros"],
        sector_keywords=[
            "installatietechniek",
            "W-techniek",
            "HVAC",
            "klimaat",
            "sanitair",
            "koude",
            "warmte",
            "verwarming",
            "ventilatie",
            "luchtbehandeling",
            "utiliteit",
        ],
    ),
    "calculator_bouw": FunctieGroep(
        id="calculator_bouw",
        naam="Calculator Bouw",
        categorie="werkvoorbereiding",
        titels=["Calculator", "Kostencalculator", "Bouwcalculator", "Tender Manager"],
        synoniemen=[
            "Calculator Bouw",
            "Bouwkostencalculator",
            "Tender Calculator",
            "Aanbestedingscalculator",
            "Prijscalculator",
            "Calculator Utiliteitsbouw",
            "Calculator Woningbouw",
            "Calculator GWW",
            "Calculator Infra",
            "Senior Calculator",
            "Junior Calculator",
            "Medior Calculator",
            "Tendermanager",
            "Inschrijvingsmanager",
            "Calculatiespecialist",
            "Kostenspecialist Bouw",
            "Calculator Nieuwbouw",
            "Calculator Renovatie",
        ],
        english_titles=[
            "Quantity Surveyor",
            "Cost Estimator",
            "Tender Specialist",
            "Bid Manager",
            "Estimation Manager",
            "Construction Estimator",
            "Tender Manager",
            "Cost Engineer",
        ],
        skills=[
            "calculatie",
            "IBIS",
            "Excel",
            "kostprijsberekening",
            "bouwkunde",
            "aanbestedingen",
            "contracten",
            "Orca",
            "Kraan",
            "12Build",
            "BIM",
            "Revit",
            "RAW-bestekken",
            "UAV",
            "STABU",
            "bouwbesluit",
            "bestekken schrijven",
            "MS Project",
            "Primavera",
            "kostenbewaking",
            "nacalculatie",
            "offertes",
            "begroten",
            "inschrijvingen",
        ],
        certificeringen=[
            "VCA",
            "VCA VOL",
            "HBO Bouwkunde",
            "MBO Bouwkunde niveau 4",
            "RICS",
            "NVBK certificering",
        ],
        look_alikes=[
            "werkvoorbereider_elektro",
            "werkvoorbereider_installatie",
            "projectleider_bouw",
        ],
        typische_werkgevers=[
            "BAM",
            "Heijmans",
            "VolkerWessels",
            "Dura Vermeer",
            "Strukton",
        ],
        concurrenten=[
            "BAM",
            "Heijmans",
            "VolkerWessels",
            "Dura Vermeer",
            "Strukton",
            "TBI",
            "Ballast Nedam",
            "Van Wijnen",
        ],
        sector_keywords=[
            "bouw",
            "construction",
            "utiliteitsbouw",
            "woningbouw",
            "infra",
            "GWW",
            "nieuwbouw",
            "renovatie",
            "civiel",
        ],
    ),
    # === SOFTWARE DEVELOPMENT ===
    "software_engineer": FunctieGroep(
        id="software_engineer",
        naam="Software Engineer / Developer",
        categorie="software",
        titels=["Software Engineer", "Developer", "Software Developer", "Programmer"],
        synoniemen=[
            "Software Engineer",
            "Software Developer",
            "Developer",
            "Programmer",
            "Softwareontwikkelaar",
            "Application Developer",
            "Full Stack Developer",
            "Frontend Developer",
            "Backend Developer",
            "Web Developer",
            "Mobile Developer",
            "Cloud Developer",
            "Junior Developer",
            "Medior Developer",
            "Senior Developer",
            "Lead Developer",
            "Software Architect",
            "Technical Lead",
            "Senior Software Engineer",
            "Staff Engineer",
            "Principal Engineer",
            "Tech Lead",
            "Embedded Engineer",
            "Cloud Engineer",
            "DevOps Engineer",
            "Platform Engineer",
            "SRE",
            "Data Engineer",
            "ML Engineer",
            "AI Engineer",
        ],
        english_titles=[
            "Software Engineer",
            "Software Developer",
            "Full Stack Developer",
            "Frontend Developer",
            "Backend Developer",
            "Web Developer",
            "Mobile Developer",
            "Cloud Engineer",
            "DevOps Engineer",
            "Senior Software Engineer",
            "Staff Engineer",
            "Principal Engineer",
            "Tech Lead",
            "Embedded Engineer",
            "Cloud Engineer",
            "DevOps Engineer",
            "Platform Engineer",
            "SRE",
            "Data Engineer",
            "ML Engineer",
            "AI Engineer",
        ],
        skills=[
            "Python",
            "Java",
            "C++",
            "C#",
            ".NET",
            "Go",
            "Rust",
            "JavaScript",
            "TypeScript",
            "Node.js",
            "PHP",
            "Ruby",
            "Scala",
            "Kotlin",
            "C",
            "Embedded C",
            "Assembly",
            "Spring",
            "Spring Boot",
            "Django",
            "Flask",
            "FastAPI",
            "Express.js",
            "NestJS",
            "ASP.NET",
            "Ruby on Rails",
            "React",
            "Angular",
            "Vue.js",
            "Next.js",
            "Svelte",
            "Redux",
            "GraphQL",
            "REST API",
            "AWS",
            "Azure",
            "Google Cloud",
            "GCP",
            "Docker",
            "Kubernetes",
            "Terraform",
            "Ansible",
            "Jenkins",
            "GitLab CI",
            "GitHub Actions",
            "CI/CD",
            "PostgreSQL",
            "MySQL",
            "MongoDB",
            "Redis",
            "Elasticsearch",
            "Kafka",
            "RabbitMQ",
            "SQL",
            "NoSQL",
            "Database design",
            "Git",
            "Agile",
            "Scrum",
            "Kanban",
            "TDD",
            "Unit testing",
            "Integration testing",
            "Microservices",
            "API design",
            "System design",
            "RTOS",
            "FreeRTOS",
            "Linux kernel",
            "Device drivers",
            "ARM",
            "STM32",
            "ESP32",
            "Raspberry Pi",
        ],
        certificeringen=[
            "AWS Certified",
            "AWS Solutions Architect",
            "AWS Developer",
            "Azure Certified",
            "Azure Developer",
            "Azure Administrator",
            "Google Cloud Certified",
            "GCP Professional",
            "Scrum Master",
            "PSM",
            "PSPO",
            "SAFe",
            "Agile Coach",
            "Oracle Java Certified",
            "Microsoft Certified",
            "Kubernetes Certified",
            "CKA",
            "CKAD",
            "Docker Certified",
            "Terraform Certified",
            "HBO Informatica",
            "HBO Software Engineering",
            "MSc Computer Science",
            "BSc Informatica",
            "TU Delft",
            "TU Eindhoven",
            "Universiteit",
        ],
        look_alikes=["plc_programmeur", "embedded_engineer", "data_engineer"],
        typische_werkgevers=["ASML", "Philips", "TomTom", "Booking", "Adyen"],
        concurrenten=["ASML", "Philips", "TomTom", "Booking", "Adyen", "Exact"],
        sector_keywords=[
            "software",
            "IT",
            "development",
            "programmeren",
            "tech",
            "digital",
        ],
    ),
    "monteur_elektro": FunctieGroep(
        id="monteur_elektro",
        naam="Monteur Elektrotechniek",
        categorie="techniek",
        titels=["Monteur", "Elektromonteur", "Servicemonteur", "Technicus"],
        synoniemen=[
            "Elektromonteur", "Monteur Elektrotechniek", "E-Monteur",
            "Servicemonteur Elektro", "Onderhoudsmonteur Elektro",
            "Eerste Monteur Elektro", "Allround Elektromonteur",
            "Senior Elektromonteur", "Junior Elektromonteur", "Medior Elektromonteur",
            "Elektrotechnisch Monteur", "Industrieel Elektromonteur",
            "Elektromonteur Laagspanning", "Elektromonteur Middenspanning",
            "Elektromonteur Sterkstroom", "Elektromonteur Zwakstroom",
            "Elektromonteur Utiliteit", "Elektromonteur Woningbouw",
            "Elektromonteur Nieuwbouw", "Elektromonteur Onderhoud",
            "Monteur E&I", "E&I Monteur", "Monteur Elektrisch",
            "Schakelaar Monteur", "Installateur Elektro", "Storingsmonteur Elektro",
            "Aankomend Elektromonteur", "1e Elektromonteur", "2e Elektromonteur",
            "Elektricien", "Installatiemonteur Elektro", "Technicus Elektrotechniek",
            "Voorkeur Vakman Elektro", "VOP Monteur", "VP Monteur",
            "Elektromonteur Industrie", "Elektromonteur Scheepvaart"
        ],
        english_titles=[
            "Electrician", "Electrical Technician", "Service Electrician",
            "Industrial Electrician", "Maintenance Electrician", "Installation Electrician",
            "Electrical Installer", "Electrical Fitter", "E&I Technician"
        ],
        skills=[
            "elektrotechniek", "NEN1010", "NEN3140", "storingsdienst",
            "PLC", "laagspanning", "middenspanning", "installatietechniek",
            "schakelaarinstallaties", "kabelwerk", "bekabeling",
            "verdeelkasten", "lichtinstallaties", "noodverlichting",
            "brandmeldinstallaties", "domotica", "KNX", "gebouwautomatisering",
            "frequentieregelaars", "softstarters", "motorbesturing",
            "aardingssystemen", "bliksembeveiliging", "overspanningsbeveiliging",
            "tekeningen lezen", "installatietekeningen", "schema's lezen",
            "metingen", "isolatiemeting", "aardingsmeting",
            "ploegendienst", "storingswacht", "24-uurs service"
        ],
        certificeringen=[
            "NEN3140 VOP", "NEN3140 VP", "NEN3140", "VCA VOL", "VCA Basis",
            "NEN1010", "STIPEL BEI-IV", "STIPEL BEI-VP", "STIPEL BEI-VOP",
            "MBO Elektrotechniek niveau 2", "MBO Elektrotechniek niveau 3",
            "MBO Elektrotechniek niveau 4", "MBO Eerste Monteur Elektrotechnische Installaties",
            "MBO Monteur Elektrotechnische Installaties", "BOL Elektrotechniek",
            "BBL Elektrotechniek", "Kenteq E-certificaat"
        ],
        look_alikes=["monteur_installatie", "servicemonteur", "onderhoudsmonteur", "mechatronicus"],
        typische_werkgevers=[
            "Unica", "Croonwolter&dros", "Hoppenbrouwers", "Spie", "Engie",
            "Equans", "Cofely", "Imtech", "Stork", "Technische Unie"
        ],
        concurrenten=[
            "Strukton", "Heijmans", "BAM", "Imtech", "TBI", "VolkerWessels",
            "Dura Vermeer", "Van Gelder", "Joulz"
        ],
        sector_keywords=[
            "elektrotechniek", "E-techniek", "elektra", "stroom", "elektrisch",
            "installatie", "utiliteit", "industrie", "woningbouw", "nieuwbouw"
        ]
    ),
    "monteur_installatie": FunctieGroep(
        id="monteur_installatie",
        naam="Monteur Installatietechniek",
        categorie="techniek",
        titels=["Monteur", "Installatiemonteur", "Servicemonteur", "Technicus"],
        synoniemen=[
            "Installatiemonteur", "Monteur Installatietechniek",
            "W-Monteur", "HVAC Monteur", "Klimaatmonteur",
            "Loodgieter", "Sanitair Monteur", "CV Monteur",
            "Senior Installatiemonteur", "Junior Installatiemonteur", "Medior Installatiemonteur",
            "Eerste Monteur Installatietechniek", "1e Monteur W-techniek",
            "Allround Installatiemonteur", "Verwarmingsmonteur",
            "Airco Monteur", "Koelmonteur", "Koeltechnisch Monteur",
            "Klimaattechnisch Monteur", "Luchtbehandelingsmonteur",
            "Gasmonteur", "Gasfitter", "Fitter", "Pijpfitter",
            "Monteur Werktuigbouwkunde", "WTB Monteur",
            "Monteur Klimaatbeheersing", "Installateur HVAC",
            "Onderhoudsmonteur Installatie", "Storingsmonteur Installatie",
            "Mechanisch Monteur", "Monteur Warmtepompen",
            "Monteur Zonnepanelen", "Monteur Duurzame Energie",
            "Installatiemonteur Woningbouw", "Installatiemonteur Utiliteit",
            "Technicus Installatietechniek", "Aankomend Installatiemonteur"
        ],
        english_titles=[
            "HVAC Technician", "Installation Technician", "Plumber",
            "Heating Engineer", "Refrigeration Technician", "Air Conditioning Technician",
            "Mechanical Fitter", "Pipe Fitter", "HVAC Installer",
            "Climate Control Technician", "Ventilation Technician"
        ],
        skills=[
            "HVAC", "klimaattechniek", "sanitair", "loodgieterij",
            "CV-installaties", "koeltechniek", "F-gassen",
            "luchtbehandeling", "ventilatie", "airconditioning",
            "warmtepompen", "vloerverwarming", "radiatoren",
            "gasleidingen", "waterleidingen", "riolering",
            "solderen", "persen", "buiswerk", "laswerk",
            "tekeningen lezen", "isometrieën", "P&ID schema's",
            "inregelen", "balanceren", "commissioning",
            "legionellapreventie", "drinkwaterinstallaties",
            "sprinklerinstallaties", "blusinstallaties",
            "ploegendienst", "storingswacht"
        ],
        certificeringen=[
            "VCA VOL", "VCA Basis", "F-gassen categorie I", "F-gassen categorie II",
            "STEK certificaat", "EPBD certificaat",
            "MBO Installatiemonteur niveau 2", "MBO Installatiemonteur niveau 3",
            "MBO Eerste Installatiemonteur niveau 4",
            "MBO Monteur Werktuigkundige Installaties",
            "BOL Installatietechniek", "BBL Installatietechniek",
            "Legionella risicoanalyse", "ISSO cursussen",
            "Warmtepomp certificaat", "Uneto-VNI diploma"
        ],
        look_alikes=["monteur_elektro", "servicemonteur", "onderhoudsmonteur", "koeltechnicus"],
        typische_werkgevers=[
            "Kuijpers", "Breman", "Unica", "Aalberts", "Feenstra",
            "Van der Valk Installatietechniek", "Daikin", "Carrier"
        ],
        concurrenten=[
            "Strukton", "Heijmans", "Croonwolter&dros", "Imtech",
            "Spie", "Engie", "Equans"
        ],
        sector_keywords=[
            "installatietechniek", "HVAC", "klimaat", "sanitair", "CV",
            "W-techniek", "werktuigbouw", "verwarming", "koeling", "ventilatie"
        ]
    ),
    "servicemonteur": FunctieGroep(
        id="servicemonteur",
        naam="Servicemonteur",
        categorie="techniek",
        titels=["Servicemonteur", "Field Service Engineer", "Storingmonteur", "Onderhoudsmonteur"],
        synoniemen=[
            "Servicemonteur", "Service Technicus", "Field Engineer",
            "Storingsdienst Monteur", "Onderhoudsmonteur",
            "Service Engineer", "Buitendienstmonteur",
            "Senior Servicemonteur", "Junior Servicemonteur", "Medior Servicemonteur",
            "Field Service Technician", "Field Technician", "Service Technician",
            "Storingsmonteur", "Piketmonteur", "Consignatiedienst Monteur",
            "Buitendienst Technicus", "Reizend Monteur", "Mobiel Monteur",
            "Service Medewerker Technisch", "Technisch Servicemedewerker",
            "Servicemonteur Buitendienst", "Servicemonteur Industrie",
            "Allround Servicemonteur", "1e Servicemonteur",
            "Preventief Onderhoudsmonteur", "Correctief Onderhoudsmonteur",
            "Onderhoudstechnicus", "Maintenance Technician",
            "Servicemonteur Liften", "Servicemonteur Roltrappen",
            "Servicemonteur Medische Apparatuur", "Servicemonteur Kantoorapparatuur",
            "Servicemonteur Horeca", "Servicemonteur Koelapparatuur"
        ],
        english_titles=[
            "Field Service Engineer", "Service Technician", "Maintenance Technician",
            "Field Technician", "Service Engineer", "Technical Service Engineer",
            "Breakdown Engineer", "On-site Technician", "Customer Engineer",
            "Maintenance Engineer", "After Sales Engineer"
        ],
        skills=[
            "storingsdienst", "onderhoud", "troubleshooting",
            "klantcontact", "rijbewijs B", "PLC", "elektrotechniek",
            "storingsanalyse", "root cause analysis", "preventief onderhoud",
            "correctief onderhoud", "commissioning", "inbedrijfstelling",
            "rapportage", "werkorders", "servicerapporten",
            "montage", "demontage", "revisie",
            "24-uurs service", "consignatiedienst", "piketdienst",
            "klantvriendelijkheid", "communicatief", "zelfstandig werken",
            "diagnose", "foutopsporing", "meetapparatuur"
        ],
        certificeringen=[
            "VCA VOL", "VCA Basis", "NEN3140 VOP", "NEN3140 VP", "NEN3140",
            "Rijbewijs B", "Rijbewijs BE", "Rijbewijs C",
            "MBO Mechatronica", "MBO Elektrotechniek", "MBO Werktuigbouwkunde",
            "Heftruck certificaat", "Hoogwerker certificaat",
            "EHBO", "BHV"
        ],
        look_alikes=["monteur_elektro", "monteur_installatie", "onderhoudsmonteur", "mechatronicus"],
        typische_werkgevers=[
            "Thyssenkrupp", "Kone", "Otis", "Schindler",
            "Vanderlande", "Marel", "GEA", "Tetra Pak"
        ],
        concurrenten=[
            "Thyssenkrupp", "Kone", "Otis", "Schindler", "Engie",
            "Stork", "Spie", "Bilfinger"
        ],
        sector_keywords=[
            "service", "onderhoud", "storingsdienst", "field", "buitendienst",
            "maintenance", "storing", "reparatie", "revisie"
        ]
    ),
    "mechatronicus": FunctieGroep(
        id="mechatronicus",
        naam="Mechatronicus",
        categorie="techniek",
        titels=["Mechatronicus", "Technicus Mechatronica", "Mechatronic Engineer"],
        synoniemen=[
            # Basis titels
            "Mechatronicus", "Technicus Mechatronica", "Mechatronica Specialist",
            "Elektromechanicus", "Automatiseringstechnicus",
            # Seniority variaties
            "Senior Mechatronicus", "Junior Mechatronicus", "Medior Mechatronicus",
            "Lead Mechatronicus", "Allround Mechatronicus",
            # Specialisaties
            "Mechatronicus Robotica", "Mechatronicus Vision", "Mechatronicus Motion Control",
            "Mechatronicus Hightech", "Mechatronicus Semiconductor",
            "Mechatronicus Vakmanschap", "Onderhouds Mechatronicus",
            # Hybride titels
            "Mechatronisch Monteur", "Mechatronisch Technicus", "Mechatronisch Engineer",
            "Mechatronisch Specialist", "Automatisering Specialist",
            # Functievariaties
            "System Engineer Mechatronica", "Ontwikkelaar Mechatronica",
            "Mechatronica Ingenieur", "R&D Mechatronicus",
            "Mechatronicus Ontwikkeling", "Mechatronicus Onderhoud"
        ],
        english_titles=[
            "Mechatronics Engineer", "Automation Technician", "Electromechanical Technician",
            "Mechatronic Technician", "Automation Engineer", "Motion Control Engineer",
            "Robotics Engineer", "System Integration Engineer", "Controls Engineer",
            "Senior Mechatronics Engineer", "Junior Mechatronics Engineer"
        ],
        skills=[
            # PLC Systemen
            "PLC", "Siemens S7", "Siemens TIA Portal", "Allen Bradley", "Rockwell",
            "Omron", "Beckhoff TwinCAT", "Codesys", "B&R Automation",
            # Motion Control
            "Servo", "Servoaandrijving", "Motion Control", "Frequentieregeling",
            "Bosch Rexroth", "SEW", "Lenze", "Festo",
            # Robotica
            "Robotica", "KUKA", "ABB Robot", "Fanuc Robot", "Universal Robots",
            "Cobot", "Yaskawa", "Mitsubishi Robot",
            # Mechanisch & Elektrisch
            "Pneumatiek", "Hydrauliek", "Elektrotechniek", "Werktuigbouw",
            "Sensoriek", "Vision Systemen", "Cognex", "Keyence",
            # Software
            "Python", "C++", "C#", "LabVIEW", "MATLAB",
            # Overig
            "EPLAN", "SolidWorks", "CAD", "Troubleshooting", "Inbedrijfstelling"
        ],
        certificeringen=[
            # Veiligheid
            "VCA VOL", "VCA Basis", "NEN3140 VOP", "NEN3140 VP",
            # Opleidingen
            "MBO Mechatronica niveau 4", "MBO Mechatronica niveau 3",
            "HBO Mechatronica", "Associate Degree Mechatronica",
            "Bachelor Mechatronica", "Technicus Mechatronica",
            # Siemens certificaten
            "Siemens S7 certificaat", "Siemens TIA Portal certificaat",
            "Siemens SITRAIN", "Siemens Certified Professional",
            # Robot certificaten
            "KUKA certificaat", "ABB Robot certificaat", "Fanuc certificaat",
            # Overig
            "Festo Pneumatiek", "Bosch Rexroth certificaat"
        ],
        look_alikes=["automatiseringsengineer", "plc_programmeur", "monteur_elektro"],
        typische_werkgevers=[
            "ASML", "Philips", "VDL", "Thermo Fisher", "NXP"
        ],
        concurrenten=[
            "ASML", "Philips", "VDL", "Thermo Fisher", "Demcon", "TMC"
        ],
        sector_keywords=[
            "mechatronica", "automatisering", "robotica", "hightech",
            "semiconductor", "motion control", "machine", "systeem"
        ]
    ),
    "plc_programmeur": FunctieGroep(
        id="plc_programmeur",
        naam="PLC Programmeur",
        categorie="automatisering",
        titels=["PLC Programmeur", "PLC Engineer", "Automation Engineer"],
        synoniemen=[
            # Basis titels
            "PLC Programmeur", "PLC Engineer", "Besturingstechnicus",
            "Automation Engineer", "Control System Engineer",
            "Software Engineer PLC", "SCADA Engineer",
            # Seniority variaties
            "Senior PLC Programmeur", "Junior PLC Programmeur", "Medior PLC Programmeur",
            "Lead PLC Engineer", "Principal Automation Engineer",
            # Specialisaties per merk
            "Siemens PLC Programmeur", "Allen Bradley Programmeur", "Beckhoff Programmeur",
            "Omron Programmeur", "Mitsubishi PLC Programmeur", "Codesys Programmeur",
            # SCADA/DCS variaties
            "SCADA Specialist", "DCS Engineer", "DCS Programmeur",
            "MES Engineer", "MES Specialist", "Historian Engineer",
            # Hybride titels
            "Controls Engineer", "Besturingssysteem Engineer", "Control Specialist",
            "Industrial Automation Engineer", "ICS Engineer",
            "Automation Specialist", "Automatiserings Ingenieur",
            # HMI/Visualisatie
            "HMI Programmeur", "HMI Developer", "Visualisatie Specialist",
            "WinCC Programmeur", "Ignition Developer"
        ],
        english_titles=[
            "PLC Programmer", "Automation Engineer", "Control Systems Engineer",
            "Controls Engineer", "Industrial Automation Engineer", "SCADA Developer",
            "DCS Engineer", "MES Engineer", "Senior PLC Programmer",
            "Automation Specialist", "Process Control Engineer"
        ],
        skills=[
            # Siemens ecosystem
            "Siemens TIA Portal", "Step 7", "Siemens S7-1200", "Siemens S7-1500",
            "Siemens S7-300", "Siemens S7-400", "WinCC", "WinCC OA", "WinCC Unified",
            # Allen Bradley / Rockwell
            "Allen Bradley", "Rockwell", "Studio 5000", "RSLogix",
            "ControlLogix", "CompactLogix", "MicroLogix", "FactoryTalk",
            # Andere PLC merken
            "Codesys", "Beckhoff TwinCAT", "Omron", "Mitsubishi", "Schneider",
            "Simatic", "ABB PLC", "B&R Automation", "Phoenix Contact",
            # SCADA / DCS
            "SCADA", "Ignition", "Wonderware", "InTouch", "iFIX", "Citect",
            "DCS", "Emerson DeltaV", "Yokogawa", "Honeywell Experion",
            "ABB 800xA", "PI Historian", "OSIsoft",
            # HMI
            "HMI", "Comfort Panel", "AVEVA", "Proface", "Beijer",
            # Communicatie
            "Profinet", "Profibus", "EtherCAT", "Modbus", "OPC-UA", "MQTT",
            "Ethernet/IP", "DeviceNet", "CANopen",
            # Software
            "IEC 61131-3", "Structured Text", "Ladder Logic", "FBD",
            "Python", "SQL", "C#", "VB.NET"
        ],
        certificeringen=[
            # Siemens
            "Siemens TIA Portal certificaat", "Siemens SITRAIN",
            "Siemens Certified Professional", "Siemens S7 certificaat",
            # Rockwell
            "Rockwell certificaat", "Allen Bradley certificaat",
            "FactoryTalk certificaat",
            # SCADA
            "Ignition certificaat", "Wonderware certificaat",
            # Veiligheid
            "TÜV Functional Safety", "SIL certificaat", "IEC 61508",
            "VCA VOL", "VCA Basis", "NEN3140",
            # Opleidingen
            "HBO Elektrotechniek", "HBO Technische Informatica",
            "MBO Elektrotechniek niveau 4", "Certified Automation Professional"
        ],
        look_alikes=["mechatronicus", "automatiseringsengineer", "software_engineer"],
        typische_werkgevers=[
            "Siemens", "ABB", "Yokogawa", "Honeywell"
        ],
        concurrenten=[
            "Siemens", "ABB", "Yokogawa", "Honeywell", "Emerson", "Schneider"
        ],
        sector_keywords=[
            "PLC", "automatisering", "besturing", "SCADA", "DCS",
            "controls", "industrial automation", "process control", "ICS"
        ]
    ),
    "projectleider_elektro": FunctieGroep(
        id="projectleider_elektro",
        naam="Projectleider Elektrotechniek",
        categorie="projectleiding",
        titels=["Projectleider", "Project Manager", "Projectmanager"],
        synoniemen=[
            # Basis titels
            "Projectleider Elektrotechniek", "Projectmanager E-techniek",
            "Technisch Projectleider", "Project Engineer Elektro",
            # Seniority variaties
            "Senior Projectleider E-techniek", "Junior Projectleider Elektro",
            "Medior Projectleider Elektrotechniek", "Lead Projectleider",
            # Specialisaties
            "Projectleider Laagspanning", "Projectleider Middenspanning",
            "Projectleider Hoogspanning", "Projectleider Energie",
            "Projectleider Data", "Projectleider Telecom",
            "Projectleider Utiliteit", "Projectleider Industrie",
            # Hybride titels
            "Uitvoerder E-techniek", "Uitvoerder Elektro",
            "Coördinator E-techniek", "Teamleider E-techniek",
            "Projectcoördinator Elektro", "Hoofduitvoerder E-techniek",
            # Technische projectleiding
            "Technical Project Manager E-techniek", "E&I Projectleider",
            "Projectleider E&I", "Projectleider Besturingstechniek",
            "Projectleider Installatie Elektro", "Projectleider Netwerken"
        ],
        english_titles=[
            "Project Manager", "Project Leader", "Project Engineer",
            "Electrical Project Manager", "Technical Project Manager",
            "Senior Project Manager", "E&I Project Manager",
            "Project Manager Electrical", "Construction Project Manager"
        ],
        skills=[
            # Projectmanagement
            "Projectmanagement", "MS Project", "Primavera", "Planon",
            "Budgetbeheer", "Kostenbeheersing", "Risicomanagement",
            "Stakeholder Management", "Contractmanagement",
            # Technisch
            "Elektrotechniek", "EPLAN", "AutoCAD Electrical", "Revit MEP",
            "Laagspanning", "Middenspanning", "Hoogspanning",
            "NEN1010", "NEN3140", "NEN-EN-IEC normering",
            # Soft skills
            "Leidinggeven", "Teammanagement", "Klantcontact",
            "Onderhandelen", "Rapportage", "Presenteren"
        ],
        certificeringen=[
            # Projectmanagement certificeringen
            "Prince2 Foundation", "Prince2 Practitioner",
            "PMP", "PMI certificaat", "IPMA-D", "IPMA-C", "IPMA-B",
            "Lean Six Sigma Green Belt", "Lean Six Sigma Black Belt",
            "Agile certificaat", "Scrum Master",
            # Technisch
            "NEN3140 VOP", "NEN3140 VP", "VCA VOL", "VCA Basis",
            # Opleidingen
            "HBO Elektrotechniek", "HBO Technische Bedrijfskunde",
            "MBO Elektrotechniek niveau 4", "MBO Middenkaderopleiding"
        ],
        look_alikes=["projectleider_installatie", "projectleider_bouw", "werkvoorbereider_elektro"],
        typische_werkgevers=[
            "Unica", "Croonwolter&dros", "Hoppenbrouwers", "Spie"
        ],
        concurrenten=[
            "Strukton", "Heijmans", "BAM", "Engie", "Imtech"
        ],
        sector_keywords=[
            "elektrotechniek", "E-techniek", "elektro", "utiliteit",
            "industrie", "infra", "energie", "power"
        ]
    ),
    "projectleider_installatie": FunctieGroep(
        id="projectleider_installatie",
        naam="Projectleider Installatietechniek",
        categorie="projectleiding",
        titels=["Projectleider", "Project Manager", "Projectmanager"],
        synoniemen=[
            # Basis titels
            "Projectleider Installatietechniek", "Projectmanager W-techniek",
            "Projectleider HVAC", "Project Engineer Installatie",
            # Seniority variaties
            "Senior Projectleider W-techniek", "Junior Projectleider Installatie",
            "Medior Projectleider HVAC", "Lead Projectleider Installatie",
            # Specialisaties
            "Projectleider Klimaat", "Projectleider Koeling",
            "Projectleider Warmtepompen", "Projectleider Duurzame Energie",
            "Projectleider Sanitair", "Projectleider Sprinkler",
            "Projectleider Utiliteit W", "Projectleider Industrie W",
            # Hybride titels
            "Uitvoerder W-techniek", "Uitvoerder Installatie",
            "Coördinator W-techniek", "Teamleider Installatie",
            "Projectcoördinator Installatie", "Hoofduitvoerder W-techniek",
            # MEP titels
            "Projectleider MEP", "MEP Projectmanager", "MEP Coördinator",
            "Projectleider Building Services", "Technical Project Manager MEP"
        ],
        english_titles=[
            "Project Manager MEP", "HVAC Project Manager", "Mechanical Project Manager",
            "MEP Project Manager", "Building Services Project Manager",
            "Senior Project Manager HVAC", "Project Leader Installations",
            "Project Engineer MEP", "Construction Project Manager MEP"
        ],
        skills=[
            # Projectmanagement
            "Projectmanagement", "MS Project", "Primavera", "Planon",
            "Budgetbeheer", "Kostenbeheersing", "Risicomanagement",
            "Stakeholder Management", "Contractmanagement",
            # Technisch HVAC
            "HVAC", "Klimaattechniek", "Koeltechniek", "Warmtepompen",
            "Ventilatie", "Luchtbehandeling", "Gebouwautomatisering",
            # Software
            "Revit MEP", "AutoCAD MEP", "Stabicad", "DDS-CAD",
            "BIM", "Solibri", "Navisworks",
            # Soft skills
            "Leidinggeven", "Teammanagement", "Klantcontact",
            "Onderhandelen", "Rapportage", "Presenteren"
        ],
        certificeringen=[
            # Projectmanagement certificeringen
            "Prince2 Foundation", "Prince2 Practitioner",
            "PMP", "PMI certificaat", "IPMA-D", "IPMA-C", "IPMA-B",
            "Lean Six Sigma Green Belt", "Lean Six Sigma Black Belt",
            # Technisch
            "F-gassen certificaat", "STEK certificaat", "EPBD certificaat",
            "VCA VOL", "VCA Basis",
            # Opleidingen
            "HBO Installatietechniek", "HBO Technische Bedrijfskunde",
            "HBO Klimaattechniek", "MBO Installatie niveau 4"
        ],
        look_alikes=["projectleider_elektro", "projectleider_bouw", "werkvoorbereider_installatie"],
        typische_werkgevers=[
            "Kuijpers", "Breman", "Unica", "Aalberts"
        ],
        concurrenten=[
            "Strukton", "Heijmans", "Croonwolter&dros"
        ],
        sector_keywords=[
            "installatietechniek", "HVAC", "klimaat", "W-techniek",
            "MEP", "utiliteit", "building services", "duurzaam"
        ]
    ),
    "constructeur": FunctieGroep(
        id="constructeur",
        naam="Constructeur / Mechanical Engineer",
        categorie="engineering",
        titels=["Constructeur", "Mechanical Engineer", "Design Engineer"],
        synoniemen=[
            # === BASIS TITELS ===
            "Constructeur", "Mechanical Designer", "3D Constructeur",
            "Productontwerper", "CAD Engineer", "Design Engineer",
            "Werktuigbouwkundig Constructeur", "Tekenaar Constructeur",
            # === SENIORITY LEVELS ===
            "Senior Constructeur", "Junior Constructeur", "Medior Constructeur",
            "Lead Constructeur", "Hoofd Constructeur", "Principal Engineer",
            "Senior Mechanical Designer", "Junior Mechanical Designer",
            # === SPECIALISATIES ===
            "SolidWorks Constructeur", "Inventor Constructeur", "Creo Constructeur",
            "CATIA Constructeur", "NX Constructeur", "Siemens NX Designer",
            "Machinebouwer", "Machine Designer", "Machineconstructeur",
            "Apparatenbouwer", "Equipment Designer", "Tooling Engineer",
            "Jig & Fixture Designer", "Matrijzenmaker", "Mold Designer",
            "Staalconstructeur", "Steel Designer", "Staalbouwconstructeur",
            "Scheepsbouwkundig Constructeur", "Marine Designer",
            # === ANALYSE & BEREKENING ===
            "FEM Analist", "FEA Engineer", "Structural Analyst",
            "Sterkteberekening Engineer", "Stress Engineer", "Stress Analyst",
            "Simulatie Engineer", "CFD Engineer", "Thermisch Analist",
            # === PRODUCT DEVELOPMENT ===
            "Product Developer", "Productontwikkelaar", "R&D Engineer",
            "Development Engineer", "Concept Engineer", "Innovation Engineer"
        ],
        english_titles=[
            "Mechanical Engineer", "Mechanical Designer", "Design Engineer",
            "CAD Designer", "CAD Engineer", "Product Designer",
            "Senior Mechanical Engineer", "Junior Mechanical Engineer",
            "Machine Designer", "Equipment Engineer", "Tooling Engineer",
            "Structural Engineer", "FEA Engineer", "Stress Analyst",
            "R&D Engineer", "Development Engineer", "Product Developer"
        ],
        skills=[
            # === CAD SOFTWARE ===
            "SolidWorks", "Inventor", "Autodesk Inventor", "Creo", "PTC Creo",
            "CATIA", "CATIA V5", "CATIA V6", "Siemens NX", "NX", "Unigraphics",
            "AutoCAD", "AutoCAD Mechanical", "Solid Edge", "FreeCAD",
            "Fusion 360", "Onshape", "SpaceClaim",
            # === 3D MODELLEREN ===
            "3D modelleren", "3D modeling", "parametrisch ontwerpen",
            "sheet metal", "plaatwerk ontwerp", "weldments", "lasconstructies",
            "surfacing", "surface modeling", "assemblage ontwerp",
            # === ANALYSE & SIMULATIE ===
            "FEM", "FEA", "Finite Element Analysis", "eindige elementen",
            "sterkteberekening", "stress analysis", "fatigue analysis",
            "SolidWorks Simulation", "ANSYS", "ABAQUS", "Nastran", "MSC Nastran",
            "CFD", "thermische analyse", "modal analysis", "topology optimization",
            # === ENGINEERING STANDAARDEN ===
            "GD&T", "Geometric Dimensioning", "tolerantie analyse",
            "DIN", "ISO", "EN normen", "ASME Y14.5",
            "engineering change management", "ECN", "PLM",
            # === PDM/PLM ===
            "PDM", "PLM", "Teamcenter", "Windchill", "Vault", "ENOVIA",
            "SolidWorks PDM", "product data management", "BOM management",
            # === MATERIALEN & PRODUCTIE ===
            "materiaalkunde", "staal", "aluminium", "RVS", "kunststoffen",
            "composieten", "DFM", "Design for Manufacturing", "DFMA",
            "rapid prototyping", "3D printen", "additive manufacturing"
        ],
        certificeringen=[
            # === SOLIDWORKS ===
            "SolidWorks CSWA", "CSWP", "CSWE", "SolidWorks CSWP",
            "SolidWorks certificaat", "Certified SolidWorks Associate",
            "Certified SolidWorks Professional", "Certified SolidWorks Expert",
            "CSWPA-SM", "CSWPA-WD", "CSWPA-SU",
            # === AUTODESK ===
            "Autodesk Certified Professional", "Autodesk Inventor Certified",
            "AutoCAD certificaat", "Fusion 360 certificaat",
            # === CATIA/NX ===
            "CATIA certificaat", "Siemens NX certificaat", "Creo certificaat",
            # === OPLEIDINGEN ===
            "HBO Werktuigbouwkunde", "MBO Werktuigbouwkunde",
            "HBO Mechanical Engineering", "BSc Mechanical Engineering",
            "MSc Mechanical Engineering", "TU Delft", "TU Eindhoven",
            "HTS Werktuigbouwkunde", "Ingenieur", "Ir.", "ing.",
            # === AANVULLEND ===
            "VCA VOL", "VCA Basis", "PRINCE2", "Six Sigma Green Belt"
        ],
        look_alikes=["tekenaar_constructeur", "werktuigbouwer", "productontwerper"],
        typische_werkgevers=[
            "VDL", "ASML", "Philips", "DAF", "Fokker"
        ],
        concurrenten=[
            "VDL", "ASML", "Philips", "DAF", "Fokker", "Thales"
        ],
        sector_keywords=["werktuigbouw", "mechanical", "constructie", "productie", "machinebouw", "R&D"]
    ),
}

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white

def create_resume_pdf():
    filename = "Lokesh_Babu_Sharma_Resume.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter,
                           rightMargin=0.5*inch, leftMargin=0.5*inch,
                           topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#1a365d'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#2c5282'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=HexColor('#1a365d'),
        spaceAfter=6,
        spaceBefore=8,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=HexColor('#2c5282'),
        borderPadding=2,
        backColor=HexColor('#e6f0ff')
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=4,
        leftIndent=15,
        bulletIndent=5,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#2c5282'),
        spaceAfter=2,
        fontName='Helvetica-Bold'
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )
    
    # Header
    story.append(Paragraph("LOKESH BABU SHARMA", title_style))
    story.append(Paragraph("Senior Java Developer | Cloud Architect | Microservices Expert", subtitle_style))
    story.append(Paragraph("Email: luckysharma824@gmail.com | Phone: +91-9997105792", contact_style))
    story.append(Paragraph("LinkedIn: linkedin.com/in/the-lokesh-babu | GitHub: github.com/luckysharma824 | Location: Gurgaon, Haryana, India", contact_style))
    
    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_header_style))
    summary_text = """Results-driven Senior Technology Consultant with 6.5+ years of progressive experience architecting and delivering 
    enterprise-scale Java applications for Fortune 500 clients. Expert in cloud-native microservices development, AWS serverless architecture, 
    and application modernization initiatives. Proven track record of delivering $500K+ in cost savings, processing 1M+ daily transactions, 
    and achieving 80% performance improvements through strategic optimization. Specialized in transforming legacy monolithic systems into 
    scalable cloud solutions while leading cross-functional global teams. AWS Certified Cloud Practitioner with demonstrated expertise in 
    Spring Boot, Hibernate, Event-Driven Architecture, and DevOps practices."""
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Core Competencies
    story.append(Paragraph("CORE COMPETENCIES", section_header_style))
    competencies = [
        "<b>Programming Languages:</b> Java (Core & Advanced), J2EE, JSP, Servlets, JDBC, Multithreading",
        "<b>Frameworks & Libraries:</b> Spring Boot, Spring MVC, Spring Security, Spring Cloud, Hibernate, JPA, gRPC",
        "<b>Microservices & Architecture:</b> RESTful APIs, Event-Driven Design, Domain-Driven Design, SOLID Principles",
        "<b>Cloud Platforms:</b> AWS (Lambda, EC2, S3, SQS, SNS, DynamoDB, RDS, CloudWatch, Step Functions)",
        "<b>Databases:</b> MySQL, PostgreSQL, Oracle, MongoDB, DynamoDB, Cassandra, Redis, RocksDB",
        "<b>DevOps & Tools:</b> Docker, Kubernetes, Jenkins, Git, Maven, Gradle, Terraform, CloudFormation",
        "<b>Messaging & Streaming:</b> Apache Kafka, IBM MQ, AWS SQS/SNS, Event Streaming",
        "<b>Testing & Quality:</b> JUnit, Mockito, Test-Driven Development (TDD), SonarQube, Code Reviews",
        "<b>Monitoring & Logging:</b> ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch, APM",
        "<b>Methodologies:</b> Agile/Scrum, CI/CD Pipelines, DevOps, Code Quality Management, Technical Mentorship"
    ]
    for comp in competencies:
        story.append(Paragraph(f"• {comp}", bullet_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_header_style))
    
    # Ernst & Young
    story.append(Paragraph("Senior Technology Consultant (Java Developer) | Mar 2022 - Present", job_title_style))
    story.append(Paragraph("ERNST & YOUNG LLP", company_style))
    
    ey_bullets = [
        "Spearheaded enterprise application modernization initiatives for Fortune 500 clients, transforming legacy monolithic systems into cloud-native microservices architectures, migrating 500GB+ data and handling 25K+ concurrent users with zero downtime during deployment",
        "Architected and deployed serverless solutions using AWS Lambda, Step Functions, DynamoDB, and SQS/SNS, processing 500K+ events daily and reducing infrastructure costs by $200K annually (40%) while improving scalability and reducing latency from 2s to 200ms",
        "Led technical implementation within cross-functional agile teams of 15+ developers across 3 global locations, driving best practices in code review, CI/CD pipeline optimization, and DevOps workflows, delivering 12+ production releases with 98% on-time delivery rate",
        "Engineered 15+ mission-critical microservices serving as foundational components for 20+ dependent applications, processing 1M+ daily transactions and achieving 80% response time improvement (from 1.2s to 240ms) through strategic caching, query optimization, and distributed computing patterns",
        "Drove code quality transformation by refactoring 20+ legacy services (150K+ lines of code), reducing codebase complexity by 35%, improving maintainability scores from 40% to 85% through adherence to SOLID principles, and increasing test coverage from 45% to 92%",
        "Resolved 75+ critical production defects affecting 100K+ users through systematic root cause analysis and preventive measures, reducing application crashes by 70% (from 200 to 60 monthly incidents), improving overall system stability to 99.95% uptime, and reducing MTTR from 4 hours to 45 minutes"
    ]
    for bullet in ey_bullets:
        story.append(Paragraph(f"• {bullet}", bullet_style))
    
    story.append(Paragraph("<i>Key Technologies: Java 8/11/17, Spring Boot, AWS Lambda, DynamoDB, Terraform, CloudFormation, Oracle, PostgreSQL, Redis, Kafka, Docker, Jenkins, ELK Stack</i>", bullet_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Smartbox
    story.append(Paragraph("Software Engineer (Java Developer) | May 2021 - Mar 2022", job_title_style))
    story.append(Paragraph("SMARTBOX ECOMMERCE SOLUTIONS PVT. LTD.", company_style))
    
    smartbox_bullets = [
        "Developed core backend infrastructure for IoT-enabled smart locker logistics platform serving 500+ retail locations across 15 cities, handling 15K+ daily locker operations with 99.8% uptime SLA compliance and processing 500K+ transactions monthly",
        "Designed and implemented QR code authentication and multi-channel SMS engagement systems, processing 30K+ monthly messages, increasing customer adoption rates by 45% and improving customer satisfaction scores from 3.2 to 4.5/5 through seamless user experience",
        "Established comprehensive monitoring framework using ELK Stack (Elasticsearch, Logstash, Kibana) processing 2GB+ daily logs, enabling real-time analytics and proactive incident detection across 100+ endpoints, reducing MTTR by 60% (from 2.5 hours to 1 hour)",
        "Engineered automated audit service from ground up to track messaging and email costs across platform, monitoring $15K+ monthly communication spend, providing financial visibility that identified $60K annual cost optimization opportunities (35%)",
        "Championed code quality improvements through systematic refactoring initiatives across 80K+ lines of code, reducing technical debt by 30%, eliminating 200+ code smells, while enhancing test coverage from 55% to 85% and reducing build time by 40%"
    ]
    for bullet in smartbox_bullets:
        story.append(Paragraph(f"• {bullet}", bullet_style))
    
    story.append(Paragraph("<i>Key Technologies: Java 8, Spring Boot, MySQL, AWS S3, Redis, ELK Stack, REST APIs, Microservices, JUnit</i>", bullet_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Oodles
    story.append(Paragraph("Senior Associate Consultant (Java Developer) | Apr 2019 - May 2021", job_title_style))
    story.append(Paragraph("OODLES TECHNOLOGIES PVT. LTD.", company_style))
    
    oodles_bullets = [
        "Delivered technical solutions across diverse verticals for 8+ enterprise clients including blockchain-based identity systems, IoT platforms, social networking applications (15K+ active users), and e-commerce marketplaces processing $500K+ monthly GMV",
        "Architected microservices-based solutions serving 25K+ daily users with RESTful API design, implementing OAuth 2.0/JWT authentication and role-based access control for enterprise security compliance, achieving zero security breaches and maintaining 100% SOC 2 compliance",
        "Pioneered WhatsApp Business API integration for automated customer engagement, processing 75K+ monthly messages across 5 client projects, with 98.5% delivery success rate and reducing customer response time from 4 hours to 15 minutes, improving customer engagement by 65%",
        "Successfully delivered 50+ feature enhancements and resolved 80+ production defects across 6 concurrent projects, maintaining 95% sprint commitment achievement and zero missed SLA deadlines over 24 months",
        "Elevated engineering standards by introducing code review protocols (500+ reviews conducted), unit testing frameworks, and design patterns, improving overall code quality metrics by 50%, reducing defect density from 8 to 3 per KLOC, and improving code coverage from 40% to 90%"
    ]
    for bullet in oodles_bullets:
        story.append(Paragraph(f"• {bullet}", bullet_style))
    
    story.append(Paragraph("<i>Key Technologies: Java 8, Spring Boot, PostgreSQL, MySQL, MongoDB, Redis, AWS S3, OAuth 2.0, JWT, WebRTC, WhatsApp Business API</i>", bullet_style))
    
    # Page break before projects
    story.append(PageBreak())
    
    # Key Projects
    story.append(Paragraph("KEY PROJECTS", section_header_style))
    
    projects = [
        {
            "title": "CUSTOMER OUTPUT - FIDELITY | Ernst & Young LLP",
            "desc": "Architected enterprise-grade automated communication platform delivering multi-channel customer notifications (email, PDF, postal). Designed serverless AWS infrastructure processing 100K+ daily transactions with 80% latency reduction through event-driven architecture.",
            "tech": "Java, AWS Lambda, Step Functions, CloudFormation, Terraform, Oracle, DynamoDB, SQS/SNS"
        },
        {
            "title": "SMARTBOX DIGITAL LOCKERS | Smartbox Ecommerce Solutions",
            "desc": "Engineered IoT-enabled digital locker management system supporting 500+ retail locations. Implemented real-time device monitoring, QR-based authentication, and SMS engagement workflows. Achieved 99.8% system uptime and 70% performance improvement through strategic caching and query optimization.",
            "tech": "Java, Spring Boot, MySQL, AWS S3, ELK Stack, Redis, REST APIs"
        },
        {
            "title": "NEXOGIC - HEALTH PRACTITIONER NETWORK | Oodles Technologies",
            "desc": "Developed HIPAA-compliant healthcare collaboration platform enabling secure practitioner networking with encrypted chat, WebRTC video conferencing, and MFA authentication. Built research sharing infrastructure serving 10K+ healthcare professionals with zero security breaches.",
            "tech": "Java, Spring Boot, PostgreSQL, AWS S3, WebRTC, OAuth 2.0, JWT"
        },
        {
            "title": "BELFRICS & PARITEX CRYPTOCURRENCY EXCHANGE | Oodles Technologies",
            "desc": "Engineered high-frequency cryptocurrency trading platform handling real-time order matching and settlement for Bitcoin, Ethereum, and digital assets. Implemented fault-tolerant architecture with Redis caching achieving sub-100ms trade execution latency under peak load.",
            "tech": "Java, Spring Boot, MySQL, Redis, AWS, Blockchain, WebSocket, REST APIs"
        }
    ]
    
    for project in projects:
        story.append(Paragraph(f"<b>{project['title']}</b>", job_title_style))
        story.append(Paragraph(project['desc'], bullet_style))
        story.append(Paragraph(f"<i>Technologies: {project['tech']}</i>", bullet_style))
        story.append(Spacer(1, 0.05*inch))
    
    # Education & Certifications
    story.append(Paragraph("EDUCATION & CERTIFICATIONS", section_header_style))
    
    education = [
        ("<b>Master of Computer Applications (MCA)</b> | Aug 2016 - Jul 2019", "M.J.P. Rohilkhand University, Bareilly, India"),
        ("<b>Bachelor of Science (B.Sc.)</b> | Jul 2010 - Dec 2013", "M.J.P. Rohilkhand University, Bareilly, India"),
        ("<b>AWS Certified Cloud Practitioner (CFL-C01)</b> | 2023", "Amazon Web Services")
    ]
    
    for edu in education:
        story.append(Paragraph(edu[0], bullet_style))
        story.append(Paragraph(edu[1], bullet_style))
        story.append(Spacer(1, 0.05*inch))
    
    # Key Achievements
    story.append(Paragraph("KEY ACHIEVEMENTS & METRICS", section_header_style))
    
    achievements = [
        "Delivered $500K+ in cumulative cost savings through cloud optimization and infrastructure modernization",
        "Architected 15+ microservices processing 1M+ daily transactions with 99.95% uptime SLA",
        "Achieved 80% response time improvement (1.2s to 240ms) through strategic performance optimization",
        "Reduced infrastructure costs by $200K annually (40%) through serverless architecture adoption",
        "Led teams of 15+ developers across 3 global locations with 98% on-time delivery rate",
        "Improved test coverage from 45% to 92% and code maintainability from 40% to 85%",
        "Reduced production incidents by 70% and MTTR from 4 hours to 45 minutes",
        "Conducted 500+ code reviews and mentored junior developers on best practices"
    ]
    
    for achievement in achievements:
        story.append(Paragraph(f"✓ {achievement}", bullet_style))
    
    # Build PDF
    doc.build(story)
    print(f"PDF resume generated successfully: {filename}")

if __name__ == "__main__":
    create_resume_pdf()

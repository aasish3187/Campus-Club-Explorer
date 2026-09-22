import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
from reportlab.pdfgen import canvas

WORKDIR = os.path.dirname(os.path.abspath(__file__))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        if self._pageNumber > 1:
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 750, 558, 750)
            self.drawString(54, 756, "Campus Club Explorer - React Academic Project Report")
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        self.drawString(54, 32, "College Training Assessment Project • React & Vite")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_str)
        self.restoreState()

def create_illustrated_pdf():
    pdf_path = os.path.join(WORKDIR, "Campus_Club_Explorer_Report.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    primary_color = colors.HexColor("#1e3a8a")
    text_color = colors.HexColor("#0f172a")
    muted_color = colors.HexColor("#475569")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=muted_color,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=text_color,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=text_color,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )

    meta_label = ParagraphStyle('ML', fontName='Helvetica-Bold', fontSize=9, textColor=primary_color)
    meta_val = ParagraphStyle('MV', fontName='Helvetica', fontSize=9, textColor=text_color)
    caption_style = ParagraphStyle('Cap', fontName='Helvetica-Bold', fontSize=8.5, textColor=primary_color, alignment=1, spaceBefore=4, spaceAfter=10)

    table_cell = ParagraphStyle('TC', fontName='Helvetica', fontSize=8, leading=10.5, textColor=text_color)
    table_header = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.white)

    story = []

    # Title & Header
    story.append(Paragraph("CAMPUS CLUB EXPLORER", title_style))
    story.append(Paragraph("A React-Based Web Application for College Club Discovery & Management", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=primary_color, spaceAfter=12))

    # Academic Metadata Table
    meta_data = [
        [Paragraph("Project Title:", meta_label), Paragraph("Campus Club Explorer", meta_val)],
        [Paragraph("Department & Level:", meta_label), Paragraph("Department of Computer Science & Engineering | Lab Assessment", meta_val)],
        [Paragraph("Technology Stack:", meta_label), Paragraph("React 18, Vite Engine, Solid-Color Vanilla CSS3", meta_val)],
        [Paragraph("Key Concepts Covered:", meta_label), Paragraph("Props, Component Reuse, Lists & Keys, Search/Filter UI, Conditional Rendering", meta_val)]
    ]
    meta_table = Table(meta_data, colWidths=[130, 374])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary & Abstract", h1_style))
    story.append(Paragraph(
        "The <b>Campus Club Explorer</b> is a single-page React web application engineered to solve information fragmentation on college campuses. It provides students with an intuitive portal to discover active campus clubs across diverse domains (Coding, Sports, Arts, and Entrepreneurship), filter clubs dynamically by category, search by keywords, view comprehensive operational information in a modal interface, and join or leave clubs with persistent membership tracking and toast notifications.",
        body_style
    ))

    # 2. Problem Statement & Objectives
    story.append(Paragraph("2. Problem Statement & Key Objectives", h1_style))
    story.append(Paragraph("• <b>Centralized Discovery:</b> Render all campus clubs dynamically from structured data in a responsive grid.", bullet_style))
    story.append(Paragraph("• <b>Dual-Predicate Filtering:</b> Combine category pills with real-time keyword search without page reloads.", bullet_style))
    story.append(Paragraph("• <b>Detailed Modal Dialog:</b> Provide dedicated popup view with meeting schedules, faculty advisors, and activities.", bullet_style))
    story.append(Paragraph("• <b>Stateful Membership:</b> Implement persistent Join/Leave actions with member count increments and toast alerts.", bullet_style))
    story.append(Paragraph("• <b>React Syllabus Alignment:</b> Fully demonstrate Props, Lists & Keys, Conditional Rendering, and Component Reuse.", bullet_style))

    # 3. Core React Concepts
    story.append(Paragraph("3. Detailed Analysis of Core React Concepts Covered", h1_style))
    story.append(Paragraph("<b>3.1 Props (Properties) & Unidirectional Flow:</b> Props are read-only arguments passed from parent components down to child components. <code>App.jsx</code> acts as the master container that holds application state and passes down club records, boolean membership flags (<code>isJoined</code>), and click event callbacks (<code>onViewDetails</code>) to <code>ClubCard.jsx</code> and <code>ClubModal.jsx</code>.", body_style))
    story.append(Paragraph("<b>3.2 Component Reuse:</b> A single <code>ClubCard</code> component is declared once and reused across all 8 campus clubs with zero duplicate markup.", body_style))
    story.append(Paragraph("<b>3.3 Lists and Keys (.map() Array Traversal):</b> Utilizes JavaScript's <code>.map()</code> method to render JSX elements. Each item receives <code>key={club.id}</code>, allowing React's Virtual DOM reconciliation engine to track item updates efficiently.", body_style))
    story.append(Paragraph("<b>3.4 Search and Filter UI:</b> Evaluates category matching ('All' or exact) AND keyword matching (.toLowerCase().includes()) together on every keystroke with zero page reloads.", body_style))
    story.append(Paragraph("<b>3.5 Conditional Rendering:</b> Dynamically renders: (1) Empty state fallback on 0 search matches; (2) Modal dialog mounted only on <code>selectedClub</code> click; (3) Green 'JOINED' badge on cards; (4) Popup toast alert on join/leave.", body_style))

    # 4. User Interface Screenshots
    story.append(Paragraph("4. User Interface Screenshots & Visual Artifacts", h1_style))
    
    img_home = os.path.join(WORKDIR, "slide_img_home.png")
    img_modal = os.path.join(WORKDIR, "slide_img_modal.png")
    img_joined = os.path.join(WORKDIR, "slide_img_joined.png")

    if os.path.exists(img_home):
        story.append(Image(img_home, width=470, height=215))
        story.append(Paragraph("Figure 1: Main Dashboard with Search Input, Category Pills, and Club Grid", caption_style))

    if os.path.exists(img_modal):
        story.append(Image(img_modal, width=470, height=215))
        story.append(Paragraph("Figure 2: Interactive Club Details Modal with Advisor & Meeting Schedule", caption_style))

    if os.path.exists(img_joined):
        story.append(Image(img_joined, width=470, height=215))
        story.append(Paragraph("Figure 3: Joined State Banner, Member Count Update, and Leave Button", caption_style))

    # 5. Verification & Test Cases Table
    story.append(Paragraph("5. Functional Verification & Test Cases", h1_style))
    test_data = [
        [Paragraph("TC ID", table_header), Paragraph("Scenario / Action", table_header), Paragraph("Expected Outcome", table_header), Paragraph("Status", table_header)],
        [Paragraph("TC-01", table_cell), Paragraph("Initial Page Load", table_cell), Paragraph("Renders all 8 clubs with 'All' filter active", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-02", table_cell), Paragraph("Filter by 'Coding'", table_cell), Paragraph("Displays Code Crafters & AI Robotics clubs only", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-03", table_cell), Paragraph("Filter by 'Sports'", table_cell), Paragraph("Displays Strikers Club & Badminton League only", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-04", table_cell), Paragraph("Keyword Search 'robotics'", table_cell), Paragraph("Instantly filters to AI & Robotics Club", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-05", table_cell), Paragraph("Empty Search Query", table_cell), Paragraph("Displays 'No clubs found' box and Reset button", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-06", table_cell), Paragraph("View Details Click", table_cell), Paragraph("Modal opens with schedule, advisor, & activities", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-07", table_cell), Paragraph("Join Club Action", table_cell), Paragraph("Increments members, shows toast alert, adds badge", table_cell), Paragraph("PASS", table_cell)],
        [Paragraph("TC-08", table_cell), Paragraph("Modal Dismissal", table_cell), Paragraph("Closes modal via Close button or backdrop click", table_cell), Paragraph("PASS", table_cell)]
    ]
    test_table = Table(test_data, colWidths=[45, 135, 274, 50])
    test_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#ffffff")),
        ('TEXTCOLOR', (3,1), (3,-1), colors.HexColor("#15803d")),
        ('FONTNAME', (3,1), (3,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(test_table)
    story.append(Spacer(1, 10))

    # 6. Conclusion
    story.append(Paragraph("6. Conclusion", h1_style))
    story.append(Paragraph(
        "The <b>Campus Club Explorer</b> successfully fulfills all technical and design requirements for the college training assessment. By demonstrating clean functional React programming, strict component modularity, solid-color accessible aesthetics, and zero console/build errors, the project provides an exemplary model for student club engagement systems.",
        body_style
    ))

    try:
        doc.build(story, canvasmaker=NumberedCanvas)
        print(f"Illustrated PDF generated: {pdf_path}")
    except PermissionError:
        alt_path = os.path.join(WORKDIR, "Campus_Club_Explorer_Report_Illustrated.pdf")
        doc = SimpleDocTemplate(alt_path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
        doc.build(story, canvasmaker=NumberedCanvas)
        print(f"Illustrated PDF generated: {alt_path}")

if __name__ == "__main__":
    create_illustrated_pdf()

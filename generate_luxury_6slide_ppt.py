import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

WORKDIR = os.path.dirname(os.path.abspath(__file__))

def create_beautiful_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    PRIMARY_NAVY = RGBColor(30, 58, 138)    # #1e3a8a
    ACCENT_BLUE = RGBColor(37, 99, 235)     # #2563eb
    DARK_TEXT = RGBColor(15, 23, 42)        # #0f172a
    MUTED_TEXT = RGBColor(71, 85, 105)      # #475569
    LIGHT_BG = RGBColor(248, 250, 252)      # #f8fafc
    WHITE = RGBColor(255, 255, 255)
    BORDER_LIGHT = RGBColor(226, 232, 240)  # #e2e8f0
    TAG_BG = RGBColor(239, 246, 255)        # #eff6ff
    TAG_TEXT = RGBColor(29, 78, 216)        # #1d4ed8
    EMERALD_GREEN = RGBColor(21, 128, 61)   # #15803d
    EMERALD_BG = RGBColor(220, 252, 231)    # #dcfce7

    img_home = os.path.join(WORKDIR, "slide_img_home.png")
    img_modal = os.path.join(WORKDIR, "slide_img_modal.png")
    img_joined = os.path.join(WORKDIR, "slide_img_joined.png")
    img_card = os.path.join(WORKDIR, "slide_img_card.png")

    slides_data = [
        # SLIDE 1: Hero Cover
        {
            "type": "hero",
            "tag": "COLLEGE TRAINING LAB ASSESSMENT",
            "title": "Campus Club Explorer",
            "subtitle": "An Interactive React Web Application for Discovering and Managing College Student Clubs",
            "metadata": [
                ("Department:", "Computer Science & Engineering"),
                ("Key Topics:", "Props • Lists & Keys • Search/Filter UI • Conditional Rendering • Component Reuse"),
                ("Tech Stack:", "React 18 • Vite Engine • Vanilla CSS3 (Solid Palette)")
            ],
            "image": img_home,
            "notes": "Good morning respected faculty members and sir. Today I am presenting my React project, 'Campus Club Explorer'. This is a responsive single-page application built to help college students easily discover, filter, and join campus clubs that match their passions."
        },
        # SLIDE 2: Problem Statement & Architecture
        {
            "type": "content",
            "category": "PROJECT BACKGROUND & ARCHITECTURE",
            "title": "Problem Statement & Solution Architecture",
            "cards": [
                ("1. The Campus Problem", "Student club schedules, advisor details, and event updates are fragmented across noticeboards and chat groups, causing low student awareness and participation."),
                ("2. The Engineering Solution", "A centralized, single-page application categorizing clubs into Coding, Sports, Arts, and Entrepreneurship with real-time interactive search."),
                ("3. Unidirectional Data Architecture", "App.jsx serves as the single source of truth, managing reactive state and passing data down to child components via props."),
                ("4. High-Performance Front-End", "Built with React 18 functional components and Vite bundler for sub-500ms hot module replacement with zero build errors.")
            ],
            "image": img_card,
            "image_badge": "LIVE DASHBOARD SHOWCASE",
            "image_caption": "Club Directory with Search Bar, Filter Pills & Membership Count",
            "notes": "Sir, in college campuses, students frequently miss club meetings because info is scattered. Campus Club Explorer centralizes all information. Architecturally, App.jsx manages state and passes data down to child components following React's unidirectional flow."
        },
        # SLIDE 3: React Concepts - Props, Lists & Keys
        {
            "type": "content",
            "category": "CORE REACT CONCEPTS",
            "title": "Props, Component Reuse, Lists & Keys",
            "cards": [
                ("1. Props (Properties)", "Read-only arguments passed from parent (App.jsx) to child (ClubCard.jsx). ClubCard receives the club object, isJoined flag, and click handlers cleanly."),
                ("2. Component Reuse", "A single ClubCard component is authored once and dynamically reused across all 8 campus clubs with zero duplicate markup."),
                ("3. Array Mapping (.map)", "JavaScript's .map() iterates through the filtered clubs array, returning a <ClubCard /> for each matching club record."),
                ("4. The Unique 'key' Prop", "Each item receives key={club.id}. This enables React's Virtual DOM reconciliation engine to track item updates efficiently without redrawing the entire page.")
            ],
            "image": img_card,
            "image_badge": "COMPONENT REUSE IN ACTION",
            "image_caption": "8 Dynamic Club Cards Rendered using .map() and unique keys",
            "notes": "Sir, here are two major concepts: Props and Lists. Instead of writing 8 separate cards, we created one reusable ClubCard component. We map over the array using club.id as the key, which lets React re-render only the exact card that changes."
        },
        # SLIDE 4: Search & Category Filter UI
        {
            "type": "content",
            "category": "DYNAMIC INTERACTION",
            "title": "Search & Category Filter UI",
            "cards": [
                ("1. Controlled Form State", "searchQuery and selectedCategory are maintained in React state using the useState hook, making inputs fully controlled."),
                ("2. Dual-Predicate Filter Logic", "The filter function evaluates category matching ('All' or exact match) AND keyword matching (.toLowerCase().includes()) together on every keystroke."),
                ("3. Zero Page Reloads", "Filtered results update reactively in real time without refreshing the browser, providing a seamless user experience."),
                ("4. Ergonomic Controls", "Includes active category pill indicators, an instant 'Clear' button in the search bar, and dynamic club counters.")
            ],
            "image": img_home,
            "image_badge": "SEARCH & FILTER CONTROLS",
            "image_caption": "Instant Search Bar & Category Pills (Coding, Sports, Arts, E-Cell)",
            "notes": "Our search and filter UI evaluates both the active category button and the search text simultaneously. When a student selects 'Coding' and types 'AI', it filters instantly without page reloads using clean array methods."
        },
        # SLIDE 5: Conditional Rendering & Details Modal
        {
            "type": "content",
            "category": "ADVANCED UI LOGIC",
            "title": "Conditional Rendering & Interactive Modal",
            "cards": [
                ("1. Short-Circuit Evaluation", "{selectedClub && <ClubModal ... />} ensures zero modal DOM overhead until a user clicks 'View Details' on a club card."),
                ("2. Empty State Fallback", "A ternary operator renders the club grid when items exist, or a friendly 'No clubs found' box with a 'Reset Filters' button."),
                ("3. Comprehensive Club Modal", "Displays weekly meeting schedule, faculty coordinator advisor, active member counts, and bulleted activity items."),
                ("4. Accessible Dismissal", "Modal closes gracefully on clicking the 'Close' button, the 'Done' button, or tapping the darkened background.")
            ],
            "image": img_modal,
            "image_badge": "MODAL DIALOG POPUP",
            "image_caption": "Details Popup Showing Advisor, Meeting Day & Activities",
            "notes": "Sir, we demonstrated Conditional Rendering in multiple places: showing the modal only when selectedClub is not null, showing an empty state message if no clubs match, and closing the modal cleanly on background click."
        },
        # SLIDE 6: Membership Tracking & Conclusion
        {
            "type": "content",
            "category": "EVALUATION SUMMARY & RESULTS",
            "title": "Membership Tracking, Testing & Conclusion",
            "cards": [
                ("1. Interactive Join / Leave", "Clicking 'Join Club' toggles membership, increments member count, and changes button to 'Leave Club'."),
                ("2. Persistent 'JOINED' Tag", "Card immediately displays a green 'JOINED' badge on the dashboard, tracking student membership across views."),
                ("3. Real-Time Popup Alerts", "Displays a green toast alert: 'Success: You have joined [Club]!' auto-dismissed in 3 seconds."),
                ("4. Rigorous Verification", "All 8 functional test cases PASS with 0 errors. Full alignment with college lab evaluation criteria.")
            ],
            "image": img_joined,
            "image_badge": "LIVE MEMBERSHIP STATUS",
            "image_caption": "Joined Status Banner, Leave Button & Live Member Count",
            "notes": "Finally, we implemented interactive membership tracking. When you join, it shows a popup message, updates member count, and marks the card with a JOINED badge. All test cases passed with zero build errors. Thank you, Sir!"
        }
    ]

    for idx, sdata in enumerate(slides_data):
        slide = prs.slides.add_slide(blank_layout)

        # Base Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = LIGHT_BG
        bg.line.fill.background()

        # Speaker notes
        slide.notes_slide.notes_text_frame.text = sdata.get("notes", "")

        if sdata["type"] == "hero":
            # Top Navy Accent Bar
            top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
            top_bar.fill.solid()
            top_bar.fill.fore_color.rgb = PRIMARY_NAVY
            top_bar.line.fill.background()

            # Left Card Container
            lcard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(6.2), Inches(6.5))
            lcard.fill.solid()
            lcard.fill.fore_color.rgb = WHITE
            lcard.line.color.rgb = BORDER_LIGHT
            lcard.line.width = Pt(1.5)

            # Left Text Box
            ltb = slide.shapes.add_textbox(Inches(1.1), Inches(0.8), Inches(5.6), Inches(5.9))
            ltf = ltb.text_frame
            ltf.word_wrap = True

            # Category pill tag
            p_tag = ltf.paragraphs[0]
            p_tag.text = sdata["tag"]
            p_tag.font.size = Pt(11)
            p_tag.font.bold = True
            p_tag.font.color.rgb = TAG_TEXT
            p_tag.font.name = "Arial"

            # Main Title
            p_title = ltf.add_paragraph()
            p_title.text = sdata["title"]
            p_title.font.size = Pt(38)
            p_title.font.bold = True
            p_title.font.color.rgb = PRIMARY_NAVY
            p_title.font.name = "Arial"
            p_title.space_before = Pt(8)

            # Subtitle
            p_sub = ltf.add_paragraph()
            p_sub.text = sdata["subtitle"]
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = MUTED_TEXT
            p_sub.font.name = "Arial"
            p_sub.space_before = Pt(8)

            # Divider line
            p_div = ltf.add_paragraph()
            p_div.text = "—" * 28
            p_div.font.size = Pt(12)
            p_div.font.color.rgb = BORDER_LIGHT
            p_div.space_before = Pt(10)

            # Metadata items
            for label, val in sdata["metadata"]:
                p_m = ltf.add_paragraph()
                p_m.text = f"{label} {val}"
                p_m.font.size = Pt(11.5)
                p_m.font.color.rgb = DARK_TEXT
                p_m.font.name = "Arial"
                p_m.space_before = Pt(8)

            # Right Image Container
            rcard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(0.5), Inches(5.333), Inches(6.5))
            rcard.fill.solid()
            rcard.fill.fore_color.rgb = WHITE
            rcard.line.color.rgb = BORDER_LIGHT
            rcard.line.width = Pt(1.5)

            # Right Image Top Ribbon
            rtop = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.4), Inches(0.7), Inches(4.933), Inches(0.45))
            rtop.fill.solid()
            rtop.fill.fore_color.rgb = PRIMARY_NAVY
            rtop.line.fill.background()
            rtp = rtop.text_frame.paragraphs[0]
            rtp.text = "LIVE WEB APP PREVIEW (REACT + VITE)"
            rtp.font.size = Pt(10.5)
            rtp.font.bold = True
            rtp.font.color.rgb = WHITE
            rtp.alignment = PP_ALIGN.CENTER

            # Add Image
            if os.path.exists(sdata["image"]):
                slide.shapes.add_picture(sdata["image"], Inches(7.4), Inches(1.3), Inches(4.933), Inches(5.4))

        else:
            # Header Bar
            header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.2))
            header_bar.fill.solid()
            header_bar.fill.fore_color.rgb = PRIMARY_NAVY
            header_bar.line.fill.background()

            # Accent underline on header
            acc_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.2), Inches(13.333), Inches(0.04))
            acc_line.fill.solid()
            acc_line.fill.fore_color.rgb = ACCENT_BLUE
            acc_line.line.fill.background()

            # Header Text Box
            htb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(10.5), Inches(0.95))
            htf = htb.text_frame
            htf.word_wrap = True

            # Category breadcrumb
            p_cat = htf.paragraphs[0]
            p_cat.text = sdata["category"]
            p_cat.font.size = Pt(9.5)
            p_cat.font.bold = True
            p_cat.font.color.rgb = RGBColor(191, 219, 254)
            p_cat.font.name = "Arial"

            # Slide Title
            p_head = htf.add_paragraph()
            p_head.text = sdata["title"]
            p_head.font.size = Pt(23)
            p_head.font.bold = True
            p_head.font.color.rgb = WHITE
            p_head.font.name = "Arial"

            # Page Indicator Chip
            pchip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.6), Inches(0.35), Inches(1.0), Inches(0.45))
            pchip.fill.solid()
            pchip.fill.fore_color.rgb = RGBColor(30, 64, 175)
            pchip.line.color.rgb = RGBColor(96, 165, 250)
            pchip.line.width = Pt(1)
            pchip_p = pchip.text_frame.paragraphs[0]
            pchip_p.text = f"{idx + 1} of 6"
            pchip_p.font.size = Pt(12)
            pchip_p.font.bold = True
            pchip_p.font.color.rgb = WHITE
            pchip_p.alignment = PP_ALIGN.CENTER

            # Left side: 4 Content Cards
            card_x = Inches(0.8)
            card_w = Inches(6.5)
            start_y = 1.45
            card_h = 1.25
            spacing = 0.16

            for cidx, (ctitle, cdesc) in enumerate(sdata.get("cards", [])):
                y_pos = start_y + cidx * (card_h + spacing)

                # Card background
                card_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card_x, Inches(y_pos), card_w, Inches(card_h))
                card_shape.fill.solid()
                card_shape.fill.fore_color.rgb = WHITE
                card_shape.line.color.rgb = BORDER_LIGHT
                card_shape.line.width = Pt(1.5)

                # Left colored accent ribbon on each card
                ribbon = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, card_x, Inches(y_pos), Inches(0.12), Inches(card_h))
                ribbon.fill.solid()
                ribbon.fill.fore_color.rgb = ACCENT_BLUE if cidx % 2 == 0 else PRIMARY_NAVY
                ribbon.line.fill.background()

                # Text inside card
                tb = slide.shapes.add_textbox(card_x + Inches(0.25), Inches(y_pos + 0.08), card_w - Inches(0.4), Inches(card_h - 0.16))
                tf = tb.text_frame
                tf.word_wrap = True

                pt = tf.paragraphs[0]
                pt.text = ctitle
                pt.font.size = Pt(13)
                pt.font.bold = True
                pt.font.color.rgb = PRIMARY_NAVY
                pt.font.name = "Arial"

                pd = tf.add_paragraph()
                pd.text = cdesc
                pd.font.size = Pt(10.5)
                pd.font.color.rgb = DARK_TEXT
                pd.font.name = "Arial"
                pd.space_before = Pt(2)

            # Right side: Visual Showcase Card
            rx = Inches(7.5)
            rw = Inches(5.033)
            ry = Inches(1.45)
            rh = Inches(5.5)

            rcard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, ry, rw, rh)
            rcard.fill.solid()
            rcard.fill.fore_color.rgb = WHITE
            rcard.line.color.rgb = BORDER_LIGHT
            rcard.line.width = Pt(1.5)

            # Image Header Ribbon
            ibadge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx + Inches(0.15), ry + Inches(0.15), rw - Inches(0.3), Inches(0.42))
            ibadge.fill.solid()
            ibadge.fill.fore_color.rgb = PRIMARY_NAVY
            ibadge.line.fill.background()
            ibp = ibadge.text_frame.paragraphs[0]
            ibp.text = sdata.get("image_badge", "LIVE COMPONENT PREVIEW")
            ibp.font.size = Pt(10)
            ibp.font.bold = True
            ibp.font.color.rgb = WHITE
            ibp.alignment = PP_ALIGN.CENTER

            # Add Image
            if os.path.exists(sdata.get("image", "")):
                slide.shapes.add_picture(sdata["image"], rx + Inches(0.15), ry + Inches(0.68), rw - Inches(0.3), Inches(4.1))

            # Bottom caption pill
            cpill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx + Inches(0.15), ry + Inches(4.88), rw - Inches(0.3), Inches(0.48))
            cpill.fill.solid()
            cpill.fill.fore_color.rgb = TAG_BG
            cpill.line.color.rgb = RGBColor(191, 219, 254)
            cpill.line.width = Pt(1)
            cpp = cpill.text_frame.paragraphs[0]
            cpp.text = sdata.get("image_caption", "Actual Application Output")
            cpp.font.size = Pt(9.5)
            cpp.font.bold = True
            cpp.font.color.rgb = TAG_TEXT
            cpp.alignment = PP_ALIGN.CENTER

    out_file = os.path.join(WORKDIR, "Campus_Club_Explorer_Presentation_Latest.pptx")
    prs.save(out_file)
    print(f"Beautiful 6-Slide presentation saved successfully at: {out_file}")
    return out_file

if __name__ == "__main__":
    create_beautiful_presentation()

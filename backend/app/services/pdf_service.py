import io
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_360_report(user_data: dict, interpretation_data: list) -> io.BytesIO:
    """
    Tạo báo cáo PDF 360 độ dựa trên dữ liệu người dùng và các luận giải.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.goldenrod,
        alignment=1,
        spaceAfter=30
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.darkblue,
        spaceBefore=20,
        spaceAfter=10
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        alignment=4 # Justified
    )

    elements = []

    # Title
    elements.append(Paragraph("BÁO CÁO 360HUMAN", title_style))
    elements.append(Paragraph(f"Người sở hữu: {user_data.get('full_name', 'Người dùng')}", styles['Normal']))
    elements.append(Paragraph(f"Ngày xuất: {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # User Info Table
    data = [
        ["Thông tin cá nhân", ""],
        ["Họ tên", user_data.get("full_name")],
        ["Ngày sinh", f"{user_data.get('birth_date')} {user_data.get('birth_time')}"],
        ["Nơi sinh", user_data.get("birth_city")],
        ["Giới tính", user_data.get("gender")]
    ]
    t = Table(data, colWidths=[150, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.goldenrod),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.white)
    ]))
    elements.append(t)
    elements.append(Spacer(1, 30))

    # Interpretation Content
    for topic in interpretation_data:
        elements.append(Paragraph(topic.get("title", "Chủ đề"), section_style))
        elements.append(Paragraph(topic.get("content", "Đang cập nhật..."), body_style))
        elements.append(Spacer(1, 10))

    # Footer
    elements.append(Spacer(1, 50))
    elements.append(Paragraph("--- Bản quyền thuộc về 360Human ---", styles['Italic']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

#!/usr/bin/env python3
"""Render the editable resume content into a recruiter- and ATS-readable PDF."""

from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTENT = Path(__file__).with_name("content.yaml")
DEFAULT_OUTPUT = ROOT / "Resume_PZ.pdf"
BLUE = colors.HexColor("#4f81bd")


class SectionHeading(Flowable):
    """A section label and rule that adapt to the document's available width."""

    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.height = 13

    def wrap(self, available_width, available_height):
        self.width = available_width
        return available_width, self.height

    def draw(self):
        self.canv.setFillColor(colors.black)
        self.canv.setFont("Helvetica-Bold", 8.5)
        self.canv.drawString(0, 3, self.title)
        self.canv.setStrokeColor(BLUE)
        self.canv.setLineWidth(0.45)
        self.canv.line(0, 0, self.width, 0)


def load_content(path: Path) -> dict:
    with path.open(encoding="utf-8") as content_file:
        return yaml.safe_load(content_file)


def text(value: str) -> str:
    return escape(str(value))


def experience_heading(item: dict) -> str:
    parts = [item["title"], item["organization"]]
    if item.get("location"):
        parts.append(item["location"])
    parts.append(item["dates"])
    return " | ".join(parts)


def build_pdf(content: dict, output_path: Path) -> None:
    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=15.5,
            spaceAfter=1.5,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            alignment=TA_CENTER,
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.5,
            spaceAfter=0,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            spaceAfter=2,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.85,
            leading=9.8,
            leftIndent=12,
            firstLineIndent=0,
            spaceAfter=1.4,
        ),
        "job": ParagraphStyle(
            "Job",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.3,
            leading=10,
            spaceAfter=2,
        ),
        "education": ParagraphStyle(
            "Education",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=9.8,
        ),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output_path),
        pagesize=LETTER,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.19 * inch,
        bottomMargin=0.22 * inch,
        title=f"Resume | {content['basics']['name']}",
        author=content["basics"]["name"],
    )

    story = []
    basics = content["basics"]
    portfolio = basics["portfolio"]
    story.extend(
        [
            Paragraph(text(basics["name"]), styles["name"]),
            Paragraph(text(basics["email"]), styles["contact"]),
            Paragraph(text(basics["location"]), styles["contact"]),
            Paragraph(
                f'<link href="{text(portfolio["url"])}" color="#0000ff"><u>{text(portfolio["label"])}</u></link>',
                styles["contact"],
            ),
            Spacer(1, 8),
        ]
    )

    titles = content["section_titles"]
    story.append(SectionHeading(titles["education"]))
    education_rows = []
    for item in content["education"]:
        details = f"<b>{text(item['degree'])}</b><br/>{text(item['institution'])}, {text(item['location'])}"
        education_rows.append(
            [
                Paragraph("•", styles["education"]),
                Paragraph(details, styles["education"]),
                Paragraph(text(item["year"]), styles["education"]),
            ]
        )
    education_table = Table(education_rows, colWidths=[11, 460, 33], hAlign="LEFT")
    education_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.extend([education_table, Spacer(1, 8)])

    story.append(SectionHeading(titles["skills"]))
    for item in content["skills"]:
        skill_markup = f"<b>{text(item['category'])}:</b> {text(item['details'])}"
        story.append(Paragraph(skill_markup, styles["body"]))
    story.append(Spacer(1, 7))

    story.append(SectionHeading(titles["projects"]))
    for item in content["projects"]:
        project_markup = f"<b>{text(item['title'])}:</b> {text(item['details'])}"
        story.append(Paragraph(project_markup, styles["body"]))
    story.append(Spacer(1, 7))

    story.append(SectionHeading(titles["experience"]))
    for item in content["experience"]:
        entry = [Paragraph(text(experience_heading(item)), styles["job"])]
        for bullet in item["bullets"]:
            entry.append(Paragraph(text(bullet), styles["bullet"], bulletText="•"))
        story.append(KeepTogether(entry))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 5))
    story.append(SectionHeading(titles["accomplishments"]))
    accomplishments = [
        ListItem(Paragraph(text(item), styles["bullet"]), leftIndent=10)
        for item in content["accomplishments"]
    ]
    story.append(ListFlowable(accomplishments, bulletType="bullet", start="•", leftIndent=0, bulletFontSize=8))

    document.build(story)


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content", type=Path, default=DEFAULT_CONTENT, help="YAML content file")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output PDF path")
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    build_pdf(load_content(arguments.content), arguments.output)

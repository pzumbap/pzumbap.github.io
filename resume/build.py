#!/usr/bin/env python3
"""Render the resume as a single-column PDF and matching plain-text file."""

from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTENT = Path(__file__).with_name("content.yaml")
DEFAULT_OUTPUT = ROOT / "Resume_PZ.pdf"
INK = colors.HexColor("#172b40")
SECTION_ORDER = ("summary", "experience", "skills", "education", "projects", "certifications")


def load_content(path: Path) -> dict:
    with path.open(encoding="utf-8") as content_file:
        return yaml.safe_load(content_file)


def text(value: str) -> str:
    return escape(str(value))


def experience_heading(item: dict) -> str:
    parts = [item["title"], item["organization"]]
    if item.get("location"):
        parts.append(item["location"])
    return " | ".join(parts)


def education_details(item: dict) -> str:
    return f"{item['institution']} | {item['location']} | {item['year']}"


def plain_text(content: dict) -> str:
    """Use the same source and reading order as the PDF for application forms."""
    basics = content["basics"]
    lines = [
        basics["name"],
        basics["headline"],
        f"{basics['location']} | {basics['email']} | {basics['portfolio']['label']}",
        basics["linkedin"]["label"],
    ]
    for section in SECTION_ORDER:
        if not content.get(section):
            continue
        lines.extend(["", content["section_titles"][section]])
        if section == "summary":
            lines.append(content[section])
        elif section == "experience":
            for item in content[section]:
                lines.append(f"{experience_heading(item)} | {item['dates']}")
                lines.extend(f"- {bullet}" for bullet in item["bullets"])
                lines.append("")
        elif section == "skills":
            lines.extend(f"{item['category']}: {item['details']}" for item in content[section])
        elif section == "education":
            for item in content[section]:
                lines.extend([item["degree"], education_details(item)])
        elif section == "projects":
            lines.extend(f"{item['title']}: {item['details']}" for item in content[section])
        elif section == "certifications":
            lines.extend(content[section])
    return "\n".join(lines).strip() + "\n"


def linked(item: dict) -> str:
    return f'<link href={quoteattr(item["url"])}>{text(item["label"])}</link>'


def build_pdf(content: dict, output_path: Path) -> None:
    base = getSampleStyleSheet()["Normal"]
    body = ParagraphStyle(
        "ResumeBody", parent=base, fontName="Helvetica", fontSize=10,
        leading=11.8, spaceAfter=2, textColor=colors.black,
    )
    styles = {
        "body": body,
        "name": ParagraphStyle(
            "Name", parent=body, fontName="Helvetica-Bold", fontSize=21,
            leading=23, textColor=INK, spaceAfter=3,
        ),
        "headline": ParagraphStyle(
            "Headline", parent=body, fontName="Helvetica-Bold", fontSize=11,
            leading=13, spaceAfter=3,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=body, fontSize=9.5, leading=11.5, spaceAfter=1,
        ),
        "section": ParagraphStyle(
            "Section", parent=body, fontName="Helvetica-Bold", fontSize=10,
            leading=12, spaceBefore=7, spaceAfter=4, textColor=INK,
            keepWithNext=True,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=body, leftIndent=10, firstLineIndent=-8,
        ),
        "education": ParagraphStyle(
            "Education", parent=body, fontName="Helvetica-Bold", keepWithNext=True,
        ),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    basics = content["basics"]
    document = SimpleDocTemplate(
        str(output_path), pagesize=LETTER,
        leftMargin=0.5 * inch, rightMargin=0.5 * inch,
        topMargin=0.45 * inch, bottomMargin=0.45 * inch,
        title=f"{basics['name']} | Data Engineer Resume",
        author=basics["name"],
        subject="Professional experience, technical skills, and education",
    )

    contact = " | ".join([
        text(basics["location"]),
        linked({"label": basics["email"], "url": f"mailto:{basics['email']}"}),
        linked(basics["portfolio"]),
    ])
    # Contact information is in the document body, not in a page header or table.
    story = [
        Paragraph(text(basics["name"]), styles["name"]),
        Paragraph(text(basics["headline"]), styles["headline"]),
        Paragraph(contact, styles["contact"]),
        Paragraph(linked(basics["linkedin"]), styles["contact"]),
    ]

    for section in SECTION_ORDER:
        if not content.get(section):
            continue
        story.append(Paragraph(text(content["section_titles"][section]), styles["section"]))
        if section == "summary":
            story.append(Paragraph(text(content[section]), styles["body"]))
        elif section == "experience":
            for item in content[section]:
                entry = [
                    Paragraph(
                        f"<b>{text(experience_heading(item))}</b> | {text(item['dates'])}",
                        styles["body"],
                    ),
                ]
                entry.extend(
                    Paragraph(f"- {text(bullet)}", styles["bullet"])
                    for bullet in item["bullets"]
                )
                story.extend([KeepTogether(entry), Spacer(1, 3)])
        elif section == "skills":
            for item in content[section]:
                story.append(Paragraph(
                    f"<b>{text(item['category'])}:</b> {text(item['details'])}", styles["body"],
                ))
        elif section == "education":
            for item in content[section]:
                story.append(KeepTogether([
                    Paragraph(text(item["degree"]), styles["education"]),
                    Paragraph(text(education_details(item)), styles["body"]),
                ]))
        elif section == "projects":
            for item in content[section]:
                story.append(Paragraph(
                    f"<b>{text(item['title'])}:</b> {text(item['details'])}", styles["body"],
                ))
        elif section == "certifications":
            story.extend(Paragraph(text(item), styles["body"]) for item in content[section])

    document.build(story)


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content", type=Path, default=DEFAULT_CONTENT, help="YAML content file")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output PDF path")
    parser.add_argument("--text-output", type=Path, help="Plain-text output (defaults to PDF path with .txt suffix)")
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    content = load_content(arguments.content)
    build_pdf(content, arguments.output)
    text_output = arguments.text_output or arguments.output.with_suffix(".txt")
    text_output.parent.mkdir(parents=True, exist_ok=True)
    text_output.write_text(plain_text(content), encoding="utf-8")
    print(f"PDF: {arguments.output}\nText: {text_output}")

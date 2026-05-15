#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "2026.-3-16-个人简历-马梦茹.docx"
OUT = ROOT / "README.md"
ASSETS = ROOT / "assets"

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def collapse(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("导 师", "导师").replace("学 历", "学历")
    text = text.replace("姓 名", "姓名").replace("电 话", "电话")
    text = text.replace("邮 箱", "邮箱").replace("籍 贯", "籍贯")
    return text


def undouble(text: str) -> str:
    if len(text) % 2 == 0:
        half = len(text) // 2
        if text[:half] == text[half:]:
            return text[:half]
    return text


def rels(zip_file: zipfile.ZipFile) -> dict[str, str]:
    tree = ET.fromstring(zip_file.read("word/_rels/document.xml.rels"))
    out: dict[str, str] = {}
    for rel in tree:
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            out[rid] = target
    return out


def node_text(node: ET.Element, links: dict[str, str]) -> str:
    parts: list[str] = []
    for child in node:
        if child.tag == f"{{{NS['w']}}}t":
            parts.append(child.text or "")
        elif child.tag == f"{{{NS['w']}}}tab":
            parts.append(" ")
        elif child.tag == f"{{{NS['w']}}}hyperlink":
            rid = child.attrib.get(f"{{{NS['r']}}}id")
            label = collapse(node_text(child, links))
            url = links.get(rid or "")
            if label and url and not url.startswith("#"):
                parts.append(f"[{label}]({url})")
            else:
                parts.append(label)
        else:
            parts.append(node_text(child, links))
    return "".join(parts)


def paragraphs() -> list[str]:
    with zipfile.ZipFile(SRC) as zf:
        links = rels(zf)
        root = ET.fromstring(zf.read("word/document.xml"))

    lines: list[str] = []
    seen: set[str] = set()
    for para in root.findall(".//w:p", NS):
        text = undouble(collapse(node_text(para, links)))
        if not text:
            continue
        if "个人简历" in text and "谷歌学术" in text:
            continue
        if all(k in text for k in ["姓名：", "电话：", "邮箱："]):
            continue
        if text.count("西安电子科技大学") >= 2 and "河北工程大学" in text:
            continue
        if len(text) > 900:
            continue
        if text in seen:
            continue
        seen.add(text)
        lines.append(text)
    return lines


def split_compound_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        line = line.replace("2019.08-2021.03 西安电子科技大学 计算机科学与技术 硕士阶段2015.08-2019.06", "2019.08-2021.03 西安电子科技大学 计算机科学与技术 硕士阶段\n2015.08-2019.06")
        line = line.replace("会议报告：", "\n会议报告：")
        line = line.replace("人工智能科普：", "\n人工智能科普：")
        for piece in line.splitlines():
            piece = collapse(piece)
            if piece:
                out.append(piece)
    return out


def copy_assets() -> str:
    ASSETS.mkdir(exist_ok=True)
    photo_src = ASSETS / "word" / "media" / "image2.jpeg"
    if photo_src.exists():
        photo_dst = ASSETS / "avatar.jpeg"
        shutil.copyfile(photo_src, photo_dst)
        return "assets/avatar.jpeg"
    return ""


def emit(lines: list[str], photo: str) -> str:
    md: list[str] = ["# 马梦茹", ""]
    if photo:
        md += [f'<img src="{photo}" alt="马梦茹" width="140" />', ""]
    md += [
        "[Google Scholar](https://scholar.google.com.hk/citations?user=nEPyIP8AAAAJ&hl=zh-CN) | [CSDN](https://blog.csdn.net/qq_39630875?spm=1000.2115.3001.5343)",
        "",
    ]

    skip = {
        "个人简历",
        "基本信息基本信息",
        "教育及工作经历教育及工作经历",
        "科研方向及成果科研方向及成果",
        "谷歌学术 & [CSDN](https://blog.csdn.net/qq_39630875?spm=1000.2115.3001.5343)",
        "公共服务",
        "未来工作规划",
        "教学工作",
    }
    current = ""
    emitted: set[str] = set()

    def heading(title: str) -> None:
        nonlocal current
        if title not in emitted:
            md.extend([f"## {title}", ""])
            emitted.add(title)
        current = title

    def subheading(title: str) -> None:
        nonlocal current
        if title not in emitted:
            md.extend([f"### {title}", ""])
            emitted.add(title)
        current = title

    for line in lines:
        if line in skip or line == "马梦茹":
            continue
        if "姓名：" in line and "电话：" in line:
            continue
        if line in {"基本信息", "教育及工作经历", "科研方向及成果"}:
            heading(line)
            continue
        if re.fullmatch(r"[123]、.*", line):
            title = re.sub(r"^[123]、", "", line)
            if title.startswith("论文："):
                subheading("论文")
                md.extend([title, ""])
            else:
                subheading(title)
            continue
        if line.startswith("教学方面"):
            heading("未来工作规划")
        elif line.startswith("会议报告") or line.startswith("人工智能科普") or line.startswith("中国图象图形学会") or line.startswith("担任IEEE") or line.startswith("2021年至今") or line.startswith("在2021年") or line.startswith("负责课题组") or "学术博客" in line:
            heading("公共服务")
        elif line.startswith("2025学年") or line.startswith("2025年度参加"):
            heading("教学工作")

        is_basic = any(line.startswith(k) for k in ["姓名：", "电话：", "邮箱：", "籍贯：", "政治面貌：", "出生年月：", "导师：", "学历："])
        is_education = bool(re.match(r"^\d{4}\.\d{2}-", line))
        is_publication = bool(re.match(r"^(Ma |Jiao |Zhu |Jiaxuan )", line))
        is_future_item = line.startswith(("本科生课程", "研究生课程", "极端环境", "面向语义", "文生视频", "由卫星图"))
        is_list_context = current in {"项目", "专利&软著（授权）", "获奖荣誉", "论文", "教学工作", "公共服务"}

        if is_basic or is_education or is_publication or is_list_context or is_future_item:
            md.append(f"- {line}")
        else:
            md.append(line)
        md.append("")

    return "\n".join(md).replace("\n\n\n", "\n\n")


def main() -> None:
    photo = copy_assets()
    lines = split_compound_lines(paragraphs())
    OUT.write_text(emit(lines, photo), encoding="utf-8")


if __name__ == "__main__":
    main()

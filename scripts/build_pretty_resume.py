#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


BASIC = [
    ("姓名", "马梦茹"),
    ("电话", "18832029556（同微信）"),
    ("邮箱", "mamengru@xidian.edu.cn"),
    ("籍贯", "陕西省渭南市合阳县"),
    ("政治面貌", "中共党员"),
    ("出生年月", "1996.07"),
    ("导师", "焦李成"),
    ("学历", "博士研究生"),
]

EDU = [
    ("2024.12-至今", "西安电子科技大学人工智能学院", "全职博士后，助理研究员"),
    ("2021.03-2024.12", "西安电子科技大学，计算机科学与技术", "博士阶段"),
    ("2019.08-2021.03", "西安电子科技大学，计算机科学与技术", "硕士阶段"),
    ("2015.08-2019.06", "河北工程大学，通信工程", "本科阶段"),
]

PROJECTS = [
    "2025年中国博士后科学基金面上项目，2025M771532，2025年6月-至今，在研，主持。",
    "陕西省人力资源和社会保障厅：陕西省博士后科研项目资助三等资助，2025年10月，在研，主持。",
    "2023年西安电子科技大学优秀博士学位论文资助基金：空谱超融合表征学习理论及应用研究，2023-至今，在研，主持。",
    "2022年研究生创新基金项目：多尺度空谱选择的多模态遥感影像超融合解译，YJS2202，2022年3月-2022年12月，结题，主持。",
    "2023年国家自然科学基金面上项目：基于多尺度稀疏表征学习的超融合解译研究，62276199，2023-至今，在研，参与（核心成员）。",
]

PATENTS = [
    "马文萍、马梦茹、朱浩、武越、焦李成，一种逐像素分类方法、存储介质及分类设备，2024-02-06，中国，ZL 2020 1 0819496.0。（学生一作）",
    "朱浩、马梦茹、洪世宽、马文萍、张俊、焦李成，一种基于多视点深度特征融合SENet网络的分类方法，2023-04-07，中国，ZL 2020 1 0373506.2。（学生一作）",
    "马文萍、马梦茹、洪世宽、武越、朱浩、焦李成，基于深度学习的人脸检测识别系统软件V1.0，2020SR0130837。（学生一作）",
    "马梦茹、洪世宽、朱浩、李亚婷。基于视觉人脸识别签到管理系统，2019SR1248697。",
]

AWARDS = [
    "中国电子教育学会2025年度优秀博士学位论文优秀奖。",
    "2026年获西安电子科技大学本科生教学准入证。",
    "2022年 1st ACRE Cascade Competition 国际级冠军。",
    "2021年 CVPR NTIRE 2021 Challenge on Multi-modal Aerial View Object Classification: Track 2 EO + SAR 冠军。",
    "2023年获得“国家奖学金”和“盛路社会奖学金”。",
    "2024年获得“国家奖学金”和“中国电子科技集团公司-西安电子科技大学协同创新奖学金”。",
]

PAPERS = [
    "Ma Mengru, Ma Wenping, Jiao Licheng, Liu Xu, Li Lingling, Feng Zhixi, Yang Shuyuan. A Multimodal Hyper-fusion Transformer for Remote Sensing Image Classification. Information Fusion, 2023, 96: 66-79.",
    "Ma Mengru, Ma Wenping, Jiao Licheng, Li Lingling, Liu Xu, Liu Fang, Yang Shuyuan, Guo Yuwei. A 3D Self-Awareness Diffusion Network for Multimodal Classification. IEEE Transactions on Multimedia, 2025, 27: 3462-3475.",
    "Ma Mengru, Ma Wenping, Jiao Licheng, Liu Xu, Liu Fang, Li Lingling, Yang Shuyuan. MBSI-Net: Multimodal Balanced Self-Learning Interaction Network for Image Classification. IEEE Transactions on Circuits and Systems for Video Technology, 2023, 34(5): 3819-3833.",
    "Ma Mengru, Ma Wenping, Jiao Licheng, Liu Xu, Liu Fang, Li Lingling. Transfer Representation Learning Meets Multimodal Fusion Classification for Remote Sensing Images. IEEE Transactions on Geoscience and Remote Sensing, 2022, 60: 5632415.",
    "Ma Mengru, Zhao Jiaxuan, Ma Wenping, Jiao Licheng, Li Lingling, Liu Xu, Liu Fang, Yang Shuyuan. A Mamba-aware Spatial Spectral Cross-modal Network for Remote Sensing Classification. IEEE Transactions on Geoscience and Remote Sensing, 2025, 63: 4402515.",
    "Ma Wenping, Ma Mengru（通信作者）, Jiao Licheng, Liu Fang, Zhu Hao, Liu Xu, Yang Shuyuan, Hou Biao. An Adaptive Migration Collaborative Network for Multimodal Image Classification. IEEE Transactions on Neural Networks and Learning Systems, 2023, 35: 10935-10949.",
    "Ma Wenping, Chen Chuang, Ma Mengru（通信作者）, Zhang Hekai, Zhu Hao, Jiao Licheng. An Adaptive Dual-supervised Cross-deep Dependency Network for Pixel-wise Classification. IEEE Transactions on Geoscience and Remote Sensing, 2025, 63: 4402713.",
    "Ma Wenping, Zhang Hekai, Ma Mengru（通信作者）, Chen Chuang, Hou Biao. ISSP-Net: An Interactive Spatial-Spectral Perception Network for Multimodal Classification. IEEE Transactions on Geoscience and Remote Sensing, 2024, 62: 4412014.",
    "Ma Wenping, Xue Boyou, Ma Mengru（通信作者）, Chen Chuang, Zhang Hekai, Zhu Hao. A Diff-Attention Aware State Space Fusion Model for Remote Sensing Classification. IEEE Transactions on Geoscience and Remote Sensing, 2025, 63: 4421315.",
    "Ma Wenping, Zhang Hekai, Ma Mengru（通信作者）, Xue Boyou, Zhu Hao. HCMA-Net: Hierarchical Cross-Modality Aggregation Network for Multimodal Remote Sensing Image Classification. IEEE Transactions on Geoscience and Remote Sensing, 2025, 64: 4400417.",
    "Jiao Licheng, Ma Mengru, He Pei, Geng Xueli, Liu Xu, Liu Fang, Ma Wenping, Yang Shuyuan, Hou Biao, Tang Xu. Brain-Inspired Learning, Perception, and Cognition: A Comprehensive Review. IEEE Transactions on Neural Networks and Learning Systems, 2024, 36(4): 5921-5941.",
    "Zhu Hao, Ma Mengru, Ma Wenping, Jiao Licheng, Hong Shikuan, Shen Jianchao, Hou Biao. A Spatial-channel Progressive Fusion ResNet for Remote Sensing Classification. Information Fusion, 2021, 70: 72-87.",
    "Jiaxuan Zhao, Licheng Jiao, Lingling Li, Mengru Ma, Xu Liu, Chao Wang, Fang Liu, Wenping Ma, Shuyuan Yang. S3Diffuser: Frequency selected state space guided diffusion model for multimodal fusion classification. Information Fusion, 2025, 125: 103447.",
]

FUTURE = [
    "极端环境下的图像融合解译：充分挖掘源图像信息，解决夜间、雨雾、过曝、欠曝等极端问题。",
    "面向语义分割与视觉定位协同的遥感参考理解：从微尺度跨模态特征增强与“先定位、后验证”的粗细粒度对齐层级推理两方面突破。",
    "文生视频的状态一致性建模：在推理阶段显式建模语义、外观与运动状态，提升视频生成的时空一致性与稳定性。",
    "由卫星图生成全景图的跨视角重建：从多尺度特征对齐、跨视角几何关系建模以及语义一致性约束等角度探索。",
]

SERVICE = [
    "会议报告：基于Mamba感知的空谱跨模态遥感影像融合分类，第二届人工智能与遥感科学交叉论坛（AIRS-2025），云南昆明，2025-07-18至2025-07-20。",
    "人工智能科普：人工智能的发展现状及其影响，2025年陕西省全国科普月重点活动暨宝鸡市主场活动科普进校园报告会，陕西宝鸡，2025-09-12。",
    "中国图象图形学学会会员，中国电子教育学会会员，陕西省女科技工作者协会会员。",
    "担任 IEEE TNNLS，TCSVT，EAAI，Scientific Data journal (Nature)，AAAI 等权威期刊及会议审稿人。",
    "2021年至今连续四年独立负责智能感知与图像理解（IPIU）实验室公众号和今日头条，及西电人工智能研究院公众号运营，流量累计3.6万次。",
    "负责课题组会议组织、安排及团建活动，累计35人次；学术博客（CSDN）72篇原创，1000+粉丝，访问量10万+。",
]

TEACHING = [
    "2025学年春季学期，计算智能课程导论。56学时，线下40学时，线上16学时。主要负责作业批改、实验课程授课、习题课答疑、热点科普等工作，96人次。",
    "2025学年秋季学期，新生研讨与学科导论，20人次。",
    "2025年度参加新入职教师教学基本技能培训，完成专题培训、微格教学、汇报展示等，考核合格。",
]


def md_list(items: list[str]) -> str:
    return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items))


def write_readme() -> None:
    text = """# 马梦茹

个人简历 / Academic CV

- 网页版简历：请通过 GitHub Pages 访问 `docs/index.html`
- Google Scholar：https://scholar.google.com.hk/citations?user=nEPyIP8AAAAJ&hl=zh-CN
- CSDN：https://blog.csdn.net/qq_39630875
- 邮箱：mamengru@xidian.edu.cn

## 项目结构

```text
.
├── README.md
├── assets/
│   └── avatar.jpeg
├── docs/
│   ├── index.html
│   └── assets/
│       └── avatar.jpeg
└── scripts/
    ├── build_pretty_resume.py
    └── docx_to_markdown.py
```

## GitHub Pages 设置

上传到 GitHub 后，在仓库中进入：

```text
Settings -> Pages -> Build and deployment
```

然后选择：

```text
Source: Deploy from a branch
Branch: main
Folder: /docs
```

保存后，GitHub 会生成一个公开访问地址，形式通常是：

```text
https://你的用户名.github.io/仓库名/
```

正式简历页面由 `docs/index.html` 提供展示。
"""
    (ROOT / "README.md").write_text(text, encoding="utf-8")


def html_list(items: list[str]) -> str:
    return "\n".join(f"<li>{item}</li>" for item in items)


def write_html() -> None:
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    (docs / "assets").mkdir(exist_ok=True)
    avatar = ROOT / "assets" / "avatar.jpeg"
    if avatar.exists():
        (docs / "assets" / "avatar.jpeg").write_bytes(avatar.read_bytes())
    basic = "\n".join(f"<div><strong>{k}</strong><span>{v}</span></div>" for k, v in BASIC)
    edu = "\n".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in EDU)
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>马梦茹 - 个人简历</title>
  <style>
    body {{ margin: 0; background: #eef3f7; color: #263238; font: 15px/1.72 -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif; }}
    .page {{ max-width: 980px; margin: 28px auto; background: #fff; box-shadow: 0 16px 48px rgba(34, 72, 102, .16); }}
    .top {{ display: grid; grid-template-columns: 1fr 148px; gap: 28px; padding: 38px 44px 24px; border-top: 10px solid #2778a8; }}
    h1 {{ margin: 0; font-size: 38px; letter-spacing: 0; color: #173f5f; }}
    .role {{ margin-top: 8px; color: #52616b; font-size: 17px; }}
    .links {{ margin-top: 14px; }}
    .links a {{ color: #146c94; font-weight: 700; text-decoration: none; margin-right: 16px; }}
    .avatar {{ width: 132px; border: 5px solid #e2edf4; }}
    section {{ padding: 0 44px 22px; }}
    h2 {{ margin: 20px 0 14px; padding: 6px 14px; color: #fff; background: #2778a8; font-size: 20px; line-height: 1.45; }}
    h3 {{ margin: 22px 0 8px; color: #174a6b; font-size: 17px; border-bottom: 2px solid #d8e7ef; }}
    .info {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px 24px; }}
    .info div {{ border-bottom: 1px solid #e5edf2; padding: 5px 0; }}
    .info strong {{ display: inline-block; min-width: 72px; color: #174a6b; }}
    table {{ width: 100%; border-collapse: collapse; margin: 8px 0 14px; }}
    th, td {{ border: 1px solid #d9e5ec; padding: 8px 10px; vertical-align: top; }}
    th {{ background: #f0f7fb; color: #174a6b; }}
    ol {{ padding-left: 22px; margin-top: 8px; }}
    li {{ margin: 5px 0; }}
    .lead {{ font-weight: 700; color: #174a6b; }}
    @media (max-width: 720px) {{
      .page {{ margin: 0; box-shadow: none; }}
      .top {{ grid-template-columns: 1fr; padding: 28px 22px 16px; }}
      section {{ padding: 0 22px 18px; }}
      .info {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 32px; }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <header class="top">
      <div>
        <h1>马梦茹</h1>
        <div class="role">西安电子科技大学人工智能学院 · 全职博士后 / 助理研究员</div>
        <div class="links"><a href="https://scholar.google.com.hk/citations?user=nEPyIP8AAAAJ&hl=zh-CN">Google Scholar</a><a href="https://blog.csdn.net/qq_39630875?spm=1000.2115.3001.5343">CSDN</a></div>
      </div>
      <img class="avatar" src="assets/avatar.jpeg" alt="马梦茹" />
    </header>
    <section><h2>基本信息</h2><div class="info">{basic}</div></section>
    <section><h2>教育及工作经历</h2><table><thead><tr><th>时间</th><th>单位 / 专业</th><th>阶段 / 职务</th></tr></thead><tbody>{edu}</tbody></table></section>
    <section><h2>科研方向及成果</h2><p><span class="lead">研究方向：</span>多模态大模型、多源遥感影像融合解译、图文检索、视频生成、全景重建、参考语义分割与视觉定位协同等。</p><h3>项目</h3><ol>{html_list(PROJECTS)}</ol><h3>论文</h3><p>中科院一区论文累计20余篇，其中以一作/通信作者发表中科院一区论文10余篇，总引用次数为417，单篇最高引用次数为95。</p><ol>{html_list(PAPERS)}</ol><h3>专利 & 软著（授权）</h3><ol>{html_list(PATENTS)}</ol><h3>获奖荣誉</h3><ol>{html_list(AWARDS)}</ol></section>
    <section><h2>未来工作规划</h2><p><span class="lead">可胜任课程：</span>本科生课程包括计算智能导论、人工智能概论、机器学习、深度学习、图像处理与机器视觉等；研究生课程包括神经网络、模式识别、人工智能、数字图像处理、智能图像处理等。</p><ol>{html_list(FUTURE)}</ol></section>
    <section><h2>公共服务</h2><ol>{html_list(SERVICE)}</ol></section>
    <section><h2>教学工作</h2><ol>{html_list(TEACHING)}</ol></section>
  </main>
</body>
</html>
"""
    (docs / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    write_readme()
    write_html()

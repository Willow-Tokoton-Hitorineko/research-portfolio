from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'projects.json').read_text(encoding='utf-8'))
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
W,H=A4
c=canvas.Canvas(str(ROOT/'portfolio-summary.pdf'),pagesize=A4, invariant=1)
c.setTitle('Willow - Financial Research and Data Portfolio')
c.setAuthor('Willow-Tokoton-Hitorineko')
INK=colors.HexColor('#18232c');RED=colors.HexColor('#8c2f39');MUTED=colors.HexColor('#69747b')
style=ParagraphStyle('body',fontName='STSong-Light',fontSize=11,leading=18,textColor=INK,wordWrap='CJK')
def para(text,y,fs=11,color=INK):
    s=ParagraphStyle('line',parent=style,fontSize=fs,leading=fs*1.65,textColor=color)
    p=Paragraph(escape(text),s);_,height=p.wrap(W-100,H)
    if y-height<65:raise ValueError('PDF content exceeds page boundary')
    p.drawOn(c,50,y-height)
    return y-height-13
def header(label,title,page):
    c.setFillColor(colors.HexColor('#f4f1eb'));c.rect(0,0,W,H,fill=1,stroke=0)
    y=para(label,H-55,10,RED)
    y=para(title,y-8,25)
    c.setStrokeColor(colors.HexColor('#d7d2ca'));c.line(50,y-7,W-50,y-7)
    c.setFont('STSong-Light',9);c.setFillColor(MUTED)
    c.drawString(50,35,'2026-10-14 | Public portfolio | synthetic demos are labelled')
    c.drawRightString(W-50,35,f'{page} / 4')
    return y-32
def project(p,y):
    y=para(p['name'],y,16)
    y=para(p['intro'],y)
    y=para('验证：'+p['evidence'],y,10)
    y=para('边界：'+p['boundary'],y,10,MUTED)
    url='https://github.com/Willow-Tokoton-Hitorineko/'+p['repo']
    c.setFont('Helvetica',8);c.setFillColor(RED);c.drawString(50,y,url)
    c.linkURL(url,(50,y-2,W-50,y+10),relative=0)
    return y-36

y=header('Willow / research & build','金融研究 × 数据分析 × AI 工作流',1)
y=para('让金融判断有可核查的依据。',y,19)
y=para('从问题定义、字段与时点到规则和模型协作，把研究过程组织成可以检查、运行和继续迭代的作品。',y)
for title,body in [('问题与口径','区分事实、计算、假设和判断。字段、单位、时点和来源可追溯。'),('规则与模型','确定性计算交给代码；模型解释受证据与工具范围约束；关键决定由人复核。'),('验证与交付','离线演示、异常用例与局限一起交付。合成数据结果不代表真实市场表现。')]:
    y=para(title,y-8,15);y=para(body,y)
y=para('公开作品集提供摘要和源码链接。已有作品与独立公开方法演示分开标注；实现和验证有 AI 编程工具参与。',y-10,10,MUTED)
y=para('原始公司代码、内部模板、真实票据、商业数据库明细与个人联系方式不公开。',y,10,MUTED)
url='https://willow-tokoton-hitorineko.github.io/research-portfolio/'
y=para('在线作品集',y-12,13);c.setFont('Helvetica',9);c.drawString(50,y,url);c.linkURL(url,(50,y-2,W-50,y+12),relative=0)
c.showPage()
y=header('已有公开作品','市场研究与金融规则工程',2)
for p in data[:3]:y=project(p,y)
c.showPage()
y=header('独立公开方法演示','研究数据与人工复核',3)
for p in data[3:5]:y=project(p,y)
y=para('这些仓库依据公开问题重新实现。没有复用公司系统或团队受限代码，也没有把原研究数字迁移成新演示的效果指标。',y,10,MUTED)
c.showPage()
y=header('独立公开方法演示','风险预算与交付完整性',4)
for p in data[5:]:y=project(p,y)
y=para('继续查看',y,14)
y=para('FF5 课程研究存在同期间信息偏差，历史收益待重算；与政策采集工具保留在原仓库。未授权或缺少完整证据链的材料不公开。',y,10,MUTED)
c.save()
print('Created clean public PDF: 4 pages')

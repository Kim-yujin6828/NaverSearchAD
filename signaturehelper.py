import pandas as pd
from pptx import Presentation
from pptx.util import Inches
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

# ----------------------------
# Excel Template with Sample Data
# ----------------------------

excel_data = {
    "요약": pd.DataFrame({
        "항목": ["노출수", "클릭수 (CTR)", "전환수", "광고비", "CPC", "ROAS"],
        "수치": [120000, "4,200 (3.5%)", 120, "₩1,596,000", "₩380", "420%"],
        "전월 대비": ["+15%", "+5%", "-10%", "-8%", "-12%", "+20%"],
        "비고": ["키워드 확장", "광고문구 변경", "랜딩 오류", "예산 조정", "입찰 전략", "성과 집중"]
    }),
    "캠페인별 성과": pd.DataFrame({
        "캠페인명": ["브랜드 캠페인", "프로모션 캠페인", "리타겟 캠페인"],
        "노출수": [50000, 40000, 30000],
        "클릭수": [1500, 1800, 900],
        "CTR": ["3%", "4.5%", "3%"],
        "전환수": [60, 45, 15],
        "전환율": ["4%", "2.5%", "1.7%"],
        "광고비": [500000, 700000, 396000],
        "CPC": ["₩333", "₩389", "₩440"],
        "ROAS": ["500%", "300%", "200%"]
    }),
    "키워드 분석": pd.DataFrame({
        "키워드": ["브랜드명", "할인", "무료배송", "리뷰", "이벤트"],
        "노출수": [20000, 15000, 10000, 8000, 7000],
        "클릭수": [800, 600, 500, 300, 200],
        "CTR": ["4%", "4%", "5%", "3.75%", "2.85%"],
        "전환수": [30, 25, 35, 10, 5],
        "전환율": ["3.75%", "4.2%", "7%", "3.3%", "2.5%"],
        "광고비": [300000, 250000, 200000, 150000, 100000],
        "CPC": ["₩375", "₩417", "₩400", "₩500", "₩500"],
        "ROAS": ["450%", "380%", "600%", "280%", "150%"]
    }),
    "광고소재 분석": pd.DataFrame({
        "소재명/ID": ["소재1", "소재2"],
        "제목": ["할인 이벤트 진행중", "무료배송 혜택 제공"],
        "설명문구": ["전 제품 할인! 지금 확인하세요", "지금 주문 시 무료배송"],
        "클릭수": [1000, 1200],
        "CTR": ["4.5%", "5%"],
        "전환수": [40, 50],
        "광고비": [300000, 360000],
        "비고": ["A/B 테스트 A", "A/B 테스트 B"]
    }),
    "개선 사항 및 계획": pd.DataFrame({
        "항목": ["이슈 요약", "개선 제안", "다음 달 전략"],
        "내용": [
            "일부 키워드 전환률 저조, 랜딩페이지 로딩 지연",
            "랜딩 속도 개선, 부정 키워드 추가, 소재 리프레시",
            "신규 키워드 테스트, 프로모션 집중 운영"
        ]
    })
}

with pd.ExcelWriter("네이버_검색광고_월간보고서_샘플.xlsx", engine='xlsxwriter') as writer:
    for sheet_name, df in excel_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# ----------------------------
# PPT Template with Chart
# ----------------------------

ppt = Presentation()

# Slide 1: Title
slide = ppt.slides.add_slide(ppt.slide_layouts[0])
slide.shapes.title.text = "네이버 검색광고 월간 보고서"
slide.placeholders[1].text = "기간: 2025년 9월 1일 ~ 9월 30일\n작성자: 마케팅팀"

# Slide 2: Summary
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
slide.shapes.title.text = "핵심 요약"
slide.placeholders[1].text = "- 총 광고비: ₩1,596,000\n- 클릭수: 4,200\n- 전환수: 120\n- ROAS: 420%"

# Slide 3: Chart - 전환수 추이
slide = ppt.slides.add_slide(ppt.slide_layouts[5])
slide.shapes.title.text = "주차별 전환수 추이"

chart_data = CategoryChartData()
chart_data.categories = ["1주차", "2주차", "3주차", "4주차"]
chart_data.add_series("전환수", (20, 35, 30, 35))

x, y, cx, cy = Inches(1), Inches(1.5), Inches(8), Inches(4.5)
chart = slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
).chart

chart.has_legend = False
chart.value_axis.has_major_gridlines = True
chart.value_axis.axis_title.text_frame.text = "전환수"

# Save PPT
ppt.save("네이버_검색광고_월간보고서_샘플.pptx")

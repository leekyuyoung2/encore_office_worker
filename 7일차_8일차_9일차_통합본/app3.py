import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 0. 데이터 로딩 및 전처리 ---
@st.cache_data
def load_data(file_name):
    """
    CSV 파일을 로드하고 'order_date'를 datetime.date 객체로 변환하며
    'revenue' (매출액) 컬럼을 생성합니다.
    """
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        st.error(f"'{file_name}' 파일을 찾을 수 없습니다. dashboard.py와 동일한 폴더에 있는지 확인하세요.")
        return None
    except Exception as e:
        st.error(f"데이터 로딩 중 오류 발생: {e}")
        return None

    # 'order_date' 컬럼을 날짜형(datetime.date)으로 변환
    df['order_date'] = pd.to_datetime(df['order_date']).dt.date
    # 'revenue' (매출액) 컬럼 생성
    df['revenue'] = df['quantity'] * df['price']
    return df

# --- 1. 대시보드 레이아웃 설계 및 구현 ---

# 1-1. 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 1-2. 대시보드 전체 제목
st.title("🛍️ 패션 쇼핑몰 판매 성과 대시보드")

# --- (데이터 로드) ---
df_raw = load_data("fashion_sales.csv")

# 데이터 로딩에 실패하면 앱 실행 중지
if df_raw is None:
    st.stop()

# --- (필터링을 위한 데이터 범위 추출) ---
min_date = df_raw['order_date'].min()
max_date = df_raw['order_date'].max()
all_categories = sorted(df_raw['category'].unique().tolist())

# --- 1-3. 사이드바(Sidebar) 구성 ---
st.sidebar.header("대시보드 필터")

# 1-4. 기간 선택 (date_input)
selected_dates = st.sidebar.date_input(
    "주문 날짜 선택",
    value=(max_date - timedelta(days=30), max_date), # 기본값: 최근 30일
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD",
)

# 1-5. 카테고리 선택 (multiselect)
selected_categories = st.sidebar.multiselect(
    "상품 카테고리 선택",
    options=all_categories,
    default=all_categories # 기본값: 모든 카테고리 선택
)


# --- 5. 상호작용성 검증 (데이터 필터링) ---
# 사이드바에서 선택된 값에 따라 원본 데이터 필터링
# (이 부분이 2, 3번 항목의 기반 데이터가 됨)

# 날짜 범위가 올바르게 선택되었는지 확인 (시작일, 종료일 2개)
if len(selected_dates) == 2:
    start_date = selected_dates[0]
    end_date = selected_dates[1]
else:
    st.sidebar.error("시작일과 종료일을 모두 선택해주세요.")
    st.stop() # 날짜 선택이 잘못되면 앱 실행 중지

# 카테고리가 1개 이상 선택되었는지 확인
if not selected_categories:
    st.sidebar.error("하나 이상의 카테고리를 선택해주세요.")
    st.stop()

# 선택된 날짜와 카테고리로 데이터 필터링
df_filtered = df_raw[
    (df_raw['order_date'] >= start_date) & 
    (df_raw['order_date'] <= end_date) &
    (df_raw['category'].isin(selected_categories))
]

# 필터링된 데이터가 없는 경우 알림
if df_filtered.empty:
    st.warning("선택한 조건에 해당하는 판매 데이터가 없습니다.")
    st.stop() # 데이터가 없으면 하위 차트/테이블을 그리지 않고 중지


# --- 2. 핵심 성과 지표(KPI) 시각화 ---
st.markdown("## 📊 핵심 성과 지표 (KPI)")

# KPI 계산
total_revenue = df_filtered['revenue'].sum()
total_quantity = df_filtered['quantity'].sum()
# 평균 주문 금액 (AOV) 계산 (중복 없는 주문 건수 기준)
total_orders = df_filtered['order_id'].nunique()
aov = total_revenue / total_orders if total_orders > 0 else 0

# st.metric을 사용하여 3열로 KPI 표시
col1, col2, col3 = st.columns(3)
col1.metric("총 매출액", f"{total_revenue:,.0f} 원")
col2.metric("총 판매 수량", f"{total_quantity:,.0f} 개")
col3.metric("평균 주문 금액 (AOV)", f"{aov:,.0f} 원")

st.markdown("---") # 구분선


# --- 3. 차트 및 데이터 테이블 구현 ---
st.markdown("## 📈 상세 판매 분석")

# 3-1. 차트 1 (선 그래프): 일별 매출액 추이
st.subheader("일별 매출액 추이")
# 날짜별로 매출액 합계 계산
daily_revenue = df_filtered.groupby('order_date')['revenue'].sum().reset_index()
# Streamlit의 내장 선 그래프 사용 (x축을 날짜로 자동 인식)
st.line_chart(daily_revenue, x='order_date', y='revenue', height=300)


# 3-2. 차트 2 (막대 그래프): 카테고리별 총 매출액
st.subheader("카테고리별 총 매출액")
# 카테고리별 매출액 합계 계산
category_revenue = df_filtered.groupby('category')['revenue'].sum().reset_index()
# 매출액 기준으로 내림차순 정렬
category_revenue = category_revenue.sort_values(by='revenue', ascending=False)
# Streamlit의 내장 막대 차트 사용
st.bar_chart(category_revenue, x='category', y='revenue', height=300)


# 3-3. 데이터 테이블: 매출액 기준 상위 10개 상품
st.subheader("매출액 기준 상위 10개 상품")

# 상품명, 카테고리별로 판매 수량 및 매출액 집계
top_products = df_filtered.groupby(['product_name', 'category']).agg(
    total_quantity=('quantity', 'sum'),
    total_revenue=('revenue', 'sum')
).reset_index()

# 매출액(total_revenue) 기준으로 내림차순 정렬하여 상위 10개 추출
top_products = top_products.sort_values(by='total_revenue', ascending=False).head(10)

# 요청한 컬럼 순서로 재정렬 (product_name, category, total_quantity, total_revenue)
top_products_display = top_products[['product_name', 'category', 'total_quantity', 'total_revenue']]

# st.dataframe으로 테이블 표시 (인덱스 숨김, 컨테이너 너비 사용)
st.dataframe(top_products_display.style.format({
    'total_quantity': '{:,.0f} 개',
    'total_revenue': '{:,.0f} 원'
}), use_container_width=True, hide_index=True)
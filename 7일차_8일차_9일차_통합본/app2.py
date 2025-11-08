import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- (1단계) 데이터 로딩 함수 ---
@st.cache_data
def load_data(file_name):
    df = pd.read_csv(file_name)
    # 'order_date'를 datetime으로 변환 (시간 정보 제거)
    df['order_date'] = pd.to_datetime(df['order_date']).dt.date
    # 'revenue' (매출액) 컬럼 생성
    df['revenue'] = df['quantity'] * df['price']
    return df

# --- (1단계) 레이아웃 및 제목 ---
st.set_page_config(layout="wide")
st.title("🛍️ 패션 쇼핑몰 판매 성과 대시보드")

# --- (2단계) 데이터 로드 및 사이드바 ---
df_raw = load_data("fashion_sales.csv")
if df_raw is None:
    st.stop()

# 날짜형으로 변환 (load_data에서 이미 처리했지만 min/max를 위해 .date() 사용)
min_date = df_raw['order_date'].min()
max_date = df_raw['order_date'].max()
all_categories = sorted(df_raw['category'].unique().tolist())

st.sidebar.header("대시보드 필터")

# 2-1. 기간 선택 (date_input)
selected_dates = st.sidebar.date_input(
    "주문 날짜 선택",
    value=(max_date - timedelta(days=30), max_date),
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD",
)

# 2-2. 카테고리 선택 (multiselect)
selected_categories = st.sidebar.multiselect(
    "상품 카테고리 선택",
    options=all_categories,
    default=all_categories
)

# --- (신규) 5. 상호작용성 (데이터 필터링) ---
# 3단계 KPI와 4단계 차트에 사용될 필터링된 데이터를 생성합니다.

# 날짜 범위가 올바르게 선택되었는지 확인
if len(selected_dates) == 2:
    start_date = selected_dates[0]
    end_date = selected_dates[1]
else:
    st.error("시작일과 종료일을 모두 선택해주세요.")
    st.stop() # 날짜 선택이 잘못되면 앱 실행 중지

df_filtered = df_raw[
    # 날짜 필터
    (df_raw['order_date'] >= start_date) & 
    (df_raw['order_date'] <= end_date) &
    # 카테고리 필터
    (df_raw['category'].isin(selected_categories))
]

# 필터링된 데이터가 없는 경우 알림
if df_filtered.empty:
    st.warning("선택한 조건에 해당하는 판매 데이터가 없습니다.")
    st.stop() # 데이터가 없으면 하위 로직 실행 중지


# --- 3. 핵심 성과 지표(KPI) 시각화 ---
st.markdown("## 📊 핵심 성과 지표 (KPI)")

# 3-1. KPI 계산
total_revenue = df_filtered['revenue'].sum()
total_quantity = df_filtered['quantity'].sum()
# 평균 주문 금액 (AOV) 계산
total_orders = df_filtered['order_id'].nunique() # 중복 없는 주문 건수
aov = total_revenue / total_orders if total_orders > 0 else 0

# 3-2. st.metric을 사용하여 3열로 KPI 표시
col1, col2, col3 = st.columns(3)
col1.metric("총 매출액", f"{total_revenue:,.0f} 원")
col2.metric("총 판매 수량", f"{total_quantity:,.0f} 개")
col3.metric("평균 주문 금액 (AOV)", f"{aov:,.0f} 원")


# --- (3단계 검증용) ---
st.subheader("[임시] 3단계 검증")
st.write("필터링된 데이터 (상위 5개 행):")
st.dataframe(df_filtered.head())
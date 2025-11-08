import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- (신규) 데이터 로딩 함수 ---
# @st.cache_data: Streamlit이 데이터를 캐시하도록 하여 성능 향상
@st.cache_data
def load_data(file_name):
    """
    CSV 파일을 로드하고 'order_date'를 datetime 객체로 변환합니다.
    """
    try:
        df = pd.read_csv(file_name)
        # 'order_date' 컬럼을 날짜형(datetime)으로 변환 (필수!)
        df['order_date'] = pd.to_datetime(df['order_date'])
        return df
    except FileNotFoundError:
        st.error(f"'{file_name}' 파일을 찾을 수 없습니다. dashboard.py와 동일한 폴더에 있는지 확인하세요.")
        return None
    except Exception as e:
        st.error(f"데이터 로딩 중 오류 발생: {e}")
        return None

# --- 1. 대시보드 레이아웃 및 제목 (1단계 코드) ---
st.set_page_config(layout="wide")
st.title("🛍️ 패션 쇼핑몰 판매 성과 대시보드")

# --- (신규) 실제 데이터 로드 ---
df_raw = load_data("fashion_sales.csv")

# 데이터 로딩에 실패하면 앱 중지
if df_raw is None:
    st.stop()

# --- (신규) 로드된 데이터에서 필터 범위 추출 ---
min_date = df_raw['order_date'].min().date()
max_date = df_raw['order_date'].max().date()
all_categories = sorted(df_raw['category'].unique().tolist())


# --- 2. 사이드바(Sidebar) 구성 ---
st.sidebar.header("대시보드 필터")

# 2-1. 기간 선택 (date_input)
# 이제 min_value와 max_value가 CSV 데이터 기준으로 설정됩니다.
selected_dates = st.sidebar.date_input(
    "주문 날짜 선택",
    value=(max_date - timedelta(days=30), max_date), # 기본값: 최근 30일
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD",
)

# 2-2. 카테고리 선택 (multiselect)
# options가 CSV 데이터 기준으로 설정됩니다.
selected_categories = st.sidebar.multiselect(
    "상품 카테고리 선택",
    options=all_categories,
    default=all_categories
)

# --- (2단계 검증용) ---
st.subheader("[임시] 2단계 검증")
st.write("1. `fashion_sales.csv` 로드 성공 (상위 5개 행):")
st.dataframe(df_raw.head())

st.write("2. 사이드바에서 선택된 필터 값 확인:")
if len(selected_dates) == 2:
    st.write(f" - 선택된 기간: {selected_dates[0]} ~ {selected_dates[1]}")
else:
    st.write(" - 기간이 올바르게 선택되지 않았습니다.")
    
st.write(f" - 선택된 카테고리: {selected_categories}")
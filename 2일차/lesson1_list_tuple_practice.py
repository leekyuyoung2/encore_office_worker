"""
Python 기초 - 1교시: 리스트(List)와 튜플(Tuple) 실습

이 파일은 lesson1_list_tuple_theory.md와 함께 사용하는 실습 코드입니다.
리스트와 튜플의 기본 사용법과 실무 예제를 포함합니다.

실행 방법:
    python lesson1_list_tuple_practice.py
"""


def intro():
    """1교시 소개"""
    print("=" * 70)
    print("  🎓 Python 기초 - 1교시: 리스트(List)와 튜플(Tuple)")
    print("=" * 70)
    print("\n안녕하세요! 파이썬 학습에 오신 것을 환영합니다.")
    print("오늘은 여러 개의 데이터를 효율적으로 관리하는 방법을 배웁니다.\n")
    print("📚 학습 내용:")
    print("  1. 리스트(List) - 변경 가능한 데이터 모음")
    print("  2. 튜플(Tuple) - 변경 불가능한 데이터 모음")
    print("  3. 실무 예제 - 월별 매출 데이터 분기 합산")
    print("\n" + "=" * 70 + "\n")


def section1_what_is_list():
    """섹션 1: 리스트란 무엇인가?"""
    print("\n" + "=" * 70)
    print("섹션 1: 리스트(List)란 무엇인가?")
    print("=" * 70)
    
    print("\n💡 리스트는 '순서가 있는 보관함'입니다!")
    print("   일상생활 비유:")
    print("   - 쇼핑 카트: 물건을 담고, 빼고, 순서를 바꿀 수 있어요")
    print("   - 할 일 목록: 항목을 추가하고 완료하면 지울 수 있어요\n")
    
    # 예제 1: 리스트 생성
    print("[예제 1] 리스트 생성하기")
    print("-" * 70)
    shopping_cart = ["사과", "바나나", "우유", "빵"]
    print(f"쇼핑 카트: {shopping_cart}")
    print(f"카트에 담긴 물건 개수: {len(shopping_cart)}개\n")
    
    # 예제 2: 리스트 vs 개별 변수
    print("[예제 2] 리스트를 왜 사용할까?")
    print("-" * 70)
    print("❌ 리스트 없이 (비효율적):")
    score1, score2, score3, score4, score5 = 85, 90, 78, 92, 88
    print(f"   학생1: {score1}, 학생2: {score2}, 학생3: {score3}, 학생4: {score4}, 학생5: {score5}")
    print(f"   평균: {(score1 + score2 + score3 + score4 + score5) / 5:.1f}점")
    
    print("\n✅ 리스트 사용 (효율적):")
    scores = [85, 90, 78, 92, 88]
    print(f"   학생 점수: {scores}")
    print(f"   평균: {sum(scores) / len(scores):.1f}점")
    print(f"   최고 점수: {max(scores)}점")
    print(f"   최저 점수: {min(scores)}점\n")
    
    # 예제 3: 다양한 리스트
    print("[예제 3] 다양한 종류의 리스트")
    print("-" * 70)
    numbers = [1, 2, 3, 4, 5]
    fruits = ["사과", "바나나", "포도"]
    empty_list = []
    
    print(f"숫자 리스트: {numbers}")
    print(f"문자열 리스트: {fruits}")
    print(f"빈 리스트: {empty_list}")
    print()


def section2_indexing_slicing():
    """섹션 2: 인덱싱과 슬라이싱"""
    print("\n" + "=" * 70)
    print("섹션 2: 인덱싱(Indexing)과 슬라이싱(Slicing)")
    print("=" * 70)
    
    # 예제 1: 인덱싱
    print("\n[예제 1] 인덱싱 - 특정 위치의 데이터 가져오기")
    print("-" * 70)
    fruits = ["사과", "바나나", "포도", "귤", "수박"]
    print(f"과일 리스트: {fruits}")
    print(f"   인덱스:    [0]    [1]    [2]   [3]   [4]")
    print(f"   음수:     [-5]   [-4]   [-3]  [-2]  [-1]")
    print()
    print(f"첫 번째 과일 (인덱스 0): {fruits[0]}")
    print(f"세 번째 과일 (인덱스 2): {fruits[2]}")
    print(f"마지막 과일 (인덱스 -1): {fruits[-1]}")
    print(f"뒤에서 두 번째 (인덱스 -2): {fruits[-2]}")
    print()
    
    # 예제 2: 슬라이싱
    print("[예제 2] 슬라이싱 - 범위로 데이터 가져오기")
    print("-" * 70)
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"숫자 리스트: {numbers}")
    print()
    print(f"numbers[2:5]   (인덱스 2~4): {numbers[2:5]}")
    print(f"numbers[:3]    (처음부터 2까지): {numbers[:3]}")
    print(f"numbers[7:]    (7부터 끝까지): {numbers[7:]}")
    print(f"numbers[::2]   (2칸씩 건너뛰기): {numbers[::2]}")
    print(f"numbers[::-1]  (역순): {numbers[::-1]}")
    print()
    
    # 예제 3: 실무 예제 - 분기 데이터
    print("[예제 3] 실무 활용 - 분기별 매출 선택")
    print("-" * 70)
    monthly_sales = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
    print(f"월별 매출: {monthly_sales}")
    print()
    q1 = monthly_sales[0:3]
    q2 = monthly_sales[3:6]
    print(f"1분기 (1~3월): {q1}")
    print(f"2분기 (4~6월): {q2}")
    print()


def section3_list_operations():
    """섹션 3: 리스트 조작 (추가/삭제/수정)"""
    print("\n" + "=" * 70)
    print("섹션 3: 리스트 조작하기 (추가/삭제/수정)")
    print("=" * 70)
    
    # 예제 1: 추가하기
    print("\n[예제 1] 요소 추가하기")
    print("-" * 70)
    cart = ["사과", "바나나"]
    print(f"초기 카트: {cart}")
    
    cart.append("우유")
    print(f"append('우유') 후: {cart}")
    
    cart.insert(1, "딸기")
    print(f"insert(1, '딸기') 후: {cart}")
    
    cart.extend(["빵", "계란"])
    print(f"extend(['빵', '계란']) 후: {cart}")
    print()
    
    # 예제 2: 삭제하기
    print("[예제 2] 요소 삭제하기")
    print("-" * 70)
    cart = ["사과", "바나나", "우유", "빵", "계란"]
    print(f"초기 카트: {cart}")
    
    cart.remove("우유")
    print(f"remove('우유') 후: {cart}")
    
    removed = cart.pop()
    print(f"pop() 후: {cart} (제거된 항목: {removed})")
    
    removed = cart.pop(0)
    print(f"pop(0) 후: {cart} (제거된 항목: {removed})")
    print()
    
    # 예제 3: 수정하기
    print("[예제 3] 요소 수정하기")
    print("-" * 70)
    fruits = ["사과", "바나나", "포도"]
    print(f"원래 리스트: {fruits}")
    
    fruits[1] = "딸기"
    print(f"fruits[1] = '딸기' 후: {fruits}")
    print()
    
    # 예제 4: 정렬과 뒤집기
    print("[예제 4] 정렬과 뒤집기")
    print("-" * 70)
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"원래 리스트: {numbers}")
    
    numbers.sort()
    print(f"sort() 후 (오름차순): {numbers}")
    
    numbers.sort(reverse=True)
    print(f"sort(reverse=True) 후 (내림차순): {numbers}")
    
    numbers.reverse()
    print(f"reverse() 후: {numbers}")
    print()


def section4_tuples():
    """섹션 4: 튜플(Tuple) 이해하기"""
    print("\n" + "=" * 70)
    print("섹션 4: 튜플(Tuple) 이해하기")
    print("=" * 70)
    
    print("\n💡 튜플은 '변경할 수 없는 리스트'입니다!")
    print("   일상생활 비유:")
    print("   - 영화 티켓: 발권 후 좌석과 시간을 바꿀 수 없어요")
    print("   - 생년월일: 1990년 5월 15일은 영원히 바뀌지 않아요\n")
    
    # 예제 1: 튜플 생성
    print("[예제 1] 튜플 생성하기")
    print("-" * 70)
    coordinates = (37.5665, 126.9780)  # 서울 좌표
    birth_date = (1990, 5, 15)
    rgb_red = (255, 0, 0)
    
    print(f"서울 좌표: {coordinates}")
    print(f"생년월일: {birth_date}")
    print(f"빨간색 RGB: {rgb_red}")
    print()
    
    # 예제 2: 튜플의 특징
    print("[예제 2] 튜플은 변경할 수 없어요")
    print("-" * 70)
    point = (10, 20)
    print(f"좌표: {point}")
    print(f"x좌표 읽기: {point[0]}")  # 읽기는 가능
    print(f"y좌표 읽기: {point[1]}")
    
    print("\n❌ 하지만 수정은 불가능합니다:")
    print("   point[0] = 100  # TypeError 발생!")
    print("   point.append(30)  # AttributeError 발생!")
    print()
    
    # 예제 3: 튜플 언패킹
    print("[예제 3] 튜플 언패킹 (Unpacking)")
    print("-" * 70)
    point = (10, 20)
    x, y = point
    print(f"point = {point}")
    print(f"x, y = point → x={x}, y={y}")
    
    print("\n변수 값 교환도 간단해요!")
    a, b = 100, 200
    print(f"교환 전: a={a}, b={b}")
    a, b = b, a
    print(f"교환 후: a={a}, b={b}")
    print()
    
    # 예제 4: 함수에서 여러 값 반환
    print("[예제 4] 함수에서 튜플로 여러 값 반환")
    print("-" * 70)
    
    def divide(a, b):
        """나눗셈의 몫과 나머지를 반환"""
        return a // b, a % b  # 튜플 반환
    
    quotient, remainder = divide(17, 5)
    print(f"17 ÷ 5 = 몫 {quotient}, 나머지 {remainder}")
    print()


def section5_comparison():
    """섹션 5: 리스트 vs 튜플 비교"""
    print("\n" + "=" * 70)
    print("섹션 5: 리스트 vs 튜플 비교")
    print("=" * 70)
    
    print("""
┌─────────────┬────────────────┬────────────────┐
│   구분      │  리스트 (List) │  튜플 (Tuple)  │
├─────────────┼────────────────┼────────────────┤
│ 표기법      │ [1, 2, 3]      │ (1, 2, 3)      │
│ 변경 가능   │ ✅ 가능        │ ❌ 불가능      │
│ 추가/삭제   │ ✅ 가능        │ ❌ 불가능      │
│ 속도        │ 보통           │ 빠름           │
│ 메모리      │ 많이 사용      │ 적게 사용      │
│ 용도        │ 변경되는 데이터│ 고정 데이터    │
└─────────────┴────────────────┴────────────────┘
    """)
    
    print("\n[언제 무엇을 사용할까?]")
    print("-" * 70)
    
    print("\n✅ 리스트를 사용하세요:")
    cart = ["사과", "우유"]
    cart.append("빵")
    print(f"   • 쇼핑 카트 (물건 추가/제거): {cart}")
    
    todo = ["코딩하기", "운동하기"]
    todo.remove("코딩하기")
    print(f"   • 할 일 목록 (완료 항목 제거): {todo}")
    
    print("\n✅ 튜플을 사용하세요:")
    birth = (1990, 5, 15)
    print(f"   • 생년월일 (변경 불가): {birth}")
    
    seoul = (37.5665, 126.9780)
    print(f"   • GPS 좌표 (고정): {seoul}")
    
    rgb_red = (255, 0, 0)
    print(f"   • RGB 색상값 (고정): {rgb_red}")
    print()


def section6_quarterly_sales():
    """섹션 6: 실무 예제 - 분기별 매출 합산"""
    print("\n" + "=" * 70)
    print("섹션 6: 실무 예제 - 분기별 매출 합산")
    print("=" * 70)
    
    print("\n📊 문제 상황:")
    print("   회사의 2024년 월별 매출 데이터가 있습니다.")
    print("   각 분기별 매출 합계를 구해보세요!\n")
    
    # 월별 매출 데이터
    sales_2024 = [150, 180, 200, 220, 250, 230, 280, 300, 270, 290, 310, 330]
    
    print("[데이터]")
    print("-" * 70)
    months = ["1월", "2월", "3월", "4월", "5월", "6월", 
              "7월", "8월", "9월", "10월", "11월", "12월"]
    
    for month, sale in zip(months, sales_2024):
        print(f"{month:>4}: {sale:>3}만원", end="  ")
        if months.index(month) % 3 == 2:  # 3개월마다 줄바꿈
            print()
    
    print("\n" + "-" * 70)
    
    # 분기별 계산
    q1 = sales_2024[0:3]
    q2 = sales_2024[3:6]
    q3 = sales_2024[6:9]
    q4 = sales_2024[9:12]
    
    print("\n[분기별 매출 분석]")
    print("=" * 70)
    print(f"1분기 (1~3월):   {q1}  → 합계: {sum(q1):>4}만원")
    print(f"2분기 (4~6월):   {q2}  → 합계: {sum(q2):>4}만원")
    print(f"3분기 (7~9월):   {q3}  → 합계: {sum(q3):>4}만원")
    print(f"4분기 (10~12월): {q4}  → 합계: {sum(q4):>4}만원")
    print("-" * 70)
    print(f"연간 총 매출: {sum(sales_2024):>4}만원")
    print(f"월평균 매출:  {sum(sales_2024)//12:>4}만원")
    
    # 상반기/하반기 비교
    print("\n[상반기 vs 하반기]")
    print("=" * 70)
    first_half = sum(sales_2024[:6])
    second_half = sum(sales_2024[6:])
    increase = second_half - first_half
    increase_rate = (increase / first_half) * 100
    
    print(f"상반기 매출 (1~6월):  {first_half:>4}만원")
    print(f"하반기 매출 (7~12월): {second_half:>4}만원")
    print(f"증가액:              {increase:>4}만원")
    print(f"증가율:              {increase_rate:>4.1f}%")
    print()


def practice_problems():
    """연습 문제"""
    print("\n" + "=" * 70)
    print("📝 연습 문제")
    print("=" * 70)
    
    print("""
다음 문제들을 직접 풀어보세요!

【문제 1】 과일 장바구니 만들기
빈 리스트를 만들고, "사과", "바나나", "오렌지"를 순서대로 추가하세요.
그 다음 "바나나"를 "포도"로 변경하고, 마지막 항목을 제거하세요.

【문제 2】 학생 점수 분석
다음 학생들의 점수가 있습니다: [85, 92, 78, 90, 88]
1) 평균 점수를 구하세요
2) 가장 높은 점수와 낮은 점수를 찾으세요
3) 점수를 내림차순으로 정렬하세요

【문제 3】 슬라이싱 연습
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
1) 처음 3개의 숫자를 선택하세요
2) 마지막 3개의 숫자를 선택하세요
3) 홀수 인덱스의 숫자만 선택하세요

【문제 4】 좌표 튜플
두 점 A(10, 20)과 B(30, 40)를 튜플로 표현하고,
각각의 x좌표와 y좌표를 언패킹으로 추출하세요.

【문제 5】 월별 매출 심화
monthly_sales = [100, 150, 120, 180, 200, 190, 220, 210, 230, 240, 250, 260]
1) 가장 매출이 높은 달과 낮은 달을 찾으세요
2) 매출이 200만원 이상인 달이 몇 개인지 세어보세요
    """)


def practice_solutions():
    """연습 문제 해설"""
    print("\n" + "=" * 70)
    print("✅ 연습 문제 해설")
    print("=" * 70)
    
    print("\n【문제 1 해설】 과일 장바구니 만들기")
    print("-" * 70)
    basket = []
    print(f"1. 빈 리스트 생성: {basket}")
    
    basket.append("사과")
    basket.append("바나나")
    basket.append("오렌지")
    print(f"2. 과일 추가 후: {basket}")
    
    basket[1] = "포도"
    print(f"3. '바나나'를 '포도'로 변경: {basket}")
    
    basket.pop()
    print(f"4. 마지막 항목 제거: {basket}")
    
    print("\n【문제 2 해설】 학생 점수 분석")
    print("-" * 70)
    scores = [85, 92, 78, 90, 88]
    print(f"점수: {scores}")
    
    average = sum(scores) / len(scores)
    print(f"1. 평균 점수: {average:.1f}점")
    
    print(f"2. 최고 점수: {max(scores)}점, 최저 점수: {min(scores)}점")
    
    scores.sort(reverse=True)
    print(f"3. 내림차순 정렬: {scores}")
    
    print("\n【문제 3 해설】 슬라이싱 연습")
    print("-" * 70)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"원본: {numbers}")
    
    print(f"1. 처음 3개: {numbers[:3]}")
    print(f"2. 마지막 3개: {numbers[-3:]}")
    print(f"3. 홀수 인덱스: {numbers[1::2]}")
    
    print("\n【문제 4 해설】 좌표 튜플")
    print("-" * 70)
    point_a = (10, 20)
    point_b = (30, 40)
    
    x1, y1 = point_a
    x2, y2 = point_b
    
    print(f"점 A: {point_a} → x={x1}, y={y1}")
    print(f"점 B: {point_b} → x={x2}, y={y2}")
    
    print("\n【문제 5 해설】 월별 매출 심화")
    print("-" * 70)
    monthly_sales = [100, 150, 120, 180, 200, 190, 220, 210, 230, 240, 250, 260]
    
    max_sale = max(monthly_sales)
    min_sale = min(monthly_sales)
    max_month = monthly_sales.index(max_sale) + 1
    min_month = monthly_sales.index(min_sale) + 1
    
    print(f"1. 최고 매출: {max_month}월 ({max_sale}만원)")
    print(f"   최저 매출: {min_month}월 ({min_sale}만원)")
    
    count = 0
    for sale in monthly_sales:
        if sale >= 200:
            count += 1
    
    print(f"2. 200만원 이상인 달: {count}개월")
    print()


def quiz():
    """5문항 퀴즈"""
    print("\n" + "=" * 70)
    print("📝 1교시 퀴즈 (5문항)")
    print("=" * 70)
    print("\n리스트와 튜플에 대해 배운 내용을 확인해봅시다!\n")
    
    score = 0
    total = 5
    
    # 문제 1
    print("【문제 1】")
    print("리스트를 만드는 올바른 방법은? (객관식)")
    print("① {1, 2, 3}")
    print("② [1, 2, 3]")
    print("③ (1, 2, 3)")
    print("④ <1, 2, 3>")
    answer = input("\n정답: ").strip()
    if answer in ["②", "2"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ②입니다.")
        print("   리스트는 대괄호 []를 사용합니다.")
    
    # 문제 2
    print("\n" + "-" * 70)
    print("【문제 2】")
    print("다음 코드의 결과는? (단답형)")
    print("fruits = ['사과', '바나나', '포도']")
    print("print(fruits[1])")
    answer = input("\n정답: ").strip()
    if answer == "바나나":
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 '바나나'입니다.")
        print("   인덱스는 0부터 시작하므로 fruits[1]은 두 번째 요소입니다.")
    
    # 문제 3
    print("\n" + "-" * 70)
    print("【문제 3】")
    print("리스트와 튜플의 차이점은? (객관식)")
    print("① 리스트는 변경 가능, 튜플은 변경 불가능")
    print("② 리스트는 변경 불가능, 튜플은 변경 가능")
    print("③ 둘 다 변경 가능")
    print("④ 둘 다 변경 불가능")
    answer = input("\n정답: ").strip()
    if answer in ["①", "1"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ①입니다.")
        print("   리스트는 변경 가능(mutable), 튜플은 변경 불가능(immutable)합니다.")
    
    # 문제 4
    print("\n" + "-" * 70)
    print("【문제 4】")
    print("다음 중 튜플을 만드는 올바른 방법은? (객관식)")
    print("① [1, 2, 3]")
    print("② (1, 2, 3)")
    print("③ {1, 2, 3}")
    print("④ <1, 2, 3>")
    answer = input("\n정답: ").strip()
    if answer in ["②", "2"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ②입니다.")
        print("   튜플은 소괄호 ()를 사용합니다.")
    
    # 문제 5
    print("\n" + "-" * 70)
    print("【문제 5】")
    print("numbers = [1, 2, 3, 4, 5]일 때, numbers[1:4]의 결과는? (단답형)")
    print("(예시: [1, 2, 3] 형식으로 답하세요)")
    answer = input("\n정답: ").strip()
    if answer == "[2, 3, 4]":
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 [2, 3, 4]입니다.")
        print("   슬라이싱 [1:4]는 인덱스 1, 2, 3을 선택합니다 (4는 포함 안 됨).")
    
    # 결과 출력
    print("\n" + "=" * 70)
    print(f"📊 퀴즈 결과: {score}/{total}점 ({score/total*100:.0f}%)")
    print("=" * 70)
    
    if score == total:
        print("🎉 완벽합니다! 리스트와 튜플을 완전히 이해하셨네요!")
    elif score >= 3:
        print("👍 잘하셨습니다! 조금만 더 복습하면 완벽해질 거예요!")
    else:
        print("💪 다시 한 번 이론을 복습해보세요!")
    print()


def summary():
    """정리 및 마무리"""
    print("\n" + "=" * 70)
    print("🎓 1교시 정리")
    print("=" * 70)
    
    print("""
오늘 배운 내용:

1️⃣ 리스트(List)
   • 순서가 있고 변경 가능한 데이터 모음
   • 대괄호 []로 표현: [1, 2, 3]
   • append(), remove(), insert() 등으로 조작 가능
   • 인덱싱: list[0], 슬라이싱: list[1:4]

2️⃣ 튜플(Tuple)
   • 순서가 있지만 변경 불가능한 데이터 모음
   • 소괄호 ()로 표현: (1, 2, 3)
   • 읽기만 가능, 추가/삭제/수정 불가
   • 빠르고 메모리 효율적

3️⃣ 주요 차이점
   • 리스트: 자주 변경되는 데이터 (쇼핑 카트, 할 일 목록)
   • 튜플: 고정된 데이터 (좌표, 생년월일, RGB 색상)

4️⃣ 실무 활용
   • 월별 매출 데이터를 리스트로 저장
   • 슬라이싱으로 분기별 데이터 추출
   • sum(), len(), max(), min() 등으로 분석

💡 핵심 코드 패턴:
    # 리스트 생성 및 조작
    my_list = [1, 2, 3]
    my_list.append(4)           # 추가
    my_list[0] = 10             # 수정
    subset = my_list[1:3]       # 슬라이싱
    
    # 튜플 생성 및 언패킹
    point = (10, 20)
    x, y = point                # 언패킹

다음 시간 예고:
2교시에서는 딕셔너리(Dictionary)를 배웁니다!
Key-Value 구조로 더 효율적인 데이터 관리 방법을 알아봐요.

수고하셨습니다! 🎉
    """)


def main_menu():
    """메인 메뉴"""
    while True:
        print("\n" + "=" * 70)
        print("📚 1교시: 리스트와 튜플 - 학습 메뉴")
        print("=" * 70)
        print("\n[이론 + 예제]")
        print("  1. 섹션 1 - 리스트란 무엇인가?")
        print("  2. 섹션 2 - 인덱싱과 슬라이싱")
        print("  3. 섹션 3 - 리스트 조작 (추가/삭제/수정)")
        print("  4. 섹션 4 - 튜플 이해하기")
        print("  5. 섹션 5 - 리스트 vs 튜플 비교")
        print("  6. 섹션 6 - 실무 예제 (분기별 매출)")
        
        print("\n[연습 및 평가]")
        print("  7. 연습 문제")
        print("  8. 연습 문제 해설")
        print("  9. 퀴즈 (5문항)")
        print(" 10. 정리 및 마무리")
        
        print("\n[전체 실행]")
        print("  0. 모든 섹션 순서대로 실행")
        print("  q. 종료")
        
        choice = input("\n선택하세요: ").strip()
        
        if choice == "0":
            intro()
            section1_what_is_list()
            input("\nEnter를 눌러 계속...")
            section2_indexing_slicing()
            input("\nEnter를 눌러 계속...")
            section3_list_operations()
            input("\nEnter를 눌러 계속...")
            section4_tuples()
            input("\nEnter를 눌러 계속...")
            section5_comparison()
            input("\nEnter를 눌러 계속...")
            section6_quarterly_sales()
            input("\nEnter를 눌러 계속...")
            practice_problems()
            input("\nEnter를 눌러 계속...")
            practice_solutions()
            input("\nEnter를 눌러 계속...")
            quiz()
            summary()
            print("\n전체 학습을 완료했습니다! 🎉")
            break
        elif choice == "1":
            section1_what_is_list()
        elif choice == "2":
            section2_indexing_slicing()
        elif choice == "3":
            section3_list_operations()
        elif choice == "4":
            section4_tuples()
        elif choice == "5":
            section5_comparison()
        elif choice == "6":
            section6_quarterly_sales()
        elif choice == "7":
            practice_problems()
        elif choice == "8":
            practice_solutions()
        elif choice == "9":
            quiz()
        elif choice == "10":
            summary()
        elif choice.lower() == "q":
            print("\n학습을 종료합니다. 수고하셨습니다! 👋")
            break
        else:
            print("\n❌ 올바른 번호를 선택해주세요.")
        
        if choice != "0":
            input("\nEnter를 눌러 메뉴로 돌아가기...")


if __name__ == "__main__":
    intro()
    main_menu()

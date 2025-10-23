"""
Python 기초 - 3교시: 조건문과 반복문 (if, for, while) 실습

이 파일은 lesson3_control_flow_theory.md와 함께 사용하는 실습 코드입니다.
조건문, 반복문, 그리고 이들의 조합을 통한 실무 예제를 포함합니다.

실행 방법:
    python lesson3_control_flow_practice.py
"""


def intro():
    """3교시 소개"""
    print("=" * 70)
    print("  🎓 Python 기초 - 3교시: 조건문과 반복문")
    print("=" * 70)
    print("\n안녕하세요! 마지막 3교시에 오신 것을 환영합니다.")
    print("오늘은 조건에 따라 다르게 행동하고, 반복 작업을 자동화하는 방법을 배웁니다.\n")
    print("📚 학습 내용:")
    print("  1. if 조건문 - 상황에 따라 다른 행동")
    print("  2. for 반복문 - 리스트, 딕셔너리 순회")
    print("  3. while 반복문 - 조건이 만족하는 동안 반복")
    print("  4. 미니 프로젝트 - 고객 VIP 시스템")
    print("\n" + "=" * 70 + "\n")


def section1_if_statements():
    """섹션 1: if 조건문"""
    print("\n" + "=" * 70)
    print("섹션 1: if 조건문 (조건에 따라 다른 행동)")
    print("=" * 70)
    
    print("\n💡 조건문은 '상황에 따라 다르게 행동하는 것'입니다!")
    print("   일상생활 비유:")
    print("   - 비가 오면 우산을 쓰고, 안 오면 그냥 나간다")
    print("   - 나이가 18세 이상이면 성인, 미만이면 미성년자")
    print("   - 잔액이 충분하면 결제, 부족하면 거절\n")
    
    # 예제 1: 기본 if문
    print("[예제 1] 기본 if문 - 성인 판별")
    print("-" * 70)
    age = 20
    print(f"나이: {age}세")
    
    if age >= 18:
        print("→ 성인입니다")
    print()
    
    # 예제 2: if-else문
    print("[예제 2] if-else문 - 짝수/홀수 판별")
    print("-" * 70)
    number = 7
    print(f"숫자: {number}")
    
    if number % 2 == 0:
        print("→ 짝수입니다")
    else:
        print("→ 홀수입니다")
    print()
    
    # 예제 3: if-elif-else문
    print("[예제 3] if-elif-else문 - 학점 계산")
    print("-" * 70)
    score = 85
    print(f"점수: {score}점")
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"→ 학점: {grade}")
    print()
    
    # 예제 4: 논리 연산자 (and, or)
    print("[예제 4] 논리 연산자 - 할인 조건")
    print("-" * 70)
    purchase_amount = 150000
    is_member = True
    
    print(f"구매액: {purchase_amount:,}원")
    print(f"회원 여부: {'회원' if is_member else '비회원'}")
    
    # 10만원 이상 AND 회원이면 15% 할인
    if purchase_amount >= 100000 and is_member:
        discount = 0.15
        print(f"→ 회원 특별 할인 {int(discount*100)}% 적용!")
    elif purchase_amount >= 100000:
        discount = 0.10
        print(f"→ 일반 할인 {int(discount*100)}% 적용")
    else:
        discount = 0
        print("→ 할인 없음")
    
    final_price = int(purchase_amount * (1 - discount))
    print(f"최종 금액: {final_price:,}원")
    print()
    
    # 예제 5: in 연산자
    print("[예제 5] in 연산자 - 재고 확인")
    print("-" * 70)
    stock_items = ["노트북", "마우스", "키보드", "모니터"]
    search_item = "마우스"
    
    print(f"재고 목록: {stock_items}")
    print(f"검색 상품: {search_item}")
    
    if search_item in stock_items:
        print(f"→ ✅ '{search_item}'이/가 재고에 있습니다!")
    else:
        print(f"→ ❌ '{search_item}'이/가 재고에 없습니다.")
    print()


def section2_for_loops():
    """섹션 2: for 반복문"""
    print("\n" + "=" * 70)
    print("섹션 2: for 반복문 (여러 개를 하나씩 처리)")
    print("=" * 70)
    
    print("\n💡 for문은 '여러 개를 하나씩 처리하는 것'입니다!")
    print("   일상생활 비유:")
    print("   - 택배 리스트를 보고 한 곳씩 배송")
    print("   - 학생 명단을 보고 한 명씩 출석 체크")
    print("   - 이메일 리스트를 보고 한 명씩 전송\n")
    
    # 예제 1: 리스트 순회
    print("[예제 1] 리스트 순회 - 과일 출력")
    print("-" * 70)
    fruits = ["사과", "바나나", "포도", "귤"]
    print(f"과일 목록: {fruits}\n")
    
    for fruit in fruits:
        print(f"  🍎 {fruit}")
    print()
    
    # 예제 2: range 사용
    print("[예제 2] range 사용 - 구구단 2단")
    print("-" * 70)
    print("[2단]")
    for i in range(1, 10):
        print(f"  2 × {i} = {2*i}")
    print()
    
    # 예제 3: 딕셔너리 순회
    print("[예제 3] 딕셔너리 순회 - 학생 정보")
    print("-" * 70)
    student = {"name": "홍길동", "age": 20, "major": "컴퓨터공학"}
    print("학생 정보:")
    
    for key, value in student.items():
        print(f"  {key}: {value}")
    print()
    
    # 예제 4: 리스트 + 딕셔너리 순회
    print("[예제 4] 리스트 + 딕셔너리 순회 - 제품 목록")
    print("-" * 70)
    products = [
        {"name": "노트북", "price": 1200000},
        {"name": "마우스", "price": 30000},
        {"name": "키보드", "price": 80000}
    ]
    
    print("제품 목록:")
    for product in products:
        print(f"  • {product['name']}: {product['price']:,}원")
    print()
    
    # 예제 5: enumerate 사용
    print("[예제 5] enumerate - 순위 매기기")
    print("-" * 70)
    players = ["홍길동", "김철수", "이영희", "박민수"]
    print("게임 순위:")
    
    for rank, player in enumerate(players, start=1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        print(f"  {medal} {rank}등: {player}")
    print()
    
    # 예제 6: 합계 계산
    print("[예제 6] 합계 계산 - 월별 매출")
    print("-" * 70)
    monthly_sales = [150, 180, 200, 220, 250, 230]
    print(f"월별 매출: {monthly_sales}")
    
    total = 0
    for sales in monthly_sales:
        total += sales
    
    print(f"총 매출: {total:,}만원")
    print(f"평균 매출: {total // len(monthly_sales):,}만원")
    print()


def section3_while_loops():
    """섹션 3: while 반복문"""
    print("\n" + "=" * 70)
    print("섹션 3: while 반복문 (조건이 만족하는 동안 반복)")
    print("=" * 70)
    
    print("\n💡 while문은 '조건이 만족하는 동안 계속 반복'입니다!")
    print("   일상생활 비유:")
    print("   - 재고가 남아있는 동안 계속 판매")
    print("   - 목표에 도달할 때까지 계속 연습")
    print("   - 게임 오버가 아닐 동안 계속 플레이\n")
    
    # 예제 1: 카운트다운
    print("[예제 1] 카운트다운")
    print("-" * 70)
    count = 5
    print("카운트다운 시작!")
    
    while count > 0:
        print(f"  {count}...")
        count -= 1
    
    print("  🚀 발사!")
    print()
    
    # 예제 2: 재고 판매
    print("[예제 2] 재고 판매 시뮬레이션")
    print("-" * 70)
    stock = 10
    sold_count = 0
    
    print(f"초기 재고: {stock}개\n")
    
    while stock > 0 and sold_count < 5:  # 재고가 있고 5개까지만 판매
        print(f"  판매 완료! 남은 재고: {stock - 1}개")
        stock -= 1
        sold_count += 1
    
    print(f"\n총 판매: {sold_count}개")
    print(f"남은 재고: {stock}개")
    print()
    
    # 예제 3: break 사용
    print("[예제 3] break - 목표 달성 시 종료")
    print("-" * 70)
    total_sales = 0
    target = 500
    day = 0
    daily_sales = [100, 150, 120, 200, 80]
    
    print(f"목표 매출: {target}만원\n")
    
    while day < len(daily_sales):
        total_sales += daily_sales[day]
        day += 1
        print(f"  {day}일차: {daily_sales[day-1]}만원 (누적: {total_sales}만원)")
        
        if total_sales >= target:
            print(f"\n🎉 목표 달성! {day}일 만에 {total_sales}만원 달성!")
            break
    print()
    
    # 예제 4: continue 사용
    print("[예제 4] continue - 특정 조건 건너뛰기")
    print("-" * 70)
    print("1부터 10까지 중 홀수만 출력:")
    
    num = 0
    while num < 10:
        num += 1
        
        if num % 2 == 0:  # 짝수면 건너뛰기
            continue
        
        print(f"  {num}")
    print()


def section4_combined():
    """섹션 4: 조건문 + 반복문 조합"""
    print("\n" + "=" * 70)
    print("섹션 4: 조건문 + 반복문 조합 (실전 활용)")
    print("=" * 70)
    
    # 예제 1: 학생 합격 판정
    print("\n[예제 1] 학생 합격 판정")
    print("-" * 70)
    students = [
        {"name": "홍길동", "score": 85},
        {"name": "김철수", "score": 92},
        {"name": "이영희", "score": 65},
        {"name": "박민수", "score": 78}
    ]
    
    print("합격 기준: 70점 이상\n")
    
    pass_count = 0
    for student in students:
        if student["score"] >= 70:
            print(f"  ✅ {student['name']}: {student['score']}점 - 합격")
            pass_count += 1
        else:
            print(f"  ❌ {student['name']}: {student['score']}점 - 불합격")
    
    print(f"\n합격자: {pass_count}명 / 전체: {len(students)}명")
    print()
    
    # 예제 2: 제품 필터링
    print("[예제 2] 제품 필터링 - 가격대별 분류")
    print("-" * 70)
    products = [
        {"name": "노트북", "price": 1200000},
        {"name": "마우스", "price": 30000},
        {"name": "키보드", "price": 80000},
        {"name": "모니터", "price": 300000},
        {"name": "헤드셋", "price": 150000}
    ]
    
    print("고가 제품 (100만원 이상):")
    for product in products:
        if product["price"] >= 1000000:
            print(f"  💎 {product['name']}: {product['price']:,}원")
    
    print("\n중가 제품 (10만원 이상 100만원 미만):")
    for product in products:
        if 100000 <= product["price"] < 1000000:
            print(f"  💰 {product['name']}: {product['price']:,}원")
    
    print("\n저가 제품 (10만원 미만):")
    for product in products:
        if product["price"] < 100000:
            print(f"  💵 {product['name']}: {product['price']:,}원")
    print()
    
    # 예제 3: 재고 상태 보고
    print("[예제 3] 재고 상태 보고")
    print("-" * 70)
    inventory = [
        {"name": "노트북", "stock": 5, "min_stock": 3},
        {"name": "마우스", "stock": 2, "min_stock": 5},
        {"name": "키보드", "stock": 0, "min_stock": 3},
        {"name": "모니터", "stock": 10, "min_stock": 5}
    ]
    
    for item in inventory:
        print(f"\n{item['name']}:")
        print(f"  현재 재고: {item['stock']}개")
        print(f"  최소 재고: {item['min_stock']}개")
        
        if item['stock'] == 0:
            print("  ⚠️  재고 없음 - 긴급 발주 필요!")
        elif item['stock'] < item['min_stock']:
            print("  ⚠️  재고 부족 - 발주 권장")
        else:
            print("  ✅ 재고 충분")
    print()


def section5_vip_mini_project():
    """섹션 5: 미니 프로젝트 - 고객 VIP 시스템"""
    print("\n" + "=" * 70)
    print("섹션 5: 미니 프로젝트 - 고객 VIP 시스템")
    print("=" * 70)
    
    print("\n📋 프로젝트 목표:")
    print("   고객의 구매 금액에 따라 VIP 등급을 판정하고")
    print("   적절한 감사 메시지를 전송하는 시스템을 만듭니다.\n")
    
    print("🎯 등급 기준:")
    print("   • VIP:    100만원 이상 → 'VIP 고객님 감사합니다!'")
    print("   • 우수:   50만원 이상 → '우수 고객님 감사합니다!'")
    print("   • 일반:   50만원 미만 → '감사합니다!'\n")
    
    # 고객 데이터
    customers = [
        {"name": "홍길동", "purchase": 1200000},
        {"name": "김철수", "purchase": 800000},
        {"name": "이영희", "purchase": 1500000},
        {"name": "박민수", "purchase": 300000},
        {"name": "최지수", "purchase": 600000}
    ]
    
    print("=" * 70)
    print(" " * 20 + "고객 메시지 전송 시스템")
    print("=" * 70)
    
    # 통계 변수
    vip_count = 0
    premium_count = 0
    regular_count = 0
    
    # 고객별 처리
    for customer in customers:
        name = customer["name"]
        purchase = customer["purchase"]
        
        # VIP 등급 판정
        if purchase >= 1000000:
            grade = "VIP"
            message = f"💎 VIP 고객님 {name}님, 감사합니다!"
            vip_count += 1
        elif purchase >= 500000:
            grade = "우수"
            message = f"⭐ 우수 고객님 {name}님, 감사합니다!"
            premium_count += 1
        else:
            grade = "일반"
            message = f"🙂 {name}님, 감사합니다!"
            regular_count += 1
        
        # 결과 출력
        print(f"\n[{grade}] {name}")
        print(f"   구매액: {purchase:,}원")
        print(f"   메시지: {message}")
    
    # 통계 출력
    print("\n" + "=" * 70)
    print("고객 등급 통계")
    print("=" * 70)
    print(f"VIP 고객:  {vip_count}명")
    print(f"우수 고객: {premium_count}명")
    print(f"일반 고객: {regular_count}명")
    print(f"총 고객:   {len(customers)}명")
    print()


def practice_problems():
    """연습 문제"""
    print("\n" + "=" * 70)
    print("📝 연습 문제")
    print("=" * 70)
    
    print("""
다음 문제들을 직접 풀어보세요!

【문제 1】 온도에 따른 메시지
temperature = 25
온도가 30도 이상이면 "더워요", 20도 이상이면 "적당해요",
20도 미만이면 "추워요"를 출력하세요.

【문제 2】 1부터 10까지 합계
for문을 사용하여 1부터 10까지의 합을 구하세요.

【문제 3】 짝수만 출력
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
리스트에서 짝수만 출력하세요. (for + if 사용)

【문제 4】 제품 검색
products = [
    {"name": "노트북", "price": 1200000},
    {"name": "마우스", "price": 30000},
    {"name": "키보드", "price": 80000}
]
"마우스"를 찾아서 가격을 출력하세요.

【문제 5】 재고 감소
stock = 10
while문을 사용하여 재고가 0이 될 때까지 1개씩 판매하고,
각 단계마다 남은 재고를 출력하세요.

【문제 6】 VIP 고객 찾기
customers = [
    {"name": "홍길동", "purchase": 1200000},
    {"name": "김철수", "purchase": 800000},
    {"name": "이영희", "purchase": 300000}
]
구매액이 100만원 이상인 VIP 고객의 이름만 출력하세요.

【문제 7】 평균 점수
scores = [85, 90, 78, 92, 88]
for문을 사용하여 평균 점수를 계산하세요.
    """)


def practice_solutions():
    """연습 문제 해설"""
    print("\n" + "=" * 70)
    print("✅ 연습 문제 해설")
    print("=" * 70)
    
    print("\n【문제 1 해설】 온도에 따른 메시지")
    print("-" * 70)
    temperature = 25
    print(f"온도: {temperature}도")
    
    if temperature >= 30:
        print("→ 더워요")
    elif temperature >= 20:
        print("→ 적당해요")
    else:
        print("→ 추워요")
    
    print("\n【문제 2 해설】 1부터 10까지 합계")
    print("-" * 70)
    total = 0
    for i in range(1, 11):
        total += i
    print(f"1부터 10까지의 합: {total}")
    
    print("\n【문제 3 해설】 짝수만 출력")
    print("-" * 70)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("짝수:")
    for num in numbers:
        if num % 2 == 0:
            print(f"  {num}")
    
    print("\n【문제 4 해설】 제품 검색")
    print("-" * 70)
    products = [
        {"name": "노트북", "price": 1200000},
        {"name": "마우스", "price": 30000},
        {"name": "키보드", "price": 80000}
    ]
    
    for product in products:
        if product["name"] == "마우스":
            print(f"마우스 가격: {product['price']:,}원")
            break
    
    print("\n【문제 5 해설】 재고 감소")
    print("-" * 70)
    stock = 10
    print(f"초기 재고: {stock}개\n")
    
    while stock > 0:
        print(f"판매! 남은 재고: {stock - 1}개")
        stock -= 1
    
    print("재고 소진!")
    
    print("\n【문제 6 해설】 VIP 고객 찾기")
    print("-" * 70)
    customers = [
        {"name": "홍길동", "purchase": 1200000},
        {"name": "김철수", "purchase": 800000},
        {"name": "이영희", "purchase": 300000}
    ]
    
    print("VIP 고객 (100만원 이상):")
    for customer in customers:
        if customer["purchase"] >= 1000000:
            print(f"  • {customer['name']}")
    
    print("\n【문제 7 해설】 평균 점수")
    print("-" * 70)
    scores = [85, 90, 78, 92, 88]
    
    total = 0
    for score in scores:
        total += score
    
    average = total / len(scores)
    print(f"점수: {scores}")
    print(f"평균: {average:.1f}점")
    print()


def final_quiz():
    """최종 종합 퀴즈 (7문항)"""
    print("\n" + "=" * 70)
    print("📝 최종 종합 퀴즈 (7문항)")
    print("=" * 70)
    print("\n3교시 내용을 종합적으로 확인하는 퀴즈입니다!\n")
    
    score = 0
    total = 7
    
    # 문제 1
    print("【문제 1】 조건문")
    print("다음 코드의 결과는? (단답형)")
    print("age = 25")
    print("if age >= 18:")
    print("    print('성인')")
    print("else:")
    print("    print('미성년자')")
    answer = input("\n정답: ").strip()
    if answer == "성인":
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 '성인'입니다.")
        print("   25 >= 18이므로 첫 번째 블록이 실행됩니다.")
    
    # 문제 2
    print("\n" + "-" * 70)
    print("【문제 2】 for문")
    print("for i in range(3)을 실행하면 i는 몇 번 반복되나요? (객관식)")
    print("① 1번")
    print("② 2번")
    print("③ 3번")
    print("④ 4번")
    answer = input("\n정답: ").strip()
    if answer in ["③", "3"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ③입니다.")
        print("   range(3)은 0, 1, 2로 총 3번 반복됩니다.")
    
    # 문제 3
    print("\n" + "-" * 70)
    print("【문제 3】 while문")
    print("while문을 종료하는 키워드는? (객관식)")
    print("① stop")
    print("② break")
    print("③ exit")
    print("④ end")
    answer = input("\n정답: ").strip()
    if answer in ["②", "2"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ②입니다.")
        print("   break는 반복문을 즉시 종료합니다.")
    
    # 문제 4
    print("\n" + "-" * 70)
    print("【문제 4】 리스트 순회")
    print("다음 코드의 결과는? (단답형)")
    print("fruits = ['사과', '바나나']")
    print("for fruit in fruits:")
    print("    print(fruit)")
    print("\n몇 줄이 출력되나요?")
    answer = input("\n정답: ").strip()
    if answer in ["2", "2줄"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 2줄입니다.")
        print("   리스트에 2개의 요소가 있으므로 2번 반복됩니다.")
    
    # 문제 5
    print("\n" + "-" * 70)
    print("【문제 5】 조건 판단")
    print("x = 10일 때, x > 5 and x < 15의 결과는? (객관식)")
    print("① True")
    print("② False")
    answer = input("\n정답: ").strip()
    if answer in ["①", "1", "True"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ①입니다.")
        print("   10 > 5도 True이고 10 < 15도 True이므로 and 결과는 True입니다.")
    
    # 문제 6
    print("\n" + "-" * 70)
    print("【문제 6】 딕셔너리 순회")
    print("딕셔너리의 Key와 Value를 동시에 가져오는 메서드는? (객관식)")
    print("① dict.keys()")
    print("② dict.values()")
    print("③ dict.items()")
    print("④ dict.get()")
    answer = input("\n정답: ").strip()
    if answer in ["③", "3"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ③입니다.")
        print("   items()는 (key, value) 튜플을 반환합니다.")
    
    # 문제 7
    print("\n" + "-" * 70)
    print("【문제 7】 종합 문제")
    print("다음 중 VIP 고객을 찾는 올바른 코드는? (객관식)")
    print("① if customer > 1000000:")
    print("② if customer['purchase'] >= 1000000:")
    print("③ if 'purchase' > 1000000:")
    print("④ if purchase >= 1000000:")
    answer = input("\n정답: ").strip()
    if answer in ["②", "2"]:
        print("✅ 정답입니다!")
        score += 1
    else:
        print("❌ 오답입니다. 정답은 ②입니다.")
        print("   딕셔너리에서 값을 가져올 때는 dict['key'] 형식을 사용합니다.")
    
    # 결과 출력
    print("\n" + "=" * 70)
    print(f"📊 최종 퀴즈 결과: {score}/{total}점 ({score/total*100:.0f}%)")
    print("=" * 70)
    
    if score == total:
        print("🎉🎉🎉 완벽합니다! Python 기초를 완전히 마스터하셨네요!")
    elif score >= 5:
        print("👍👍 아주 잘하셨습니다! 조금만 더 복습하면 완벽해질 거예요!")
    elif score >= 3:
        print("💪 잘하고 계세요! 한 번 더 복습해보세요!")
    else:
        print("📚 다시 한 번 이론과 예제를 복습해보세요!")
    print()


def comprehensive_review():
    """전체 과정 복습"""
    print("\n" + "=" * 70)
    print("🎓 전체 과정 복습")
    print("=" * 70)
    
    print("""
축하합니다! Python 기초 3교시를 모두 완료하셨습니다! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 1교시 복습: 리스트(List)와 튜플(Tuple)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 리스트
   • 순서가 있고 변경 가능한 자료구조
   • 대괄호 []로 표현: [1, 2, 3]
   • append(), remove(), insert() 등으로 조작
   • 슬라이싱: list[1:4]

✅ 튜플
   • 순서가 있지만 변경 불가능한 자료구조
   • 소괄호 ()로 표현: (1, 2, 3)
   • 빠르고 메모리 효율적
   • 고정된 데이터에 사용

💡 핵심 코드:
    fruits = ["사과", "바나나", "포도"]
    fruits.append("귤")              # 추가
    quarter1 = sales[0:3]             # 슬라이싱
    x, y = (10, 20)                   # 튜플 언패킹

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 2교시 복습: 딕셔너리(Dictionary)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 딕셔너리
   • Key-Value 구조로 데이터 저장
   • 중괄호 {}로 표현: {"name": "홍길동"}
   • Key로 빠르게 값을 찾을 수 있음
   • dict["key"] 또는 dict.get("key")로 조회

✅ 복합 자료구조
   • 리스트 안에 딕셔너리 (가장 많이 사용!)
   • 딕셔너리 안에 리스트
   • 실무에서 데이터 관리의 핵심

💡 핵심 코드:
    person = {"name": "홍길동", "age": 25}
    person["city"] = "서울"           # 추가/수정
    for key, value in person.items(): # 순회
        print(f"{key}: {value}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 3교시 복습: 조건문과 반복문
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ if 조건문
   • 조건에 따라 다른 코드 실행
   • if / elif / else 구조
   • 비교 연산자: ==, !=, >, <, >=, <=
   • 논리 연산자: and, or, not

✅ for 반복문
   • 정해진 범위를 반복
   • 리스트, 딕셔너리 순회에 사용
   • range(), enumerate(), items()

✅ while 반복문
   • 조건이 만족하는 동안 반복
   • break로 즉시 종료
   • continue로 다음 반복으로 건너뛰기

💡 핵심 코드:
    # 조건문
    if score >= 90:
        print("A학점")
    elif score >= 80:
        print("B학점")
    
    # for문
    for customer in customers:
        if customer["purchase"] >= 1000000:
            print("VIP 고객")
    
    # while문
    while stock > 0:
        stock -= 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 다음 단계 학습 로드맵
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 함수 (Function)
   • 재사용 가능한 코드 블록 만들기
   • 매개변수와 반환값
   • 람다 함수

2. 파일 입출력
   • 파일 읽기/쓰기
   • CSV, JSON 파일 처리
   • with 문 사용

3. 예외 처리
   • try-except로 에러 처리
   • 안전한 프로그램 만들기

4. 객체 지향 프로그래밍
   • 클래스와 객체
   • 캡슐화, 상속, 다형성

5. 라이브러리 활용
   • pandas (데이터 분석)
   • matplotlib (데이터 시각화)
   • requests (웹 크롤링)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💪 여러분은 이제 Python의 기초를 탄탄하게 다졌습니다!
   배운 내용을 바탕으로 작은 프로젝트를 만들어보세요.
   
   예시:
   • 나만의 할 일 관리 프로그램
   • 간단한 주소록 프로그램
   • 가계부 프로그램
   • 학생 성적 관리 프로그램

🎉 수고하셨습니다! 계속해서 코딩을 즐기세요! 🚀
    """)


def main_menu():
    """메인 메뉴"""
    while True:
        print("\n" + "=" * 70)
        print("📚 3교시: 조건문과 반복문 - 학습 메뉴")
        print("=" * 70)
        print("\n[이론 + 예제]")
        print("  1. 섹션 1 - if 조건문")
        print("  2. 섹션 2 - for 반복문")
        print("  3. 섹션 3 - while 반복문")
        print("  4. 섹션 4 - 조건문 + 반복문 조합")
        print("  5. 섹션 5 - 미니 프로젝트 (고객 VIP 시스템)")
        
        print("\n[연습 및 평가]")
        print("  6. 연습 문제")
        print("  7. 연습 문제 해설")
        print("  8. 최종 종합 퀴즈 (7문항)")
        print("  9. 전체 과정 복습")
        
        print("\n[전체 실행]")
        print("  0. 모든 섹션 순서대로 실행")
        print("  q. 종료")
        
        choice = input("\n선택하세요: ").strip()
        
        if choice == "0":
            intro()
            section1_if_statements()
            input("\nEnter를 눌러 계속...")
            section2_for_loops()
            input("\nEnter를 눌러 계속...")
            section3_while_loops()
            input("\nEnter를 눌러 계속...")
            section4_combined()
            input("\nEnter를 눌러 계속...")
            section5_vip_mini_project()
            input("\nEnter를 눌러 계속...")
            practice_problems()
            input("\nEnter를 눌러 계속...")
            practice_solutions()
            input("\nEnter를 눌러 계속...")
            final_quiz()
            comprehensive_review()
            print("\n🎉 전체 학습을 완료했습니다!")
            print("Python 기초 과정을 모두 마스터하셨습니다! 축하합니다! 🎊")
            break
        elif choice == "1":
            section1_if_statements()
        elif choice == "2":
            section2_for_loops()
        elif choice == "3":
            section3_while_loops()
        elif choice == "4":
            section4_combined()
        elif choice == "5":
            section5_vip_mini_project()
        elif choice == "6":
            practice_problems()
        elif choice == "7":
            practice_solutions()
        elif choice == "8":
            final_quiz()
        elif choice == "9":
            comprehensive_review()
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

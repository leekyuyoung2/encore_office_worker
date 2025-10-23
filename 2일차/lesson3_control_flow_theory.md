# Python 기초 - 3교시: 조건문과 반복문 (if, for, while)

> **난이도**: 초급 (비전공자 대상)
> 
> **예상 학습 시간**: 2시간 (이론 50분 + 실습 70분)

---

## 🎯 학습 목표

이 과정을 마치면 다음을 할 수 있게 됩니다:

1. **조건문 이해**: if/elif/else로 조건에 따라 다른 코드를 실행할 수 있습니다
2. **for 반복문**: 리스트, 딕셔너리를 순회하며 작업을 수행할 수 있습니다
3. **while 반복문**: 조건이 만족하는 동안 반복 작업을 수행할 수 있습니다
4. **조합 활용**: 조건문과 반복문을 조합하여 복잡한 문제를 해결할 수 있습니다
5. **실무 프로젝트**: 고객 VIP 판별 및 메시지 전송 시스템을 만들 수 있습니다

---

## 📚 목차

1. [조건문 (if문)](#1-조건문-if문)
2. [for 반복문](#2-for-반복문)
3. [while 반복문](#3-while-반복문)
4. [조건문 + 반복문 조합](#4-조건문--반복문-조합)
5. [미니 프로젝트: 고객 VIP 시스템](#5-미니-프로젝트-고객-vip-시스템)

---

## 1. 조건문 (if문)

### 1.1 if문이란? (쉬운 비유)

**조건문은 "상황에 따라 다르게 행동하는 것"입니다!**

일상생활 비유:
- 🌧️ **날씨에 따른 결정**: "비가 오면 우산을 쓰고, 안 오면 그냥 나간다"
- 🎫 **나이에 따른 요금**: "13세 미만이면 어린이 요금, 65세 이상이면 경로 요금, 그 외는 일반 요금"
- 🚦 **신호등**: "빨간불이면 멈추고, 파란불이면 간다"
- 💰 **할인**: "구매액이 10만원 이상이면 10% 할인"

### 1.2 기본 if문 구조

```python
# 기본 형태
if 조건:
    실행할 코드
```

**예제 1: 나이 확인**
```python
age = 20

if age >= 18:
    print("성인입니다")
# 출력: 성인입니다
```

**예제 2: 온도 확인**
```python
temperature = 30

if temperature > 25:
    print("더워요! 에어컨을 켜세요")
# 출력: 더워요! 에어컨을 켜세요
```

### 1.3 if-else문

```python
# if-else 형태
if 조건:
    조건이 True일 때 실행
else:
    조건이 False일 때 실행
```

**예제: 성인/미성년자 판별**
```python
age = 15

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")
# 출력: 미성년자입니다
```

### 1.4 if-elif-else문 (다중 조건)

```python
# if-elif-else 형태
if 조건1:
    조건1이 True일 때
elif 조건2:
    조건2가 True일 때
elif 조건3:
    조건3이 True일 때
else:
    모든 조건이 False일 때
```

**예제: 학점 계산**
```python
score = 85

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

print(f"점수 {score}점은 {grade}학점입니다")
# 출력: 점수 85점은 B학점입니다
```

### 1.5 비교 연산자

```python
# 비교 연산자
==  # 같다
!=  # 다르다
>   # 크다
<   # 작다
>=  # 크거나 같다
<=  # 작거나 같다

# 예제
x = 10
print(x == 10)  # True
print(x != 5)   # True
print(x > 5)    # True
print(x < 20)   # True
```

### 1.6 논리 연산자 (and, or, not)

```python
# and: 모두 True여야 True
age = 25
has_license = True

if age >= 18 and has_license:
    print("운전할 수 있습니다")

# or: 하나라도 True면 True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("쉬는 날입니다")

# not: True면 False, False면 True
is_raining = False

if not is_raining:
    print("우산이 필요 없습니다")
```

### 1.7 in 연산자 (포함 여부)

```python
# 리스트에서 확인
fruits = ["사과", "바나나", "포도"]

if "사과" in fruits:
    print("사과가 있습니다")

# 딕셔너리에서 Key 확인
student = {"name": "홍길동", "age": 20}

if "name" in student:
    print(f"이름: {student['name']}")

# 문자열에서 확인
text = "Hello Python"

if "Python" in text:
    print("Python이 포함되어 있습니다")
```

---

## 2. for 반복문

### 2.1 for문이란? (쉬운 비유)

**for문은 "여러 개를 하나씩 처리하는 것"입니다!**

일상생활 비유:
- 📦 **택배 배송**: "배송지 리스트를 보고 한 곳씩 배송한다"
- 🏫 **출석 체크**: "학생 명단을 보고 한 명씩 이름을 부른다"
- 📧 **이메일 전송**: "고객 리스트를 보고 한 명씩 이메일을 보낸다"
- 🎵 **재생 목록**: "노래 목록을 처음부터 끝까지 한 곡씩 재생한다"

### 2.2 기본 for문 구조

```python
# 기본 형태
for 변수 in 리스트:
    반복할 코드
```

**예제 1: 리스트 순회**
```python
fruits = ["사과", "바나나", "포도"]

for fruit in fruits:
    print(f"나는 {fruit}을/를 좋아합니다")

# 출력:
# 나는 사과을/를 좋아합니다
# 나는 바나나을/를 좋아합니다
# 나는 포도을/를 좋아합니다
```

**예제 2: 숫자 반복 (range 사용)**
```python
# range(n): 0부터 n-1까지
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4

# range(start, end): start부터 end-1까지
for i in range(1, 6):
    print(i)
# 출력: 1, 2, 3, 4, 5

# range(start, end, step): step만큼 증가
for i in range(0, 10, 2):
    print(i)
# 출력: 0, 2, 4, 6, 8
```

### 2.3 딕셔너리 순회

```python
student = {"name": "홍길동", "age": 20, "major": "컴퓨터공학"}

# 방법 1: Key만 순회
for key in student:
    print(f"{key}: {student[key]}")

# 방법 2: Key-Value 쌍으로 순회 (가장 많이 사용!)
for key, value in student.items():
    print(f"{key}: {value}")

# 출력:
# name: 홍길동
# age: 20
# major: 컴퓨터공학
```

### 2.4 리스트 + 딕셔너리 순회

```python
students = [
    {"name": "홍길동", "score": 85},
    {"name": "김철수", "score": 92},
    {"name": "이영희", "score": 78}
]

for student in students:
    print(f"{student['name']}: {student['score']}점")

# 출력:
# 홍길동: 85점
# 김철수: 92점
# 이영희: 78점
```

### 2.5 enumerate() - 인덱스와 값 함께 가져오기

```python
fruits = ["사과", "바나나", "포도"]

for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# 출력:
# 1. 사과
# 2. 바나나
# 3. 포도

# 시작 인덱스 지정 가능
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### 2.6 중첩 for문

```python
# 구구단 예제
for i in range(2, 4):  # 2단, 3단
    print(f"\n[{i}단]")
    for j in range(1, 10):  # 1~9
        print(f"{i} × {j} = {i*j}")
```

---

## 3. while 반복문

### 3.1 while문이란? (쉬운 비유)

**while문은 "조건이 만족하는 동안 계속 반복하는 것"입니다!**

일상생활 비유:
- 🎮 **게임**: "게임 오버가 아닐 동안 계속 플레이한다"
- 🏃 **달리기**: "목표 지점에 도착할 때까지 계속 달린다"
- 📦 **재고 판매**: "재고가 남아있는 동안 계속 판다"
- ⏰ **알람**: "사용자가 끌 때까지 계속 울린다"

### 3.2 기본 while문 구조

```python
# 기본 형태
while 조건:
    반복할 코드
    # 조건을 False로 만들 코드 필요!
```

**예제 1: 카운트다운**
```python
count = 5

while count > 0:
    print(f"{count}초 남음...")
    count -= 1  # 조건을 False로 만드는 코드!

print("발사!")

# 출력:
# 5초 남음...
# 4초 남음...
# 3초 남음...
# 2초 남음...
# 1초 남음...
# 발사!
```

**예제 2: 재고 판매**
```python
stock = 10

while stock > 0:
    print(f"판매! 남은 재고: {stock}개")
    stock -= 1

print("재고 소진!")
```

### 3.3 무한 루프와 break

```python
# 무한 루프 (조건이 항상 True)
while True:
    user_input = input("종료하려면 'q'를 입력하세요: ")
    
    if user_input == 'q':
        print("프로그램을 종료합니다")
        break  # 반복문 탈출!
    
    print(f"입력하신 내용: {user_input}")
```

### 3.4 continue - 다음 반복으로 건너뛰기

```python
# 1부터 10까지 중 홀수만 출력
count = 0

while count < 10:
    count += 1
    
    if count % 2 == 0:  # 짝수면
        continue  # 다음 반복으로 건너뛰기
    
    print(count)  # 홀수만 출력됨

# 출력: 1, 3, 5, 7, 9
```

### 3.5 for vs while 비교

| 구분 | for문 | while문 |
|------|-------|---------|
| **사용 시점** | 반복 횟수를 알 때 | 조건에 따라 반복할 때 |
| **예시** | 리스트 순회, 정해진 횟수 | 사용자 입력, 조건 만족까지 |
| **종료 조건** | 자동 (리스트 끝) | 수동 (조건 False) |

**for문 사용 예시**:
```python
# 리스트 순회 (횟수가 정해짐)
for student in students:
    print(student["name"])

# 10번 반복 (횟수가 정해짐)
for i in range(10):
    print(i)
```

**while문 사용 예시**:
```python
# 조건이 만족할 때까지
stock = 100
while stock > 0:
    # 판매 처리
    stock -= 1

# 사용자 입력 받기
while True:
    answer = input("계속하시겠습니까? (y/n): ")
    if answer == 'n':
        break
```

---

## 4. 조건문 + 반복문 조합

### 4.1 for문 안에서 if문 사용

**예제 1: 짝수만 출력**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num}은 짝수입니다")
```

**예제 2: 학생 합격 판정**
```python
students = [
    {"name": "홍길동", "score": 85},
    {"name": "김철수", "score": 92},
    {"name": "이영희", "score": 65},
    {"name": "박민수", "score": 58}
]

print("=" * 50)
print("합격자 명단 (70점 이상)")
print("=" * 50)

for student in students:
    if student["score"] >= 70:
        print(f"✅ {student['name']}: {student['score']}점 - 합격")
    else:
        print(f"❌ {student['name']}: {student['score']}점 - 불합격")
```

### 4.2 리스트 필터링

```python
# 매출이 200만원 이상인 달만 선택
monthly_sales = [150, 180, 220, 250, 190, 210, 280, 300, 270, 240, 260, 290]

high_sales_months = []

for i, sales in enumerate(monthly_sales, start=1):
    if sales >= 200:
        high_sales_months.append({"month": i, "sales": sales})

print("매출 200만원 이상인 달:")
for data in high_sales_months:
    print(f"  {data['month']}월: {data['sales']}만원")
```

### 4.3 다중 조건 처리

```python
products = [
    {"name": "노트북", "price": 1200000, "stock": 5},
    {"name": "마우스", "price": 30000, "stock": 0},
    {"name": "키보드", "price": 80000, "stock": 3},
    {"name": "모니터", "price": 300000, "stock": 15}
]

print("재고 상태 보고서")
print("=" * 50)

for product in products:
    print(f"\n상품: {product['name']}")
    
    # 재고 상태 판단
    if product['stock'] == 0:
        print("  ⚠️  재고 없음 - 긴급 발주 필요!")
    elif product['stock'] < 5:
        print("  ⚠️  재고 부족 - 발주 권장")
    else:
        print("  ✅ 재고 충분")
    
    # 가격대 판단
    if product['price'] >= 1000000:
        print("  💎 고가 제품")
    elif product['price'] >= 100000:
        print("  💰 중가 제품")
    else:
        print("  💵 저가 제품")
```

---

## 5. 미니 프로젝트: 고객 VIP 시스템

### 5.1 프로젝트 개요

**목표**: 고객의 구매 금액에 따라 VIP 등급을 판정하고, 적절한 감사 메시지를 전송하는 시스템을 만듭니다.

**요구사항**:
- 구매액 100만원 이상: VIP 고객 → "VIP 고객님 감사합니다!"
- 구매액 50만원 이상: 우수 고객 → "우수 고객님 감사합니다!"
- 구매액 50만원 미만: 일반 고객 → "감사합니다!"

### 5.2 기본 버전

```python
# 고객 데이터
customers = [
    {"name": "홍길동", "purchase": 1200000},
    {"name": "김철수", "purchase": 800000},
    {"name": "이영희", "purchase": 1500000},
    {"name": "박민수", "purchase": 300000},
    {"name": "최지수", "purchase": 600000}
]

# VIP 판별 및 메시지 전송
print("=" * 60)
print(" " * 20 + "고객 메시지 전송")
print("=" * 60)

for customer in customers:
    name = customer["name"]
    purchase = customer["purchase"]
    
    # VIP 등급 판정
    if purchase >= 1000000:
        grade = "VIP"
        message = f"VIP 고객님 {name}님, 감사합니다!"
    elif purchase >= 500000:
        grade = "우수"
        message = f"우수 고객님 {name}님, 감사합니다!"
    else:
        grade = "일반"
        message = f"{name}님, 감사합니다!"
    
    # 결과 출력
    print(f"\n[{grade}] {name} - 구매액: {purchase:,}원")
    print(f"메시지: {message}")
```

### 5.3 고급 버전 (할인 쿠폰 포함)

```python
# 고객 데이터
customers = [
    {"name": "홍길동", "purchase": 1200000, "visit_count": 15},
    {"name": "김철수", "purchase": 800000, "visit_count": 8},
    {"name": "이영희", "purchase": 1500000, "visit_count": 20},
    {"name": "박민수", "purchase": 300000, "visit_count": 3},
    {"name": "최지수", "purchase": 600000, "visit_count": 10}
]

print("=" * 70)
print(" " * 20 + "고객 혜택 안내 시스템")
print("=" * 70)

# 통계 변수
vip_count = 0
premium_count = 0
regular_count = 0

for customer in customers:
    name = customer["name"]
    purchase = customer["purchase"]
    visit_count = customer["visit_count"]
    
    print(f"\n{'='*70}")
    print(f"고객명: {name}")
    print(f"누적 구매액: {purchase:,}원")
    print(f"방문 횟수: {visit_count}회")
    print(f"{'-'*70}")
    
    # VIP 등급 판정
    if purchase >= 1000000:
        grade = "VIP"
        discount = 20  # 20% 할인
        vip_count += 1
    elif purchase >= 500000:
        grade = "우수"
        discount = 10  # 10% 할인
        premium_count += 1
    else:
        grade = "일반"
        discount = 5   # 5% 할인
        regular_count += 1
    
    # 등급별 메시지
    print(f"등급: [{grade}]")
    print(f"할인율: {discount}%")
    
    # 추가 혜택 (방문 횟수)
    if visit_count >= 15:
        print("🎁 특별 혜택: 추가 포인트 5,000점")
    elif visit_count >= 10:
        print("🎁 특별 혜택: 추가 포인트 3,000점")
    
    # 메시지 생성
    if grade == "VIP":
        message = f"💎 {name}님, 항상 저희 쇼핑몰을 이용해 주셔서 감사합니다!"
        message += f"\n   VIP 고객님만을 위한 {discount}% 할인 쿠폰을 드립니다!"
    elif grade == "우수":
        message = f"⭐ {name}님, 저희 쇼핑몰을 자주 이용해 주셔서 감사합니다!"
        message += f"\n   우수 고객님을 위한 {discount}% 할인 쿠폰을 드립니다!"
    else:
        message = f"🙂 {name}님, 저희 쇼핑몰을 이용해 주셔서 감사합니다!"
        message += f"\n   {discount}% 할인 쿠폰을 드립니다!"
    
    print(f"\n{message}")

# 최종 통계
print(f"\n{'='*70}")
print("고객 등급 통계")
print(f"{'='*70}")
print(f"VIP 고객: {vip_count}명")
print(f"우수 고객: {premium_count}명")
print(f"일반 고객: {regular_count}명")
print(f"총 고객: {len(customers)}명")
```

### 5.4 함수로 모듈화하기

```python
def get_customer_grade(purchase):
    """구매액에 따른 고객 등급 반환"""
    if purchase >= 1000000:
        return "VIP", 20
    elif purchase >= 500000:
        return "우수", 10
    else:
        return "일반", 5


def send_message(customer):
    """고객에게 메시지 전송"""
    name = customer["name"]
    purchase = customer["purchase"]
    
    grade, discount = get_customer_grade(purchase)
    
    # 메시지 생성
    if grade == "VIP":
        message = f"💎 VIP 고객님 {name}님, 감사합니다! (할인율: {discount}%)"
    elif grade == "우수":
        message = f"⭐ 우수 고객님 {name}님, 감사합니다! (할인율: {discount}%)"
    else:
        message = f"🙂 {name}님, 감사합니다! (할인율: {discount}%)"
    
    return message


# 메인 실행
customers = [
    {"name": "홍길동", "purchase": 1200000},
    {"name": "김철수", "purchase": 800000},
    {"name": "이영희", "purchase": 1500000}
]

print("고객 메시지 전송 시스템")
print("=" * 50)

for customer in customers:
    message = send_message(customer)
    print(message)
```

---

## 📝 정리

### 핵심 개념

1. **조건문 (if)**: 조건에 따라 다른 코드를 실행
   - `if 조건:` - 조건이 True일 때 실행
   - `elif 조건:` - 첫 조건이 False이고 이 조건이 True일 때
   - `else:` - 모든 조건이 False일 때

2. **for 반복문**: 정해진 범위를 반복
   - `for item in list:` - 리스트 순회
   - `for key, value in dict.items():` - 딕셔너리 순회
   - `for i in range(n):` - n번 반복

3. **while 반복문**: 조건이 만족하는 동안 반복
   - `while 조건:` - 조건이 True인 동안 계속
   - `break` - 반복문 즉시 종료
   - `continue` - 다음 반복으로 건너뛰기

4. **조합 활용**: 조건문과 반복문을 함께 사용
   - for문 안에 if문으로 필터링
   - 복잡한 비즈니스 로직 구현

### 자주 사용하는 코드 패턴

```python
# 패턴 1: 리스트 필터링
for item in items:
    if item["score"] >= 80:
        print(item["name"])

# 패턴 2: 카운팅
count = 0
for item in items:
    if item["status"] == "active":
        count += 1

# 패턴 3: 조건부 메시지
for customer in customers:
    if customer["vip"]:
        print("VIP 고객님 감사합니다")
    else:
        print("감사합니다")

# 패턴 4: 딕셔너리 순회
for key, value in data.items():
    print(f"{key}: {value}")

# 패턴 5: enumerate로 인덱스 포함
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

---

## 🎯 다음 단계

조건문과 반복문을 마스터했다면, 다음을 학습해보세요:

1. **리스트 컴프리헨션**: 리스트를 간결하게 생성하는 고급 문법
2. **함수**: 반복되는 코드를 함수로 만들어 재사용
3. **예외 처리**: try-except로 에러 상황 처리
4. **파일 입출력**: 파일에서 데이터 읽고 쓰기

**축하합니다! 🎉 Python 기초 과정을 모두 마스터하셨습니다!**

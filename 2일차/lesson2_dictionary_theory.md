# Python 기초 - 2교시: 딕셔너리(Dictionary)

> **난이도**: 초급 (비전공자 대상)
> 
> **예상 학습 시간**: 1시간 30분 (이론 40분 + 실습 50분)

---

## 🎯 학습 목표

이 과정을 마치면 다음을 할 수 있게 됩니다:

1. **딕셔너리 이해**: Key-Value 구조를 실생활 비유로 이해할 수 있습니다
2. **딕셔너리 조작**: 데이터 조회, 수정, 추가, 삭제를 자유롭게 할 수 있습니다
3. **리스트와 비교**: 딕셔너리와 리스트의 차이점을 이해합니다
4. **복합 자료구조**: 리스트와 딕셔너리를 조합하여 사용할 수 있습니다
5. **실무 활용**: 제품 정보 관리 프로그램을 만들 수 있습니다

---

## 📚 목차

1. [딕셔너리(Dictionary)란 무엇인가?](#1-딕셔너리dictionary란-무엇인가)
2. [딕셔너리 기본 조작](#2-딕셔너리-기본-조작)
3. [딕셔너리 메서드](#3-딕셔너리-메서드)
4. [리스트 + 딕셔너리 조합](#4-리스트--딕셔너리-조합)
5. [자료구조 비교 (리스트 vs 튜플 vs 딕셔너리)](#5-자료구조-비교)
6. [실무 예제: 제품 관리 시스템](#6-실무-예제-제품-관리-시스템)

---

## 1. 딕셔너리(Dictionary)란 무엇인가?

### 1.1 딕셔너리의 개념 (쉬운 비유)

**딕셔너리는 "단어와 뜻을 연결한 사전"입니다!**

일상생활에서 비유하면:
- 📖 **영한 사전**: "apple" → "사과", "banana" → "바나나"
- 📞 **전화번호부**: "홍길동" → "010-1234-5678", "김철수" → "010-9876-5432"
- 🏷️ **상품 바코드**: "8801234567890" → "삼다수 2L"
- 🏫 **학번-이름 매칭**: "20240001" → "이영희", "20240002" → "박민수"

프로그래밍에서 딕셔너리는:
```python
# Key(키)와 Value(값)를 쌍으로 저장
phone_book = {
    "홍길동": "010-1234-5678",
    "김철수": "010-9876-5432"
}
```

### 1.2 딕셔너리를 왜 사용할까?

**문제 상황**: 학생 3명의 정보(이름, 나이, 전공)를 저장하려면?

❌ **리스트만 사용 (비효율적)**:
```python
student1 = ["홍길동", 25, "컴퓨터공학"]
student2 = ["김철수", 23, "경영학"]
student3 = ["이영희", 24, "디자인"]

# 각 값이 무엇을 의미하는지 기억해야 해요!
# student1[0]이 이름인지, 나이인지 헷갈려요 😓
```

✅ **딕셔너리 사용 (명확하고 효율적)**:
```python
student1 = {"name": "홍길동", "age": 25, "major": "컴퓨터공학"}
student2 = {"name": "김철수", "age": 23, "major": "경영학"}
student3 = {"name": "이영희", "age": 24, "major": "디자인"}

# 의미가 명확해요!
print(student1["name"])   # "홍길동"
print(student1["age"])    # 25
```

### 1.3 딕셔너리 생성 방법

```python
# 방법 1: 중괄호 사용 (가장 일반적)
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

# 방법 2: dict() 함수 사용
person = dict(name="홍길동", age=25, city="서울")

# 빈 딕셔너리
empty_dict = {}
empty_dict2 = dict()

# 다양한 자료형 값 사용 가능
mixed = {
    "name": "홍길동",
    "age": 25,
    "scores": [85, 90, 88],  # 리스트도 값으로 가능
    "is_student": True
}
```

### 1.4 딕셔너리의 특징

| 특징 | 설명 | 예시 |
|------|------|------|
| **Key-Value 구조** | 키로 값을 찾음 | `person["name"]` → "홍길동" |
| **Key는 고유** | 같은 Key는 하나만 존재 | 중복 Key 입력 시 덮어씀 |
| **순서 없음** (Python 3.7+는 순서 유지) | 인덱스로 접근 불가 | `person[0]` ❌ |
| **변경 가능** | 값 추가/삭제/수정 가능 | `person["age"] = 26` ✅ |
| **Key 자료형 제한** | 불변 자료형만 Key 가능 | 문자열, 숫자, 튜플 ✅ / 리스트 ❌ |

### 1.5 Key와 Value 이해하기

```python
product = {
    "name": "노트북",      # Key: "name",      Value: "노트북"
    "price": 1200000,      # Key: "price",     Value: 1200000
    "stock": 5             # Key: "stock",     Value: 5
}

# Key로 Value에 접근
print(product["name"])     # "노트북"
print(product["price"])    # 1200000
```

**💡 규칙**:
- **Key는 고유해야 함**: 같은 Key가 2개 있으면 마지막 값만 남음
- **Key는 불변 자료형**: 문자열, 숫자, 튜플만 가능 (리스트는 불가)
- **Value는 제한 없음**: 모든 자료형 가능 (리스트, 딕셔너리도 가능)

---

## 2. 딕셔너리 기본 조작

### 2.1 값 조회하기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}

# 방법 1: 대괄호 사용
print(product["name"])      # "노트북"
print(product["price"])     # 1200000

# 방법 2: get() 메서드 (안전한 방법)
print(product.get("name"))  # "노트북"
print(product.get("color")) # None (에러 발생 안 함!)

# get()에 기본값 지정
print(product.get("color", "정보 없음"))  # "정보 없음"
```

**❓ 왜 get()을 사용할까?**
```python
# 대괄호: Key가 없으면 에러 발생!
# print(product["color"])  # ❌ KeyError 발생!

# get(): Key가 없으면 None 반환 (에러 없음)
print(product.get("color"))  # None (안전!)
```

### 2.2 값 추가하기

```python
product = {
    "name": "노트북",
    "price": 1200000
}

# 새로운 Key-Value 추가
product["stock"] = 5
product["brand"] = "Apple"

print(product)
# {'name': '노트북', 'price': 1200000, 'stock': 5, 'brand': 'Apple'}
```

### 2.3 값 수정하기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}

# 기존 Key의 값 변경
product["price"] = 1100000  # 가격 인하
product["stock"] = 3        # 재고 감소

print(product["price"])     # 1100000
print(product["stock"])     # 3
```

### 2.4 값 삭제하기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5,
    "discontinued": True
}

# 방법 1: del 키워드
del product["discontinued"]

# 방법 2: pop() 메서드 (삭제된 값 반환)
stock = product.pop("stock")
print(f"삭제된 재고: {stock}")  # 5

# 방법 3: clear() - 전체 삭제
product.clear()
print(product)  # {}
```

### 2.5 Key 존재 확인하기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}

# in 연산자 사용
if "price" in product:
    print(f"가격: {product['price']}원")

if "color" not in product:
    print("색상 정보가 없습니다")
```

---

## 3. 딕셔너리 메서드

### 3.1 keys() - 모든 Key 가져오기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}

# 모든 Key 조회
keys = product.keys()
print(keys)  # dict_keys(['name', 'price', 'stock'])

# 리스트로 변환
keys_list = list(product.keys())
print(keys_list)  # ['name', 'price', 'stock']

# 반복문에서 사용
for key in product.keys():
    print(f"{key}: {product[key]}")
```

### 3.2 values() - 모든 Value 가져오기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}

# 모든 값 조회
values = product.values()
print(values)  # dict_values(['노트북', 1200000, 5])

# 합계 구하기 (숫자 값만)
scores = {"수학": 85, "영어": 90, "과학": 88}
total = sum(scores.values())
average = total / len(scores)
print(f"평균: {average:.1f}점")  # 87.7점
```

### 3.3 items() - Key-Value 쌍 가져오기

```python
product = {
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}

# Key-Value 쌍으로 조회
items = product.items()
print(items)  # dict_items([('name', '노트북'), ('price', 1200000), ('stock', 5)])

# 반복문에서 자주 사용 (가장 유용!)
for key, value in product.items():
    print(f"{key}: {value}")

# 출력:
# name: 노트북
# price: 1200000
# stock: 5
```

### 3.4 update() - 여러 항목 추가/수정

```python
product = {
    "name": "노트북",
    "price": 1200000
}

# 여러 항목을 한 번에 추가/수정
product.update({
    "stock": 5,
    "brand": "Apple",
    "price": 1100000  # 기존 값 수정
})

print(product)
# {'name': '노트북', 'price': 1100000, 'stock': 5, 'brand': 'Apple'}
```

---

## 4. 리스트 + 딕셔너리 조합

### 4.1 딕셔너리 안에 리스트

```python
student = {
    "name": "홍길동",
    "age": 20,
    "scores": [85, 90, 88, 92]  # 리스트를 값으로 사용
}

# 점수 평균 구하기
average = sum(student["scores"]) / len(student["scores"])
print(f"{student['name']}의 평균: {average:.1f}점")
```

### 4.2 리스트 안에 딕셔너리 (가장 많이 사용!)

```python
# 여러 제품 정보를 리스트에 저장
products = [
    {"name": "노트북", "price": 1200000, "stock": 5},
    {"name": "마우스", "price": 30000, "stock": 20},
    {"name": "키보드", "price": 80000, "stock": 15}
]

# 모든 제품 정보 출력
print("=" * 50)
print("제품 목록")
print("=" * 50)
for product in products:
    print(f"상품명: {product['name']}")
    print(f"가격: {product['price']:,}원")
    print(f"재고: {product['stock']}개")
    print("-" * 50)

# 총 재고 가치 계산
total_value = 0
for product in products:
    value = product['price'] * product['stock']
    total_value += value

print(f"총 재고 가치: {total_value:,}원")
```

### 4.3 딕셔너리 안에 딕셔너리

```python
# 학생별 과목 점수
students = {
    "홍길동": {"수학": 85, "영어": 90, "과학": 88},
    "김철수": {"수학": 92, "영어": 88, "과학": 95},
    "이영희": {"수학": 78, "영어": 85, "과학": 80}
}

# 홍길동의 수학 점수
print(students["홍길동"]["수학"])  # 85

# 모든 학생의 평균 출력
for name, scores in students.items():
    average = sum(scores.values()) / len(scores)
    print(f"{name}의 평균: {average:.1f}점")
```

---

## 5. 자료구조 비교

### 5.1 리스트 vs 튜플 vs 딕셔너리 비교표

| 구분 | 리스트 (List) | 튜플 (Tuple) | 딕셔너리 (Dictionary) |
|------|--------------|-------------|---------------------|
| **표기법** | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1, "b": 2}` |
| **순서** | ✅ 있음 (인덱스) | ✅ 있음 (인덱스) | ❌ 없음 (Key로 접근) |
| **변경 가능** | ✅ 가능 | ❌ 불가능 | ✅ 가능 |
| **중복 허용** | ✅ 허용 | ✅ 허용 | ❌ Key는 고유 |
| **접근 방법** | `list[0]` | `tuple[0]` | `dict["key"]` |
| **추가** | `append()` | ❌ 불가능 | `dict["key"] = value` |
| **삭제** | `remove()` | ❌ 불가능 | `del dict["key"]` |
| **속도** | 보통 | 빠름 | 매우 빠름 (검색) |
| **용도** | 순서있는 데이터 | 고정 데이터 | Key-Value 매핑 |

### 5.2 실제 사용 예시 비교

```python
# 📝 리스트: 순서가 중요한 데이터
shopping_list = ["사과", "우유", "빵", "계란"]  # 장보기 순서
todo_list = ["코딩", "운동", "독서"]          # 할 일 순서

# 🔒 튜플: 변경하면 안 되는 데이터
rgb_red = (255, 0, 0)              # RGB 색상 (고정)
coordinates = (37.5665, 126.9780)  # GPS 좌표 (고정)
birth_date = (1990, 5, 15)         # 생년월일 (고정)

# 🔍 딕셔너리: 이름으로 찾는 데이터
person = {                          # 사람 정보 (이름으로 검색)
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

product = {                         # 제품 정보 (항목명으로 검색)
    "name": "노트북",
    "price": 1200000,
    "stock": 5
}
```

### 5.3 언제 무엇을 사용할까?

**리스트 사용 시점**:
```python
# ✅ 순서가 중요할 때
ranking = ["1위: 홍길동", "2위: 김철수", "3위: 이영희"]

# ✅ 같은 종류의 데이터를 여러 개 저장할 때
monthly_sales = [100, 120, 130, 140, 150, 160]

# ✅ 데이터를 추가/삭제가 자주 일어날 때
cart = []
cart.append("사과")
cart.append("우유")
```

**튜플 사용 시점**:
```python
# ✅ 데이터가 절대 변하지 않을 때
ADMIN_ID = (1, "admin", "admin@company.com")

# ✅ 함수에서 여러 값을 반환할 때
def get_user_info():
    return "홍길동", 25, "서울"  # 튜플 반환

# ✅ 딕셔너리의 Key로 사용할 때
locations = {
    (37.5665, 126.9780): "서울",
    (35.1796, 129.0756): "부산"
}
```

**딕셔너리 사용 시점**:
```python
# ✅ Key로 데이터를 빠르게 찾아야 할 때
phone_book = {
    "홍길동": "010-1234-5678",
    "김철수": "010-9876-5432"
}

# ✅ 데이터에 의미 있는 이름을 붙여야 할 때
student = {
    "name": "홍길동",    # 의미가 명확
    "age": 20,
    "major": "컴퓨터공학"
}

# ✅ 설정 정보를 저장할 때
config = {
    "debug": True,
    "port": 8080,
    "host": "localhost"
}
```

---

## 6. 실무 예제: 제품 관리 시스템

### 6.1 단일 제품 관리

```python
# 제품 정보 생성
product = {
    "product_name": "노트북",
    "price": 1200000,
    "stock": 5,
    "category": "전자제품"
}

# 제품 정보 출력
print("=" * 50)
print("제품 정보")
print("=" * 50)
print(f"상품명: {product['product_name']}")
print(f"가격: {product['price']:,}원")
print(f"재고: {product['stock']}개")
print(f"카테고리: {product['category']}")

# 재고 판매
product["stock"] -= 1
print(f"\n판매 후 재고: {product['stock']}개")

# 가격 인하
discount_rate = 0.1  # 10% 할인
product["price"] = int(product["price"] * (1 - discount_rate))
print(f"할인 후 가격: {product['price']:,}원")
```

### 6.2 여러 제품 관리 (리스트 + 딕셔너리)

```python
# 제품 목록
products = [
    {"product_name": "노트북", "price": 1200000, "stock": 5},
    {"product_name": "마우스", "price": 30000, "stock": 20},
    {"product_name": "키보드", "price": 80000, "stock": 15},
    {"product_name": "모니터", "price": 300000, "stock": 8}
]

# 전체 제품 목록 출력
print("=" * 60)
print(" " * 20 + "제품 목록")
print("=" * 60)
print(f"{'상품명':<10} {'가격':>12} {'재고':>8}")
print("-" * 60)

for product in products:
    print(f"{product['product_name']:<10} {product['price']:>10,}원 {product['stock']:>6}개")

# 총 재고 가치 계산
total_value = sum(p['price'] * p['stock'] for p in products)
print("-" * 60)
print(f"총 재고 가치: {total_value:,}원")
```

### 6.3 제품 조회 프로그램

```python
def find_product(products, product_name):
    """
    제품명으로 제품을 찾는 함수
    
    Args:
        products: 제품 리스트
        product_name: 찾을 제품명
    
    Returns:
        찾은 제품 딕셔너리 또는 None
    """
    for product in products:
        if product["product_name"] == product_name:
            return product
    return None


# 제품 목록
products = [
    {"product_name": "노트북", "price": 1200000, "stock": 5},
    {"product_name": "마우스", "price": 30000, "stock": 20},
    {"product_name": "키보드", "price": 80000, "stock": 15}
]

# 제품 검색
search_name = "노트북"
found = find_product(products, search_name)

if found:
    print(f"제품을 찾았습니다!")
    print(f"상품명: {found['product_name']}")
    print(f"가격: {found['price']:,}원")
    print(f"재고: {found['stock']}개")
else:
    print(f"'{search_name}' 제품을 찾을 수 없습니다.")
```

### 6.4 제품 판매 시스템

```python
def sell_product(products, product_name, quantity):
    """
    제품을 판매하는 함수
    
    Args:
        products: 제품 리스트
        product_name: 판매할 제품명
        quantity: 판매 수량
    
    Returns:
        성공 여부와 메시지
    """
    # 제품 찾기
    for product in products:
        if product["product_name"] == product_name:
            # 재고 확인
            if product["stock"] >= quantity:
                product["stock"] -= quantity
                total_price = product["price"] * quantity
                return True, f"판매 완료! 총액: {total_price:,}원"
            else:
                return False, f"재고 부족! (현재 재고: {product['stock']}개)"
    
    return False, "제품을 찾을 수 없습니다."


# 제품 목록
products = [
    {"product_name": "노트북", "price": 1200000, "stock": 5},
    {"product_name": "마우스", "price": 30000, "stock": 20}
]

# 판매 시도
success, message = sell_product(products, "노트북", 2)
print(message)

if success:
    # 재고 확인
    for product in products:
        if product["product_name"] == "노트북":
            print(f"남은 재고: {product['stock']}개")
```

---

## 📝 정리

### 핵심 개념

1. **딕셔너리**는 Key-Value 구조로 데이터를 저장합니다
2. **Key**로 빠르게 값을 찾을 수 있습니다
3. `[]` 또는 `get()`으로 값을 **조회**합니다
4. `dict[key] = value`로 값을 **추가/수정**합니다
5. `del dict[key]`로 값을 **삭제**합니다
6. **리스트와 딕셔너리를 조합**하여 복잡한 데이터를 관리합니다

### 자주 사용하는 코드 패턴

```python
# 딕셔너리 생성
person = {"name": "홍길동", "age": 25}

# 값 조회
name = person.get("name", "이름 없음")

# 값 추가/수정
person["city"] = "서울"

# 값 삭제
del person["age"]

# 반복문
for key, value in person.items():
    print(f"{key}: {value}")

# 리스트 + 딕셔너리
products = [
    {"name": "상품1", "price": 1000},
    {"name": "상품2", "price": 2000}
]
```

### 리스트 vs 튜플 vs 딕셔너리 선택 가이드

```
데이터에 순서가 중요한가?
├─ Yes → 리스트 또는 튜플
│   └─ 데이터가 변경되는가?
│       ├─ Yes → 리스트
│       └─ No → 튜플
└─ No → 딕셔너리
    └─ 이름으로 데이터를 찾는가?
        └─ Yes → 딕셔너리
```

---

## 🎯 다음 단계

딕셔너리를 마스터했다면, 다음 단계로 진행하세요:

1. **조건문 (if/elif/else)**: 데이터를 기반으로 의사결정
2. **반복문 (for/while)**: 딕셔너리와 리스트를 순회하며 작업
3. **함수**: 딕셔너리를 매개변수로 받아 처리하는 함수 작성

**잘하셨습니다! 🎉**

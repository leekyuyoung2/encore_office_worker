# 직장인을 위한 파이썬 완성 강의 (7교시)

---

# 📘 1교시: 함수(Function)의 정의 및 호출 / 원화→달러 환율 함수 만들기

---

## 1) 이론 설명

### 함수란 무엇인가?

**함수(Function)**는 특정 작업을 수행하는 코드 묶음입니다. 마치 회사에서 사용하는 "업무 매뉴얼"과 같습니다. 

**직장인 예시로 이해하기:**
- 회사에서 "출장비 정산" 업무를 할 때마다 같은 절차를 반복합니다
- 영수증 모으기 → 엑셀에 입력 → 합계 계산 → 결재 요청
- 이 절차를 매번 처음부터 다시 생각하지 않고, "출장비 정산 매뉴얼"을 따르면 됩니다
- **함수도 마찬가지입니다!** 자주 사용하는 코드를 함수로 만들어두면, 필요할 때마다 간단히 호출만 하면 됩니다

### 함수를 사용하는 이유

1. **코드 재사용**: 같은 코드를 여러 번 작성하지 않아도 됩니다
2. **유지보수 용이**: 수정이 필요하면 함수 한 곳만 고치면 됩니다
3. **가독성 향상**: 복잡한 코드를 의미 있는 이름의 함수로 나눌 수 있습니다
4. **협업 효율**: 동료가 내가 만든 함수를 쉽게 사용할 수 있습니다

### 함수의 기본 구조

```python
def 함수이름(매개변수1, 매개변수2):
    """함수 설명 (docstring)"""
    # 실행할 코드
    결과 = 매개변수1 + 매개변수2
    return 결과  # 결과값 반환
```

**구성 요소:**
- `def`: 함수를 정의한다는 키워드 (define의 약자)
- `함수이름`: 함수의 이름 (스네이크 케이스 사용 권장)
- `매개변수`: 함수에 전달하는 입력값
- `return`: 함수의 결과값을 반환
- `docstring`: 함수 설명 (선택사항이지만 권장)

### 함수 호출하기

```python
결과값 = 함수이름(인자1, 인자2)
```

- **인자(argument)**: 함수를 호출할 때 실제로 전달하는 값

### 매개변수와 반환값

**매개변수(Parameter)가 없는 함수:**
```python
def say_hello():
    print("안녕하세요!")
    
say_hello()  # 출력: 안녕하세요!
```

**반환값(Return)이 없는 함수:**
```python
def greet(name):
    print(f"{name}님, 환영합니다!")
    # return이 없으면 None을 반환
    
greet("홍길동")  # 출력: 홍길동님, 환영합니다!
```

**매개변수와 반환값이 모두 있는 함수:**
```python
def add(a, b):
    return a + b
    
result = add(10, 20)  # result = 30
```

---

## 2) 실습 예제 코드

### 예제 1: 기본 함수 만들기

```python
# 인사 함수 - 매개변수 없음, 반환값 없음
def greet():
    """간단한 인사말을 출력하는 함수"""
    print("안녕하세요! 좋은 하루 되세요!")

# 함수 호출
greet()  # 출력: 안녕하세요! 좋은 하루 되세요!
```

### 예제 2: 매개변수가 있는 함수

```python
# 직원 정보 출력 함수
def print_employee_info(name, department, position):
    """직원 정보를 출력하는 함수
    
    Args:
        name: 직원 이름
        department: 부서명
        position: 직급
    """
    print(f"이름: {name}")
    print(f"부서: {department}")
    print(f"직급: {position}")

# 함수 호출
print_employee_info("김철수", "영업팀", "대리")
# 출력:
# 이름: 김철수
# 부서: 영업팀
# 직급: 대리
```

### 예제 3: 반환값이 있는 함수

```python
# 월급 계산 함수
def calculate_monthly_salary(annual_salary):
    """연봉을 월급으로 변환하는 함수
    
    Args:
        annual_salary: 연봉 (원)
    
    Returns:
        월급 (원)
    """
    monthly_salary = annual_salary / 12
    return monthly_salary

# 함수 호출 및 결과 저장
연봉 = 36000000  # 3천6백만원
월급 = calculate_monthly_salary(연봉)
print(f"연봉 {연봉:,}원의 월급: {월급:,.0f}원")
# 출력: 연봉 36,000,000원의 월급: 3,000,000원
```

### 예제 4: 원화를 달러로 환전하는 함수 (핵심 예제)

```python
# 원화를 달러로 환전하는 함수
def krw_to_usd(krw_amount, exchange_rate=1300):
    """원화를 달러로 환전하는 함수
    
    Args:
        krw_amount: 원화 금액
        exchange_rate: 환율 (기본값 1300원, 생략 가능)
    
    Returns:
        달러 금액
    """
    usd_amount = krw_amount / exchange_rate
    return usd_amount

# 사용 예시 1: 환율 지정하지 않음 (기본값 1300 사용)
원화 = 130000
달러 = krw_to_usd(원화)
print(f"{원화:,}원 = ${달러:.2f}")
# 출력: 130,000원 = $100.00

# 사용 예시 2: 환율 직접 지정
원화 = 260000
환율 = 1350
달러 = krw_to_usd(원화, 환율)
print(f"{원화:,}원 = ${달러:.2f} (환율: {환율}원)")
# 출력: 260,000원 = $192.59 (환율: 1350원)
```

### 예제 5: 달러를 원화로 환전하는 함수 (역방향)

```python
# 달러를 원화로 환전하는 함수
def usd_to_krw(usd_amount, exchange_rate=1300):
    """달러를 원화로 환전하는 함수
    
    Args:
        usd_amount: 달러 금액
        exchange_rate: 환율 (기본값 1300원)
    
    Returns:
        원화 금액
    """
    krw_amount = usd_amount * exchange_rate
    return krw_amount

# 사용 예시
달러 = 500
원화 = usd_to_krw(달러)
print(f"${달러} = {원화:,.0f}원")
# 출력: $500 = 650,000원
```

### 예제 6: 여러 값을 반환하는 함수

```python
# 환전 정보를 한 번에 계산하는 함수
def currency_exchange(krw_amount, exchange_rate=1300):
    """원화→달러 환전 시 상세 정보를 반환
    
    Args:
        krw_amount: 원화 금액
        exchange_rate: 환율
    
    Returns:
        tuple: (달러 금액, 수수료, 실제 받는 달러)
    """
    usd_amount = krw_amount / exchange_rate
    fee = usd_amount * 0.02  # 2% 수수료
    actual_usd = usd_amount - fee
    
    return usd_amount, fee, actual_usd

# 사용 예시
원화 = 1000000
달러, 수수료, 실제달러 = currency_exchange(원화)

print(f"환전 금액: {원화:,}원")
print(f"환전 달러: ${달러:.2f}")
print(f"수수료(2%): ${수수료:.2f}")
print(f"실제 수령: ${실제달러:.2f}")
# 출력:
# 환전 금액: 1,000,000원
# 환전 달러: $769.23
# 수수료(2%): $15.38
# 실제 수령: $753.85
```

---

## 3) 코드 상세 설명

### 함수 정의 단계별 설명

```python
def krw_to_usd(krw_amount, exchange_rate=1300):
    """원화를 달러로 환전하는 함수"""
    usd_amount = krw_amount / exchange_rate
    return usd_amount
```

**1단계: 함수 선언**
- `def krw_to_usd(...)`: "krw_to_usd"라는 이름의 함수를 정의합니다
- 함수명은 소문자와 언더스코어(_)로 작성 (스네이크 케이스)

**2단계: 매개변수 설정**
- `krw_amount`: 원화 금액 (필수 매개변수)
- `exchange_rate=1300`: 환율 (기본값이 있는 선택 매개변수)
- 기본값이 있으면 함수 호출 시 생략 가능

**3단계: 함수 본문 (실행 코드)**
- `usd_amount = krw_amount / exchange_rate`
- 원화를 환율로 나누어 달러로 계산

**4단계: 반환값**
- `return usd_amount`
- 계산된 달러 금액을 함수 밖으로 반환
- `return`을 만나면 함수 실행이 종료됩니다

### 함수 호출 과정

```python
result = krw_to_usd(130000, 1300)
```

1. `krw_to_usd` 함수를 찾습니다
2. `krw_amount`에 130000을 대입
3. `exchange_rate`에 1300을 대입
4. 함수 내부 코드 실행: `usd_amount = 130000 / 1300 = 100.0`
5. `return 100.0` 으로 결과 반환
6. `result` 변수에 100.0이 저장됨

### 기본값(Default Value) 활용

```python
def krw_to_usd(krw_amount, exchange_rate=1300):
    ...
```

- `exchange_rate=1300`은 기본값 설정
- 호출 시 환율을 지정하지 않으면 자동으로 1300 사용

```python
# 환율 생략 → 기본값 1300 사용
krw_to_usd(130000)

# 환율 명시 → 1350 사용
krw_to_usd(130000, 1350)
```

### 여러 값 반환 (Tuple Unpacking)

```python
def currency_exchange(krw_amount, exchange_rate=1300):
    usd_amount = krw_amount / exchange_rate
    fee = usd_amount * 0.02
    actual_usd = usd_amount - fee
    return usd_amount, fee, actual_usd  # 3개 값을 튜플로 반환
```

**반환 과정:**
- 여러 값을 쉼표로 구분하면 자동으로 튜플(tuple)로 묶임
- `return (usd_amount, fee, actual_usd)`와 동일

**받기 과정:**
```python
달러, 수수료, 실제달러 = currency_exchange(1000000)
```
- 튜플의 각 요소가 순서대로 변수에 할당됨 (언패킹)

---

## 4) 실습 미션

### 미션 1: 기본 함수 만들기 ⭐
**목표:** 직원 출퇴근 시간을 출력하는 함수를 작성하세요.

**요구사항:**
- 함수명: `print_work_hours`
- 매개변수: `start_time` (출근 시간), `end_time` (퇴근 시간)
- 출력 형식: "출근: 09:00, 퇴근: 18:00"

**예상 출력:**
```
출근: 09:00, 퇴근: 18:00
```

---

### 미션 2: 근무 시간 계산 함수 ⭐⭐
**목표:** 출퇴근 시간을 입력받아 총 근무 시간을 계산하는 함수를 작성하세요.

**요구사항:**
- 함수명: `calculate_work_hours`
- 매개변수: `start_hour` (출근 시각, 정수), `end_hour` (퇴근 시각, 정수)
- 점심시간 1시간 자동 제외
- 반환값: 실제 근무 시간

**예시:**
```python
hours = calculate_work_hours(9, 18)  # 9시 출근, 18시 퇴근
print(f"근무 시간: {hours}시간")  # 출력: 근무 시간: 8시간
```

---

### 미션 3: 환율 계산기 업그레이드 ⭐⭐⭐
**목표:** 원화를 여러 통화로 환전하는 함수를 작성하세요.

**요구사항:**
- 함수명: `convert_currency`
- 매개변수: 
  - `krw_amount`: 원화 금액
  - `currency`: 통화 종류 ("USD", "JPY", "EUR" 중 하나)
- 환율 정보:
  - USD: 1300원
  - JPY: 900원 (100엔 기준)
  - EUR: 1400원
- 반환값: 환전된 금액

**예시:**
```python
usd = convert_currency(130000, "USD")
print(f"${usd:.2f}")  # $100.00

jpy = convert_currency(90000, "JPY")
print(f"¥{jpy:.0f}")  # ¥10000

eur = convert_currency(140000, "EUR")
print(f"€{eur:.2f}")  # €100.00
```

---

### 미션 4: 왕복 환전 손실 계산 ⭐⭐⭐
**목표:** 원화→달러→원화로 환전 시 수수료로 인한 손실을 계산하세요.

**요구사항:**
- 함수명: `calculate_exchange_loss`
- 매개변수: `krw_amount` (초기 원화 금액)
- 환율: 1달러 = 1300원 (고정)
- 수수료: 왕복 각 2% (총 2번 수수료 부과)
- 반환값: (최종 원화, 손실액)

**계산 과정:**
1. 원화 → 달러 환전 (2% 수수료)
2. 달러 → 원화 환전 (2% 수수료)
3. 최종 원화와 손실액 반환

**예시:**
```python
final, loss = calculate_exchange_loss(1000000)
print(f"초기: 1,000,000원")
print(f"최종: {final:,.0f}원")
print(f"손실: {loss:,.0f}원")
```

---

## 5) 퀴즈

### 퀴즈 1 (기본 개념) 📝
다음 중 함수를 정의할 때 사용하는 키워드는?

**A)** `func`  
**B)** `define`  
**C)** `def`  
**D)** `function`

---

### 퀴즈 2 (매개변수와 반환값) 📝
다음 함수의 실행 결과는?

```python
def multiply(a, b=10):
    return a * b

result = multiply(5)
print(result)
```

**A)** 5  
**B)** 10  
**C)** 50  
**D)** 에러 발생

---

### 퀴즈 3 (응용 문제) 📝
다음 코드의 출력 결과는?

```python
def discount_price(price, rate=0.1):
    discount = price * rate
    final_price = price - discount
    return final_price

item_price = 50000
result = discount_price(item_price, 0.2)
print(f"{result:,.0f}원")
```

**A)** 5,000원  
**B)** 10,000원  
**C)** 40,000원  
**D)** 45,000원

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **C) def**

**해설:**
- Python에서 함수를 정의할 때는 `def` 키워드를 사용합니다
- `def`는 "define"의 약자입니다
- 문법: `def 함수이름(매개변수):`

**예시:**
```python
def my_function():
    print("Hello!")
```

---

### 퀴즈 2 정답: **C) 50**

**해설:**
- 함수 정의: `def multiply(a, b=10)`
- `b=10`은 기본값(default value)입니다
- `multiply(5)` 호출 시:
  - `a = 5`
  - `b = 10` (기본값 사용)
  - `return 5 * 10 = 50`

**기본값의 특징:**
- 매개변수를 생략하면 기본값이 자동으로 사용됩니다
- `multiply(5, 20)`처럼 값을 지정하면 기본값 대신 지정한 값 사용

---

### 퀴즈 3 정답: **C) 40,000원**

**해설:**

**단계별 계산:**
1. 함수 호출: `discount_price(50000, 0.2)`
   - `price = 50000`
   - `rate = 0.2` (20% 할인)

2. 함수 내부 실행:
   - `discount = 50000 * 0.2 = 10000`
   - `final_price = 50000 - 10000 = 40000`
   - `return 40000`

3. 출력: `40,000원`

**포인트:**
- 원가 50,000원에서 20% 할인 → 10,000원 할인
- 최종 가격 = 50,000 - 10,000 = 40,000원

---

## 💡 1교시 핵심 요약

### 함수의 4가지 핵심 요소
1. **정의**: `def` 키워드로 시작
2. **매개변수**: 함수에 전달할 입력값
3. **실행 코드**: 함수가 수행할 작업
4. **반환값**: `return`으로 결과를 돌려줌

### 실무 활용 팁
✅ 함수명은 동사로 시작하면 이해하기 쉽습니다
   - `calculate_salary()` ⭐ (좋음)
   - `salary()` ❌ (애매함)

✅ 하나의 함수는 하나의 기능만 수행
   - 함수가 너무 길면 여러 개로 나누기

✅ 기본값 활용으로 편의성 향상
   - 자주 사용하는 값은 기본값으로 설정

✅ docstring으로 함수 설명 작성
   - 나중에 다시 봐도 이해하기 쉬움

---

## 🎯 다음 교시 예고

**2교시: 텍스트(.txt) 파일 입출력**
- 파일 읽기/쓰기 기본
- `open()`, `read()`, `write()` 함수
- `with` 문을 활용한 안전한 파일 처리
- **실습 프로젝트:** 오늘의 목표 자동 기록 프로그램

---

**1교시를 완료하셨습니다! 수고하셨습니다! 🎉**

"다음 교시"를 입력하시면 2교시 내용을 시작하겠습니다.

---
---

# 📘 2교시: 텍스트(.txt) 파일 입출력 / 오늘의 목표 자동 기록 프로그램

---

## 1) 이론 설명

### 파일 입출력이란?

**파일 입출력(File I/O)**은 프로그램에서 파일을 읽고 쓰는 작업입니다. 직장에서 문서를 작성하고 저장하는 것과 같습니다.

**직장인 예시로 이해하기:**
- 회의록을 작성하고 파일로 저장 → **파일 쓰기 (Write)**
- 저장된 회의록을 다시 열어서 확인 → **파일 읽기 (Read)**
- 회의록에 추가 내용 작성 → **파일 추가 (Append)**

**왜 파일 입출력이 중요한가?**
- 데이터를 영구적으로 보관할 수 있습니다
- 프로그램을 종료해도 데이터가 사라지지 않습니다
- 다른 프로그램과 데이터를 공유할 수 있습니다

### 파일 열기: open() 함수

```python
파일객체 = open(파일경로, 모드, encoding='utf-8')
```

**주요 모드:**
- `'r'` (read): 읽기 모드 - 파일을 읽기만 함
- `'w'` (write): 쓰기 모드 - 새로 쓰기 (기존 내용 삭제)
- `'a'` (append): 추가 모드 - 파일 끝에 내용 추가
- `'r+'`: 읽기+쓰기 모드

**encoding 파라미터:**
- `encoding='utf-8'`: 한글이 깨지지 않도록 UTF-8 인코딩 지정
- Windows에서 한글 파일 다룰 때 필수!

### 파일 닫기: close() 메서드

```python
파일객체.close()
```

**왜 파일을 닫아야 하나?**
- 파일을 열어두면 메모리 낭비
- 다른 프로그램이 파일을 사용할 수 없음
- 데이터 손실 방지

### with 문: 자동으로 파일 닫기

```python
with open('파일.txt', 'r', encoding='utf-8') as f:
    내용 = f.read()
# with 블록을 벗어나면 자동으로 파일이 닫힘
```

**장점:**
- 파일을 자동으로 닫아주므로 안전
- close()를 잊어버릴 걱정 없음
- 에러가 발생해도 파일이 제대로 닫힘

### 파일 읽기 메서드

**1. read() - 전체 읽기**
```python
내용 = f.read()  # 파일 전체를 문자열로 읽음
```

**2. readline() - 한 줄씩 읽기**
```python
줄 = f.readline()  # 한 줄만 읽음
```

**3. readlines() - 모든 줄을 리스트로**
```python
줄들 = f.readlines()  # 각 줄이 리스트의 요소가 됨
```

### 파일 쓰기 메서드

**1. write() - 문자열 쓰기**
```python
f.write("안녕하세요\n")  # \n을 직접 추가해야 줄바꿈
```

**2. writelines() - 여러 줄 쓰기**
```python
줄들 = ["첫 번째 줄\n", "두 번째 줄\n"]
f.writelines(줄들)
```

---

## 2) 실습 예제 코드

### 예제 1: 파일 쓰기 기본 (write 모드)

```python
# 파일에 텍스트 쓰기
# 'w' 모드는 파일이 없으면 생성하고, 있으면 내용을 지우고 새로 씀

# 방법 1: 수동으로 close()
file = open('greetings.txt', 'w', encoding='utf-8')
file.write("안녕하세요!\n")
file.write("파이썬으로 파일을 작성합니다.\n")
file.close()

print("✅ greetings.txt 파일이 생성되었습니다.")
```

### 예제 2: with 문을 사용한 안전한 파일 쓰기

```python
# with 문 사용 (권장 방법)
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write("=== 업무 보고서 ===\n")
    f.write("날짜: 2024년 10월 25일\n")
    f.write("작성자: 홍길동\n")
    f.write("\n")
    f.write("오늘의 업무:\n")
    f.write("1. 고객 미팅\n")
    f.write("2. 프로젝트 진행 상황 점검\n")
    f.write("3. 주간 보고서 작성\n")

# with 블록이 끝나면 자동으로 파일이 닫힘
print("✅ report.txt 파일이 생성되었습니다.")
```

### 예제 3: 파일 읽기 - read()로 전체 읽기

```python
# 파일 전체 내용을 한 번에 읽기
with open('report.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("📄 파일 내용:")
    print(content)

# 출력:
# 📄 파일 내용:
# === 업무 보고서 ===
# 날짜: 2024년 10월 25일
# 작성자: 홍길동
# 
# 오늘의 업무:
# 1. 고객 미팅
# 2. 프로젝트 진행 상황 점검
# 3. 주간 보고서 작성
```

### 예제 4: 파일 읽기 - readline()으로 한 줄씩 읽기

```python
# 한 줄씩 읽기
with open('report.txt', 'r', encoding='utf-8') as f:
    print("📄 첫 세 줄만 읽기:")
    line1 = f.readline()  # 첫 번째 줄
    line2 = f.readline()  # 두 번째 줄
    line3 = f.readline()  # 세 번째 줄
    
    print(line1.strip())  # strip()으로 양쪽 공백 제거
    print(line2.strip())
    print(line3.strip())

# 출력:
# 📄 첫 세 줄만 읽기:
# === 업무 보고서 ===
# 날짜: 2024년 10월 25일
# 작성자: 홍길동
```

### 예제 5: 파일 읽기 - readlines()로 모든 줄을 리스트로

```python
# 모든 줄을 리스트로 읽기
with open('report.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
    print(f"📄 총 {len(lines)}줄입니다.")
    print("\n각 줄 출력:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")

# 출력:
# 📄 총 8줄입니다.
# 
# 각 줄 출력:
# 1. === 업무 보고서 ===
# 2. 날짜: 2024년 10월 25일
# 3. 작성자: 홍길동
# 4. 
# 5. 오늘의 업무:
# 6. 1. 고객 미팅
# 7. 2. 프로젝트 진행 상황 점검
# 8. 3. 주간 보고서 작성
```

### 예제 6: 파일 추가 (append 모드)

```python
# 기존 파일에 내용 추가하기
with open('report.txt', 'a', encoding='utf-8') as f:
    f.write("\n")
    f.write("=== 추가 사항 ===\n")
    f.write("- 내일 고객사 방문 예정\n")
    f.write("- 제안서 준비 필요\n")

print("✅ 파일에 내용이 추가되었습니다.")

# 추가된 내용 확인
with open('report.txt', 'r', encoding='utf-8') as f:
    print("\n📄 업데이트된 파일 내용:")
    print(f.read())
```

### 예제 7: 오늘의 목표 기록 프로그램 (핵심 예제)

```python
import datetime

def save_daily_goal():
    """오늘의 목표를 파일에 저장하는 프로그램"""
    
    # 오늘 날짜 가져오기
    today = datetime.date.today()
    date_str = today.strftime("%Y년 %m월 %d일")
    
    # 사용자로부터 목표 입력받기
    print(f"📅 {date_str}")
    print("오늘의 목표를 입력하세요 (완료하려면 빈 줄 입력):")
    
    goals = []
    goal_num = 1
    
    while True:
        goal = input(f"{goal_num}. ")
        if goal == "":  # 빈 줄이면 종료
            break
        goals.append(f"{goal_num}. {goal}\n")
        goal_num += 1
    
    # 파일명: goals_2024-10-25.txt 형식
    filename = f"goals_{today}.txt"
    
    # 파일에 저장
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"=== {date_str} 목표 ===\n")
        f.write("\n")
        f.writelines(goals)
        f.write("\n")
        f.write("화이팅! 💪\n")
    
    print(f"\n✅ '{filename}' 파일에 목표가 저장되었습니다!")
    
    # 저장된 내용 확인
    with open(filename, 'r', encoding='utf-8') as f:
        print("\n📄 저장된 내용:")
        print(f.read())

# 프로그램 실행 예시:
# save_daily_goal()

# 실행 예시:
# 📅 2024년 10월 25일
# 오늘의 목표를 입력하세요 (완료하려면 빈 줄 입력):
# 1. 보고서 작성 완료하기
# 2. 고객 미팅 준비
# 3. 이메일 답장 보내기
# 4. [엔터]
# 
# ✅ 'goals_2024-10-25.txt' 파일에 목표가 저장되었습니다!
```

### 예제 8: 목표 달성 체크 프로그램

```python
def check_goals(filename):
    """저장된 목표를 불러와서 달성 여부를 체크하는 프로그램"""
    
    try:
        # 파일 읽기
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print("📄 저장된 목표:")
        for line in lines:
            print(line.strip())
        
        print("\n" + "="*40)
        print("달성한 목표 앞에 체크 표시를 입력하세요 (완료: O, 미완료: X)")
        print("="*40 + "\n")
        
        # 목표만 추출 (숫자로 시작하는 줄)
        goals = [line for line in lines if line.strip() and line.strip()[0].isdigit()]
        
        checked_goals = []
        for goal in goals:
            check = input(f"{goal.strip()} -> ")
            if check.upper() == 'O':
                checked_goals.append(f"✅ {goal}")
            else:
                checked_goals.append(f"❌ {goal}")
        
        # 결과 파일에 저장
        result_filename = filename.replace('.txt', '_결과.txt')
        with open(result_filename, 'w', encoding='utf-8') as f:
            f.write("=== 목표 달성 결과 ===\n\n")
            f.writelines(checked_goals)
            
            completed = sum(1 for g in checked_goals if '✅' in g)
            total = len(checked_goals)
            f.write(f"\n달성률: {completed}/{total} ({completed/total*100:.0f}%)\n")
        
        print(f"\n✅ 결과가 '{result_filename}'에 저장되었습니다!")
        
    except FileNotFoundError:
        print(f"❌ '{filename}' 파일을 찾을 수 없습니다.")

# 사용 예시:
# check_goals('goals_2024-10-25.txt')
```

---

## 3) 코드 상세 설명

### open() 함수의 동작 원리

```python
file = open('example.txt', 'w', encoding='utf-8')
```

**단계별 설명:**
1. `'example.txt'`: 파일 경로 (현재 디렉토리에 생성)
2. `'w'`: 쓰기 모드 
   - 파일이 없으면 새로 생성
   - 파일이 있으면 기존 내용 삭제하고 새로 씀
3. `encoding='utf-8'`: 한글 등 유니코드 문자를 올바르게 처리
4. 반환값: 파일 객체 (파일을 제어할 수 있는 객체)

### with 문의 동작 원리

```python
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 여기서 파일이 자동으로 닫힘
```

**장점:**
- **자동 정리**: with 블록을 벗어날 때 자동으로 `f.close()` 호출
- **예외 안전**: 에러가 발생해도 파일이 확실히 닫힘
- **메모리 효율**: 파일 핸들을 빨리 해제하여 메모리 절약

**일반 방식과 비교:**
```python
# 일반 방식 (권장하지 않음)
f = open('file.txt', 'r', encoding='utf-8')
try:
    content = f.read()
finally:
    f.close()  # 반드시 닫아야 함

# with 문 (권장)
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 자동으로 닫힘!
```

### 파일 모드별 동작 차이

| 모드 | 설명 | 파일이 없을 때 | 파일이 있을 때 |
|------|------|---------------|---------------|
| `'r'` | 읽기 | 에러 발생 | 읽기만 가능 |
| `'w'` | 쓰기 | 새로 생성 | 기존 내용 삭제 |
| `'a'` | 추가 | 새로 생성 | 끝에 추가 |
| `'r+'` | 읽기+쓰기 | 에러 발생 | 읽기/쓰기 가능 |

**실무 팁:**
- 로그 파일: `'a'` 모드 사용 (계속 추가)
- 설정 파일 읽기: `'r'` 모드
- 보고서 생성: `'w'` 모드 (매번 새로 작성)

### read() vs readline() vs readlines()

```python
# 파일 내용:
# Line 1
# Line 2
# Line 3

# read() - 전체를 하나의 문자열로
content = f.read()
# 결과: "Line 1\nLine 2\nLine 3"

# readline() - 한 줄씩
line = f.readline()  # "Line 1\n"
line = f.readline()  # "Line 2\n"

# readlines() - 모든 줄을 리스트로
lines = f.readlines()
# 결과: ["Line 1\n", "Line 2\n", "Line 3"]
```

**선택 기준:**
- 파일이 작고 전체를 처리: `read()`
- 파일이 크고 한 줄씩 처리: `readline()` 또는 `for line in f:`
- 모든 줄을 리스트로 필요: `readlines()`

### strip() 메서드의 중요성

```python
# readlines()로 읽으면 각 줄에 \n이 포함됨
lines = f.readlines()  # ["안녕하세요\n", "반갑습니다\n"]

# strip()으로 양쪽 공백과 \n 제거
for line in lines:
    print(line.strip())  # "안녕하세요", "반갑습니다"
```

**strip() 변형:**
- `strip()`: 양쪽 공백/줄바꿈 제거
- `lstrip()`: 왼쪽만 제거
- `rstrip()`: 오른쪽만 제거

---

## 4) 실습 미션

### 미션 1: 직원 명단 저장 ⭐
**목표:** 직원 정보를 파일에 저장하는 프로그램을 작성하세요.

**요구사항:**
- 파일명: `employees.txt`
- 저장 내용:
  ```
  === 직원 명단 ===
  1. 홍길동 - 영업팀 - 대리
  2. 김철수 - 개발팀 - 과장
  3. 이영희 - 인사팀 - 사원
  ```
- `with` 문 사용
- `encoding='utf-8'` 지정

---

### 미션 2: 파일 읽고 특정 줄 출력 ⭐⭐
**목표:** employees.txt 파일을 읽어서 "개발팀" 직원만 출력하세요.

**요구사항:**
- 파일을 한 줄씩 읽기
- "개발팀"이 포함된 줄만 출력
- 결과 예시: `2. 김철수 - 개발팀 - 과장`

**힌트:**
```python
if "개발팀" in line:
    print(line.strip())
```

---

### 미션 3: 출퇴근 기록 프로그램 ⭐⭐⭐
**목표:** 매일 출퇴근 시간을 기록하고 조회하는 프로그램을 작성하세요.

**요구사항:**
- 함수 1: `record_attendance(name, time_in, time_out)`
  - 파일명: `attendance.txt`
  - 추가 모드('a')로 기록
  - 형식: `2024-10-25, 홍길동, 09:00, 18:00`
  
- 함수 2: `view_attendance()`
  - attendance.txt 파일 전체 내용 출력
  
**예시:**
```python
record_attendance("홍길동", "09:00", "18:00")
record_attendance("김철수", "08:50", "17:30")
view_attendance()
```

**출력:**
```
=== 출퇴근 기록 ===
2024-10-25, 홍길동, 09:00, 18:00
2024-10-25, 김철수, 08:50, 17:30
```

---

### 미션 4: 회의록 자동 작성기 ⭐⭐⭐
**목표:** 회의 내용을 입력받아 정형화된 회의록 파일을 생성하세요.

**요구사항:**
- 입력 정보: 회의 제목, 날짜, 참석자, 안건 (여러 개)
- 파일명: `meeting_YYYYMMDD.txt` 형식
- 출력 형식:
  ```
  ==================
  회의록
  ==================
  제목: [회의 제목]
  날짜: [날짜]
  참석자: [참석자 명단]
  
  안건:
  1. [안건1]
  2. [안건2]
  ...
  ==================
  ```

**힌트:**
- `input()`으로 사용자 입력받기
- 안건은 while 문으로 여러 개 입력받기
- f-string으로 파일명 생성

---

## 5) 퀴즈

### 퀴즈 1 (파일 모드) 📝
다음 중 기존 파일에 내용을 추가하고 싶을 때 사용하는 모드는?

**A)** `'r'`  
**B)** `'w'`  
**C)** `'a'`  
**D)** `'x'`

---

### 퀴즈 2 (파일 읽기) 📝
다음 코드의 실행 결과는?

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("Hello\n")
    f.write("World\n")

with open('test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(len(lines))
```

**A)** 1  
**B)** 2  
**C)** 10  
**D)** 에러 발생

---

### 퀴즈 3 (응용 문제) 📝
다음 코드의 실행 후 `data.txt` 파일의 최종 내용은?

```python
# 첫 번째 쓰기
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("First\n")

# 두 번째 쓰기
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Second\n")

# 세 번째 추가
with open('data.txt', 'a', encoding='utf-8') as f:
    f.write("Third\n")
```

**A)** First  
**B)** Second  
**C)** Second<br>Third  
**D)** First<br>Second<br>Third

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **C) 'a'**

**해설:**
- `'r'` (read): 읽기 전용 - 파일 수정 불가
- `'w'` (write): 쓰기 모드 - **기존 내용을 모두 삭제**하고 새로 씀
- `'a'` (append): **추가 모드 - 기존 내용 유지하고 끝에 추가** ✅
- `'x'`: 배타적 생성 - 파일이 이미 존재하면 에러

**실무 활용:**
```python
# 로그 파일에 계속 기록할 때
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write("2024-10-25 10:30 - 사용자 로그인\n")
```

---

### 퀴즈 2 정답: **B) 2**

**해설:**

**단계별 실행:**
1. 파일 쓰기:
   ```python
   f.write("Hello\n")  # 첫 번째 줄
   f.write("World\n")  # 두 번째 줄
   ```

2. 파일 읽기:
   ```python
   lines = f.readlines()
   # 결과: ["Hello\n", "World\n"]
   ```

3. 줄 개수:
   ```python
   print(len(lines))  # 2
   ```

**포인트:**
- `readlines()`는 각 줄을 리스트의 요소로 반환
- `\n`(줄바꿈)으로 구분하여 2개의 요소가 생성됨

---

### 퀴즈 3 정답: **C) Second<br>Third**

**해설:**

**단계별 실행:**

1. **첫 번째 쓰기** (`'w'` 모드):
   ```python
   with open('data.txt', 'w', encoding='utf-8') as f:
       f.write("First\n")
   ```
   파일 내용: `First`

2. **두 번째 쓰기** (`'w'` 모드):
   ```python
   with open('data.txt', 'w', encoding='utf-8') as f:
       f.write("Second\n")
   ```
   파일 내용: `Second` (First가 삭제됨!)

3. **세 번째 추가** (`'a'` 모드):
   ```python
   with open('data.txt', 'a', encoding='utf-8') as f:
       f.write("Third\n")
   ```
   파일 내용: `Second\nThird` (Second 뒤에 추가)

**최종 파일 내용:**
```
Second
Third
```

**주의사항:**
- `'w'` 모드는 파일을 열 때 기존 내용을 **모두 삭제**합니다
- 기존 내용을 보존하려면 `'a'` 모드를 사용해야 합니다

---

## 💡 2교시 핵심 요약

### 파일 입출력 3단계
1. **열기**: `open(파일명, 모드, encoding='utf-8')`
2. **작업**: `read()`, `write()`, `readlines()` 등
3. **닫기**: `close()` 또는 `with` 문으로 자동

### 파일 모드 기억하기
- **'r'**: Read (읽기) - 파일이 없으면 에러
- **'w'**: Write (쓰기) - 기존 내용 삭제
- **'a'**: Append (추가) - 끝에 추가

### 실무 활용 팁
✅ 항상 `with` 문 사용 (자동으로 파일 닫힘)
✅ `encoding='utf-8'` 지정 (한글 깨짐 방지)
✅ `strip()` 으로 불필요한 공백/줄바꿈 제거
✅ 로그 파일은 `'a'` 모드로 계속 추가
✅ 파일명에 날짜 포함하면 관리 편함 (`log_2024-10-25.txt`)

### 에러 처리
```python
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"에러 발생: {e}")
```

---

## 🎯 다음 교시 예고

**3교시: CSV 라이브러리를 활용한 데이터 처리**
- CSV 파일이란?
- `csv` 모듈로 CSV 읽기/쓰기
- `DictReader`와 `DictWriter` 활용
- **실습 프로젝트:** 고객 명단을 CSV로 읽어 리스트로 변환

---

**2교시를 완료하셨습니다! 수고하셨습니다! 🎉**

"다음 교시"를 입력하시면 3교시 내용을 시작하겠습니다.

---
---

# 📘 3교시: csv 라이브러리를 활용한 CSV 데이터 읽기 및 쓰기 / 고객 명단 처리

---

## 1) 이론 설명

### CSV 파일이란?

**CSV (Comma-Separated Values)**는 쉼표로 구분된 값들을 저장하는 텍스트 파일 형식입니다.

**직장인 예시로 이해하기:**
- 엑셀에서 "다른 이름으로 저장" → CSV 파일 선택
- 고객 명단, 매출 데이터, 직원 목록 등을 저장할 때 사용
- 간단하고 호환성이 좋아 많은 프로그램에서 지원

**CSV 파일 예시:**
```
이름,부서,직급,연봉
홍길동,영업팀,대리,45000000
김철수,개발팀,과장,55000000
이영희,인사팀,사원,38000000
```

**특징:**
- 첫 줄은 보통 **헤더(Header)** - 각 열(column)의 이름
- 각 줄은 하나의 **레코드(Record)** - 하나의 데이터 항목
- 쉼표(,)로 각 **필드(Field)** 구분

### 왜 CSV를 사용하나?

1. **범용성**: 모든 스프레드시트 프로그램에서 사용 가능
2. **단순성**: 텍스트 파일이라 쉽게 읽고 쓸 수 있음
3. **경량성**: 엑셀 파일보다 용량이 작음
4. **프로그래밍 친화적**: Python, R, SQL 등에서 쉽게 처리

### Python csv 모듈

Python에는 CSV 파일을 쉽게 다룰 수 있는 `csv` 모듈이 내장되어 있습니다.

```python
import csv  # CSV 모듈 import
```

### CSV 읽기: csv.reader()

```python
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # 각 행이 리스트로 반환됨
```

**특징:**
- 각 행을 **리스트**로 반환
- 첫 번째 행(헤더)도 일반 데이터로 취급

### CSV 쓰기: csv.writer()

```python
import csv

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['이름', '나이', '직급'])  # 한 행 쓰기
    writer.writerow(['홍길동', 30, '대리'])
    writer.writerow(['김철수', 35, '과장'])
```

**주의사항:**
- `newline=''`: Windows에서 빈 줄이 추가되는 것을 방지
- `writerow()`: 리스트를 한 행으로 쓰기
- `writerows()`: 여러 행을 한 번에 쓰기

### DictReader: 딕셔너리로 읽기

```python
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['이름'])  # 딕셔너리 키로 접근
```

**장점:**
- 헤더를 자동으로 딕셔너리 키로 사용
- 컬럼 이름으로 데이터에 접근 가능
- 코드 가독성이 좋음

### DictWriter: 딕셔너리로 쓰기

```python
import csv

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['이름', '나이', '직급']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()  # 헤더 쓰기
    writer.writerow({'이름': '홍길동', '나이': 30, '직급': '대리'})
```

---

## 2) 실습 예제 코드

### 예제 1: CSV 파일 생성하기

```python
import csv

# 직원 데이터를 CSV 파일로 저장
employees = [
    ['이름', '부서', '직급', '연봉'],
    ['홍길동', '영업팀', '대리', 45000000],
    ['김철수', '개발팀', '과장', 55000000],
    ['이영희', '인사팀', '사원', 38000000],
    ['박민수', '영업팀', '과장', 52000000],
    ['정수진', '개발팀', '대리', 47000000]
]

# CSV 파일로 저장
with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(employees)  # 모든 행을 한 번에 쓰기

print("✅ employees.csv 파일이 생성되었습니다.")
```

### 예제 2: CSV 파일 읽기 - csv.reader()

```python
import csv

# CSV 파일 읽기
print("📄 직원 명단:")
print("-" * 50)

with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    
    for i, row in enumerate(reader):
        if i == 0:
            # 첫 번째 행은 헤더
            print(f"{'  |  '.join(row)}")
            print("-" * 50)
        else:
            # 데이터 행
            print(f"{row[0]:8} | {row[1]:6} | {row[2]:4} | {int(row[3]):,}원")

# 출력:
# 📄 직원 명단:
# --------------------------------------------------
# 이름  |  부서  |  직급  |  연봉
# --------------------------------------------------
# 홍길동      | 영업팀    | 대리   | 45,000,000원
# 김철수      | 개발팀    | 과장   | 55,000,000원
# ...
```

### 예제 3: CSV를 리스트로 변환

```python
import csv

# CSV 파일을 리스트로 읽어오기
def read_csv_to_list(filename):
    """CSV 파일을 리스트로 변환하는 함수"""
    data = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    
    return data

# 사용 예시
employees = read_csv_to_list('employees.csv')

print(f"총 {len(employees)-1}명의 직원 데이터 (헤더 제외)")
print(f"헤더: {employees[0]}")
print(f"첫 번째 직원: {employees[1]}")

# 출력:
# 총 5명의 직원 데이터 (헤더 제외)
# 헤더: ['이름', '부서', '직급', '연봉']
# 첫 번째 직원: ['홍길동', '영업팀', '대리', '45000000']
```

### 예제 4: DictReader로 읽기 (핵심 예제)

```python
import csv

# DictReader 사용 - 딕셔너리로 읽기
print("📄 직원 정보 (DictReader):")
print("-" * 60)

with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # row는 딕셔너리 형태
        name = row['이름']
        dept = row['부서']
        position = row['직급']
        salary = int(row['연봉'])
        
        print(f"{name} ({dept} {position}) - 연봉: {salary:,}원")

# 출력:
# 📄 직원 정보 (DictReader):
# ------------------------------------------------------------
# 홍길동 (영업팀 대리) - 연봉: 45,000,000원
# 김철수 (개발팀 과장) - 연봉: 55,000,000원
# 이영희 (인사팀 사원) - 연봉: 38,000,000원
# ...
```

### 예제 5: 조건에 맞는 데이터 필터링

```python
import csv

# 연봉 5천만원 이상인 직원만 추출
print("📊 고연봉 직원 (5천만원 이상):")
print("-" * 60)

high_salary_employees = []

with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        salary = int(row['연봉'])
        if salary >= 50000000:
            high_salary_employees.append(row)
            print(f"{row['이름']} - {row['부서']} - {salary:,}원")

print(f"\n총 {len(high_salary_employees)}명")

# 출력:
# 📊 고연봉 직원 (5천만원 이상):
# ------------------------------------------------------------
# 김철수 - 개발팀 - 55,000,000원
# 박민수 - 영업팀 - 52,000,000원
# 
# 총 2명
```

### 예제 6: DictWriter로 쓰기

```python
import csv

# 고객 데이터를 딕셔너리 형태로 준비
customers = [
    {'고객명': 'ABC 기업', '담당자': '홍길동', '연락처': '010-1234-5678', '등급': 'VIP'},
    {'고객명': 'XYZ 회사', '담당자': '김철수', '연락처': '010-2345-6789', '등급': '일반'},
    {'고객명': 'DEF 상사', '담당자': '이영희', '연락처': '010-3456-7890', '등급': 'VIP'},
]

# DictWriter로 CSV 파일 생성
fieldnames = ['고객명', '담당자', '연락처', '등급']

with open('customers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()  # 헤더 쓰기
    writer.writerows(customers)  # 모든 데이터 쓰기

print("✅ customers.csv 파일이 생성되었습니다.")

# 생성된 파일 확인
with open('customers.csv', 'r', encoding='utf-8') as f:
    print("\n📄 생성된 파일 내용:")
    print(f.read())
```

### 예제 7: 부서별 평균 연봉 계산

```python
import csv
from collections import defaultdict

# 부서별 연봉 합계와 인원수를 계산
dept_data = defaultdict(lambda: {'total': 0, 'count': 0})

with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        dept = row['부서']
        salary = int(row['연봉'])
        
        dept_data[dept]['total'] += salary
        dept_data[dept]['count'] += 1

# 부서별 평균 연봉 계산 및 출력
print("📊 부서별 평균 연봉:")
print("-" * 50)

for dept, data in dept_data.items():
    avg_salary = data['total'] / data['count']
    print(f"{dept}: {avg_salary:,.0f}원 (인원: {data['count']}명)")

# 출력:
# 📊 부서별 평균 연봉:
# --------------------------------------------------
# 영업팀: 48,500,000원 (인원: 2명)
# 개발팀: 51,000,000원 (인원: 2명)
# 인사팀: 38,000,000원 (인원: 1명)
```

### 예제 8: 고객 명단 관리 프로그램 (핵심 예제)

```python
import csv

def add_customer():
    """새로운 고객을 CSV 파일에 추가"""
    print("\n=== 신규 고객 등록 ===")
    
    # 고객 정보 입력받기
    customer_name = input("고객명: ")
    contact_person = input("담당자: ")
    phone = input("연락처: ")
    grade = input("등급 (VIP/일반): ")
    
    # 새 고객 데이터
    new_customer = {
        '고객명': customer_name,
        '담당자': contact_person,
        '연락처': phone,
        '등급': grade
    }
    
    # CSV 파일에 추가 (append 모드)
    fieldnames = ['고객명', '담당자', '연락처', '등급']
    
    with open('customers.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(new_customer)
    
    print(f"✅ '{customer_name}' 고객이 등록되었습니다!")

def view_customers():
    """모든 고객 명단 조회"""
    print("\n📋 전체 고객 명단:")
    print("-" * 70)
    
    try:
        with open('customers.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for i, row in enumerate(reader, 1):
                grade_icon = "⭐" if row['등급'] == 'VIP' else "●"
                print(f"{i}. {grade_icon} {row['고객명']:15} | {row['담당자']:8} | {row['연락처']}")
    
    except FileNotFoundError:
        print("❌ customers.csv 파일이 없습니다.")

def search_customer(keyword):
    """고객명으로 검색"""
    print(f"\n🔍 '{keyword}' 검색 결과:")
    print("-" * 70)
    
    found = False
    
    with open('customers.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            if keyword in row['고객명']:
                found = True
                print(f"고객명: {row['고객명']}")
                print(f"담당자: {row['담당자']}")
                print(f"연락처: {row['연락처']}")
                print(f"등급: {row['등급']}")
                print("-" * 70)
    
    if not found:
        print("검색 결과가 없습니다.")

# 프로그램 메뉴
def main():
    """고객 관리 프로그램 메인"""
    while True:
        print("\n" + "="*40)
        print("고객 관리 시스템")
        print("="*40)
        print("1. 고객 등록")
        print("2. 전체 고객 조회")
        print("3. 고객 검색")
        print("4. 종료")
        print("="*40)
        
        choice = input("\n선택: ")
        
        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            keyword = input("검색할 고객명: ")
            search_customer(keyword)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

# 실행: main()
```

---

## 3) 코드 상세 설명

### csv.reader() vs csv.DictReader()

**csv.reader() - 리스트로 반환:**
```python
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['홍길동', '영업팀', '대리']
        # 인덱스로 접근: row[0], row[1], row[2]
```

**csv.DictReader() - 딕셔너리로 반환:**
```python
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # {'이름': '홍길동', '부서': '영업팀', '직급': '대리'}
        # 키로 접근: row['이름'], row['부서'], row['직급']
```

**선택 기준:**
- 데이터 구조가 단순하고 순서가 중요: `csv.reader()`
- 컬럼이 많고 가독성이 중요: `csv.DictReader()` ✅ (권장)

### newline='' 파라미터의 역할

```python
# Windows에서 newline=''이 없으면
with open('data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['A', 'B', 'C'])
# 결과: 각 행 사이에 빈 줄이 추가됨

# newline=''을 추가하면
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['A', 'B', 'C'])
# 결과: 정상적인 CSV 파일 생성
```

**결론:**
- CSV 파일을 쓸 때는 항상 `newline=''` 추가
- 읽을 때는 필요 없음

### writerow() vs writerows()

```python
import csv

# writerow() - 한 행씩 쓰기
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['이름', '나이'])
    writer.writerow(['홍길동', 30])
    writer.writerow(['김철수', 35])

# writerows() - 여러 행을 한 번에 쓰기
data = [
    ['이름', '나이'],
    ['홍길동', 30],
    ['김철수', 35]
]

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)  # 리스트의 리스트
```

**성능:**
- `writerows()`가 더 효율적 (한 번에 처리)

### DictWriter의 fieldnames

```python
fieldnames = ['이름', '부서', '직급']
writer = csv.DictWriter(f, fieldnames=fieldnames)
```

**역할:**
1. CSV 파일의 컬럼 순서 지정
2. `writeheader()` 호출 시 헤더로 사용
3. 딕셔너리의 어떤 키를 사용할지 명시

**주의사항:**
- fieldnames에 없는 키는 무시됨
- fieldnames 순서대로 CSV에 기록됨

### 데이터 타입 변환

CSV 파일에서 읽은 데이터는 **모두 문자열(str)**입니다!

```python
import csv

with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        salary = row['연봉']  # 문자열 '45000000'
        print(type(salary))   # <class 'str'>
        
        # 정수로 변환 필요
        salary_int = int(salary)
        print(type(salary_int))  # <class 'int'>
```

**변환 방법:**
- 정수: `int(row['컬럼명'])`
- 실수: `float(row['컬럼명'])`
- 불린: `row['컬럼명'] == 'True'`

---

## 4) 실습 미션

### 미션 1: 매출 데이터 CSV 생성 ⭐
**목표:** 월별 매출 데이터를 CSV 파일로 저장하세요.

**요구사항:**
- 파일명: `sales.csv`
- 헤더: 월, 매출액, 목표달성률
- 데이터:
  ```
  1월, 15000000, 75
  2월, 18000000, 90
  3월, 22000000, 110
  ```
- `csv.writer()` 사용

---

### 미션 2: CSV 데이터 합계 계산 ⭐⭐
**목표:** sales.csv 파일을 읽어서 총 매출액을 계산하세요.

**요구사항:**
- `csv.reader()` 또는 `csv.DictReader()` 사용
- 헤더는 제외하고 계산
- 출력 형식: `총 매출액: 55,000,000원`

**힌트:**
```python
total = 0
for row in reader:
    if row[0] != '월':  # 헤더가 아니면
        total += int(row[1])
```

---

### 미션 3: VIP 고객만 추출하기 ⭐⭐⭐
**목표:** customers.csv에서 VIP 등급 고객만 추출하여 새 파일로 저장하세요.

**요구사항:**
- 입력 파일: `customers.csv`
- 출력 파일: `vip_customers.csv`
- `csv.DictReader()`와 `csv.DictWriter()` 사용
- VIP 고객만 필터링하여 저장

**예시 출력 (vip_customers.csv):**
```
고객명,담당자,연락처,등급
ABC 기업,홍길동,010-1234-5678,VIP
DEF 상사,이영희,010-3456-7890,VIP
```

---

### 미션 4: 직원 정보 업데이트 시스템 ⭐⭐⭐
**목표:** 직원의 연봉을 업데이트하는 프로그램을 작성하세요.

**요구사항:**
- 함수: `update_salary(name, new_salary)`
- employees.csv 파일을 읽어서 특정 직원의 연봉을 수정
- 수정된 내용을 다시 CSV 파일에 저장

**동작 과정:**
1. CSV 파일을 리스트로 읽기
2. 해당 직원을 찾아서 연봉 업데이트
3. 전체 데이터를 다시 CSV로 저장

**힌트:**
```python
def update_salary(name, new_salary):
    # 1. 파일 읽기
    with open('employees.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    # 2. 데이터 수정
    for row in data:
        if row['이름'] == name:
            row['연봉'] = str(new_salary)
    
    # 3. 파일 쓰기
    fieldnames = ['이름', '부서', '직급', '연봉']
    with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
```

---

## 5) 퀴즈

### 퀴즈 1 (기본 개념) 📝
CSV 파일에서 각 행을 딕셔너리 형태로 읽고 싶을 때 사용하는 클래스는?

**A)** `csv.reader()`  
**B)** `csv.DictReader()`  
**C)** `csv.writer()`  
**D)** `csv.DictWriter()`

---

### 퀴즈 2 (파일 쓰기) 📝
다음 코드의 실행 결과는?

```python
import csv

data = [
    ['이름', '점수'],
    ['철수', '90'],
    ['영희', '85']
]

with open('scores.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

**A)** 에러 발생  
**B)** 빈 파일 생성  
**C)** 3행 2열의 CSV 파일 생성  
**D)** 2행 3열의 CSV 파일 생성

---

### 퀴즈 3 (응용 문제) 📝
다음 코드의 출력 결과는?

```python
import csv

with open('test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)
    print(len(data))

# test.csv 내용:
# 이름,나이
# 홍길동,30
# 김철수,35
# 이영희,28
```

**A)** 2  
**B)** 3  
**C)** 4  
**D)** 에러 발생

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **B) csv.DictReader()**

**해설:**
- `csv.reader()`: 각 행을 **리스트**로 반환
- `csv.DictReader()`: 각 행을 **딕셔너리**로 반환 ✅
- `csv.writer()`: CSV 파일에 쓰기 (리스트 형태)
- `csv.DictWriter()`: CSV 파일에 쓰기 (딕셔너리 형태)

**사용 예시:**
```python
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['이름'])  # 딕셔너리 키로 접근
```

---

### 퀴즈 2 정답: **C) 3행 2열의 CSV 파일 생성**

**해설:**

**데이터 구조:**
```python
data = [
    ['이름', '점수'],   # 1행
    ['철수', '90'],     # 2행
    ['영희', '85']      # 3행
]
```

**생성되는 CSV 파일:**
```
이름,점수
철수,90
영희,85
```

- 총 3개의 행 (3행)
- 각 행에 2개의 값 (2열)

**포인트:**
- `writerows(data)`: 리스트의 각 요소를 한 행씩 쓰기
- `newline=''`: Windows에서 빈 줄 방지

---

### 퀴즈 3 정답: **B) 3**

**해설:**

**CSV 파일 구조:**
```
이름,나이      <- 헤더 (DictReader가 자동으로 키로 사용)
홍길동,30      <- 1번째 데이터
김철수,35      <- 2번째 데이터
이영희,28      <- 3번째 데이터
```

**실행 과정:**
1. `csv.DictReader(f)` 생성
   - 첫 번째 행('이름,나이')을 헤더로 인식
   - 헤더를 딕셔너리 키로 사용

2. `list(reader)` 변환
   ```python
   [
       {'이름': '홍길동', '나이': '30'},
       {'이름': '김철수', '나이': '35'},
       {'이름': '이영희', '나이': '28'}
   ]
   ```

3. `len(data)` = 3
   - 헤더는 제외되고 데이터 행만 3개

**포인트:**
- `DictReader`는 첫 행을 자동으로 헤더로 인식
- 헤더는 데이터에 포함되지 않음

---

## 💡 3교시 핵심 요약

### CSV 파일 다루기 4단계
1. **import csv**: csv 모듈 불러오기
2. **파일 열기**: `open()` with문 사용
3. **reader/writer 생성**: 읽기/쓰기 객체 생성
4. **데이터 처리**: 반복문으로 읽기 또는 쓰기

### reader vs DictReader

| 특징 | csv.reader() | csv.DictReader() |
|------|--------------|------------------|
| 반환 형식 | 리스트 | 딕셔너리 |
| 접근 방법 | row[0], row[1] | row['이름'], row['부서'] |
| 헤더 처리 | 수동 | 자동 |
| 가독성 | 낮음 | 높음 ✅ |

### 실무 활용 팁
✅ CSV 쓰기 시 항상 `newline=''` 추가
✅ 한글 데이터는 `encoding='utf-8'` 필수
✅ 딕셔너리 형태 선호 시 DictReader/DictWriter 사용
✅ CSV 데이터는 모두 문자열 → 숫자 변환 필요
✅ 대용량 파일은 한 줄씩 처리 (메모리 효율)

### 자주 하는 실수
❌ `newline=''` 누락 → 빈 줄 생김
❌ 타입 변환 안 함 → 문자열로 계산
❌ 헤더를 데이터로 처리 → enumerate나 next() 사용

---

## 🎯 다음 교시 예고

**4교시: JSON 형식 이해 및 딕셔너리 변환**
- JSON이란? (JavaScript Object Notation)
- `json` 모듈로 JSON 읽기/쓰기
- 딕셔너리 ↔ JSON 변환
- **실습 프로젝트:** API 응답 데이터 파싱 및 정보 추출

---

**3교시를 완료하셨습니다! 수고하셨습니다! 🎉**

"다음 교시"를 입력하시면 4교시 내용을 시작하겠습니다.

---
---

# 📘 4교시: JSON 형식 이해 및 딕셔너리 변환 후 정보 추출

---

## 1) 이론 설명

### JSON이란?

**JSON (JavaScript Object Notation)**은 데이터를 주고받을 때 사용하는 가벼운 텍스트 형식입니다.

**직장인 예시로 이해하기:**
- 카카오톡에서 메시지를 보낼 때 JSON 형식으로 데이터 전송
- 회사 시스템 간 데이터 교환 (ERP ↔ 회계 시스템)
- 웹사이트에서 서버와 통신할 때 JSON 사용
- API(응용 프로그램 인터페이스)로 외부 데이터 가져올 때

**예시: 직원 정보를 JSON으로 표현**
```json
{
    "이름": "홍길동",
    "부서": "영업팀",
    "직급": "대리",
    "연봉": 45000000,
    "기술": ["Excel", "PowerPoint", "영업"]
}
```

### JSON의 특징

1. **사람이 읽기 쉬움**: 텍스트 형식이라 눈으로 확인 가능
2. **언어 독립적**: Python, Java, JavaScript 등 모든 언어에서 사용
3. **가벼움**: XML보다 간단하고 용량이 작음
4. **구조화**: 중첩된 데이터를 표현하기 좋음

### JSON 데이터 타입

**1. 객체(Object)** - Python 딕셔너리와 유사
```json
{
    "이름": "홍길동",
    "나이": 30
}
```

**2. 배열(Array)** - Python 리스트와 유사
```json
["사과", "바나나", "오렌지"]
```

**3. 기본 타입**
- 문자열: `"Hello"`
- 숫자: `123`, `3.14`
- 불린: `true`, `false`
- null: `null` (Python의 None)

### Python에서 JSON 다루기

Python에는 JSON을 쉽게 다룰 수 있는 `json` 모듈이 내장되어 있습니다.

```python
import json  # JSON 모듈 import
```

### Python 딕셔너리 ↔ JSON 변환

**Python 딕셔너리를 JSON 문자열로 (직렬화, Serialization)**
```python
import json

data = {"이름": "홍길동", "나이": 30}
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)  # '{"이름": "홍길동", "나이": 30}'
```

**JSON 문자열을 Python 딕셔너리로 (역직렬화, Deserialization)**
```python
import json

json_string = '{"이름": "홍길동", "나이": 30}'
data = json.loads(json_string)
print(data)  # {'이름': '홍길동', '나이': 30}
```

### JSON 파일 읽기/쓰기

**JSON 파일에 쓰기:**
```python
import json

data = {"이름": "홍길동", "부서": "영업팀"}

with open('employee.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

**JSON 파일에서 읽기:**
```python
import json

with open('employee.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data['이름'])  # '홍길동'
```

### 주요 함수 정리

| 함수 | 설명 | 사용 |
|------|------|------|
| `json.dumps()` | 딕셔너리 → JSON 문자열 | 데이터를 문자열로 변환 |
| `json.loads()` | JSON 문자열 → 딕셔너리 | 문자열을 데이터로 변환 |
| `json.dump()` | 딕셔너리 → JSON 파일 | 파일에 저장 |
| `json.load()` | JSON 파일 → 딕셔너리 | 파일에서 읽기 |

**암기 팁:**
- `dumps` / `loads`: **s**tring (문자열)
- `dump` / `load`: 파일

---

## 2) 실습 예제 코드

### 예제 1: 딕셔너리를 JSON 문자열로 변환

```python
import json

# 직원 정보 딕셔너리
employee = {
    "이름": "홍길동",
    "부서": "영업팀",
    "직급": "대리",
    "연봉": 45000000,
    "입사일": "2020-03-15"
}

# 딕셔너리를 JSON 문자열로 변환
json_string = json.dumps(employee, ensure_ascii=False, indent=2)

print("📄 JSON 문자열:")
print(json_string)
print(f"\n타입: {type(json_string)}")

# 출력:
# 📄 JSON 문자열:
# {
#   "이름": "홍길동",
#   "부서": "영업팀",
#   "직급": "대리",
#   "연봉": 45000000,
#   "입사일": "2020-03-15"
# }
# 
# 타입: <class 'str'>
```

### 예제 2: JSON 문자열을 딕셔너리로 변환

```python
import json

# JSON 형식의 문자열 (API 응답이라고 가정)
json_response = '''
{
    "status": "success",
    "data": {
        "고객명": "ABC 기업",
        "담당자": "김철수",
        "계약금액": 50000000
    }
}
'''

# JSON 문자열을 딕셔너리로 변환
data = json.loads(json_response)

print("📊 파싱된 데이터:")
print(f"상태: {data['status']}")
print(f"고객명: {data['data']['고객명']}")
print(f"담당자: {data['data']['담당자']}")
print(f"계약금액: {data['data']['계약금액']:,}원")

# 출력:
# 📊 파싱된 데이터:
# 상태: success
# 고객명: ABC 기업
# 담당자: 김철수
# 계약금액: 50,000,000원
```

### 예제 3: JSON 파일 저장하기

```python
import json

# 프로젝트 정보
project = {
    "프로젝트명": "신규 시스템 구축",
    "시작일": "2024-01-01",
    "종료일": "2024-12-31",
    "예산": 200000000,
    "팀원": [
        {"이름": "홍길동", "역할": "PM"},
        {"이름": "김철수", "역할": "개발자"},
        {"이름": "이영희", "역할": "디자이너"}
    ],
    "진행률": 45.5
}

# JSON 파일로 저장
with open('project.json', 'w', encoding='utf-8') as f:
    json.dump(project, f, ensure_ascii=False, indent=4)

print("✅ project.json 파일이 생성되었습니다.")

# 저장된 파일 확인
with open('project.json', 'r', encoding='utf-8') as f:
    print("\n📄 저장된 파일 내용:")
    print(f.read())
```

### 예제 4: JSON 파일 읽기 (핵심 예제)

```python
import json

# JSON 파일 읽기
with open('project.json', 'r', encoding='utf-8') as f:
    project = json.load(f)

# 정보 추출 및 출력
print("📋 프로젝트 정보:")
print("=" * 50)
print(f"프로젝트명: {project['프로젝트명']}")
print(f"기간: {project['시작일']} ~ {project['종료일']}")
print(f"예산: {project['예산']:,}원")
print(f"진행률: {project['진행률']}%")

print("\n👥 팀원 목록:")
for member in project['팀원']:
    print(f"  - {member['이름']} ({member['역할']})")

# 출력:
# 📋 프로젝트 정보:
# ==================================================
# 프로젝트명: 신규 시스템 구축
# 기간: 2024-01-01 ~ 2024-12-31
# 예산: 200,000,000원
# 진행률: 45.5%
# 
# 👥 팀원 목록:
#   - 홍길동 (PM)
#   - 김철수 (개발자)
#   - 이영희 (디자이너)
```

### 예제 5: 중첩된 JSON 데이터 처리

```python
import json

# 부서별 직원 정보 (중첩 구조)
company_data = {
    "회사명": "테크 기업",
    "부서": {
        "영업팀": {
            "팀장": "홍길동",
            "팀원": ["김철수", "이영희"],
            "목표": 500000000
        },
        "개발팀": {
            "팀장": "박민수",
            "팀원": ["정수진", "최동욱", "강민지"],
            "목표": 10
        }
    }
}

# JSON 파일로 저장
with open('company.json', 'w', encoding='utf-8') as f:
    json.dump(company_data, f, ensure_ascii=False, indent=4)

# 파일에서 읽어서 정보 추출
with open('company.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"📊 {data['회사명']} 조직 정보\n")

for dept_name, dept_info in data['부서'].items():
    print(f"▶ {dept_name}")
    print(f"   팀장: {dept_info['팀장']}")
    print(f"   팀원 수: {len(dept_info['팀원'])}명")
    print(f"   팀원: {', '.join(dept_info['팀원'])}")
    print(f"   목표: {dept_info['목표']:,}")
    print()
```

### 예제 6: API 응답 형식 처리

```python
import json

# 실제 API 응답 예시 (날씨 API라고 가정)
api_response = '''
{
    "location": "서울",
    "current": {
        "temperature": 22,
        "humidity": 65,
        "condition": "맑음"
    },
    "forecast": [
        {"day": "월요일", "temp": 23, "condition": "맑음"},
        {"day": "화요일", "temp": 20, "condition": "흐림"},
        {"day": "수요일", "temp": 18, "condition": "비"}
    ]
}
'''

# JSON 파싱
weather = json.loads(api_response)

# 현재 날씨 정보
print(f"🌤️  {weather['location']} 날씨")
print("=" * 40)
print(f"현재 기온: {weather['current']['temperature']}°C")
print(f"습도: {weather['current']['humidity']}%")
print(f"날씨: {weather['current']['condition']}")

# 주간 예보
print("\n📅 주간 예보:")
for day in weather['forecast']:
    condition_icon = "☀️" if day['condition'] == "맑음" else "🌧️" if day['condition'] == "비" else "☁️"
    print(f"{condition_icon} {day['day']}: {day['temp']}°C, {day['condition']}")
```

### 예제 7: 설정 파일 관리 (핵심 예제)

```python
import json

def save_config(config):
    """설정을 JSON 파일로 저장"""
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    print("✅ 설정이 저장되었습니다.")

def load_config():
    """JSON 파일에서 설정 읽기"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️  설정 파일이 없습니다. 기본 설정을 사용합니다.")
        return {
            "언어": "한국어",
            "테마": "밝음",
            "알림": True,
            "자동저장": True
        }

def update_config(key, value):
    """설정 값 변경"""
    config = load_config()
    config[key] = value
    save_config(config)
    print(f"✅ '{key}' 설정이 '{value}'(으)로 변경되었습니다.")

# 사용 예시
print("📋 현재 설정:")
current_config = load_config()
for key, value in current_config.items():
    print(f"  {key}: {value}")

print("\n설정 변경:")
update_config("테마", "어두움")
update_config("알림", False)

print("\n📋 변경된 설정:")
new_config = load_config()
for key, value in new_config.items():
    print(f"  {key}: {value}")
```

### 예제 8: 고객 데이터 JSON 변환 프로그램

```python
import json

def add_customer_json(customer_data):
    """고객 정보를 JSON 파일에 추가"""
    # 기존 데이터 읽기
    try:
        with open('customers.json', 'r', encoding='utf-8') as f:
            customers = json.load(f)
    except FileNotFoundError:
        customers = []
    
    # 새 고객 추가
    customers.append(customer_data)
    
    # 파일에 저장
    with open('customers.json', 'w', encoding='utf-8') as f:
        json.dump(customers, f, ensure_ascii=False, indent=4)
    
    print(f"✅ '{customer_data['고객명']}' 고객이 등록되었습니다.")

def search_customer_json(keyword):
    """고객명으로 검색"""
    try:
        with open('customers.json', 'r', encoding='utf-8') as f:
            customers = json.load(f)
        
        print(f"\n🔍 '{keyword}' 검색 결과:")
        print("=" * 60)
        
        found = False
        for customer in customers:
            if keyword in customer['고객명']:
                found = True
                print(f"고객명: {customer['고객명']}")
                print(f"등급: {customer['등급']}")
                print(f"담당자: {customer['담당자']}")
                print(f"계약금액: {customer['계약금액']:,}원")
                print("-" * 60)
        
        if not found:
            print("검색 결과가 없습니다.")
    
    except FileNotFoundError:
        print("❌ customers.json 파일이 없습니다.")

# 사용 예시
customer1 = {
    "고객명": "ABC 기업",
    "등급": "VIP",
    "담당자": "홍길동",
    "계약금액": 100000000
}

customer2 = {
    "고객명": "XYZ 회사",
    "등급": "일반",
    "담당자": "김철수",
    "계약금액": 30000000
}

add_customer_json(customer1)
add_customer_json(customer2)

search_customer_json("ABC")
```

---

## 3) 코드 상세 설명

### json.dumps() 파라미터

```python
json.dumps(data, ensure_ascii=False, indent=4)
```

**파라미터 설명:**
1. `data`: 변환할 딕셔너리
2. `ensure_ascii=False`: 한글을 그대로 표시 (True면 유니코드로 변환)
3. `indent=4`: 들여쓰기 4칸 (가독성 향상)

**ensure_ascii 비교:**
```python
# ensure_ascii=True (기본값)
json.dumps({"이름": "홍길동"})
# '{"\\uc774\\ub984": "\\ud64d\\uae38\\ub3d9"}'

# ensure_ascii=False
json.dumps({"이름": "홍길동"}, ensure_ascii=False)
# '{"이름": "홍길동"}'
```

### json.load() vs json.loads()

**json.load() - 파일에서 읽기:**
```python
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # 파일 객체를 전달
```

**json.loads() - 문자열에서 읽기:**
```python
json_string = '{"이름": "홍길동"}'
data = json.loads(json_string)  # 문자열을 전달
```

**차이점:**
- `load()`: 파일 객체 → 딕셔너리
- `loads()`: 문자열 → 딕셔너리 (string의 's')

### 중첩된 JSON 데이터 접근

```python
data = {
    "회사": {
        "부서": {
            "영업팀": {
                "팀장": "홍길동"
            }
        }
    }
}

# 단계별 접근
print(data['회사']['부서']['영업팀']['팀장'])  # '홍길동'
```

**안전한 접근 (get 메서드):**
```python
# 키가 없으면 None 반환
팀장 = data.get('회사', {}).get('부서', {}).get('영업팀', {}).get('팀장')

# 키가 없으면 기본값 반환
팀장 = data.get('회사', {}).get('부서', {}).get('영업팀', {}).get('팀장', '미정')
```

### JSON과 Python 타입 매핑

| JSON | Python |
|------|--------|
| object | dict |
| array | list |
| string | str |
| number (int) | int |
| number (real) | float |
| true | True |
| false | False |
| null | None |

**변환 예시:**
```python
json_data = '''
{
    "이름": "홍길동",
    "나이": 30,
    "키": 175.5,
    "결혼": false,
    "주소": null,
    "취미": ["독서", "영화"]
}
'''

data = json.loads(json_data)

print(type(data))           # <class 'dict'>
print(type(data['나이']))   # <class 'int'>
print(type(data['키']))     # <class 'float'>
print(type(data['결혼']))   # <class 'bool'>
print(type(data['주소']))   # <class 'NoneType'>
print(type(data['취미']))   # <class 'list'>
```

### 예외 처리

```python
import json

json_string = '{"이름": "홍길동", "나이": 30'  # 잘못된 JSON (} 누락)

try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"❌ JSON 파싱 에러: {e}")
    # 출력: ❌ JSON 파싱 에러: Expecting ',' delimiter: line 1 column 23 (char 22)
```

---

## 4) 실습 미션

### 미션 1: 직원 정보 JSON 저장 ⭐
**목표:** 직원 정보를 딕셔너리로 만들고 JSON 파일로 저장하세요.

**요구사항:**
- 딕셔너리 생성: 이름, 부서, 직급, 연봉 포함
- 파일명: `employee.json`
- `json.dump()` 사용
- `ensure_ascii=False`, `indent=4` 적용

---

### 미션 2: JSON 파일 읽고 정보 출력 ⭐⭐
**목표:** employee.json 파일을 읽어서 연봉을 천 단위 구분하여 출력하세요.

**요구사항:**
- `json.load()` 사용
- 출력 형식: `홍길동 (영업팀 대리) - 연봉: 45,000,000원`

---

### 미션 3: 여러 직원 정보를 리스트로 관리 ⭐⭐⭐
**목표:** 여러 직원의 정보를 리스트에 담아 JSON 파일로 저장하고, 연봉이 가장 높은 직원을 찾으세요.

**요구사항:**
- 직원 3명 이상의 데이터 생성
- 파일명: `employees.json`
- 구조: `[{직원1}, {직원2}, {직원3}]`
- 최고 연봉자 출력

**힌트:**
```python
employees = [
    {"이름": "홍길동", "연봉": 45000000},
    {"이름": "김철수", "연봉": 55000000},
    # ...
]

max_employee = max(employees, key=lambda x: x['연봉'])
```

---

### 미션 4: API 응답 데이터 파싱 ⭐⭐⭐
**목표:** 다음 JSON 형식의 API 응답을 파싱하여 필요한 정보만 추출하세요.

**API 응답 (문자열):**
```json
{
    "status": "success",
    "data": {
        "products": [
            {"name": "노트북", "price": 1500000, "stock": 10},
            {"name": "마우스", "price": 30000, "stock": 50},
            {"name": "키보드", "price": 80000, "stock": 25}
        ],
        "total": 3
    }
}
```

**요구사항:**
- JSON 문자열을 딕셔너리로 변환
- 재고가 30개 이상인 제품만 출력
- 출력 형식: `마우스 - 30,000원 (재고: 50개)`

---

## 5) 퀴즈

### 퀴즈 1 (기본 개념) 📝
Python 딕셔너리를 JSON 문자열로 변환할 때 사용하는 함수는?

**A)** `json.load()`  
**B)** `json.loads()`  
**C)** `json.dump()`  
**D)** `json.dumps()`

---

### 퀴즈 2 (파일 처리) 📝
다음 코드의 실행 결과는?

```python
import json

data = {"이름": "홍길동", "나이": 30}

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

with open('test.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
    print(type(result))
```

**A)** `<class 'str'>`  
**B)** `<class 'dict'>`  
**C)** `<class 'list'>`  
**D)** 에러 발생

---

### 퀴즈 3 (응용 문제) 📝
다음 JSON 데이터에서 "김철수"의 역할을 출력하려면?

```python
import json

json_string = '''
{
    "프로젝트": {
        "팀원": [
            {"이름": "홍길동", "역할": "PM"},
            {"이름": "김철수", "역할": "개발자"}
        ]
    }
}
'''

data = json.loads(json_string)
# 여기에 코드 작성
```

**A)** `print(data['팀원'][1]['역할'])`  
**B)** `print(data['프로젝트']['팀원'][1]['역할'])`  
**C)** `print(data['프로젝트'][1]['역할'])`  
**D)** `print(data['팀원']['김철수']['역할'])`

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **D) json.dumps()**

**해설:**
- `json.load()`: JSON **파일** → 딕셔너리
- `json.loads()`: JSON **문자열** → 딕셔너리
- `json.dump()`: 딕셔너리 → JSON **파일**
- `json.dumps()`: 딕셔너리 → JSON **문자열** ✅

**암기 팁:**
- `dump**s**()` / `load**s**()`: **s**tring (문자열)
- `dump()` / `load()`: 파일

**예시:**
```python
import json

data = {"이름": "홍길동"}

# 딕셔너리 → JSON 문자열
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)  # '{"이름": "홍길동"}'
print(type(json_string))  # <class 'str'>
```

---

### 퀴즈 2 정답: **B) <class 'dict'>**

**해설:**

**단계별 실행:**
1. 딕셔너리 생성: `data = {"이름": "홍길동", "나이": 30}`
2. JSON 파일로 저장: `json.dump(data, f)`
3. JSON 파일 읽기: `result = json.load(f)`
   - `json.load()`는 JSON 파일을 읽어서 **딕셔너리로 반환**
4. 타입 출력: `print(type(result))` → `<class 'dict'>`

**포인트:**
- `json.dump()`: 딕셔너리를 JSON 파일로 저장
- `json.load()`: JSON 파일을 읽어서 딕셔너리로 반환
- 파일에 저장했다가 다시 읽어도 딕셔너리로 복원됨

---

### 퀴즈 3 정답: **B) print(data['프로젝트']['팀원'][1]['역할'])**

**해설:**

**JSON 구조 분석:**
```json
{
    "프로젝트": {              ← 최상위 키
        "팀원": [              ← "프로젝트" 안의 키
            {...},            ← 인덱스 0
            {                 ← 인덱스 1
                "이름": "김철수",
                "역할": "개발자"  ← 여기에 접근!
            }
        ]
    }
}
```

**접근 경로:**
1. `data['프로젝트']`: 프로젝트 객체에 접근
2. `['팀원']`: 팀원 배열에 접근
3. `[1]`: 두 번째 요소 (김철수)
4. `['역할']`: 역할 값 가져오기

**결과:**
```python
print(data['프로젝트']['팀원'][1]['역할'])  # '개발자'
```

**다른 선택지 분석:**
- **A)** ❌ `data['팀원']` - 최상위에 '팀원' 키가 없음
- **C)** ❌ `data['프로젝트'][1]` - '프로젝트'는 딕셔너리라 인덱스 불가
- **D)** ❌ `data['팀원']['김철수']` - 팀원은 리스트, 이름으로 접근 불가

---

## 💡 4교시 핵심 요약

### JSON 다루기 4단계
1. **import json**: json 모듈 불러오기
2. **데이터 준비**: 딕셔너리 또는 JSON 문자열
3. **변환**: dumps/loads 또는 dump/load
4. **활용**: 딕셔너리처럼 데이터 접근

### 핵심 함수 4가지

| 함수 | 입력 | 출력 | 용도 |
|------|------|------|------|
| `dumps()` | dict | str | 딕셔너리 → 문자열 |
| `loads()` | str | dict | 문자열 → 딕셔너리 |
| `dump()` | dict | 파일 | 딕셔너리 → 파일 |
| `load()` | 파일 | dict | 파일 → 딕셔너리 |

### 실무 활용 팁
✅ 한글 데이터는 `ensure_ascii=False` 필수
✅ 가독성을 위해 `indent=4` 권장
✅ 파일 작업 시 `encoding='utf-8'` 지정
✅ 중첩 데이터는 `get()` 메서드로 안전하게 접근
✅ API 응답 데이터는 대부분 JSON 형식

### JSON vs CSV

| 특징 | CSV | JSON |
|------|-----|------|
| 구조 | 평면적 (2차원 테이블) | 계층적 (중첩 가능) |
| 복잡도 | 단순 | 복잡한 데이터 표현 가능 |
| 크기 | 작음 | 상대적으로 큼 |
| 사용처 | 엑셀, 데이터베이스 | API, 설정 파일 |

---

## 🎯 다음 교시 예고

**5교시: Pandas 데이터프레임 개념 이해**
- Pandas란? (데이터 분석의 핵심 라이브러리)
- Series와 DataFrame
- 딕셔너리/리스트를 DataFrame으로 변환
- **실습 프로젝트:** 직원 데이터를 DataFrame으로 관리하고 분석

---

**4교시를 완료하셨습니다! 수고하셨습니다! 🎉**

"다음 교시"를 입력하시면 5교시 내용을 시작하겠습니다.

---
---

# 📘 5교시: Pandas 데이터프레임 개념 이해 / 딕셔너리·리스트를 DataFrame으로 변환

---

## 1) 이론 설명

### Pandas란?

**Pandas**는 Python에서 데이터 분석을 위한 가장 강력한 라이브러리입니다.

**직장인 예시로 이해하기:**
- 엑셀 작업을 Python 코드로 자동화
- 수백만 건의 데이터를 빠르게 처리
- 복잡한 데이터 집계와 분석을 간단하게
- 보고서 작성 시간을 획기적으로 단축

**왜 Pandas를 배워야 하나?**
1. **엑셀의 한계 극복**: 대용량 데이터 처리 가능
2. **반복 작업 자동화**: 매월 하는 보고서 작성 자동화
3. **데이터 분석**: 매출 추이, 고객 분석 등
4. **업무 효율**: 수작업 시간 단축

### Pandas 설치

```bash
pip install pandas
```

### DataFrame이란?

**DataFrame**은 Pandas의 핵심 데이터 구조로, **표(테이블) 형태**의 데이터입니다.

**엑셀 시트와 비교:**
- 엑셀 시트 = Pandas DataFrame
- 행(Row) = 각각의 데이터 레코드
- 열(Column) = 각각의 필드/속성
- 셀(Cell) = 개별 데이터 값

**예시: 직원 정보 DataFrame**
```
   이름    부서    직급      연봉
0  홍길동  영업팀  대리  45000000
1  김철수  개발팀  과장  55000000
2  이영희  인사팀  사원  38000000
```

### Series란?

**Series**는 DataFrame의 한 열(Column)을 나타내는 1차원 데이터 구조입니다.

```python
# DataFrame의 한 열 = Series
이름_시리즈 = ['홍길동', '김철수', '이영희']
```

### DataFrame 생성 방법

**1. 딕셔너리로부터 생성**
```python
import pandas as pd

data = {
    '이름': ['홍길동', '김철수'],
    '나이': [30, 35]
}
df = pd.DataFrame(data)
```

**2. 리스트의 리스트로부터 생성**
```python
data = [
    ['홍길동', 30],
    ['김철수', 35]
]
df = pd.DataFrame(data, columns=['이름', '나이'])
```

**3. 딕셔너리의 리스트로부터 생성**
```python
data = [
    {'이름': '홍길동', '나이': 30},
    {'이름': '김철수', '나이': 35}
]
df = pd.DataFrame(data)
```

### DataFrame 기본 조작

**데이터 확인:**
- `df.head()`: 처음 5행 보기
- `df.tail()`: 마지막 5행 보기
- `df.info()`: 데이터 정보 (타입, 개수 등)
- `df.describe()`: 통계 요약

**열 선택:**
```python
df['이름']  # 한 개 열 → Series
df[['이름', '나이']]  # 여러 열 → DataFrame
```

**행 선택:**
```python
df.loc[0]  # 인덱스로 선택
df.iloc[0]  # 위치로 선택
```

---

## 2) 실습 예제 코드

### 예제 1: Pandas 기본 - 딕셔너리로 DataFrame 생성

```python
import pandas as pd

# 딕셔너리로 데이터 준비
employee_data = {
    '이름': ['홍길동', '김철수', '이영희', '박민수'],
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀'],
    '직급': ['대리', '과장', '사원', '과장'],
    '연봉': [45000000, 55000000, 38000000, 52000000]
}

# DataFrame 생성
df = pd.DataFrame(employee_data)

print("📊 직원 정보 DataFrame:")
print(df)
print(f"\n타입: {type(df)}")

# 출력:
# 📊 직원 정보 DataFrame:
#     이름   부서  직급      연봉
# 0  홍길동  영업팀  대리  45000000
# 1  김철수  개발팀  과장  55000000
# 2  이영희  인사팀  사원  38000000
# 3  박민수  영업팀  과장  52000000
# 
# 타입: <class 'pandas.core.frame.DataFrame'>
```

### 예제 2: 리스트로 DataFrame 생성

```python
import pandas as pd

# 리스트의 리스트로 데이터 준비
data = [
    ['홍길동', '영업팀', '대리', 45000000],
    ['김철수', '개발팀', '과장', 55000000],
    ['이영희', '인사팀', '사원', 38000000],
    ['박민수', '영업팀', '과장', 52000000]
]

# 컬럼명 지정하여 DataFrame 생성
columns = ['이름', '부서', '직급', '연봉']
df = pd.DataFrame(data, columns=columns)

print("📊 DataFrame 생성 (리스트):")
print(df)
```

### 예제 3: 딕셔너리 리스트로 DataFrame 생성

```python
import pandas as pd

# 딕셔너리의 리스트 (JSON 데이터와 유사)
employees = [
    {'이름': '홍길동', '부서': '영업팀', '직급': '대리', '연봉': 45000000},
    {'이름': '김철수', '부서': '개발팀', '직급': '과장', '연봉': 55000000},
    {'이름': '이영희', '부서': '인사팀', '직급': '사원', '연봉': 38000000},
    {'이름': '박민수', '부서': '영업팀', '직급': '과장', '연봉': 52000000}
]

# DataFrame 생성
df = pd.DataFrame(employees)

print("📊 DataFrame 생성 (딕셔너리 리스트):")
print(df)
```

### 예제 4: DataFrame 기본 정보 확인 (핵심 예제)

```python
import pandas as pd

# 샘플 데이터
employee_data = {
    '이름': ['홍길동', '김철수', '이영희', '박민수', '정수진'],
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀', '개발팀'],
    '직급': ['대리', '과장', '사원', '과장', '대리'],
    '연봉': [45000000, 55000000, 38000000, 52000000, 47000000],
    '입사년도': [2020, 2018, 2022, 2019, 2021]
}

df = pd.DataFrame(employee_data)

# 1. 처음 3행 보기
print("📊 head(3) - 처음 3행:")
print(df.head(3))

# 2. 마지막 2행 보기
print("\n📊 tail(2) - 마지막 2행:")
print(df.tail(2))

# 3. DataFrame 정보
print("\n📊 info() - 데이터 정보:")
df.info()

# 4. 통계 요약
print("\n📊 describe() - 통계 요약:")
print(df.describe())

# 5. Shape (행, 열 개수)
print(f"\n📊 Shape: {df.shape}")  # (5, 5) → 5행, 5열

# 6. 컬럼 목록
print(f"\n📊 Columns: {df.columns.tolist()}")
```

### 예제 5: 열(Column) 선택하기

```python
import pandas as pd

df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '부서': ['영업팀', '개발팀', '인사팀'],
    '연봉': [45000000, 55000000, 38000000]
})

# 방법 1: 한 개 열 선택 → Series
print("📊 이름 열 (Series):")
이름_시리즈 = df['이름']
print(이름_시리즈)
print(f"타입: {type(이름_시리즈)}")

# 방법 2: 여러 열 선택 → DataFrame
print("\n📊 이름, 연봉 열 (DataFrame):")
선택_df = df[['이름', '연봉']]
print(선택_df)
print(f"타입: {type(선택_df)}")

# 방법 3: 점(.) 표기법 (공백이 없는 컬럼만 가능)
print("\n📊 점 표기법:")
print(df.이름)  # df['이름']과 동일
```

### 예제 6: 행(Row) 선택하기

```python
import pandas as pd

df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '부서': ['영업팀', '개발팀', '인사팀'],
    '연봉': [45000000, 55000000, 38000000]
})

# loc: 인덱스(라벨)로 선택
print("📊 loc[0] - 첫 번째 행:")
print(df.loc[0])

# iloc: 위치(정수)로 선택
print("\n📊 iloc[1] - 두 번째 행:")
print(df.iloc[1])

# 여러 행 선택
print("\n📊 iloc[0:2] - 처음 두 행:")
print(df.iloc[0:2])

# 조건으로 행 선택
print("\n📊 연봉이 50000000 이상인 직원:")
고연봉_df = df[df['연봉'] >= 50000000]
print(고연봉_df)
```

### 예제 7: 새로운 열 추가하기

```python
import pandas as pd

df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '연봉': [45000000, 55000000, 38000000]
})

print("📊 원본 DataFrame:")
print(df)

# 방법 1: 직접 계산하여 추가
df['월급'] = df['연봉'] / 12

# 방법 2: 고정값 추가
df['회사'] = '테크 기업'

# 방법 3: 조건부 값 추가
df['등급'] = df['연봉'].apply(lambda x: 'A' if x >= 50000000 else 'B')

print("\n📊 열 추가 후 DataFrame:")
print(df)

# 출력:
#     이름      연봉        월급    회사 등급
# 0  홍길동  45000000  3750000.0  테크 기업  B
# 1  김철수  55000000  4583333.3  테크 기업  A
# 2  이영희  38000000  3166666.7  테크 기업  B
```

### 예제 8: 실무 예제 - 직원 데이터 분석 (핵심 예제)

```python
import pandas as pd

# 직원 데이터
employees = [
    {'이름': '홍길동', '부서': '영업팀', '직급': '대리', '연봉': 45000000, '입사년도': 2020},
    {'이름': '김철수', '부서': '개발팀', '직급': '과장', '연봉': 55000000, '입사년도': 2018},
    {'이름': '이영희', '부서': '인사팀', '직급': '사원', '연봉': 38000000, '입사년도': 2022},
    {'이름': '박민수', '부서': '영업팀', '직급': '과장', '연봉': 52000000, '입사년도': 2019},
    {'이름': '정수진', '부서': '개발팀', '직급': '대리', '연봉': 47000000, '입사년도': 2021},
    {'이름': '최동욱', '부서': '영업팀', '직급': '사원', '연봉': 40000000, '입사년도': 2023}
]

df = pd.DataFrame(employees)

print("📊 전체 직원 데이터:")
print(df)

# 1. 부서별 평균 연봉
print("\n📊 부서별 평균 연봉:")
dept_avg = df.groupby('부서')['연봉'].mean()
print(dept_avg)

# 2. 직급별 인원수
print("\n📊 직급별 인원수:")
position_count = df['직급'].value_counts()
print(position_count)

# 3. 연봉이 가장 높은 직원
print("\n📊 최고 연봉자:")
max_salary_employee = df.loc[df['연봉'].idxmax()]
print(f"{max_salary_employee['이름']} - {max_salary_employee['연봉']:,}원")

# 4. 영업팀 직원만 필터링
print("\n📊 영업팀 직원:")
sales_df = df[df['부서'] == '영업팀']
print(sales_df[['이름', '직급', '연봉']])

# 5. 연봉을 천만원 단위로 표시
df['연봉(천만)'] = df['연봉'] / 10000000
print("\n📊 연봉(천만원 단위):")
print(df[['이름', '연봉(천만)']])
```

---

## 3) 코드 상세 설명

### DataFrame vs 딕셔너리 vs 리스트

**비교 표:**

| 구조 | Python 기본 | Pandas |
|------|-------------|--------|
| 1차원 | list | Series |
| 2차원(표) | list of lists or dict | DataFrame |

**변환 예시:**
```python
# 딕셔너리 → DataFrame
data_dict = {'이름': ['홍길동'], '나이': [30]}
df = pd.DataFrame(data_dict)

# DataFrame → 딕셔너리
back_to_dict = df.to_dict()

# DataFrame → 리스트
back_to_list = df.values.tolist()
```

### head() vs tail()

```python
df.head()     # 기본 5행
df.head(3)    # 3행
df.head(10)   # 10행

df.tail()     # 마지막 5행
df.tail(2)    # 마지막 2행
```

**용도:**
- 데이터 구조 빠르게 확인
- 샘플 데이터 확인
- 코드 실행 결과 미리보기

### loc vs iloc

**loc: 라벨(인덱스 이름)로 선택**
```python
df.loc[0]         # 인덱스 0인 행
df.loc[0:2]       # 인덱스 0, 1, 2 (끝 포함!)
df.loc[:, '이름']  # 모든 행의 '이름' 열
```

**iloc: 정수 위치로 선택**
```python
df.iloc[0]        # 0번째 행
df.iloc[0:2]      # 0, 1번째 행 (끝 미포함!)
df.iloc[:, 0]     # 모든 행의 0번째 열
```

**차이점:**
- `loc`: 라벨 기반, 끝 인덱스 **포함**
- `iloc`: 위치 기반, 끝 인덱스 **미포함**

### groupby() 이해하기

```python
# 부서별 그룹화
grouped = df.groupby('부서')

# 각 그룹의 평균
grouped.mean()

# 각 그룹의 합계
grouped.sum()

# 각 그룹의 개수
grouped.count()

# 특정 열만 선택하여 집계
df.groupby('부서')['연봉'].mean()
```

**직장인 예시:**
- 부서별 평균 연봉
- 지역별 매출 합계
- 제품별 판매 수량

### apply() 함수

```python
# 각 값에 함수 적용
df['연봉'].apply(lambda x: x / 12)  # 월급 계산

# 조건부 값 생성
def grade(salary):
    if salary >= 50000000:
        return 'A'
    elif salary >= 40000000:
        return 'B'
    else:
        return 'C'

df['등급'] = df['연봉'].apply(grade)
```

**apply vs 반복문:**
- `apply`: 빠르고 간결
- 반복문: 느리고 코드가 길어짐

---

## 4) 실습 미션

### 미션 1: 딕셔너리로 DataFrame 생성 ⭐
**목표:** 고객 정보 딕셔너리를 DataFrame으로 변환하세요.

**데이터:**
```python
customers = {
    '고객명': ['ABC기업', 'XYZ회사', 'DEF상사'],
    '담당자': ['홍길동', '김철수', '이영희'],
    '계약금액': [100000000, 50000000, 75000000]
}
```

**요구사항:**
- DataFrame 생성
- `print(df)` 로 출력

---

### 미션 2: 특정 조건의 데이터 필터링 ⭐⭐
**목표:** 계약금액이 60000000 이상인 고객만 추출하세요.

**요구사항:**
- 미션 1의 DataFrame 사용
- 조건: `계약금액 >= 60000000`
- 필터링된 DataFrame 출력

**힌트:**
```python
filtered_df = df[df['계약금액'] >= 60000000]
```

---

### 미션 3: 월별 매출 데이터 DataFrame 생성 및 분석 ⭐⭐⭐
**목표:** 월별 매출 데이터를 DataFrame으로 만들고 분석하세요.

**데이터:**
```python
sales = [
    {'월': 1, '매출': 15000000, '목표': 20000000},
    {'월': 2, '매출': 18000000, '목표': 20000000},
    {'월': 3, '매출': 22000000, '목표': 20000000},
    {'월': 4, '매출': 19000000, '목표': 20000000}
]
```

**요구사항:**
1. DataFrame 생성
2. '달성률' 열 추가 (매출/목표 * 100)
3. 평균 매출 계산
4. 목표 달성한 월(100% 이상) 출력

---

### 미션 4: CSV 데이터를 DataFrame으로 변환 후 분석 ⭐⭐⭐
**목표:** CSV 형식의 직원 데이터를 리스트로 준비하고, DataFrame으로 변환한 후 분석하세요.

**데이터:**
```python
employees = [
    ['홍길동', '영업팀', 45000000],
    ['김철수', '개발팀', 55000000],
    ['이영희', '영업팀', 42000000],
    ['박민수', '개발팀', 58000000],
    ['정수진', '인사팀', 40000000]
]
```

**요구사항:**
1. 컬럼명: ['이름', '부서', '연봉']
2. DataFrame 생성
3. 부서별 평균 연봉 계산
4. 가장 높은 연봉의 직원 이름과 연봉 출력

---

## 5) 퀴즈

### 퀴즈 1 (기본 개념) 📝
Pandas에서 표(테이블) 형태의 2차원 데이터 구조를 무엇이라고 하나요?

**A)** Series  
**B)** DataFrame  
**C)** Array  
**D)** List

---

### 퀴즈 2 (코드 실행) 📝
다음 코드의 출력 결과는?

```python
import pandas as pd

data = {'이름': ['홍길동', '김철수'], '나이': [30, 35]}
df = pd.DataFrame(data)

print(len(df))
```

**A)** 1  
**B)** 2  
**C)** 3  
**D)** 에러 발생

---

### 퀴즈 3 (응용 문제) 📝
다음 중 DataFrame의 처음 10행을 보는 올바른 방법은?

**A)** `df.head()`  
**B)** `df.head(10)`  
**C)** `df.top(10)`  
**D)** `df.first(10)`

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **B) DataFrame**

**해설:**
- **Series**: 1차원 데이터 (한 개의 열)
- **DataFrame**: 2차원 데이터 (표 형태) ✅
- **Array**: NumPy의 배열
- **List**: Python 기본 리스트

**DataFrame의 특징:**
- 행(Row)과 열(Column)로 구성
- 엑셀 시트와 유사한 구조
- 각 열은 Series 객체

**예시:**
```python
import pandas as pd

# DataFrame 생성
df = pd.DataFrame({
    '이름': ['홍길동', '김철수'],
    '나이': [30, 35]
})

print(type(df))  # <class 'pandas.core.frame.DataFrame'>
```

---

### 퀴즈 2 정답: **B) 2**

**해설:**

**코드 분석:**
```python
data = {'이름': ['홍길동', '김철수'], '나이': [30, 35]}
df = pd.DataFrame(data)
```

**생성된 DataFrame:**
```
     이름  나이
0  홍길동  30
1  김철수  35
```

**len(df) 의미:**
- DataFrame의 **행(row) 개수**를 반환
- 2개의 행이 있으므로 → **2**

**참고:**
- 열 개수 확인: `len(df.columns)` → 2
- Shape 확인: `df.shape` → (2, 2) → (행, 열)

---

### 퀴즈 3 정답: **B) df.head(10)**

**해설:**

**head() 메서드:**
```python
df.head()      # 기본값: 처음 5행
df.head(10)    # 처음 10행 ✅
df.head(3)     # 처음 3행
```

**다른 선택지:**
- **A)** `df.head()` ❌ - 5행만 보여줌 (기본값)
- **C)** `df.top(10)` ❌ - 존재하지 않는 메서드
- **D)** `df.first(10)` ❌ - 시간 기반 선택 메서드 (다른 용도)

**관련 메서드:**
```python
df.head(n)    # 처음 n행
df.tail(n)    # 마지막 n행
df.sample(n)  # 랜덤 n행
```

**실무 활용:**
```python
# 대용량 데이터 미리보기
df = pd.read_csv('large_file.csv')
print(df.head(10))  # 전체가 아닌 10행만 확인
```

---

## 💡 5교시 핵심 요약

### Pandas DataFrame 핵심 3단계
1. **생성**: 딕셔너리/리스트 → DataFrame
2. **조회**: head(), info(), describe()
3. **조작**: 열/행 선택, 필터링, 그룹화

### DataFrame 생성 방법

| 방법 | 코드 | 용도 |
|------|------|------|
| 딕셔너리 | `pd.DataFrame({'열1': [값들]})` | 가장 직관적 |
| 리스트 | `pd.DataFrame([행들], columns=[...])` | CSV 변환 시 |
| 딕셔너리 리스트 | `pd.DataFrame([{행1}, {행2}])` | JSON 변환 시 |

### 필수 메서드 5가지

1. **head(n)**: 처음 n행 보기
2. **info()**: 데이터 타입, 개수 확인
3. **describe()**: 통계 요약 (평균, 최대, 최소 등)
4. **groupby()**: 그룹별 집계
5. **apply()**: 함수 적용

### 실무 활용 팁
✅ 엑셀 대신 DataFrame으로 데이터 관리
✅ `groupby()`로 부서별/월별 집계 자동화
✅ 조건 필터링으로 원하는 데이터만 추출
✅ `apply()`로 복잡한 계산 간단하게
✅ CSV/JSON 데이터를 바로 DataFrame으로 변환

### DataFrame vs 엑셀

| 특징 | 엑셀 | Pandas DataFrame |
|------|------|------------------|
| 용량 | 100만 행 제한 | 제한 없음 |
| 속도 | 느림 | 매우 빠름 |
| 자동화 | 매크로 필요 | 코드로 간단히 |
| 반복 작업 | 수동 | 자동 |

---

## 🎯 다음 교시 예고

**6교시: read_csv()로 대용량 CSV 파일 불러오기**
- `pd.read_csv()` 함수 상세
- 인코딩 문제 해결
- 대용량 파일 효율적으로 읽기
- **실습 프로젝트:** 실제 매출 데이터 CSV 파일 분석

---

**5교시를 완료하셨습니다! 수고하셨습니다! 🎉**

"다음 교시"를 입력하시면 6교시 내용을 시작하겠습니다.

---
---

# 📘 6교시: read_csv()로 대용량 CSV 파일 불러오기

---

## 1) 이론 설명

### pd.read_csv()란?

**read_csv()**는 Pandas에서 CSV 파일을 DataFrame으로 읽어오는 가장 중요한 함수입니다.

**직장인 예시로 이해하기:**
- 엑셀 파일을 Python으로 불러오기
- 수백만 건의 매출 데이터 로드
- 고객 명단, 재고 현황 등 업무 데이터 처리
- 수작업 없이 자동으로 데이터 분석

### read_csv() 기본 사용법

```python
import pandas as pd

df = pd.read_csv('파일명.csv')
```

**간단하지만 강력!**
- 자동으로 헤더 인식
- 데이터 타입 자동 추론
- 대용량 파일도 빠르게 처리

### 주요 파라미터

**1. encoding (인코딩)**
```python
df = pd.read_csv('data.csv', encoding='utf-8')
df = pd.read_csv('data.csv', encoding='cp949')  # Windows 한글
```

**인코딩 문제 해결:**
- `utf-8`: 대부분의 파일 (권장)
- `cp949` 또는 `euc-kr`: Windows에서 생성된 한글 파일
- 에러 발생 시 다른 인코딩 시도

**2. header (헤더 행 지정)**
```python
df = pd.read_csv('data.csv', header=0)  # 첫 번째 행이 헤더 (기본값)
df = pd.read_csv('data.csv', header=None)  # 헤더 없음
df = pd.read_csv('data.csv', header=2)  # 3번째 행이 헤더
```

**3. names (컬럼명 지정)**
```python
df = pd.read_csv('data.csv', names=['이름', '나이', '직급'])
```

**4. usecols (특정 열만 읽기)**
```python
df = pd.read_csv('data.csv', usecols=['이름', '연봉'])  # 필요한 열만
```

**5. nrows (행 개수 제한)**
```python
df = pd.read_csv('data.csv', nrows=100)  # 처음 100행만
```

**6. dtype (데이터 타입 지정)**
```python
df = pd.read_csv('data.csv', dtype={'나이': int, '이름': str})
```

### 대용량 파일 처리 방법

**1. 필요한 열만 읽기**
```python
# 전체 100개 열 중 5개만 필요
df = pd.read_csv('large.csv', usecols=['열1', '열2', '열3', '열4', '열5'])
```

**2. 샘플링하여 읽기**
```python
# 전체 중 처음 1000행만 확인
df_sample = pd.read_csv('large.csv', nrows=1000)
```

**3. 청크 단위로 읽기**
```python
# 파일을 나눠서 읽기
chunk_size = 10000
for chunk in pd.read_csv('large.csv', chunksize=chunk_size):
    # chunk별로 처리
    process(chunk)
```

### 인코딩 에러 해결

**에러 예시:**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte...
```

**해결 방법:**
```python
# 방법 1: cp949 시도
try:
    df = pd.read_csv('data.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('data.csv', encoding='cp949')

# 방법 2: errors 파라미터
df = pd.read_csv('data.csv', encoding='utf-8', errors='ignore')
```

---

## 2) 실습 예제 코드

### 예제 1: 기본 CSV 파일 읽기

```python
import pandas as pd

# 먼저 샘플 CSV 파일 생성
sample_data = {
    '이름': ['홍길동', '김철수', '이영희', '박민수'],
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀'],
    '연봉': [45000000, 55000000, 38000000, 52000000]
}
df_sample = pd.DataFrame(sample_data)
df_sample.to_csv('employees.csv', index=False, encoding='utf-8')

# CSV 파일 읽기
df = pd.read_csv('employees.csv')

print("📊 CSV 파일에서 읽은 데이터:")
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# 출력:
# 📊 CSV 파일에서 읽은 데이터:
#     이름   부서      연봉
# 0  홍길동  영업팀  45000000
# 1  김철수  개발팀  55000000
# 2  이영희  인사팀  38000000
# 3  박민수  영업팀  52000000
```

### 예제 2: 인코딩 지정하여 읽기

```python
import pandas as pd

# UTF-8 인코딩으로 저장
df = pd.DataFrame({
    '제품명': ['노트북', '마우스', '키보드'],
    '가격': [1500000, 30000, 80000]
})
df.to_csv('products_utf8.csv', index=False, encoding='utf-8')

# UTF-8로 읽기
df_utf8 = pd.read_csv('products_utf8.csv', encoding='utf-8')
print("📊 UTF-8 인코딩 파일:")
print(df_utf8)

# CP949 인코딩으로 저장 (Windows 한글)
df.to_csv('products_cp949.csv', index=False, encoding='cp949')

# CP949로 읽기
df_cp949 = pd.read_csv('products_cp949.csv', encoding='cp949')
print("\n📊 CP949 인코딩 파일:")
print(df_cp949)
```

### 예제 3: 특정 열만 선택하여 읽기

```python
import pandas as pd

# 여러 컬럼이 있는 CSV 생성
df_full = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '부서': ['영업팀', '개발팀', '인사팀'],
    '직급': ['대리', '과장', '사원'],
    '연봉': [45000000, 55000000, 38000000],
    '입사년도': [2020, 2018, 2022],
    '이메일': ['hong@company.com', 'kim@company.com', 'lee@company.com']
})
df_full.to_csv('employees_full.csv', index=False, encoding='utf-8')

# 필요한 열만 읽기
df_selected = pd.read_csv('employees_full.csv', 
                          usecols=['이름', '부서', '연봉'],
                          encoding='utf-8')

print("📊 선택한 열만 읽기:")
print(df_selected)

# 출력:
#     이름   부서      연봉
# 0  홍길동  영업팀  45000000
# 1  김철수  개발팀  55000000
# 2  이영희  인사팀  38000000
```

### 예제 4: 대용량 파일 미리보기 (핵심 예제)

```python
import pandas as pd

# 큰 데이터셋 시뮬레이션 (실제로는 수백만 행)
large_data = {
    '날짜': ['2024-01-01'] * 1000 + ['2024-01-02'] * 1000,
    '제품코드': ['P001', 'P002'] * 1000,
    '판매량': list(range(2000)),
    '매출': [x * 10000 for x in range(2000)]
}
df_large = pd.DataFrame(large_data)
df_large.to_csv('sales_large.csv', index=False, encoding='utf-8')

# 방법 1: 처음 10행만 읽기
df_preview = pd.read_csv('sales_large.csv', nrows=10, encoding='utf-8')
print("📊 처음 10행 미리보기:")
print(df_preview)

# 방법 2: 파일 정보만 확인
df_full = pd.read_csv('sales_large.csv', encoding='utf-8')
print(f"\n📊 전체 파일 정보:")
print(f"Shape: {df_full.shape}")
print(f"Memory Usage: {df_full.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"\nColumns: {df_full.columns.tolist()}")
print(f"\nFirst 5 rows:")
print(df_full.head())
```

### 예제 5: 헤더가 없는 CSV 파일 읽기

```python
import pandas as pd

# 헤더 없는 CSV 생성
data = [
    ['홍길동', '영업팀', 45000000],
    ['김철수', '개발팀', 55000000],
    ['이영희', '인사팀', 38000000]
]
df_no_header = pd.DataFrame(data)
df_no_header.to_csv('no_header.csv', index=False, header=False)

# 방법 1: 자동 컬럼명 (0, 1, 2...)
df1 = pd.read_csv('no_header.csv', header=None)
print("📊 자동 컬럼명:")
print(df1)

# 방법 2: 직접 컬럼명 지정
df2 = pd.read_csv('no_header.csv', 
                  header=None,
                  names=['이름', '부서', '연봉'])
print("\n📊 컬럼명 지정:")
print(df2)
```

### 예제 6: 데이터 타입 지정하여 읽기

```python
import pandas as pd

# CSV 생성
df_sample = pd.DataFrame({
    '직원ID': ['001', '002', '003'],
    '이름': ['홍길동', '김철수', '이영희'],
    '연봉': [45000000, 55000000, 38000000]
})
df_sample.to_csv('employees_dtype.csv', index=False, encoding='utf-8')

# 데이터 타입 지정
dtype_dict = {
    '직원ID': str,  # 문자열로 유지
    '이름': str,
    '연봉': int
}

df = pd.read_csv('employees_dtype.csv', dtype=dtype_dict, encoding='utf-8')

print("📊 데이터 타입 정보:")
print(df.dtypes)
print("\n데이터:")
print(df)

# 직원ID가 문자열로 유지됨 (001, 002, 003)
```

### 예제 7: 실무 예제 - 월별 매출 데이터 분석 (핵심 예제)

```python
import pandas as pd

# 월별 매출 데이터 생성
monthly_sales = {
    '월': [f'2024-{i:02d}' for i in range(1, 13)],
    '매출': [15000000, 18000000, 22000000, 19000000, 
             21000000, 25000000, 23000000, 24000000,
             26000000, 28000000, 30000000, 35000000],
    '목표': [20000000] * 12,
    '지역': ['서울', '부산', '서울', '대구', '서울', '부산',
            '서울', '대구', '서울', '부산', '서울', '대구']
}
df_sales = pd.DataFrame(monthly_sales)
df_sales.to_csv('monthly_sales.csv', index=False, encoding='utf-8')

# CSV 파일 읽기 및 분석
df = pd.read_csv('monthly_sales.csv', encoding='utf-8')

print("📊 월별 매출 데이터:")
print(df.head())

# 분석 1: 총 매출
total_sales = df['매출'].sum()
print(f"\n총 매출: {total_sales:,}원")

# 분석 2: 평균 매출
avg_sales = df['매출'].mean()
print(f"평균 매출: {avg_sales:,.0f}원")

# 분석 3: 목표 달성률
df['달성률'] = (df['매출'] / df['목표'] * 100).round(1)
print(f"\n📊 달성률 추가:")
print(df[['월', '매출', '목표', '달성률']].head())

# 분석 4: 지역별 매출
region_sales = df.groupby('지역')['매출'].sum()
print(f"\n📊 지역별 총 매출:")
print(region_sales)

# 분석 5: 최고 매출 월
max_month = df.loc[df['매출'].idxmax()]
print(f"\n🏆 최고 매출 월: {max_month['월']} - {max_month['매출']:,}원")
```

### 예제 8: 인코딩 에러 처리

```python
import pandas as pd

# 인코딩 에러 안전하게 처리하는 함수
def safe_read_csv(filename):
    """다양한 인코딩을 시도하여 CSV 파일 읽기"""
    encodings = ['utf-8', 'cp949', 'euc-kr', 'latin-1']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(filename, encoding=encoding)
            print(f"✅ 성공! 인코딩: {encoding}")
            return df
        except UnicodeDecodeError:
            print(f"❌ {encoding} 실패, 다음 인코딩 시도...")
            continue
        except Exception as e:
            print(f"❌ {encoding}에서 다른 에러: {e}")
            continue
    
    print("❌ 모든 인코딩 시도 실패")
    return None

# 사용 예시
df_sample = pd.DataFrame({
    '이름': ['홍길동', '김철수'],
    '부서': ['영업팀', '개발팀']
})
df_sample.to_csv('test_encoding.csv', index=False, encoding='utf-8')

df = safe_read_csv('test_encoding.csv')
if df is not None:
    print("\n📊 읽은 데이터:")
    print(df)
```

---

## 3) 코드 상세 설명

### read_csv() 전체 프로세스

```python
df = pd.read_csv('file.csv', encoding='utf-8')
```

**단계별 동작:**
1. 파일 열기
2. 인코딩 확인 및 디코드
3. 첫 행을 헤더로 인식
4. 각 열의 데이터 타입 자동 추론
5. DataFrame 객체 생성
6. 메모리에 로드

### encoding 파라미터의 중요성

| 인코딩 | 설명 | 사용처 |
|--------|------|--------|
| utf-8 | 유니코드 표준 | 대부분의 최신 파일 |
| cp949 | Windows 한글 | Windows 엑셀에서 생성 |
| euc-kr | 한국어 인코딩 | 옛날 시스템 |
| latin-1 | 서유럽 문자 | 영문 파일 |

**문제 상황:**
```python
# Windows 엑셀에서 저장한 파일
df = pd.read_csv('file.csv', encoding='utf-8')  # ❌ 에러!
df = pd.read_csv('file.csv', encoding='cp949')  # ✅ 성공!
```

### usecols로 메모리 절약

```python
# 전체 읽기 (100개 컬럼)
df_all = pd.read_csv('large.csv')  # 메모리 많이 사용

# 필요한 5개만 읽기
df_selected = pd.read_csv('large.csv', 
                          usecols=['col1', 'col2', 'col3', 'col4', 'col5'])
# 메모리 95% 절약!
```

**효과:**
- 로딩 속도 향상
- 메모리 사용량 감소
- 불필요한 데이터 제외

### nrows로 샘플링

```python
# 전체 100만 행 읽기
df_full = pd.read_csv('huge.csv')  # 느림!

# 처음 1000행만 미리보기
df_sample = pd.read_csv('huge.csv', nrows=1000)  # 빠름!
```

**활용:**
- 데이터 구조 빠르게 확인
- 코드 테스트
- 샘플 분석

### chunksize로 분할 처리

```python
chunk_size = 10000
for chunk in pd.read_csv('huge.csv', chunksize=chunk_size):
    # chunk는 10000행씩 처리
    process(chunk)
```

**장점:**
- 메모리 부담 감소
- 대용량 파일 처리 가능
- 실시간 처리

---

## 4) 실습 미션

### 미션 1: CSV 파일 읽고 정보 확인 ⭐
**목표:** CSV 파일을 읽고 기본 정보를 출력하세요.

**요구사항:**
1. `employees.csv` 파일 생성 (이름, 부서, 연봉 포함)
2. `read_csv()`로 읽기
3. `shape`, `columns`, `head()` 출력

---

### 미션 2: 특정 열만 선택하여 읽기 ⭐⭐
**목표:** 대용량 CSV 파일에서 필요한 열만 읽어오세요.

**요구사항:**
- 10개 컬럼 중 3개만 선택
- `usecols` 파라미터 사용
- 메모리 사용량 비교

---

### 미션 3: 인코딩 문제 해결 ⭐⭐⭐
**목표:** 여러 인코딩을 시도하여 파일을 읽는 함수 작성

**요구사항:**
- 함수명: `read_csv_auto_encoding(filename)`
- utf-8, cp949, euc-kr 순서로 시도
- 성공한 인코딩 출력
- DataFrame 반환

---

### 미션 4: 월별 매출 분석 자동화 ⭐⭐⭐
**목표:** CSV 파일에서 매출 데이터를 읽어 자동 분석

**요구사항:**
1. `sales.csv` 파일 읽기
2. 총 매출, 평균 매출 계산
3. 월별 최고/최저 매출 찾기
4. 결과를 새로운 CSV로 저장

---

## 5) 퀴즈

### 퀴즈 1 (기본 개념) 📝
CSV 파일을 DataFrame으로 읽어오는 Pandas 함수는?

**A)** `pd.load_csv()`  
**B)** `pd.read_csv()`  
**C)** `pd.import_csv()`  
**D)** `pd.open_csv()`

---

### 퀴즈 2 (인코딩) 📝
Windows 엑셀에서 저장한 한글 CSV 파일을 읽을 때 자주 사용하는 인코딩은?

**A)** `utf-8`  
**B)** `cp949`  
**C)** `ascii`  
**D)** `latin-1`

---

### 퀴즈 3 (응용 문제) 📝
100만 행의 CSV 파일에서 처음 1000행만 빠르게 확인하려면?

**A)** `df = pd.read_csv('file.csv'); df.head(1000)`  
**B)** `df = pd.read_csv('file.csv', rows=1000)`  
**C)** `df = pd.read_csv('file.csv', nrows=1000)`  
**D)** `df = pd.read_csv('file.csv', limit=1000)`

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **B) pd.read_csv()**

**해설:**
- `pd.read_csv()`: CSV 파일 → DataFrame ✅
- 나머지는 존재하지 않는 함수

**기본 사용법:**
```python
import pandas as pd
df = pd.read_csv('data.csv')
```

---

### 퀴즈 2 정답: **B) cp949**

**해설:**

**Windows 엑셀의 특징:**
- Windows 한글 엑셀은 기본적으로 cp949 인코딩 사용
- UTF-8로 읽으면 한글이 깨짐

**해결 방법:**
```python
# ❌ UTF-8로 읽으면 에러
df = pd.read_csv('excel_file.csv', encoding='utf-8')

# ✅ CP949로 읽기
df = pd.read_csv('excel_file.csv', encoding='cp949')
```

**다른 인코딩:**
- **utf-8**: 최신 시스템, 웹
- **ascii**: 영문만
- **latin-1**: 서유럽 문자

---

### 퀴즈 3 정답: **C) df = pd.read_csv('file.csv', nrows=1000)**

**해설:**

**선택지 분석:**

**A)** `df = pd.read_csv('file.csv'); df.head(1000)` ❌
- 전체 100만 행을 먼저 읽음 → 느림
- 메모리 낭비

**B)** `df = pd.read_csv('file.csv', rows=1000)` ❌
- `rows` 파라미터는 존재하지 않음

**C)** `df = pd.read_csv('file.csv', nrows=1000)` ✅
- 처음 1000행만 읽음
- 빠르고 메모리 효율적

**D)** `df = pd.read_csv('file.csv', limit=1000)` ❌
- `limit` 파라미터는 존재하지 않음

**올바른 방법:**
```python
# 대용량 파일 미리보기
df_sample = pd.read_csv('large_file.csv', nrows=1000)
print(df_sample.head())
```

---

## 💡 6교시 핵심 요약

### read_csv() 필수 파라미터 5가지

1. **encoding**: 인코딩 지정 (utf-8, cp949)
2. **header**: 헤더 행 위치
3. **names**: 컬럼명 직접 지정
4. **usecols**: 필요한 열만 선택
5. **nrows**: 읽을 행 개수 제한

### 인코딩 문제 해결 3단계

1. UTF-8 시도
2. 실패하면 CP949 시도
3. 그래도 실패하면 EUC-KR 시도

### 대용량 파일 처리 전략

✅ **usecols**로 필요한 열만 읽기
✅ **nrows**로 샘플링
✅ **chunksize**로 분할 처리
✅ **dtype** 지정으로 메모리 최적화

---

---

# 📘 7교시: head(), info(), describe()로 데이터 정보 확인

---

## 1) 이론 설명

### 데이터 탐색의 중요성

**데이터 분석 첫 단계:**
1. 데이터 읽기 (`read_csv()`)
2. **데이터 탐색 (Exploration)** ← 7교시 내용
3. 데이터 정제 (Cleaning)
4. 데이터 분석 (Analysis)

**직장인 예시:**
- 보고서 작성 전 데이터 확인
- 이상치 발견
- 데이터 구조 파악
- 통계 요약 생성

### head() - 데이터 미리보기

**기능:** DataFrame의 처음 n행 출력

```python
df.head()     # 처음 5행 (기본값)
df.head(10)   # 처음 10행
df.head(3)    # 처음 3행
```

**용도:**
- 데이터 구조 빠르게 확인
- 샘플 데이터 보기
- 컬럼명 확인

### tail() - 끝부분 보기

**기능:** DataFrame의 마지막 n행 출력

```python
df.tail()     # 마지막 5행
df.tail(10)   # 마지막 10행
```

**용도:**
- 데이터 끝 확인
- 최신 데이터 보기 (시계열 데이터)

### info() - 데이터 정보 요약

**기능:** DataFrame의 전체적인 정보 출력

```python
df.info()
```

**출력 내용:**
- 행/열 개수
- 각 열의 데이터 타입
- Null 값 개수
- 메모리 사용량

**예시 출력:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   이름    100 non-null    object
 1   나이    98 non-null     float64
 2   연봉    100 non-null    int64  
```

### describe() - 통계 요약

**기능:** 수치형 데이터의 통계 정보 출력

```python
df.describe()
```

**출력 내용:**
- count: 데이터 개수
- mean: 평균
- std: 표준편차
- min: 최소값
- 25%, 50%, 75%: 사분위수
- max: 최대값

**예시 출력:**
```
              나이          연봉
count   100.000000  1.000000e+02
mean     35.500000  4.750000e+07
std       5.200000  5.500000e+06
min      25.000000  3.800000e+07
25%      30.000000  4.250000e+07
50%      35.000000  4.500000e+07
75%      40.000000  5.250000e+07
max      50.000000  6.000000e+07
```

### 데이터 탐색 3단계

**1단계: 구조 파악**
```python
df.head()      # 샘플 보기
df.shape       # (행, 열) 개수
df.columns     # 컬럼 목록
```

**2단계: 타입 확인**
```python
df.info()      # 전체 정보
df.dtypes      # 데이터 타입
```

**3단계: 통계 확인**
```python
df.describe()  # 통계 요약
df.isnull().sum()  # Null 개수
```

---

## 2) 실습 예제 코드

### 예제 1: head()와 tail() 기본 사용

```python
import pandas as pd

# 샘플 데이터 생성
employees = {
    '이름': ['홍길동', '김철수', '이영희', '박민수', '정수진', 
            '최동욱', '강민지', '윤서연', '장한별', '오지혜'],
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀', '개발팀',
            '영업팀', '인사팀', '개발팀', '영업팀', '인사팀'],
    '연봉': [45000000, 55000000, 38000000, 52000000, 47000000,
            43000000, 40000000, 58000000, 46000000, 42000000]
}
df = pd.DataFrame(employees)

print("📊 head() - 처음 5행:")
print(df.head())

print("\n📊 head(3) - 처음 3행:")
print(df.head(3))

print("\n📊 tail() - 마지막 5행:")
print(df.tail())

print("\n📊 tail(2) - 마지막 2행:")
print(df.tail(2))
```

### 예제 2: info()로 데이터 정보 확인

```python
import pandas as pd
import numpy as np

# Null 값이 포함된 데이터
employees = {
    '이름': ['홍길동', '김철수', '이영희', None, '정수진'],
    '나이': [30, 35, 28, 32, None],
    '부서': ['영업팀', '개발팀', None, '영업팀', '개발팀'],
    '연봉': [45000000, 55000000, 38000000, 52000000, 47000000]
}
df = pd.DataFrame(employees)

print("📊 DataFrame 정보:")
df.info()

# 출력:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   이름      4 non-null      object 
#  1   나이      4 non-null      float64
#  2   부서      4 non-null      object 
#  3   연봉      5 non-null      int64  
# dtypes: float64(1), int64(1), object(2)
# memory usage: 288.0+ bytes

print("\n📊 추가 정보:")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Data types:\n{df.dtypes}")
```

### 예제 3: describe()로 통계 요약

```python
import pandas as pd

# 직원 데이터
employees = {
    '이름': ['홍길동', '김철수', '이영희', '박민수', '정수진'],
    '나이': [30, 35, 28, 32, 29],
    '연봉': [45000000, 55000000, 38000000, 52000000, 47000000],
    '근속연수': [5, 8, 2, 6, 4]
}
df = pd.DataFrame(employees)

print("📊 수치형 데이터 통계 요약:")
print(df.describe())

print("\n📊 특정 열만 통계:")
print(df['연봉'].describe())

print("\n📊 소수점 자리수 조정:")
print(df.describe().round(2))
```

### 예제 4: 종합 데이터 탐색 (핵심 예제)

```python
import pandas as pd
import numpy as np

# 실무 데이터 시뮬레이션
np.random.seed(42)
n = 100

sales_data = {
    '날짜': pd.date_range('2024-01-01', periods=n, freq='D'),
    '지역': np.random.choice(['서울', '부산', '대구', '인천'], n),
    '제품': np.random.choice(['A', 'B', 'C'], n),
    '판매량': np.random.randint(10, 100, n),
    '매출': np.random.randint(100000, 1000000, n)
}
df = pd.DataFrame(sales_data)

# CSV로 저장
df.to_csv('sales_data.csv', index=False, encoding='utf-8')

# 1단계: 데이터 읽기
df = pd.read_csv('sales_data.csv', encoding='utf-8')
print("✅ 데이터 로드 완료\n")

# 2단계: 기본 정보 확인
print("📊 1. 데이터 미리보기 (head):")
print(df.head())

print(f"\n📊 2. 데이터 크기: {df.shape[0]}행 x {df.shape[1]}열")

# 3단계: 상세 정보
print("\n📊 3. 데이터 정보 (info):")
df.info()

# 4단계: 통계 요약
print("\n📊 4. 통계 요약 (describe):")
print(df.describe())

# 5단계: Null 값 확인
print("\n📊 5. 결측값 확인:")
print(df.isnull().sum())

# 6단계: 고유값 개수
print("\n📊 6. 범주형 데이터 고유값:")
print(f"지역: {df['지역'].unique()}")
print(f"제품: {df['제품'].unique()}")
print(f"지역별 데이터 수:\n{df['지역'].value_counts()}")
```

### 예제 5: 데이터 품질 체크

```python
import pandas as pd
import numpy as np

# 문제가 있는 데이터 생성
problematic_data = {
    '이름': ['홍길동', '김철수', None, '박민수', '정수진'],
    '나이': [30, 35, 28, -5, 150],  # 이상치
    '연봉': [45000000, None, 38000000, 52000000, 47000000],  # 결측
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀', None]
}
df = pd.DataFrame(problematic_data)

print("📊 데이터 품질 체크")
print("=" * 50)

# 1. 결측값 확인
print("\n1. 결측값 개수:")
print(df.isnull().sum())

# 2. 데이터 타입 확인
print("\n2. 데이터 타입:")
print(df.dtypes)

# 3. 이상치 확인
print("\n3. 나이 통계 (이상치 발견):")
print(df['나이'].describe())

print("\n4. 나이가 이상한 데이터:")
print(df[(df['나이'] < 20) | (df['나이'] > 100)])

# 5. 데이터 완전성
total_cells = df.shape[0] * df.shape[1]
missing_cells = df.isnull().sum().sum()
completeness = (1 - missing_cells / total_cells) * 100

print(f"\n5. 데이터 완전성: {completeness:.1f}%")
```

### 예제 6: 부서별 연봉 분석

```python
import pandas as pd

# 직원 데이터
employees = {
    '이름': ['홍길동', '김철수', '이영희', '박민수', '정수진', '최동욱'],
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀', '개발팀', '영업팀'],
    '연봉': [45000000, 55000000, 38000000, 52000000, 47000000, 43000000]
}
df = pd.DataFrame(employees)

print("📊 전체 데이터:")
print(df)

# 부서별 그룹화하여 통계
print("\n📊 부서별 연봉 통계:")
dept_stats = df.groupby('부서')['연봉'].describe()
print(dept_stats)

# 부서별 평균
print("\n📊 부서별 평균 연봉:")
dept_avg = df.groupby('부서')['연봉'].mean().sort_values(ascending=False)
for dept, avg in dept_avg.items():
    print(f"{dept}: {avg:,.0f}원")
```

### 예제 7: 시계열 데이터 탐색

```python
import pandas as pd
import numpy as np

# 일별 매출 데이터
dates = pd.date_range('2024-01-01', '2024-01-31', freq='D')
sales = {
    '날짜': dates,
    '매출': np.random.randint(1000000, 5000000, len(dates)),
    '방문자': np.random.randint(100, 500, len(dates))
}
df = pd.DataFrame(sales)

print("📊 시계열 데이터 탐색:")
print(df.head())

print("\n📊 기간 정보:")
print(f"시작일: {df['날짜'].min()}")
print(f"종료일: {df['날짜'].max()}")
print(f"총 일수: {len(df)}일")

print("\n📊 매출 통계:")
print(f"총 매출: {df['매출'].sum():,}원")
print(f"평균 일 매출: {df['매출'].mean():,.0f}원")
print(f"최고 매출: {df['매출'].max():,}원")
print(f"최저 매출: {df['매출'].min():,}원")

print("\n📊 주말/평일 구분:")
df['요일'] = df['날짜'].dt.day_name()
print(df[['날짜', '요일', '매출']].head(10))
```

### 예제 8: 종합 보고서 생성 (핵심 예제)

```python
import pandas as pd
import numpy as np

# 월별 직원 데이터
employees = {
    '이름': ['홍길동', '김철수', '이영희', '박민수', '정수진', '최동욱', '강민지', '윤서연'],
    '부서': ['영업팀', '개발팀', '인사팀', '영업팀', '개발팀', '영업팀', '인사팀', '개발팀'],
    '직급': ['대리', '과장', '사원', '과장', '대리', '사원', '사원', '과장'],
    '연봉': [45000000, 55000000, 38000000, 52000000, 47000000, 43000000, 40000000, 58000000],
    '입사년도': [2020, 2018, 2022, 2019, 2021, 2023, 2022, 2017]
}
df = pd.DataFrame(employees)

# 종합 보고서
print("=" * 60)
print("📊 직원 데이터 종합 보고서")
print("=" * 60)

print("\n1️⃣ 데이터 개요")
print("-" * 60)
print(f"총 직원 수: {len(df)}명")
print(f"부서 수: {df['부서'].nunique()}개")
print(f"직급 수: {df['직급'].nunique()}개")

print("\n2️⃣ 샘플 데이터")
print("-" * 60)
print(df.head(3))

print("\n3️⃣ 데이터 정보")
print("-" * 60)
df.info()

print("\n4️⃣ 연봉 통계")
print("-" * 60)
print(df['연봉'].describe())

print("\n5️⃣ 부서별 현황")
print("-" * 60)
dept_summary = df.groupby('부서').agg({
    '이름': 'count',
    '연봉': ['mean', 'min', 'max']
})
dept_summary.columns = ['인원', '평균연봉', '최소연봉', '최고연봉']
print(dept_summary)

print("\n6️⃣ 직급별 현황")
print("-" * 60)
position_summary = df.groupby('직급').size()
print(position_summary)

print("\n7️⃣ 결론")
print("-" * 60)
print(f"✅ 평균 연봉: {df['연봉'].mean():,.0f}원")
print(f"✅ 최고 연봉자: {df.loc[df['연봉'].idxmax(), '이름']} ({df['연봉'].max():,}원)")
print(f"✅ 가장 많은 부서: {df['부서'].value_counts().index[0]} ({df['부서'].value_counts().iloc[0]}명)")
```

---

## 3) 코드 상세 설명

### head() vs tail() vs sample()

```python
df.head(5)    # 처음 5행
df.tail(5)    # 마지막 5행
df.sample(5)  # 랜덤 5행
```

**용도:**
- `head()`: 데이터 구조 확인
- `tail()`: 최신 데이터 확인
- `sample()`: 랜덤 샘플링

### info()가 보여주는 정보

```python
df.info()
```

**출력 항목:**
1. **클래스**: DataFrame 타입
2. **인덱스**: RangeIndex, DatetimeIndex 등
3. **컬럼**: 각 열의 이름
4. **Non-Null Count**: Null이 아닌 값 개수
5. **Dtype**: 데이터 타입
6. **Memory usage**: 메모리 사용량

### describe()의 통계 지표

| 지표 | 의미 | 활용 |
|------|------|------|
| count | 데이터 개수 | 결측값 확인 |
| mean | 평균 | 중심 경향 |
| std | 표준편차 | 분산 정도 |
| min | 최소값 | 이상치 확인 |
| 25% | 1사분위수 | 하위 25% |
| 50% | 중앙값 | 중심값 |
| 75% | 3사분위수 | 상위 25% |
| max | 최대값 | 이상치 확인 |

### 데이터 타입 확인

```python
# 전체 타입
df.dtypes

# 특정 열 타입
df['연봉'].dtype

# 타입별 컬럼 선택
df.select_dtypes(include=['int64', 'float64'])  # 숫자형만
df.select_dtypes(include=['object'])  # 문자형만
```

---

## 4) 실습 미션

### 미션 1: 데이터 기본 탐색 ⭐
**목표:** CSV 파일을 읽고 head(), info(), describe()로 탐색

**요구사항:**
1. 직원 데이터 CSV 파일 생성
2. `head()`로 처음 5행 확인
3. `info()`로 데이터 정보 확인
4. `describe()`로 통계 요약 확인

---

### 미션 2: 결측값 찾기 ⭐⭐
**목표:** 데이터에서 Null 값을 찾아 보고서 작성

**요구사항:**
- `isnull().sum()`으로 결측값 개수 계산
- 결측값 비율 계산 (%)
- 결측값이 있는 행 출력

---

### 미션 3: 부서별 통계 보고서 ⭐⭐⭐
**목표:** 부서별로 데이터를 그룹화하여 통계 생성

**요구사항:**
1. 부서별 직원 수
2. 부서별 평균/최소/최대 연봉
3. 가장 많은 직원이 있는 부서
4. 평균 연봉이 가장 높은 부서

---

### 미션 4: 종합 데이터 품질 리포트 ⭐⭐⭐
**목표:** 데이터 품질을 종합적으로 분석하는 함수 작성

**요구사항:**
- 함수명: `data_quality_report(df)`
- 출력 내용:
  1. 데이터 크기 (행, 열)
  2. 결측값 비율
  3. 데이터 타입 분포
  4. 수치형 데이터 통계 요약
  5. 범주형 데이터 고유값 개수
  
---

## 5) 퀴즈

### 퀴즈 1 (기본 개념) 📝
DataFrame의 처음 10행을 보려면?

**A)** `df.show(10)`  
**B)** `df.head(10)`  
**C)** `df.top(10)`  
**D)** `df.first(10)`

---

### 퀴즈 2 (info 이해) 📝
`df.info()`가 보여주지 않는 정보는?

**A)** 각 열의 데이터 타입  
**B)** Null 값 개수  
**C)** 데이터의 평균값  
**D)** 메모리 사용량

---

### 퀴즈 3 (응용 문제) 📝
다음 중 수치형 데이터의 통계 요약을 보는 함수는?

**A)** `df.summary()`  
**B)** `df.stats()`  
**C)** `df.describe()`  
**D)** `df.info()`

---

## 6) 정답 및 해설

### 퀴즈 1 정답: **B) df.head(10)**

**해설:**
```python
df.head()      # 처음 5행 (기본값)
df.head(10)    # 처음 10행 ✅
df.head(3)     # 처음 3행
```

**다른 선택지:**
- **A)** `df.show()` ❌ - Pandas에 없음 (Spark에 있음)
- **C)** `df.top()` ❌ - 존재하지 않음
- **D)** `df.first()` ❌ - 다른 용도

---

### 퀴즈 2 정답: **C) 데이터의 평균값**

**해설:**

**info()가 보여주는 것:**
- ✅ 데이터 타입 (Dtype)
- ✅ Null 값 개수 (Non-Null Count)
- ✅ 메모리 사용량 (Memory usage)
- ❌ 평균값 (이건 describe()에서 확인)

**평균값 확인:**
```python
df.describe()  # 평균, 표준편차, 최소, 최대 등
```

---

### 퀴즈 3 정답: **C) df.describe()**

**해설:**

**describe() 출력 내용:**
- count: 개수
- mean: 평균 ✅
- std: 표준편차
- min: 최소값
- 25%, 50%, 75%: 사분위수
- max: 최대값

**예시:**
```python
df.describe()

#               나이          연봉
# count   100.000000  1.000000e+02
# mean     35.500000  4.750000e+07  ← 평균
# std       5.200000  5.500000e+06
# min      25.000000  3.800000e+07
# ...
```

**다른 선택지:**
- **A)** `df.summary()` ❌ - 존재하지 않음
- **B)** `df.stats()` ❌ - 존재하지 않음
- **D)** `df.info()` ❌ - 통계 아닌 구조 정보

---

## 💡 7교시 핵심 요약

### 데이터 탐색 3대 함수

1. **head()**: 데이터 샘플 보기
2. **info()**: 구조와 타입 확인
3. **describe()**: 통계 요약

### 데이터 분석 워크플로우

```python
# 1. 데이터 로드
df = pd.read_csv('data.csv')

# 2. 기본 탐색
df.head()
df.info()
df.describe()

# 3. 결측값 확인
df.isnull().sum()

# 4. 분석 시작
...
```

### 실무 활용 팁

✅ **head()**: 코드 테스트 시 먼저 확인
✅ **info()**: Null 값과 타입 문제 파악
✅ **describe()**: 이상치 발견
✅ **value_counts()**: 범주형 데이터 분포 확인

---

## 🎉 전체 7교시 완료!

**축하합니다!** 직장인을 위한 파이썬 7교시 강의를 모두 완료하셨습니다!

### 배운 내용 총정리

1. **1교시**: 함수 정의와 환율 계산
2. **2교시**: 텍스트 파일 입출력
3. **3교시**: CSV 라이브러리 활용
4. **4교시**: JSON 데이터 처리
5. **5교시**: Pandas DataFrame 기초
6. **6교시**: read_csv()로 파일 읽기
7. **7교시**: 데이터 탐색 (head/info/describe)
---

**수고하셨습니다! 🚀**

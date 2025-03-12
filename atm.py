#balance : 통장 처음 만들 때 들어있는 기본금액
#1. 입금 / 2. 출금 / 3. 영수증 보기 / 4. 종료
#deposit_amount : 

balance = 3000

while True:
    num = input("사용할 서비스를 선택해주세요 (입금, 출금, 영수증 보기, 종료) :")

    if num == "입금" :
       deposit_amount = input("입금할 금액을 입력해주세요 :")
       if deposit_amount.isdigit() and int(deposit_amount) > 0:
           balance += int(deposit_amount)
           print(f'입금하신 금액은{deposit_amount}원이고, 입금 후 잔액은{balance}원 입니다.')

       else:
           print("제대로 된 금액을 입력해주세요.")

       
    if num == "출금" :
        pass 
    if num == "영수증 보기" :
        pass
    if num == "종료" :
        print("서비스를 종료합니다.")
        break
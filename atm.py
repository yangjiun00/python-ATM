#balance : 통장 처음 만들 때 들어있는 기본금액
#1. 입금 / 2. 출금 / 3. 영수증 보기 / 4. 종료
#deposit_amount : 
#영수증 타입은 list

#영수증을 위한 리스트
check = []

balance = 3000



while True:
    num = input("사용할 서비스를 선택해주세요 (입금, 출금, 영수증 보기, 종료) :")

    if num == "입금" :
       deposit_amount = input("입금할 금액을 입력해주세요 :")
       if deposit_amount.isdigit() and int(deposit_amount) > 0:
           balance += int(deposit_amount)
           print(f'입금하신 금액은{deposit_amount}원이고, 입금 후 잔액은{balance}원 입니다.')

           check.append(("입금액", deposit_amount, balance)) 

       else:
           print("제대로 된 금액을 입력해주세요.")

       
    if num == "출금" :
        withdraw_amount = input("출금할 금액을 입력해주세요 :")
        if withdraw_amount.isdigit() and int(withdraw_amount) > balance :
            print("잔액이 부족합니다.")

        elif withdraw_amount.isdigit() and int(withdraw_amount) > 0:
           balance -= int(withdraw_amount)
           print(f'출금하신 금액은{withdraw_amount}원이고, 출금 후 잔액은{balance}원 입니다.')

           check.append(("출금액", withdraw_amount, balance)) 

        else:
            print("제대로 된 금액을 입력해주세요.")
        
    if num == "영수증 보기" :
        if check:
            print("===영수증 내역===")
            for i in check:
                print(f'{i[0]} : {i[1]}원 | 잔액 : {i[2]}원')
        
        else:
            print("내역이 없습니다.")
    if num == "종료" :
        print("서비스를 종료합니다.")
        break
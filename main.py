# 쇼핑몰 장바구니 & 할인쿠폰

products = {
    1: {"name": "무선 이어폰", "price": 89000, "stock": 3},
    2: {"name": "텀블러", "price": 15000, "stock": 10},
    3: {"name": "보조 배터리", "price": 32000, "stock": 5},
    4: {"name": "마우스 패드", "price": 9000, "stock": 0},
    5: {"name": "USB 허브", "price": 18000, "stock": 4}
}

cart = {}

while True:
    print("-" * 50)
    print("1.상품목록  2.담기  3.빼기  4.장바구니  5.쿠폰  6.결제  q.종료")
    print("-" * 50)

    choice = input("선택: ")

    # 1. 상품 목록
    if choice == "1":
        for num, product in products.items():
            name = product["name"]
            price = product["price"]
            stock = product["stock"]

            if stock == 0:
                print(f"{num}. {name:<12} {price:>7,}원 (품절)")
            else:
                print(f"{num}. {name:<12} {price:>7,}원 (재고 {stock}개)")

    # 2. 상품 담기
    elif choice == "2":
        num = int(input("상품 번호: "))

        if num not in products:
            print("잘못된 상품 번호입니다.")

        elif products[num]["stock"] == 0:
            print("품절된 상품입니다.")

        else:
            print(f"재고가 {products[num]['stock']}개 남았습니다.")
            quantity = int(input("수량: "))

            if quantity <= 0:
                print("수량은 1개 이상 입력해야 합니다.")

            elif quantity > products[num]["stock"]:
                print("재고가 부족합니다.")

            else:
                if num in cart:
                    cart[num] += quantity
                else:
                    cart[num] = quantity

                products[num]["stock"] -= quantity

                print(f"{products[num]['name']} {quantity}개를 장바구니에 담았습니다.")

    # 3. 상품 빼기
    elif choice == "3":
        num = int(input("상품 번호: "))

        if num not in cart:
            print("장바구니에 없는 상품입니다.")

        else:
            quantity = cart[num]
            products[num]["stock"] += quantity
            del cart[num]

            print(f"{products[num]['name']} 상품을 장바구니에서 제거했습니다.")

    # 장바구니
    elif choice =="4":
        if not cart:
            print("장바구니가 비어있습니다")
        else:
            total = 0

            print("=" * 50)
            print("[장바구니]")

            for num, quantity in cart.items():
                name = products[num]["name"]
                price = products[num]["price"]
                subtotal = price * quantity

                total += subtotal

                print(f"{name:<12} {price:>7,}원 * {quantity}개 = {subtotal:>9,}원")
            print("=" * 50)

            # 상품합계
            print(f"상품 합계: {total:,}원")

            # 배송비
            if total >= 50000:
                delivery = 0
            else:
                delivery = 3000

            print(f"배송비: {delivery:,}원")

            # 최종 결제 금액
            discount = 0
            final_price = total - discount + delivery

            print("=" * 50)
            print(f"최종 결제 금액: {final_price:,}원")
            print("=" * 50)

            


    # q. 종료
    elif choice == "q":
        print("쇼핑몰을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")

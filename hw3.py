def get_fixed_price(discount_price,discount) :
    fixed_price = discount_price/(100-discount)*100
    return int(fixed_price)

dc = int(input("할인율은?"))
dcprice_a = int(input("A상품의 할인된 가격은?"))
a_price = get_fixed_price(dcprice_a,dc)
dcprice_b = int(input("B상품의 할인된 가격은?"))
b_price = get_fixed_price(dcprice_b,dc)
print('A상품의 정가는',a_price,'원')
print('B상품의 정가는',b_price,'원')


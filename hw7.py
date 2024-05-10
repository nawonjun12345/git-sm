shopping_bag = []
while True :
  object = input('상품명?')
  shopping_bag.append(object)
  if object == '' :
    del shopping_bag[-1]
    break
print(f'장바구니 보기:{shopping_bag}')

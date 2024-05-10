shopping_bag = {}

while True:
  object = input('상품명?')
  if object == '':
    break
  
  quantity = int(input('수량은?'))
  shopping_bag[object] = quantity
  print(f'장바구니에 {object} {quantity}개가 담겼습니다.')

print(f'장바구니 보기: {shopping_bag}')

search_item = input('장바구니에서 확인하고자 하는 상품은?')

if search_item in shopping_bag:
  quantity = shopping_bag[search_item]
  print(f'{search_item}은(는) {quantity}개 담겨 있습니다.')
else:
  print(f'{search_item}은(는) 장바구니에 없습니다.')

#조건1

def get_radius(prompt1) :
    r = int(input( prompt1))
    return r

prompt1 = ("넓이를 구하고자 하는 원의 반지름은?")
a = get_radius(prompt1)
print('반지름 ',a,'인 원의 넓이 = 3.14 x',a,'x',a,'=', a*a*3.14)


#조건2

def get_radius(prompt2):
  r=int(input(prompt2))
  return r
def get_circle_area(radius):
  area= radius * radius * 3.14
  return area

prompt2 = ("넓이를 구하고자 하는 원의 반지름은? ")

radius = get_radius(prompt2)
area2= get_circle_area(radius)

print('반지름',radius,'인 원의 넓이 = 3.14 x',radius,'x',radius,'=',area2)

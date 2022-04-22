import lotto_machine as lm


balls = []

balls.append(lm.ball('a'))
balls.append(lm.ball('b'))
balls.append(lm.ball('c'))
balls.append(lm.ball('d'))
balls.append(lm.ball('e'))

basket = lm.basket(balls)

print('tatal count in my basket = {}'.format(len(basket.myBasket)))

#k=0
#for i in basket.myBasket:
#	k=k+1
#	print('{}번째 Ball={}'.format(k, i.getValue()))

myM = lm.lotto_machine(basket)

for i in range(len(balls)):
	print(myM.pop())

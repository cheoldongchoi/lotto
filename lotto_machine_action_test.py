import lotto_machine_action as lma

'''
#Test Case 1
active_machine = lma.lotto_machine_action('a','b','c','d','e')
print('test case#1 :{} '.format(active_machine.pop_balls(2)))

del active_machine

#Test Case 2
active_machine = lma.lotto_machine_action('1','2','3','4','5')
print('test case#2 :{} '.format(active_machine.pop_ball()))
print('test case#2 :{} '.format(active_machine.pop_ball()))
print('test case#2 :{} '.format(active_machine.pop_ball()))
print('test case#2 :{} '.format(active_machine.pop_ball()))
print('test case#2 :{} '.format(active_machine.pop_ball()))
print('test case#2 :{} '.format(active_machine.pop_ball()))

del active_machine

#Test Case3
active_machine = lma.lotto_machine_action('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21', '22','23','24', '25', '26', '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41', '42','43', '44', '45')

for i in range(5):
	print('test case#1 :{} '.format(active_machine.pop_balls(6)))

del active_machine

# Test Case 4
'''
active_machine = lma.lotto_machine_action(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21', '22','23','24', '25', '26', '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41', '42','43', '44', '45'])

for i in range(5):
        print('test case#1 :{} '.format(active_machine.pop_balls(6)))

del active_machine



#Workout.py

class person:

	def __init__(self,name,gender,exercise,time):
		self.name = name
		self.gender = gender
		self.exercise = exercise
		self.time = time

	def hello(self):
		if self.gender == 'ชาย':
			tail =  'ครับ'
			callme = 'ผม'
		else:
			tail = 'คะ'

		print(f'สวัสดี{tail} วันนี้มาออกกำลังกาย {self.time} ชั่วโมงนะ{tail}')

	def sawatdee(self):
		print('สวัสดีครับ คุณชื่ออะไรครับ')

	def talk(self):
		print('วันนี้มาทำอะไรเหรอ')

	def talk2(self):
		print(f'{self.exercise}ครับ คนนี้น้องสาวผม')

	def talk3(self):
		print(f'สวัสดีค่ะ ชื่อ{self.name} ค่ะ มา{self.exercise}ค่ะ ขอตัวไปออกกำลังกายก่อนนะคะ')



class people:


	def __init__(self,name,gender,cardio,time):
		self.name = name  
		self.gender = gender
		self.cardio = cardio
		self.time = time

	def hello(self):
		print(f'สวัสดีค่ะ วันนี้มาออกกำลังกาย {self.time} ชั่วโมงนะคะ')

	def sawatdee(self):
		print(f'{self.name} ค่ะ')

	def talk(self):
		print(f'{self.cardio} แล้วคุณล่ะ?')


if __name__=='__main__':
	man = person('เอ','ชาย','วิดพื้นและวิ่ง','2')
	woman = person('บี','หญิง','กระโดดเชือก','2')

	woman2 = people('ซี','หญิง','วิ่ง','1')

	print ('--- ลงทะเบียน ---')
	man.hello()
	woman.hello()
	woman2.hello()
	print('--บังเอิญเดินมาเจอกัน--')
	man.sawatdee()
	woman2.sawatdee()
	man.talk()
	woman2.talk()
	man.talk2()
	woman.talk3()


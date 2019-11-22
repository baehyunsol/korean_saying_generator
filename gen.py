import korean
import random


class yong_eon:

	def __init__(self, base, verb, nounHa, obj):

		self.base = base
		self.verb = verb
		self.nounHa = nounHa  # ex) 성공 + -하
		self.obj = obj  # only '-를'
		self.last = self.base[len(self.base) - 1]

	def __repr__(self):
		return self.base


def josa(noun, type_):

	if type_ == 1:
		return noun

	# 이/가
	elif type_ == 2:

		if korean.hasBatchim(noun[-1]):
			return noun + '이'

		else:

			if noun == '나':
				noun = '내'

			elif noun == '너':
				noun = '네'

			return noun + '가'

	# '의'
	elif type_ == 3:
		return noun + '의'

	# '을/를'
	elif type_ == 4:

		if korean.hasBatchim(noun[-1]):
			return noun + '을'

		else:
			return noun + '를'

	# '은/는'
	elif type_ == 5:

		if korean.hasBatchim(noun[-1]):
			return noun + '은'

		else:
			return noun + '는'

	# '이다'
	elif type_ == 6:
		return noun + '이다'

	# '와/과'
	elif type_ == 7:

		if korean.hasBatchim(noun[-1]):
			return noun + '과'

		else:
			return noun + '와'


def hwalyong(yong_eon, type_):

	if type_ == 1:
		return yong_eon.base + '다'

	elif type_ == 2:

		if yong_eon.verb:
			return yong_eon.base + '는'

		if korean.hasBatchim(yong_eon.last):
			return yong_eon.base + '은'

		tmp = korean.divide(yong_eon.last)
		tmp[2] = 'ㄴ'

		return yong_eon.base[:-1] + korean.combine(tmp)

	elif type_ == 3:

		if yong_eon.nounHa:
			return yong_eon.base[:-1]

		if korean.hasBatchim(yong_eon.last):
			return yong_eon.base + '음'

		tmp = korean.divide(yong_eon.last)
		tmp[2] = 'ㅁ'

		return yong_eon.base[:-1] + korean.combine(tmp)

	elif type_ == 4:
		return yong_eon.base + '자'

	elif type_ == 5:
		return yong_eon.base + '고 싶다'

	elif type_ == 6:

		if korean.hasBatchim(yong_eon.last):
			return yong_eon.base + '으면'

		return yong_eon.base + '면'

	elif type_ == 7:
		return yong_eon.base + '고'


def _myungsa(yong_eon):

	return hwalyong(yong_eon, 3)


yong_eons = [
	yong_eon('가', verb=True, nounHa=False, obj=False),
	yong_eon('경고하', verb=True, nounHa=True, obj=True),
	yong_eon('결심하', verb=True, nounHa=True, obj=True),
	yong_eon('공부하', verb=True, nounHa=True, obj=True),
	yong_eon('관찰하', verb=True, nounHa=True, obj=True),
	yong_eon('교육하', verb=True, nounHa=True, obj=True),
	yong_eon('굳', verb=False, nounHa=False, obj=False),
	yong_eon('극복하', verb=True, nounHa=True, obj=True),
	yong_eon('기다리', verb=True, nounHa=False, obj=True),
	yong_eon('기억하', verb=True, nounHa=True, obj=True),
	yong_eon('깊', verb=False, nounHa=False, obj=False),
	yong_eon('나타나', verb=True, nounHa=False, obj=False),
	yong_eon('넘치', verb=True, nounHa=False, obj=False),
	yong_eon('노래하', verb=True, nounHa=True, obj=True),
	yong_eon('놓', verb=True, nounHa=False, obj=True),
	yong_eon('늙', verb=False, nounHa=False, obj=False),
	yong_eon('닫히', verb=False, nounHa=False, obj=False),
	# yong_eon('달리', verb=True, nounHa=False, obj=True), '달리기' sounds better than '달림'
	yong_eon('던지', verb=True, nounHa=False, obj=True),
	yong_eon('떠나', verb=True, nounHa=False, obj=True),
	yong_eon('똑똑하', verb=False, nounHa=False, obj=False),
	yong_eon('떨어지', verb=True, nounHa=False, obj=False),
	yong_eon('만나', verb=True, nounHa=False, obj=True),
	yong_eon('매달리', verb=True, nounHa=False, obj=False),
	yong_eon('먹', verb=True, nounHa=False, obj=True),
	yong_eon('멍청하', verb=False, nounHa=False, obj=False),
	yong_eon('미세하', verb=False, nounHa=False, obj=False),
	yong_eon('미워하', verb=True, nounHa=False, obj=True),
	yong_eon('미련하', verb=False, nounHa=True, obj=False),
	yong_eon('미치', verb=False, nounHa=False, obj=False),
	yong_eon('배고프', verb=False, nounHa=False, obj=False),
	yong_eon('배우', verb=True, nounHa=False, obj=True),
	yong_eon('배부르', verb=False, nounHa=False, obj=False),
	yong_eon('변하', verb=True, nounHa=False, obj=False),
	yong_eon('보', verb=True, nounHa=False, obj=True),
	yong_eon('불행하', verb=False, nounHa=True, obj=False),
	yong_eon('빌리', verb=True, nounHa=False, obj=True),
	yong_eon('사과하', verb=True, nounHa=True, obj=True),
	yong_eon('사라지', verb=True, nounHa=False, obj=False),
	yong_eon('사랑하', verb=True, nounHa=True, obj=True),
	yong_eon('선택하', verb=True, nounHa=True, obj=True),
	yong_eon('성공하', verb=False, nounHa=True, obj=True),
	yong_eon('순수하', verb=False, nounHa=False, obj=False),
	yong_eon('승리하', verb=False, nounHa=True, obj=False),
	yong_eon('시작하', verb=True, nounHa=True, obj=True),
	yong_eon('식사하', verb=True, nounHa=True, obj=False),
	yong_eon('실패하', verb=False, nounHa=True, obj=True),
	yong_eon('아프', verb=False, nounHa=False, obj=False),
	yong_eon('안내하', verb=True, nounHa=True, obj=True),
	yong_eon('안전하', verb=False, nounHa=True, obj=False),
	yong_eon('약속하', verb=True, nounHa=True, obj=True),
	yong_eon('얘기하', verb=True, nounHa=True, obj=True),
	yong_eon('어색하', verb=False, nounHa=False, obj=False),
	yong_eon('여행하', verb=True, nounHa=True, obj=True),
	yong_eon('열리', verb=False, nounHa=False, obj=False),
	yong_eon('영원하', verb=False, nounHa=True, obj=False),
	yong_eon('오', verb=True, nounHa=False, obj=False),
	yong_eon('완벽하', verb=False, nounHa=True, obj=False),
	yong_eon('외면하', verb=True, nounHa=True, obj=True),
	yong_eon('움직이', verb=True, nounHa=False, obj=False),
	yong_eon('위험하', verb=False, nounHa=True, obj=False),
	yong_eon('웃', verb=True, nounHa=False, obj=False),
	yong_eon('이별하', verb=True, nounHa=True, obj=False),
	yong_eon('인정하', verb=True, nounHa=True, obj=True),
	yong_eon('자', verb=True, nounHa=False, obj=False),
	yong_eon('젊', verb=False, nounHa=False, obj=False),
	yong_eon('좋아하', verb=True, nounHa=False, obj=True),
	yong_eon('죽', verb=False, nounHa=False, obj=False),
	yong_eon('지나가', verb=True, nounHa=False, obj=True),
	yong_eon('작', verb=False, nounHa=False, obj=False),
	yong_eon('청소하', verb=True, nounHa=True, obj=True),
	yong_eon('채우', verb=True, nounHa=False, obj=True),
	yong_eon('치열하', verb=False, nounHa=False, obj=False),
	yong_eon('키우', verb=True, nounHa=False, obj=True),
	yong_eon('크', verb=False, nounHa=False, obj=False),
	yong_eon('태어나', verb=False, nounHa=False, obj=False),
	yong_eon('패배하', verb=False, nounHa=True, obj=False),
	yong_eon('행복하', verb=False, nounHa=True, obj=False),
	yong_eon('후회하', verb=True, nounHa=False, obj=True),
	yong_eon('흐리', verb=False, nounHa=False, obj=False),
	yong_eon('흩어지', verb=True, nounHa=False, obj=False),
]

objYongEons = list(filter(lambda x: x.obj, yong_eons))
verbs = list(filter(lambda x: x.verb, yong_eons))
adjs = list(filter(lambda x: not x.verb, yong_eons))
objVerbs = list(filter(lambda x: x.obj, verbs))

nouns = list(map(_myungsa, yong_eons))

nouns += [
	'가을',
	'감동',
	'강아지',
	'겨울',
	'고통',
	'과거',
	'관계',
	'국가',
	'굴욕',
	'그것',
	'끝',
	'나',
	'날개',
	'내일',
	'너',
	'노을',
	'눈물',
	'단어',
	'돌멩이',
	'마지막',
	'물',
	'미래',
	'미소',
	'바다',
	'바보',
	'불',
	'비극',
	'사람',
	'산',
	'선생님',
	'소녀',
	'소년',
	'소식',
	'아기',
	'아버지',
	'아침',
	'안부',
	'애교',
	'어른',
	'어머니',
	'어제',
	'여름',
	'연극',
	'오늘',
	'우리',
	'인생',
	'자식',
	'저녁',
	'죄',
	'죽음',
	'지갑',
	'지식',
	'집',
	'찰나',
	'처음',
	'천재',
	'학교',
	'학생',
	'희극',
]

nouns.sort()
print(len(nouns), 'nouns: ', nouns)


def wordGen(type_):

	# nouns
	if type_ // 10 == 0:
		return josa(random.choice(nouns), type_ % 10) + ' '

	# yong_eons without obj
	elif type_ // 10 == 1:

		if type_ % 10 == 4:
			return hwalyong(random.choice(verbs), 4)

		return hwalyong(random.choice(yong_eons), type_ % 10) + ' '

	# yong_eons with obj
	elif type_ // 10 == 2:

		if type_ % 10 == 4:
			return hwalyong(random.choice(objVerbs), 4)

		return hwalyong(random.choice(objYongEons), type_ % 10) + ' '


def sentenceGen(seq):

	result = ''

	for s in seq:
		result += wordGen(s)

	return result


sequences = [
	(4, 22, 5, 12, 6),
	(7, 4, 25),
	(16, 17, 16, 12, 5, 6),
	(12, 1),
	(4, 22, 1),
	(3, 5, 6),
	(7, 4, 14)
]

if __name__ == '__main__':

	while input() != 'q':
		print(sentenceGen(random.choice(sequences)))

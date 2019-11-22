# 12593~12622
# ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ

# 12623~12643
# ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ

# (ord(t) - 44032) // 588 -> 초성
# ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ
# 가 44032
# 까 44620
# 나 45208
# 다 45796
# 따 46384

# ((ord(t) - 44032) % 588) // 28 -> 중성
# 가개갸걔거게겨계고과괘괴교구궈궤귀규그긔기
# 가 44032
# 개 44060
# 갸 44088
# 걔 44116
# 거 44144

# ((ord(t) - 44032) % 588) % 28 -> 종성
# 가각갂갃간갅갆갇갈갉갊갋갌갍갎갏감갑값갓갔강갖갗갘같갚갛

cho = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
joong = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ')
jong = (None, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
ja = ('ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
mo = joong

qwerty2kor = {
	'q': 'ㅂ',
	'Q': 'ㅃ',
	'w': 'ㅈ',
	'W': 'ㅉ',
	'e': 'ㄷ',
	'E': 'ㄸ',
	'r': 'ㄱ',
	'R': 'ㄲ',
	't': 'ㅅ',
	'T': 'ㅆ',
	'y': 'ㅛ',  # don't forget qwerty2kor.get(x, qwerty2kor[x.lower()])
	'u': 'ㅕ',
	'i': 'ㅑ',
	'o': 'ㅐ',
	'O': 'ㅒ',
	'p': 'ㅔ',
	'P': 'ㅖ',
	'a': 'ㅁ',
	's': 'ㄴ',
	'd': 'ㅇ',
	'f': 'ㄹ',
	'g': 'ㅎ',
	'h': 'ㅗ',
	'j': 'ㅓ',
	'k': 'ㅏ',
	'l': 'ㅣ',
	'z': 'ㅋ',
	'x': 'ㅌ',
	'c': 'ㅊ',
	'v': 'ㅍ',
	'b': 'ㅠ',
	'n': 'ㅜ',
	'm': 'ㅡ'
}

kor2qwerty = dict((v, k) for k, v in qwerty2kor.items())


def divide(char):

	ord_ = ord(char)

	if ord_ < 44032 or ord_ > 55203:
		return [char]

	ord_ -= 44032

	return [cho[ord_ // 588], joong[(ord_ % 588) // 28], jong[(ord_ % 588) % 28]]


def hasBatchim(char):

	return 0 != ((ord(char) - 44032) % 588) % 28


# chars -> [cho, joong, jong]
def combine(chars):

	if len(chars) == 1:
		return chars[0]

	if type(chars) == tuple:
		chars = list(chars)

	if len(chars) == 2:
		chars.append(None)

	return chr(cho.index(chars[0]) * 588 + joong.index(chars[1]) * 28 + jong.index(chars[2]) + 44032)


def isKor(char):

	ord_ = ord(char)

	if 44031 < ord_ < 55204:
		return True

	if 12592 < ord_ < 12644:
		return True

	return False


def forgotHanYoung(chars):
	pass
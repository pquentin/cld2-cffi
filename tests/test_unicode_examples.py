import cld2
import cld2full
import os
from codecs import open as uopen


def test_unicode_examples():
	test01 = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "unicode01.html"))
	with uopen(test01, encoding="utf8") as data:
		data = data.read().encode('utf8')
		for detector in cld2, cld2full:
			isReliable, textBytesFound, details, vectors = detector.detect(data, returnVectors=True)
			print details

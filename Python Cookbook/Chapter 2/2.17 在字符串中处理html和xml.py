s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
# 'Elements are written as "<tag>text</tag>".'
print(html.escape(s))
# 'Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.'

# Disable escaping of quotes
print(html.escape(s, quote=False))
# 'Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".'



s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
# b'Spicy Jalape&#241;o'
 

s = 'Spicy &quot;Jalape&#241;o&quot.'
# from html.parser import HTMLParser
# p = HTMLParser()
import html
print(html.unescape(s))
# 'Spicy "Jalapeño".'

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
# 'The prompt is >>>'

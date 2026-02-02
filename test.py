data = b"\xc2\xae\xbcv........\".QY&..X....\".QY&..X......\xbae\"I can\xe2..t seem to call you at all... .."

# Extract printable ASCII characters
import string

ascii_text = ''.join([chr(b) for b in data if chr(b) in string.printable])
print(ascii_text)

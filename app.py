import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'

import fitz
doc = fitz.open('66.뷰티아트과 김채린(서인천고).pdf')
page = doc.load_page(2)
mat = fitz.Matrix(2,2)
pix = page.get_pixmap(matrix = mat)
output = '66.뷰티아트과 김채린(서인천고)_p2.png'
pix.save(output)

a = Image.open('66.뷰티아트과 김채린(서인천고)_p2.png')
result = pytesseract.image_to_string(a, lang='kor')
print(result)
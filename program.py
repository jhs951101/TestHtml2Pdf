# pip install pyhtml2pdf (python 3.11.4)

from pyhtml2pdf import converter

path = 'C:/Users/tails/OneDrive/바탕 화면/test/input_hwp.html'
converter.convert(f'file:///{path}', 'output.pdf')
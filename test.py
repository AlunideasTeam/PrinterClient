label = """
^XA
^FO100, 30
^A0,65,40^FH
^FDJEFFERSON^FS
^FO100, 90
^A0,65,40^FH
^FDAGUILAR^FS
^FO100, 160
^A0,40,25^FH
^FDALUN IDEAS^FS
^FO100, 240
^A0,40,25^FH
^FDASISTENTE^FS
^FO600,220
^BQN,2,5
^FDMA,1234567890^FS
^XZ
"""
from zebra import zebra
z = zebra("GT800_01")
z.output(label)

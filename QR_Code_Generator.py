import qrcode

img = qrcode.make("This is a testt qrcode generator.")
img.save("qr_code.png")
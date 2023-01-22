import qrcode

qr=qrcode.make("hello world")
qr.save("hello.png")
qr.show()

import sys
import cv2
from pyzbar.pyzbar import decode
import qrcode
import os

def barcodeReader(image):

    img = cv2.imread(image)

    detectedBarcodes = decode(img)

    if not detectedBarcodes:
        print('Não foi possível realizar a leitura')
        barcode_data = 'none'
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)

            if barcode.data!="":
                print(barcode.data)
                print(barcode.type)
                barcode_data = barcode.data

    cv2.imshow("Image", img)
    cv2.waitKey(0)

    return barcode_data
    sys.exit()

def QRcode_gen(barcode_data):
    qr = qrcode.QRCode(version=10, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=3)
    qr.add_data(barcode_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="darkblue", back_color="white")
    img.save("qrcode.png")

def check_file(imagefile):
    current_dir = os.getcwd()
    path = os.path.join(current_dir, imagefile)
    isExist = os.path.exists(path)
    return isExist

if __name__ == "__main__":
    imagefile = input('Insira a imagem com o código de barras')
    print('A imagem que você inseriou foi {imagefile}')
    existcheck = check_file(imagefile)

    if existcheck:
        barcodedata = barcodeReader(imagefile)

        if barcodedata != 'none':
            QRcode_gen(barcodedata)
        else:
            print('Não foi possível gerar o QR code')
    else:
        print('Não foi encontrado o arquivo nesse diretório')

cv2.destrotAllWindows()
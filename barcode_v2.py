import sys
import os
import cv2
import qrcode
from pyzbar.pyzbar import decode


def read_barcode(image_path):
    img = cv2.imread(image_path)
    barcodes = decode(img)

    if not barcodes:
        print("Não foi possível realizar a leitura.")
        return None

    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)

        if barcode.data:
            print(f'Dados: {barcode.data.decode("utf-8")}')
            print(f'Tipo: {barcode.type}')
            cv2.imshow("Imagem", img)
            cv2.waitKey(0)
            return barcode.data.decode("utf-8")

    return None


def generate_qrcode(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=3,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="darkblue", back_color="white")
    img.save(filename)
    print(f"QR Code salvo como {filename}")


def file_exists(filename):
    return os.path.exists(os.path.join(os.getcwd(), filename))


def main():
    image_filename = input("Insira o nome do arquivo da imagem com o código de barras: ")
    print(f"A imagem que você inseriu foi: {image_filename}")

    if not file_exists(image_filename):
        print("Arquivo não encontrado neste diretório.")
        return

    barcode_data = read_barcode(image_filename)

    if barcode_data:
        generate_qrcode(barcode_data)
    else:
        print("Não foi possível gerar o QR Code.")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

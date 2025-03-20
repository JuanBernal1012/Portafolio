from flask import Flask, render_template, request, redirect, url_for
import re
import requests
import gnupg
import os

app = Flask(__name__)

    
@app.route('/')
def index():
    # r = verify_file()
    # file = 
    return render_template('index.html', result="")

@app.route('/', methods=['GET','POST'])
def verify_file():
    if request.method == 'POST':
        def search_file():
            with open('Tec\\Sexto\\Criptografía\\Prototipo\\templates\\index.html') as file:
                for line in file:
                    # print(line)
                    if re.findall(r'href="https://congresoweb\.congresojal\.gob\.mx/infolej/[^"]+\.pdf"', line):
                        return re.findall(r'https://congresoweb\.congresojal\.gob\.mx/infolej/[^"]+\.pdf', line)[0]

        def download_pdf(url, filename):
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    file.write(response.content)
                return True
            else:
                print(f"Error al descargar el archivo: {response.status_code}")
                return False

        def sign_pdf(gpg, filename, signed_filename):
            with open(filename, 'rb') as f:
                signed_data = gpg.sign_file(f, output=signed_filename, passphrase='sony0521 ')
                if signed_data:
                    # print(f"Archivo firmado guardado como {signed_filename}")
                    return True
                else:
                    print("Error al firmar el archivo")
                    return False

        def compare_signatures(signed_file1, signed_file2):
            with open(signed_file1, 'rb') as f1, open(signed_file2, 'rb') as f2:
                signature1 = f1.read()
                signature2 = f2.read()
                return signature1 == signature2
        # Inicializar GnuPG
        gpg = gnupg.GPG()

        # URLs de los archivos PDF
        # url1 = 'https://congresoweb.congresojal.gob.mx/infolej/agendakioskos/documentos/sistemaintegral/estados/R_54387.pdf'
        url1 = search_file()
        # print(url1)

        # Nombres de los archivos PDF descargados última palabra es el nombre del archivo
        pdf_filename1 =re.search(r'[^/]+\.pdf$', url1).group(0)
        pdf_filename2 = "Online_"+pdf_filename1
        # pdf_filename2 = 'R_54387.pdf'

        # Nombres de los archivos firmados
        signed_filename1 = pdf_filename1+'.gpg'
        signed_filename2 = pdf_filename1[:-4]+'_url_signed.pdf.gpg'

        # Descargar los archivos PDF
        if not (download_pdf(url1, pdf_filename2)):
            r = """
            <div>
                <p>Error al descargar un archivo PDF</p>
            </div>"""

            print("Error")

            return r

        # Firmar los archivos PDF descargados
        if not (sign_pdf(gpg, pdf_filename1, signed_filename1) and sign_pdf(gpg, pdf_filename2, signed_filename2)):
            r = """
            <div>
                <p>Error al firmar uno o ambos archivos PDF</p>
            </div>
            """
            print("Error")
            return r

        # Comparar las firmas
        if compare_signatures(signed_filename1, signed_filename2):
            r = """
                <p>Las firmas son iguales</p>
                """
            # r = "Las firmas son iguales"
        else:
            r = """
                <p>Las firmas son diferentes</p>
                """
            # r = "Las firmas son diferentes"

        # Eliminar los archivos descargados y firmados si ya no son necesarios
        # os.remove(pdf_filename1)
        os.remove(pdf_filename2)
        os.remove(signed_filename1)
        os.remove(signed_filename2)

        # return render_template('verify_file.html', result=r)
        # return r
        r = "Las firmas son iguales"
        return render_template('index.html', result=r)
    return redirect(url_for('index', result=r))


    def search_file():
        with open('Tec\\Sexto\\Criptografía\\Prototipo\\templates\\index.html') as file:
            for line in file:
                # print(line)
                if re.findall(r'href="https://congresoweb\.congresojal\.gob\.mx/infolej/[^"]+\.pdf"', line):
                    return re.findall(r'https://congresoweb\.congresojal\.gob\.mx/infolej/[^"]+\.pdf', line)[0]

    def download_pdf(url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            return True
        else:
            print(f"Error al descargar el archivo: {response.status_code}")
            return False

    def sign_pdf(gpg, filename, signed_filename):
        with open(filename, 'rb') as f:
            signed_data = gpg.sign_file(f, output=signed_filename)
            if signed_data:
                print(f"Archivo firmado guardado como {signed_filename}")
                return True
            else:
                print("Error al firmar el archivo")
                return False

    def compare_signatures(signed_file1, signed_file2):
        with open(signed_file1, 'rb') as f1, open(signed_file2, 'rb') as f2:
            signature1 = f1.read()
            signature2 = f2.read()
            return signature1 == signature2
    # Inicializar GnuPG
    gpg = gnupg.GPG()

    # URLs de los archivos PDF
    # url1 = 'https://congresoweb.congresojal.gob.mx/infolej/agendakioskos/documentos/sistemaintegral/estados/R_54387.pdf'
    url1 = search_file()
    # print(url1)

    # Nombres de los archivos PDF descargados última palabra es el nombre del archivo
    pdf_filename1 =re.search(r'[^/]+\.pdf$', url1).group(0)
    pdf_filename2 = "Online_"+pdf_filename1
    # pdf_filename2 = 'R_54387.pdf'

    # Nombres de los archivos firmados
    signed_filename1 = pdf_filename1+'.gpg'
    signed_filename2 = pdf_filename1[:-4]+'_url_signed.pdf.gpg'

    # Descargar los archivos PDF
    if not (download_pdf(url1, pdf_filename2)):
        r = """
        <div>
            <p>Error al descargar un archivo PDF</p>
        </div>"""

        print("Error")

        return r

    # Firmar los archivos PDF descargados
    if not (sign_pdf(gpg, pdf_filename1, signed_filename1) and sign_pdf(gpg, pdf_filename2, signed_filename2)):
        r = """
        <div>
            <p>Error al firmar uno o ambos archivos PDF</p>
        </div>
        """
        print("Error")
        return r

    # Comparar las firmas
    if compare_signatures(signed_filename1, signed_filename2):
        r = """
            <p>Las firmas son iguales</p>
            """
        # r = "Las firmas son iguales"
    else:
        r = """
            <p>Las firmas son diferentes</p>
            """
        # r = "Las firmas son diferentes"

    # Eliminar los archivos descargados y firmados si ya no son necesarios
    # os.remove(pdf_filename1)
    os.remove(pdf_filename2)
    os.remove(signed_filename1)
    os.remove(signed_filename2)

    # return render_template('verify_file.html', result=r)
    # return r
    r = "Las firmas son iguales"
    return render_template('index.html', result=r)
if __name__ == '__main__':
  app.run(debug=True)
import zipfile

def descomprimir_archivo(archivo_zip):
    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        zip_ref.extractall('.')
    print(f'Archivo descomprimido: {archivo_zip}')

archivo_a_descomprimir = 'mundo_amigos.zip'
descomprimir_archivo(archivo_a_descomprimir)

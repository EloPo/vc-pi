import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Função para verificar a autenticidade da imagem
def verificar_autenticidade(imagem_original, imagem_suspeita):
    # Carregar as imagens
    img1 = cv2.imread(imagem_original)
    img2 = cv2.imread(imagem_suspeita)

    # Converter para escala de cinza
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Redimensionar imagens para o mesmo tamanho
    gray1 = cv2.resize(gray1, (500, 500))
    gray2 = cv2.resize(gray2, (500, 500))

    # Detectar bordas
    edges1 = cv2.Canny(gray1, 100, 200)
    edges2 = cv2.Canny(gray2, 100, 200)

    # Comparar as imagens utilizando SSIM
    similarity_index, diff = ssim(edges1, edges2, full=True)
    
    # Exibir resultados
    print(f'Índice de Similaridade SSIM: {similarity_index:.4f}')
    
    if similarity_index > 0.9:  # Ajuste o limiar conforme necessário
        print("A imagem é autêntica.")
    else:
        print("A imagem pode ter sido manipulada.")

# Chame a função com os caminhos das imagens
verificar_autenticidade('imagem_original.png', 'imagem_suspeita.webp')

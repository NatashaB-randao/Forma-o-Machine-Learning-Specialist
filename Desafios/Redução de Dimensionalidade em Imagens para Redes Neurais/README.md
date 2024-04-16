## **Projeto de Redução de Dimensionalidade em Imagens** 

**Descrição:**
O projeto de Redução de Dimensionalidade em Imagens tem como objetivo implementar algoritmos básicos para transformar imagens coloridas em representações mais simples e compactas. Utilizando Python, o projeto consiste em duas etapas principais: conversão para tons de cinza e binarização.

Na primeira etapa, a imagem colorida é convertida para tons de cinza, resultando em uma representação em escala de cinza que mantém as informações de luminosidade, mas descarta as informações de cor. Isso é feito aplicando uma combinação linear dos canais de cor RGB, onde o canal vermelho (R), o canal verde (G) e o canal azul (B) contribuem com diferentes pesos para formar o tom de cinza correspondente a cada pixel.

Na segunda etapa, a imagem em tons de cinza é binarizada, transformando-a em uma imagem preto e branco onde cada pixel é atribuído como preto ou branco com base em um determinado limiar de intensidade. Pixels com intensidade abaixo do limiar são considerados pretos, enquanto pixels com intensidade acima ou igual ao limiar são considerados brancos.

O projeto inclui a implementação dessas etapas utilizando apenas bibliotecas básicas do Python, sem depender de bibliotecas especializadas para processamento de imagens. Além disso, é fornecida uma visualização das imagens originais, em tons de cinza e binarizadas, para facilitar a compreensão do processo de redução de dimensionalidade realizado.
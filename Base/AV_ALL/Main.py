from Base.AV_ALL.Filtros import filtros

valor_de_filtro=int(input("Inserir um valor impár para a matriz de filtro: "))
img="capacete.jpg"
test = filtros(img)

test.guassiano(valor_de_filtro)
test.mediana(valor_de_filtro)
test.media(valor_de_filtro)
test.laplaciano(valor_de_filtro)
test.prewitt(valor_de_filtro)
test.sobel(valor_de_filtro)
# :orange_book: Disse-O-Nário
Aplicação web de dicionário simples utilizando o framework Django. 
Está precisando saber o significado de uma palavra da nossa querida Língua Portuguesa? Não se preocupe, o Nário está aqui para te ajudar! Escreva a palavra que queres saber o significado, e o Nário te dará seu significado, sinônimos e frases de exemplo (quando disponíveis).

![Imagem do front](https://github.com/WallaceLCS/Disse-O-Nario/blob/main/disseonario/static/img/front.png?raw=true)

## Como rodar o projeto? 

1. Com o Python instalado e com um terminal aberto na pasta do projeto, instale as bibliotecas necessárias com o pip do Python utilizando:
``` 
pip install -r requirements.txt
```
2. Após isso, com um terminal ainda na pasta do projeto, escreva o seguinte comando para rodar:
```
python ./manage.py runserver
```
3. Abra no navegador a URL:
```
http://127.0.0.1:8000/
```

## Bibliotecas Utilizadas

- [dicio](https://github.com/felipemfp/dicio) por [Felipe Pontes](https://github.com/felipemfp) - A Python API for Dicio.com.br

# <div align="center">ByteBit</div>
## 1° Projeto para gerar CRUD Curso Técnico do Ensino Médio

O objetivo é deixar claro, como o CRUD se conecta com os comandos de Banco de Dados (SQL) e com as requisições de APIs na web (HTTP):


# A História: O Sistema de Inventário da "ByteBit"
Imagine que a ByteBit, é uma lanchonete local voltada para o público geek, que está crescendo rápido. O dono, Seu Felicio, gerencia o estoque de ingredientes (pães, hambúrgueres, queijos) em um caderno, mas os papéis estão sumindo.

Ele contratou a turma do ensino médio para criar uma API REST para o Inventário da ByteBite. O objetivo é gerenciar os itens do estoque de forma digital.

Como a lanchonete funciona na nuvem, vamos desenvolver o sistema diretamente no Google Cloud Shell e testar as requisições usando a extensão REST Client (do VS Code/Cloud Shell Editor).

## A Arquitetura Modular
Para o código não virar uma "festa do espaguete", vamos dividir o projeto em 3 arquivos principais:

* **database.py:** Onde guardamos nossos dados (simulados em memória).
* **routes.py:** Onde criamos as rotas (endpoints) da nossa API.
* **app.py:** O ponto de entrada que une tudo e liga o servidor.
* E para testar, criaremos o arquivo **api.http**.

## Recursos necessários
Sera necessário ter o python instalado e o VS Code.

* **python3 -m venv . venv**
* **source .venv/bin/activate**
* **pip install Flask**
* **pip list**
   
## Principais Recursos do github

* **git clone “http ou ssh”** Copia o repositório e seu endereço
* **git add .** Seleciona os arquivos que irão subir para a nuvem.
* **git commit -m “mensagem do commit”** Prepara e coloca o rótulo
* **git push -u origin main** Empurra para a nuvem, especificando a origem.
* **git push** Empurra para a nuvem.
* **git fetch** Verifica se há atualização na nuvem
* **git pull origin main** Atualiza o programa na máquina.

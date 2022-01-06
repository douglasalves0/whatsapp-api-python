
<div>
<h1 align="center">WhatsApp API Python ChatBot</h1>
<p align="center">Este repositório contém uma aplicação que se utiliza da API do Moorse para envio e recebimento de mensagens, tornando possível, a partir do uso de uma simples base de dados como o sqlite, a simulação de atendimento de uma pizzaria.</p>
<h4 align="center">
	<strong>
		<a href="https://whatsapp.moorse.io/">Nosso Site</a>
		<span> · </span>
		<a href="https://moorse.readme.io/">Documentação</a>
	</strong>
</h4>

<h2>Como usar?</h2>

### :mag: Pré-instalação

Para utilizar esta aplicação, é necessário antes de tudo estar registrado em nosso <a href="https://app.moorse.io/">site</a>, apenas necessitamos do seu e-mail e uma senha que você pode escolher e tudo estará pronto.

### :rocket: Instalando e configurando
Este tópico objetiva concluir corretamente a instalação e configuração do projeto. 

1. O primeiro requisito para conseguir executar esta aplicação com sucesso é ter o Python 3 instalado corretamente em sua máquina, para isso, segue <a href="https://www.python.org/">link</a> da página oficial do Python para download e instalação do mesmo, após tê-lo instalado certifique-se de ter instalado o pip (instalador de módulos do Python) juntamente ao Python. Sua instalação pode ser verificada pela simples execução no terminal do comando `pip` quando em Linux, entretanto, se o usuário utilizar Windows podem haver 3 combinações diferentes para chamada do pip, são elas: `python -m pip`, `python3 -m pip` e `py -m pip`, tal variação ocorre porque o caminho do `pip` não vem por padrão no caminho da variável PATH, entretanto, para sanar tal variação, recomenda-se fortemente que o usuário adicione o caminho do `pip` à variável de ambiente PATH, para que possa utilizar o `pip` igualmente no Linux e no Windows.

_A partir daqui, consideraremos que o leitor usuário de Windows já colocou o caminho do pip dentro da variável PATH, porém, é possível continuar a leitura da documentação tendo que lidar com as três possibilidades de utilização do pip._

2.   Pós instalação do Python e do pip, devemos instalar os pacotes necessários à utilização da aplicação. Tais pacotes se encontram na raiz do projeto dentro do arquivo `requirements.txt`, para a instalação destes basta executar o comando `install` do pip com o argumento `-r` que servirá para ler o arquivo `requirements.txt`. Então, vá até a pasta onde o requirements.txt está e no terminal/cmd utilize: `pip install -r requirements.txt`

3. Agora com todas as dependências instaladas, entre na pasta resources do repositório e edite o arquivo `application.yml`, aqui, basta trocar o adicionar seu token e sua integração desejada nos respectivos lugares indicados no arquivo. Para conseguir tais dados siga os passos:

    1. Para conseguir o token, logue na sua conta do Moorse e em *dashboard*, vá até o canto superior direito e clique em "copiar token de acesso".

    2. De forma semelhante à de conseguir o token, para conseguir o id da sua integração logue na sua conta do Moorse e na aba lateral esquerda clique em *whatsapp*, quando ver sua integração desejada clique no ícone de engrenagem (*Gerenciar integração*),  após isso, sua integração surge na URL do site, basta retirar ela de lá.


## Moorse support free on Whatsapp/Telegram

<a target="_blank" href="https://web.whatsapp.com/send?phone=5511975923164&text=oi" target="_blank"><img title="whatsapp" height="50" width="187.5" src="https://whatsapp.moorse.io/assets/img/whatsapp.png"></a>

<a target="_blank" href="https://t.me/moorseio" target="_blank"><img title="Telegram" height="50" width="187.5" src="https://whatsapp.moorse.io/assets/img/telegram.png"></a>

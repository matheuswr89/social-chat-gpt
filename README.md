# Implementação básica para usar o Chat-GPT no Discord, Telegram e WhatsApp

[![Python][python-shield]][python-url]

<div align="center">
  <img src="./assets/init.png" width="350px">
</div>
# Configuração

Primeiramente você terá que ter as KEY's da OpenAI, Telegram, Discord e WhatsApp. Abaixo está aonde requisitar elas:

- OpenAI: Acesse https://platform.openai.com/ e logue ou crie uma conta, depois vá em Personal -> View API keys, caso seja nescessario crie uma nova API key;
- Discord: Acesse https://discord.com/developers/applications e logue ou crie uma conta, depois crie uma nova aplicação ou use uma já existente.

  - Caso você tenha criado uma nova aplicação, depois de ser redirecionado para a pagina dela, clique na opção Bot -> Add Bot, e depois clique em View Token e copie o token gerado.
  - Para adidionar o Bot em um canal use o link abaixo e substiua o client_id pelo o do seu bot

    https://discord.com/oauth2/authorize?client_id=SEU_CLIENT_ID_AQUI&scope=bot+applications.commands&permissions=1374891928950

- Telegram: Caso você já use o Telegram converse com o https://t.me/BotFather para criar um bot;
- WhatsApp: Siga esse passo a passo: https://almondine-stock-16e.notion.site/Configura-o-para-o-WhatsApp-159c49c7a8c440919dfe739dcdfcd892

Depois que terminado os passos acima, adicione as KEY's no arquivo `env.sample` e renomeie ele para `.env`

# Execução

1. Instale as dependencias com o comando `pip3 install -r requirements.txt`
2. Os arquivos executáveis são `bot_discord.py`, `whatsapp.py` e `telegram.py`, eles são executados individualmente com o comando: `python3 nome_arquivo`

[python-shield]: https://img.shields.io/github/pipenv/locked/python-version/matheuswr89/social-chat-gpt?style=for-the-badge
[python-url]: https://www.python.org/
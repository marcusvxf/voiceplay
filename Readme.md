# VoicePlay

Olá esse é um aplicativo em pyhton de um sistema de voz para controle de medias, a intenção é facilitar o controle das medias do seu computador por controle de voz.
O projeto apresenta uma gui adicionando alguns controles para quando a aplicação ira lhe escutar junto ao controle por voz.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   ```
2. Navegue para o diretório do projeto:
   ```bash
   cd seu-projeto
   ```
3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     .\venv\Scripts\activate
     ```
5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para rodar esse projeto é necessario baixar um dos modelos do vosk, e adionar o caminho nas envs.

```python
# Para rodar bastar usar
python main.py
```

A aplicação conta com 3 comandos:

- play/start para iniciar
- stop/pause para parar
- next/move para avançar a media

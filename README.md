# 🤖 Agente Triggo AI

Agente de Inteligência Artificial desenvolvido durante o Bootcamp de Engenharia de IA da Triggo.

O projeto utiliza a API do **Google Gemini** para criar um agente conversacional em Python, com arquitetura modular preparada para evolução com ferramentas, memória e recuperação de informações (RAG).

---

## 🚀 Tecnologias utilizadas

- Python 3.12
- Google Gemini API
- Google GenAI SDK
- Gradio
- python-dotenv

---

## 🧠 Modelo utilizado

**Gemini 3.1 Flash Lite**

Escolhido por oferecer:

- Alta velocidade de resposta
- Baixo custo para testes e desenvolvimento
- Boa capacidade para aplicações com agentes de IA

---

## 📂 Estrutura do projeto

```
Agente-Triggo/
│
├── main.py          # Execução do agente via terminal
├── app.py           # Interface web com Gradio
├── agent.py         # Lógica principal do agente
├── config.py        # Configurações da aplicação
├── prompts.py       # Instruções e comportamento do agente
├── tools.py         # Ferramentas disponíveis para o agente
├── modelos.py       # Testes e validação dos modelos Gemini
├── requirements.txt # Dependências do projeto
├── .env.example     # Exemplo de configuração da API
└── .gitignore       # Arquivos ignorados pelo Git
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/alvesjessica508-art/agente-triggo.git
```

Entre na pasta:

```bash
cd agente-triggo
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente:

Windows:

```powershell
venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure a API do Gemini

Crie um arquivo chamado:

```
.env
```

Com:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

---

### 5. Execute o agente

Modo terminal:

```bash
python main.py
```

Interface web:

```bash
python app.py
```

A interface estará disponível em:

```
http://127.0.0.1:7860
```

---

## 💬 Exemplo de uso

Pergunta:

```
Quem descobriu o Brasil?
```

Resposta:

```
Historicamente, a chegada dos portugueses ao território brasileiro é atribuída a Pedro Álvares Cabral em 1500...
```

---

## 🏗️ Arquitetura

```
Usuário
   |
   v
Interface Gradio / Terminal
   |
   v
Agente Python
   |
   v
Google Gemini API
   |
   v
Resposta gerada
```

---

## 🔮 Próximas evoluções

- [ ] Implementação de Function Calling
- [ ] Integração de ferramentas externas
- [ ] Memória de conversação
- [ ] RAG com documentos
- [ ] Integração com bancos de dados
- [ ] Deploy em ambiente cloud

---

## 👩‍💻 Desenvolvimento

Projeto desenvolvido como parte do Bootcamp de Engenharia de IA da Triggo.

---

## 📄 Licença

Este projeto é destinado para fins educacionais e demonstração de desenvolvimento com agentes de Inteligência Artificial.

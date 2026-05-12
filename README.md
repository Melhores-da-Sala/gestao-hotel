# 🏨 Sistema Web de Gestão Hoteleira

## ✨ Sobre o Projeto

**Nome do banco:** `hotelaria`
O **Sistema Web de Gestão Hoteleira** foi criado para modernizar e facilitar a administração de hotéis, oferecendo uma solução prática para organizar as principais operações do estabelecimento.

### 📌 Funcionalidades
👥 **Hóspedes** → cadastro, edição e exclusão  
🛏 **Quartos** → controle de disponibilidade e status  
📅 **Reservas** → gerenciamento completo das hospedagens  
💵 **Diárias** → cálculo estimado de valores  
📊 **Dashboard** → visão geral do hotel  

### 🚀 Diferenciais
✔ Interface simples e intuitiva  
✔ Arquitetura MVC bem organizada  
✔ Integração com MySQL  
✔ Templates dinâmicos com Jinja2  
✔ Backend com FastAPI  

### 🎯 Finalidade
Automatizar processos manuais e tornar a gestão hoteleira mais rápida, eficiente e organizada.

---

<h2 align="center">💻 Tecnologias Utilizadas</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,mysql,html,css" />
</p>

- **Python** → Backend principal  
- **FastAPI** → Desenvolvimento das rotas  
- **Jinja2** → Renderização dos templates  
- **MySQL** → Banco de dados  
- **HTML5/CSS3** → Estrutura e estilização  
- **JavaScript** → Interatividade do sistema  

---

## 📂 Estrutura do Projeto

```bash
Projeto/
│
├── static/
│   ├── img/
│   ├── js/
│   └── css/
│
├── templates/
│   ├── index.html
│   ├── hospedes.html
│   ├── quartos.html
│   ├── reservas.html
│   ├── add_hospede.html
│   ├── edit_hospede.html
│   ├── add_quarto.html
│   ├── edit_quarto.html
│   ├── add_reserva.html
│   ├── edit_reserva.html
│   └── view_reserva.html
│
├── app.py
├── dao.py
├── model.py
└── README.md
```

---

## ⚙️ Instalação

Para clonar e configurar o projeto, execute:

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Entrar na pasta do projeto
cd seu-repositorio

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

---

## 📦 Instalação das Dependências

```bash
pip install fastapi uvicorn jinja2 mysql-connector-python
```

ou

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuração do Banco de Dados

Crie o banco:

```sql
CREATE DATABASE hotelaria;
```

Importe o arquivo `.sql` do projeto contendo:

- Criação das tabelas  
- Relacionamentos  
- Inserts para testes  

---

## 🔌 Configuração da Conexão

No arquivo `dao.py`, configure:

```python
host="localhost"
user="root"
password="sua_senha"
database="hotelaria"
```

---

## ▶️ Executando o Projeto

```bash
uvicorn app:app --reload
```

Acesse no navegador:

```bash
http://127.0.0.1:8000
```

## 📸 Prints do Sistema

# 👨‍💻 Desenvolvedores

| Nº | Nome |
|----|--------------------------------------------|
| 02 | Gabriel Leonardo Vicente Cancian |
| 09 | Gustavo Lopez Zampiron |
| 20 | Matheus Lima Catarucci |
| 22 | Moisés Gabriel Tafarello |
| 25 | Nicolas Luciani |
| 30 | Samuel Gustavo Gracias Dio Falco |

### 🏆 Equipe: Melhores da Sala

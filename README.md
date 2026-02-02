# Vulnerable Web Lab – Pentest Practice

⚠️ **Aplicação web intencionalmente vulnerável, criada exclusivamente para fins educacionais.**
Não utilize este código em ambientes de produção.

## 🎯 Objetivo
Demonstrar habilidades práticas em **Pentest Web**, incluindo:
- Identificação de vulnerabilidades
- Exploração controlada
- Análise de impacto
- Proposta de mitigação

## 🧰 Tecnologias
- Python
- Flask
- SQLite

## 🐞 Vulnerabilidades Implementadas
- SQL Injection (Login)
- IDOR – Broken Access Control

## ▶️ Como rodar o projeto
```bash
pip install flask
cd app
python init_db.py
python app.py

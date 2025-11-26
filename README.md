# Cadastro de Clientes – Sistema de Exportação para WhatsApp

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)
![License](https://img.shields.io/badge/Licença-MIT-lightgrey)

Este projeto é uma aplicação prática desenvolvida em **Python**, criada para simplificar o cadastro de clientes e permitir a exportação de contatos em formato **VCF**, possibilitando a importação direta no WhatsApp.  
O sistema é ideal para pequenos comércios que desejam manter uma base de clientes organizada e enviar novidades por **listas de transmissão**, respeitando a privacidade e confirmação de opt-in.

---

## 🚀 Funcionalidades

- Cadastro de clientes com:
  - Nome
  - Telefone (convertido automaticamente para o padrão internacional E.164)
  - Consentimento explícito (opt-in)
- Armazenamento local de dados em arquivo **CSV**
- Exportação dos contatos autorizados para arquivo **.VCF**
- Menu interativo simples e intuitivo
- Versão compilada em **.exe**, permitindo uso sem Python instalado

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- Módulo `csv` para armazenamento local
- `regex` para validação estruturada de telefone
- `PyInstaller` para geração do executável
- Manipulação manual do padrão **vCard (.vcf)**

---

## 📦 Estrutura do Projeto

```bash
cadastro_clientes.py      # Código principal da aplicação
.gitignore                # Arquivos e pastas ignorados pelo Git
README.md                 # Documentação do projeto

# Gerados automaticamente e ignorados no GitHub
dist/                     # Local onde o .exe é criado pelo PyInstaller
build/                    # Arquivos temporários da compilação
cadastro_clientes.spec    # Metadados da compilação do PyInstaller

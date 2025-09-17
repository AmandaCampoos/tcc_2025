# 🌐 TCC - Provisionamento Multi-Nuvem

Este projeto acadêmico tem como objetivo desenvolver uma aplicação em **Python** capaz de **comparar custo e performance entre diferentes provedores de nuvem (AWS, Azure e GCP)**.  
A ideia central é auxiliar usuários e empresas a escolherem a melhor opção de nuvem para suas necessidades, automatizando a coleta de dados e gerando relatórios de custo-benefício.

---

## 📂 Estrutura do Projeto

tcc_2025/

---

## 🚀 Primeiros Passos

### 1. Clonar o repositório
```bash
git clone https://github.com/AmandaCampoos/tcc_2025.git
cd tcc_2025
```
## 2. Criar ambiente virtual
bash
```
Copiar código
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```
## 3. Instalar dependências
bash
Copiar código
pip install -r requirements.txt

## ✅ Funcionalidades Atuais
 Estrutura inicial de pastas organizada

 Configuração de ambiente virtual e dependências

 Script para listar todas as regiões AWS disponíveis

## Exemplo de execução:

````bash
Copiar código
python src/aws/list_regions.py
````
### Saída:



```
🌍 Regiões disponíveis na AWS:
- us-east-1
- us-west-1
- eu-central-1
```
...
## 🛠️ Próximos Passos
 Criar script para listar tipos de instância AWS (CPU, memória, etc)

 Integrar com API de preços da AWS

 Adicionar suporte para Azure

 Adicionar suporte para GCP

 Criar módulo de comparação multi-nuvem

 Gerar relatórios de análise de custo-benefício

## 🕒 Histórico de Versões
v0.1 - Estrutura inicial

Organização de pastas (src, tests, docs)

Criação de requirements.txt

Primeiro script: listagem de regiões AWS

(as próximas versões serão adicionadas conforme evoluímos o projeto)

👩‍💻 Autora
Amanda Campos Ximenes – Estudante de Sistemas para Internet
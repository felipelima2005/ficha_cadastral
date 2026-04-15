# 🗂️ Ficha Cadastral

Sistema simples de cadastro via terminal que permite incluir, consultar e exibir informações em uma ficha dinâmica, utilizando dicionários em Python.

---

## 📋 Funcionalidades

| Opção | Descrição |
|---|---|
| `1` | Incluir um novo campo e valor na ficha |
| `2` | Recuperar o valor de um campo específico |
| `3` | Exibir todos os campos cadastrados |
| `4` | Encerrar o programa |

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
python ficha_cadastral.py
```

---

## 🖥️ Exemplo de Uso

```
FICHA CADASTRAL
1 - Incluir informações na ficha
2 - Recuperar informações na ficha
3 - Exibir ficha completa
4 - Sair
Informe a opção desejada: 1

Informe o campo que vc deseja na ficha: nome
Informe o valor que deseja inserir: João Silva

Informe a opção desejada: 1
Informe o campo que vc deseja na ficha: cidade
Informe o valor que deseja inserir: São Paulo

Informe a opção desejada: 3

FICHA CADASTRAL
NOME --> João Silva
CIDADE --> São Paulo

Informe a opção desejada: 2
Os campos disponíveis na ficha são dict_keys(['nome', 'cidade'])
Informe qual campo deseja exibir: nome
O campo nome contém o dado João Silva

Informe a opção desejada: 4
Saindo da ficha
```

---

## 🧠 Conceitos Utilizados

- **Dicionários (`dict`)** — armazenamento de dados no formato `chave: valor`
- **`dict.update()`** — inserção de novos campos na ficha
- **`dict.keys()`** — listagem dos campos disponíveis
- **`dict.get()`** — recuperação segura de valores
- **`dict.items()`** — iteração sobre todos os pares chave/valor
- **Laço `while`** — menu interativo com repetição até o usuário sair
- **`if/elif/else`** — controle de fluxo por opção escolhida

---

## 📁 Estrutura do Projeto

```
ficha-cadastral/
│
├── ficha_cadastral.py   # Código principal
└── README.md            # Documentação
```

---

## 🔧 Possíveis Melhorias

- [ ] Adicionar opção para **editar** um campo já cadastrado
- [ ] Adicionar opção para **remover** um campo da ficha
- [ ] Salvar a ficha em um arquivo `.txt` ou `.json`
- [ ] Validar entradas vazias
- [ ] Adicionar suporte a múltiplas fichas

---

## 👨‍💻 Nível

> 🟡 **Intermediário** — Ideal para quem está aprendendo dicionários e menus interativos em Python.

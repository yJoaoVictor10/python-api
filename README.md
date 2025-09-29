# Projeto de Fatos Aleatórios

Este projeto é um script Python que permite ao usuário visualizar fatos aleatórios a partir de uma API pública. Se a API não estiver acessível, o programa exibirá um fato de backup local, armazenado em um arquivo JSON.

## Funcionalidades

- **Ver um fato novo**: O usuário pode solicitar um fato aleatório, obtido de uma API.
- **Modo de backup**: Caso a API não esteja disponível ou ocorra algum erro na requisição, o programa exibe um fato armazenado em um arquivo de backup local (`arquivo_backup.json`).
- **Interface simples**: O programa interage com o usuário através de um menu simples no terminal, permitindo escolher entre visualizar um novo fato ou sair do programa.

## Requisitos

- Python 3.x
- Biblioteca `requests` (instalada automaticamente via `pip`)


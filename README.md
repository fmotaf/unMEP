# unMEP

O unMEP é um aplicativo de gerenciamento de tarefas que segue os requisitos especificados no processo seletivo da unMEP.
O projeto foi feito usando framework Flask linguagem Python e usando banco de dados SQLite.

## Funcionalidades Principais

- Criar, editar e remover tarefas, não foi implementado autenticação
- Foram realizados testes unitários

## Como Começar

Siga estas instruções para começar a utilizar o unMEP no seu ambiente local.

### Pré-requisitos

Certifique-se de que tanto interpretador Python quanto gerenciador de pacotes Pip estejam instalados

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/fmotaf/unMEP.git
    ```

(Sem Docker)
2. Navegue até o diretório do projeto:
``` 
	cd unMEP 
```

3. Ative o ambiente virtual
    ```bash
    .\venv\Scripts\activate.ps1 (Windows)
    source venv/bin/activate (Linux)
    ```
    
4. Instale o projeto (certifique-se de estar na pasta raiz, onde está o arquivo pyproject.toml)    
```
    pip install -e .
```

5. Execute o projeto:
```bash
    flask --app src init-db (Inicializa o banco de dados)
    flask --app src run (Roda o servidor na porta 5000)
```

6. Execute os testes unitários:
```bash
   coverage run -m pytest -vv tests
```

Alternativamente, caso você tenha Docker instalado em sua máquina, na pasta raíz do projeto execute:
```
    # Constrói a imagem
    docker build -t <nome-da-imagem> .

    # Roda o container
    docker run -p 5000:5000 <nome-da-imagem>
```
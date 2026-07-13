# Minha Vitrine - Vitrine Virtual MVP

## Descrição

Minha Vitrine é uma plataforma de vitrine virtual que conecta pessoas aos melhores estabelecimentos e eventos da cidade. 

### Funcionalidades Principais

- ✅ Sistema de autenticação (Login/Registro)
- ✅ Cadastro de estabelecimentos (apenas para DEVs/Admins)
- ✅ Cadastro de eventos (com compartilhamento de link e localização no mapa)
- ✅ Categorização de estabelecimentos (Moda, Gastronomia, Farmácia, Mercado, Lanchonete, etc.)
- ✅ Sistema de favoritos
- ✅ Avaliações e comentários
- ✅ Mapa interativo com rotas e foco em eventos/estabelecimentos
- ✅ Busca de estabelecimentos
- ✅ Design moderno e responsivo

## Tecnologias Utilizadas

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento)
- **Fontes**: Inter, Poppins (Google Fonts)
- **Ícones**: Font Awesome 6

## Instalação

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar superusuário (DEV/Admin)

```bash
python manage.py createsuperuser
```

### 6. Criar dados iniciais (categorias)

```bash
python manage.py shell
```

Depois execute:

```python
from apps.core.models import Categoria

categorias = [
    {'nome': 'Moda', 'slug': 'moda', 'ordem': 1},
    {'nome': 'Gastronomia', 'slug': 'gastronomia', 'ordem': 2},
    {'nome': 'Farmácia', 'slug': 'farmacia', 'ordem': 3},
    {'nome': 'Mercado', 'slug': 'mercado', 'ordem': 4},
    {'nome': 'Lanchonete', 'slug': 'lanchonete', 'ordem': 5},
    {'nome': 'Eventos', 'slug': 'eventos', 'ordem': 6},
    {'nome': 'Outros', 'slug': 'outros', 'ordem': 7},
]

for cat_data in categorias:
    Categoria.objects.get_or_create(**cat_data)

exit()
```

### 7. Marcar seu usuário como DEV

Após criar o superusuário, você precisa marcar o perfil como desenvolvedor:

```bash
python manage.py shell
```

Depois execute:

```python
from django.contrib.auth.models import User
from apps.core.models import Profile

user = User.objects.get(username='seu_username')  # substitua pelo seu username
user.profile.is_dev = True
user.profile.save()
exit()
```

### 8. Executar servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Estrutura do Projeto

```
minha-vitrine-v2-main/
│
├── manage.py                          # Ponto de entrada do Django
├── db.sqlite3                         # Banco de dados SQLite (desenvolvimento)
├── requirements.txt                   # Dependências de produção
├── requirements-dev.txt               # Dependências de desenvolvimento
├── .gitignore
│
├── config/                            # Configuração central do projeto
│   ├── __init__.py
│   ├── settings.py                    # Configurações Django
│   ├── urls.py                        # Roteamento principal
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/                              # Apps Django
│   └── core/                          # App principal
│       ├── __init__.py
│       ├── models.py                  # Modelos: Categoria, Estabelecimento,
│       │                              #   FotoEstabelecimento, Avaliacao,
│       │                              #   Evento, Feedback, Profile
│       ├── views.py                   # Views e lógica de negócio
│       ├── urls.py                    # Rotas da app core
│       ├── forms.py                   # Formulários: Registro, Login,
│       │                              #   Avaliacao, Feedback
│       ├── admin.py                   # Configuração do painel admin
│       ├── signals.py                 # Signal: cria Profile ao criar User
│       ├── apps.py
│       ├── context_processors.py      # Variáveis globais de contexto
│       ├── tests.py
│       └── management/
│           └── commands/
│               └── seed_data.py       # Comando para popular dados iniciais
│
├── templates/                         # Templates HTML (camada de apresentação)
│   ├── base.html                      # Template base com navbar e footer
│   └── core/
│       ├── home.html                  # Página inicial (carrossel + categorias)
│       ├── estabelecimento_detalhe.html
│       ├── eventos.html
│       ├── evento_detalhe.html
│       ├── mapa_interativo.html
│       ├── favoritos.html
│       ├── busca.html
│       ├── login.html
│       ├── registro.html
│       └── admin_feedbacks.html       # Painel de feedbacks (superuser)
│
├── static/                            # Arquivos estáticos
│   ├── css/
│   │   └── style.css                  # Estilos globais e sistema de design
│   ├── js/
│   │   └── main.js                    # JavaScript principal
│   └── images/
│       └── .gitkeep
│
├── media/                             # Uploads gerados pelos usuários/admin
│   └── estabelecimentos/              # Imagens de estabelecimentos
│       └── fotos/                     # Galeria de fotos dos estabelecimentos
│
├── docs/                              # Documentação adicional do projeto
│   ├── INICIO_RAPIDO.md
│   ├── GUIA_ADMIN.md
│   ├── COMANDOS_RAPIDOS.md
│   ├── COMO_ADICIONAR_COORDENADAS.md
│   ├── MODIFICACOES_GOOGLE_MAPS.md
│   ├── CONTRIBUINDO.md
│   ├── CHANGELOG.md
│   ├── SEGURANCA_DADOS.md
│   ├── LEIA-ME-PRIMEIRO.md
│   └── LICENCA.txt
│
├── scripts/
│   └── setup.py                       # Script utilitário de setup inicial
│
├── deploy/                            # Configuração de deploy
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── env_example.txt                # Exemplo de variáveis de ambiente
│
└── _revisar/                          # Arquivos pendentes de revisão
    ├── ARQUIVOS_CRIADOS.md
    ├── LEIA-ME.txt
    ├── exec.py
    ├── static/css/
    └── templates/
```

Documentação adicional: `docs/INICIO_RAPIDO.md`

## Uso

### Como usuário comum:

1. Crie uma conta ou faça login
2. Navegue pelas categorias
3. Favorite seus estabelecimentos preferidos
4. Deixe avaliações
5. Explore o mapa interativo
6. Veja eventos da cidade

### Como DEV/Admin:

1. Acesse o painel administrativo em `/admin/`
2. Cadastre novos estabelecimentos
3. Cadastre eventos
4. Gerencie categorias
5. Modere avaliações

## Personalização

### Cores

As cores principais estão definidas no arquivo `static/css/style.css`:

```css
:root {
    --primary-color: #17C3B2;    /* Verde água */
    --secondary-color: #227C9D;   /* Azul */
    --dark-color: #2C2C2C;        /* Preto suave */
}
```

### Categorias

Para adicionar novas categorias, acesse o admin Django e crie uma nova categoria.

## Melhorias Futuras

- [ ] Integração com Google Maps API
- [ ] Sistema de notificações
- [ ] Chat online
- [ ] Sistema de cupons/promoções
- [ ] App mobile
- [ ] API REST
- [ ] Sistema de recomendações
- [ ] Histórico de visualizações

## Licença

Este é um projeto MVP para fins educacionais.

## Contato

Para mais informações, entre em contato através do painel administrativo.


# 🏪 MINHA VITRINE - PROJETO COMPLETO

## ✨ Bem-vindo ao seu projeto!

Este é um projeto Django completo de uma **Vitrine Virtual** baseado nas imagens fornecidas. O sistema permite que usuários naveguem por estabelecimentos e eventos, enquanto apenas DEVs/Administradores podem cadastrar novos conteúdos.

---

## 🎯 O QUE FOI CRIADO

### ✅ Funcionalidades Implementadas

#### Para Usuários:
- 🔐 **Sistema de Autenticação**: Login, Registro e Logout
- ⭐ **Favoritos**: Salvar estabelecimentos favoritos
- 💬 **Avaliações**: Avaliar estabelecimentos com estrelas (1-5) e comentários
- 🏷️ **Categorias**: Navegar por Moda, Gastronomia, Farmácia, Mercado, Lanchonete, Eventos, Outros
- 🔍 **Busca**: Pesquisar estabelecimentos
- 🗺️ **Mapa Interativo**: Visualizar estabelecimentos no mapa
- 📱 **Design Responsivo**: Funciona em mobile e desktop

#### Para DEVs/Administradores:
- 👨‍💼 **Painel Admin**: Interface completa do Django Admin
- 🏪 **Gestão de Estabelecimentos**: Cadastrar, editar, excluir
- 📅 **Gestão de Eventos**: Cadastrar e gerenciar eventos
- 🏷️ **Gestão de Categorias**: Criar e organizar categorias
- 📊 **Moderação**: Gerenciar avaliações e comentários
- 👥 **Gestão de Usuários**: Controlar permissões

### 🎨 Design

- **Cores Principais**: Verde água (#17C3B2) e Azul (#227C9D)
- **Fontes Modernas**: Inter (corpo) e Poppins (títulos)
- **Ícones**: Font Awesome 6
- **Layout**: Moderno, limpo e profissional
- **Animações**: Suaves e elegantes

---

## 🚀 COMO COMEÇAR (3 MINUTOS)

### Passo 1: Instalar Dependências
```bash
# (já na raiz do projeto Minha-Vitrine-main)
pip install -r requirements.txt
```

### Passo 2: Configurar o Banco de Dados
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
```

### Passo 3: Criar Admin
```bash
python manage.py createsuperuser
```

### Passo 4: Marcar como DEV
```bash
python manage.py shell
```
Digite:
```python
from django.contrib.auth.models import User
from apps.core.models import Profile
user = User.objects.get(username='SEU_USERNAME')
user.profile.is_dev = True
user.profile.save()
exit()
```

### Passo 5: Rodar o Servidor
```bash
python manage.py runserver
```

### Passo 6: Acessar
- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 📁 ESTRUTURA DO PROJETO

```
Minha-Vitrine/
│
├── 📄 manage.py                    # Gerenciador Django
├── 📄 requirements.txt             # Dependências
├── 📄 README.md                    # Documentação principal
│
├── 📁 config/                      # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── 📁 apps/core/                   # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── management/commands/seed_data.py
│
├── 📁 templates/                   # Templates HTML
├── 📁 static/                      # CSS, JS, imagens
├── 📁 media/                       # Uploads
├── 📁 docs/                        # Documentação (este arquivo, guias, etc.)
├── 📁 scripts/                     # setup.py
├── 📁 deploy/                      # Docker
└── 📁 _revisar/                    # Arquivos para revisão manual
```

Documentação: `docs/INICIO_RAPIDO.md`, `docs/GUIA_ADMIN.md`

---

## 🎓 DOCUMENTAÇÃO DISPONÍVEL

1. **README.md** - Documentação completa do projeto
2. **INICIO_RAPIDO.md** - Guia de instalação rápida
3. **GUIA_ADMIN.md** - Manual do administrador
4. **CHANGELOG.md** - Histórico de versões
5. **CONTRIBUINDO.md** - Guia para contribuidores

---

## 📊 MODELOS DE DADOS

### 1. Categoria
- Nome, Slug, Ícone, Ordem

### 2. Estabelecimento
- Informações básicas (nome, descrição, categoria)
- Endereço completo + Coordenadas GPS
- Contatos (telefone, email, WhatsApp, redes sociais)
- Dados administrativos (CNPJ, proprietário, horário)
- Sistema de favoritos
- Upload de imagem principal

### 3. FotoEstabelecimento
- Múltiplas fotos por estabelecimento
- Legenda e ordem

### 4. Avaliacao
- Usuário, estabelecimento
- Estrelas (1-5)
- Comentário opcional

### 5. Evento
- Informações (nome, tipo, descrição)
- Localização + Coordenadas
- Data/hora (início e fim)
- Banner

### 6. Profile
- Perfil estendido do usuário
- Telefone, avatar, bio
- Flag is_dev (para acesso admin)

---

## 🌟 PRINCIPAIS FUNCIONALIDADES

### Sistema de Autenticação
- ✅ Registro com validação
- ✅ Login/Logout
- ✅ Perfil automático criado via signals
- ✅ Sistema de permissões (DEV vs Usuário)

### Estabelecimentos
- ✅ Listagem por categoria
- ✅ Busca e filtros
- ✅ Detalhes completos
- ✅ Galeria de fotos
- ✅ Sistema de favoritos (AJAX)
- ✅ Avaliações com estrelas
- ✅ Comentários

### Eventos
- ✅ Listagem com filtros por tipo
- ✅ Detalhes do evento
- ✅ Sistema de datas
- ✅ Upload de banner

### Mapa Interativo
- ✅ Sidebar com estabelecimentos
- ✅ Filtro por categoria
- ✅ Cards informativos
- ✅ Preparado para integração com Google Maps

### Interface
- ✅ Design moderno e profissional
- ✅ Totalmente responsivo
- ✅ Animações suaves
- ✅ Menu mobile
- ✅ Mensagens de feedback
- ✅ Loading states
- ✅ Scroll to top

---

## 🎨 PALETA DE CORES

```css
--primary-color: #17C3B2    /* Verde água - Principal */
--secondary-color: #227C9D  /* Azul - Secundário */
--dark-color: #2C2C2C       /* Preto suave - Texto escuro */
--star-color: #FFD700       /* Dourado - Estrelas */
--success-color: #27ae60    /* Verde - Sucesso */
--error-color: #e74c3c      /* Vermelho - Erro */
--warning-color: #f39c12    /* Laranja - Aviso */
```

---

## 🔧 TECNOLOGIAS UTILIZADAS

### Backend
- Django 4.2.7
- Python 3.11+
- SQLite (pode ser alterado para PostgreSQL)

### Frontend
- HTML5
- CSS3 (Flexbox, Grid, Animations)
- JavaScript Vanilla (ES6+)
- Font Awesome 6
- Google Fonts (Inter, Poppins)

### Bibliotecas Python
- Pillow (manipulação de imagens)
- python-decouple (variáveis de ambiente)

---

## 📱 PÁGINAS CRIADAS

1. **Página Inicial** (/)
   - Hero section com busca
   - Tabs de categorias
   - Grid de estabelecimentos
   - Botão de favoritos flutuante

2. **Login** (/login/)
   - Design moderno
   - Validação

3. **Registro** (/registro/)
   - Formulário completo
   - Criação automática de perfil

4. **Detalhes do Estabelecimento** (/estabelecimento/ID/)
   - Galeria de imagens
   - Informações completas
   - Sistema de avaliações
   - Botão de favoritar

5. **Eventos** (/eventos/)
   - Grid de eventos
   - Filtros por tipo

6. **Detalhes do Evento** (/evento/ID/)
   - Banner grande
   - Meta informações

7. **Favoritos** (/favoritos/)
   - Lista personalizada

8. **Mapa Interativo** (/mapa/)
   - Sidebar + Mapa
   - Filtros

9. **Busca** (/buscar/)
   - Resultados filtrados

10. **Admin** (/admin/)
    - Painel completo do Django

---

## 🎯 PRÓXIMOS PASSOS RECOMENDADOS

### Agora:
1. ✅ Execute o setup básico
2. ✅ Crie um superusuário
3. ✅ Acesse o admin e cadastre alguns estabelecimentos
4. ✅ Teste todas as funcionalidades
5. ✅ Personalize conforme necessário

### Depois (Opcional):
- [ ] Integrar Google Maps API
- [ ] Adicionar mais categorias
- [ ] Criar dados de exemplo
- [ ] Configurar email SMTP
- [ ] Fazer deploy (Heroku, Vercel, etc.)
- [ ] Adicionar testes
- [ ] Implementar cache
- [ ] API REST

---

## 💡 DICAS IMPORTANTES

### Para Desenvolvedores:

1. **Variáveis de Ambiente**: Copie `env_example.txt` para `.env` (produção)
2. **Arquivos Estáticos**: Execute `python manage.py collectstatic` antes do deploy
3. **Migrações**: Sempre rode `makemigrations` e `migrate` após alterar models
4. **Admin**: Use o comando `seed_data` para popular categorias
5. **Imagens**: Crie as pastas `media/estabelecimentos/` e `media/eventos/`

### Para Usuários:

1. **Primeiro Acesso**: Crie uma conta normalmente
2. **Favoritos**: Clique na estrela nos cards
3. **Avaliações**: Só é possível avaliar uma vez por estabelecimento
4. **Busca**: Use a barra de busca no topo

### Para Administradores:

1. **Acesso Admin**: Seu usuário precisa ter `is_staff=True` e `profile.is_dev=True`
2. **Cadastro**: Use o admin (/admin/) para cadastrar estabelecimentos
3. **Imagens**: Adicione sempre uma imagem principal
4. **Coordenadas**: Use Google Maps para obter lat/long

---

## 🐛 SOLUÇÃO DE PROBLEMAS

### Erro: "No module named 'django'"
```bash
pip install -r requirements.txt
```

### Erro: "table doesn't exist"
```bash
python manage.py migrate
```

### Imagens não aparecem
```bash
# Verifique se as pastas existem
mkdir media
mkdir media/estabelecimentos
mkdir media/eventos
mkdir media/avatars
```

### Não consigo acessar o admin
```bash
# Verifique se é superusuário
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='SEU_USERNAME')
>>> user.is_staff = True
>>> user.is_superuser = True
>>> user.save()
>>> user.profile.is_dev = True
>>> user.profile.save()
>>> exit()
```

---

## 📞 SUPORTE

- Leia a documentação em `README.md`
- Consulte o `GUIA_ADMIN.md` para dúvidas de administração
- Veja `INICIO_RAPIDO.md` para setup

---

## 📜 LICENÇA

Este projeto está sob a licença MIT. Veja `LICENCA.txt`.

---

## 🎉 PRONTO PARA USAR!

Você tem em mãos um **projeto Django completo e funcional**!

**Características**:
- ✅ 100% baseado nas imagens fornecidas
- ✅ Design moderno e profissional
- ✅ Código limpo e bem documentado
- ✅ Pronto para personalização
- ✅ Preparado para deploy

**Desenvolvido com ❤️ como MVP (Minimum Viable Product)**

---

**Bom desenvolvimento! 🚀**


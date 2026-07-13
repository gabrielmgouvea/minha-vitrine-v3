# ⚡ COMANDOS RÁPIDOS - MINHA VITRINE

## 🚀 Configuração Inicial (Primeira vez)

```bash
# 1. Entrar no diretório
# (já na raiz do projeto Minha-Vitrine-main)

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Criar banco de dados
python manage.py makemigrations
python manage.py migrate

# 4. Popular categorias iniciais
python manage.py seed_data

# 5. Criar superusuário (admin)
python manage.py createsuperuser

# 6. Iniciar servidor
python manage.py runserver
```

## 👨‍💻 Marcar Usuário como DEV

```bash
# Abrir shell Django
python manage.py shell

# Executar (substitua 'admin' pelo seu username)
from django.contrib.auth.models import User
from apps.core.models import Profile
user = User.objects.get(username='admin')
user.profile.is_dev = True
user.profile.save()
print(f"✓ {user.username} agora é DEV!")
exit()
```

## 🔄 Comandos do Dia a Dia

### Iniciar o servidor
```bash
python manage.py runserver
```

### Criar novas migrações (após alterar models)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Criar arquivos estáticos (antes do deploy)
```bash
python manage.py collectstatic
```

### Popular dados iniciais
```bash
python manage.py seed_data
```

### Abrir shell Django
```bash
python manage.py shell
```

### Criar superusuário
```bash
python manage.py createsuperuser
```

## 📊 Comandos Úteis no Shell

### Ver todos os estabelecimentos
```python
from apps.core.models import Estabelecimento
for est in Estabelecimento.objects.all():
    print(f"{est.id} - {est.nome} ({est.categoria})")
```

### Ver todas as categorias
```python
from apps.core.models import Categoria
for cat in Categoria.objects.all():
    print(f"{cat.nome} ({cat.slug})")
```

### Ver avaliações
```python
from apps.core.models import Avaliacao
for av in Avaliacao.objects.all():
    print(f"{av.usuario} - {av.estabelecimento} - {av.estrelas}⭐")
```

### Marcar usuário como DEV
```python
from django.contrib.auth.models import User
from apps.core.models import Profile

user = User.objects.get(username='SEU_USERNAME')
user.is_staff = True
user.is_superuser = True
user.save()

user.profile.is_dev = True
user.profile.save()
```

### Criar categoria manualmente
```python
from apps.core.models import Categoria

Categoria.objects.create(
    nome='Nova Categoria',
    slug='nova-categoria',
    icone='fa-store',
    ordem=10
)
```

### Ver estabelecimentos mais favoritados
```python
from apps.core.models import Estabelecimento
from django.db.models import Count

favoritos = Estabelecimento.objects.annotate(
    num_favoritos=Count('favoritos')
).order_by('-num_favoritos')[:5]

for est in favoritos:
    print(f"{est.nome}: {est.num_favoritos} favoritos")
```

### Ver média de avaliações por estabelecimento
```python
from apps.core.models import Estabelecimento
from django.db.models import Avg

estabelecimentos = Estabelecimento.objects.annotate(
    media=Avg('avaliacoes__estrelas')
).filter(media__isnull=False)

for est in estabelecimentos:
    print(f"{est.nome}: {est.media:.1f}⭐")
```

## 🐳 Docker (Opcional)

### Construir e iniciar
```bash
docker-compose up --build
```

### Apenas iniciar
```bash
docker-compose up
```

### Parar
```bash
docker-compose down
```

### Ver logs
```bash
docker-compose logs -f
```

## 🔧 Manutenção

### Limpar cache Python
```bash
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

### Resetar banco de dados (CUIDADO!)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
```

### Backup do banco de dados
```bash
# Fazer backup
cp db.sqlite3 db.backup.sqlite3

# Restaurar backup
cp db.backup.sqlite3 db.sqlite3
```

## 📝 Desenvolvimento

### Instalar dependências de dev
```bash
pip install -r requirements-dev.txt
```

### Rodar testes
```bash
python manage.py test
```

### Verificar código (flake8)
```bash
flake8 core/
```

### Formatar código (black)
```bash
black .
```

### Organizar imports (isort)
```bash
isort .
```

## 🌐 Deploy

### Heroku
```bash
# Login
heroku login

# Criar app
heroku create minha-vitrine

# Deploy
git push heroku main

# Migrar banco
heroku run python manage.py migrate

# Criar super usuário
heroku run python manage.py createsuperuser

# Popular dados
heroku run python manage.py seed_data
```

### Railway
```bash
# Instalar CLI
npm i -g @railway/cli

# Login
railway login

# Iniciar projeto
railway init

# Deploy
railway up
```

## 📱 URLs Importantes

```
Site Principal:     http://127.0.0.1:8000/
Admin:              http://127.0.0.1:8000/admin/
Login:              http://127.0.0.1:8000/login/
Registro:           http://127.0.0.1:8000/registro/
Eventos:            http://127.0.0.1:8000/eventos/
Mapa:               http://127.0.0.1:8000/mapa/
Favoritos:          http://127.0.0.1:8000/favoritos/
Busca:              http://127.0.0.1:8000/buscar/?q=termo
```

## 🔐 Variáveis de Ambiente (Produção)

Crie um arquivo `.env`:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
DATABASE_URL=postgresql://user:pass@host:5432/db
```

## 🆘 Problemas Comuns

### ImportError: No module named 'django'
```bash
pip install Django
```

### OperationalError: no such table
```bash
python manage.py migrate
```

### Static files não carregam
```bash
python manage.py collectstatic --noinput
```

### Erro de permissão
```bash
# Linux/Mac
chmod +x manage.py

# Windows
# Execute como administrador
```

---

## 📚 Recursos Adicionais

- **Documentação Django**: https://docs.djangoproject.com/
- **Django Admin**: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
- **Django ORM**: https://docs.djangoproject.com/en/stable/topics/db/queries/

---

**Dica**: Salve este arquivo nos seus favoritos para acesso rápido aos comandos! 📌


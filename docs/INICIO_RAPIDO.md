# 🚀 Início Rápido - Minha Vitrine

## Passos para executar o projeto

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Criar o Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ Criar Categorias Iniciais

```bash
python manage.py seed_data
```

### 4️⃣ Criar um Superusuário (Admin/DEV)

```bash
python manage.py createsuperuser
```

Preencha as informações solicitadas:
- Username
- Email
- Password

### 5️⃣ Marcar o usuário como DEV

Abra o shell do Django:

```bash
python manage.py shell
```

Execute os comandos:

```python
from django.contrib.auth.models import User
from apps.core.models import Profile

# Substitua 'seu_username' pelo username que você criou
user = User.objects.get(username='seu_username')
user.profile.is_dev = True
user.profile.save()

print(f"✓ {user.username} agora é um DEV!")
exit()
```

### 6️⃣ Executar o Servidor

```bash
python manage.py runserver
```

> Dica: se quiser testar em outro dispositivo na mesma rede (ex: celular), rode:
>
> ```bash
> python manage.py runserver 0.0.0.0:8000
> ```
>
> Ou com IP fixo do PC:
>
> ```bash
> python manage.py runserver 192.168.x.y:8000
> ```
>
> Substitua `192.168.x.y` pelo seu IPv4 local (veja com `ipconfig`).

### 7️⃣ Acessar o Sistema (Desktop)

- **Site Principal**: http://127.0.0.1:8000/
- **Painel Admin**: http://127.0.0.1:8000/admin/

### 8️⃣ Acessar no Celular (mesma rede Wi-Fi)

1. No PC, descubra o IP:
   - `ipconfig` (Windows)
   - anote o IPv4 (ex: `192.168.0.10`)
2. Caso esteja com `DEBUG=True`, edite `config/settings.py`:
   - `ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.10']`
3. Inicie o servidor com IP:
   - `python manage.py runserver 192.168.0.10:8000`
4. No celular, abra:
   - `http://192.168.0.10:8000/`

> Se conseguir, está funcionando no mobile!

- **Site Principal**: http://127.0.0.1:8000/
- **Painel Admin**: http://127.0.0.1:8000/admin/

## 📋 Próximos Passos

### Como Admin/DEV:

1. Acesse `/admin/`
2. Faça login com o superusuário criado
3. Cadastre estabelecimentos em **Core > Estabelecimentos**
4. Cadastre eventos em **Core > Eventos**
5. Adicione fotos aos estabelecimentos

### Como Usuário:

1. Crie uma conta em "Cadastrar"
2. Navegue pelas categorias
3. Favorite estabelecimentos
4. Deixe avaliações

## 🎨 Estrutura Visual

O projeto usa:
- **Cor Primária**: Verde água (#17C3B2)
- **Cor Secundária**: Azul (#227C9D)
- **Fontes**: Inter (corpo), Poppins (títulos)

## 📱 Funcionalidades Principais

✅ Sistema de autenticação  
✅ Cadastro de estabelecimentos (DEVs apenas)  
✅ Cadastro de eventos (DEVs apenas)  
✅ Sistema de favoritos  
✅ Avaliações com estrelas  
✅ Mapa interativo  
✅ Busca de estabelecimentos  
✅ Design responsivo  

## 🔧 Solução de Problemas

### Erro: "No module named 'django'"
```bash
pip install Django==4.2.7
```

### Erro: "No such table"
```bash
python manage.py migrate
```

### Erro de permissão no upload de imagens
Certifique-se de que a pasta `media/` existe e tem permissões de escrita.

## 📞 Suporte

Para dúvidas, consulte o arquivo `README.md` ou a documentação em `docs/`.

---

**Desenvolvido como MVP - Minha Vitrine** 🏪✨
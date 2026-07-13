# 👨‍💻 Guia do Administrador - Minha Vitrine

## Acesso ao Painel Administrativo

URL: http://127.0.0.1:8000/admin/

## 📊 Seções Disponíveis

### 1. Categorias

**Caminho**: Core > Categorias

- Criar, editar e excluir categorias de estabelecimentos
- Definir ordem de exibição
- Ativar/desativar categorias
- Adicionar ícones personalizados

**Campos**:
- Nome: Nome da categoria
- Slug: URL amigável (gerado automaticamente)
- Ícone: Nome do ícone Font Awesome (ex: "fa-store")
- Ativo: Marcar para exibir no site
- Ordem: Número para ordenação (menor aparece primeiro)

### 2. Estabelecimentos

**Caminho**: Core > Estabelecimentos

**Informações Básicas**:
- Nome do estabelecimento
- Categoria
- Descrição detalhada
- Imagem principal

**Endereço**:
- Endereço completo
- Número
- Complemento
- CEP
- Latitude e Longitude (para mapa)

**Contato**:
- Email
- Telefone
- WhatsApp
- Website
- Instagram (apenas o @username)
- Facebook (URL completa)

**Dados Administrativos**:
- CNPJ (formato: XX.XXX.XXX/XXXX-XX)
- Proprietário
- Horário de funcionamento

**Controle**:
- Ativo: Marcar para exibir no site
- Destaque: Aparece em destaque na página inicial

**Fotos Adicionais**:
Você pode adicionar múltiplas fotos inline:
- Imagem
- Legenda
- Ordem de exibição

### 3. Eventos

**Caminho**: Core > Eventos

**Informações**:
- Nome do evento
- Tipo (Gastronomia, Moda, Cultura, etc.)
- Descrição
- Banner/Imagem

**Localização**:
- Endereço/Local
- Latitude e Longitude (opcional)

**Data e Hora**:
- Data de início (obrigatório)
- Hora de início (obrigatório)
- Data de término (opcional)
- Hora de término (opcional)

**Controle**:
- Ativo: Marcar para exibir no site
- Destaque: Aparece em destaque

### 4. Avaliações

**Caminho**: Core > Avaliações

- Visualizar avaliações dos usuários
- Moderar comentários
- Excluir avaliações inadequadas

**Campos**:
- Estabelecimento
- Usuário
- Estrelas (1-5)
- Comentário
- Data

### 5. Perfis de Usuários

**Caminho**: Core > Perfis

- Gerenciar perfis de usuários
- Marcar usuários como DEV (podem acessar admin)
- Visualizar telefone e biografia

### 6. Usuários

**Caminho**: Authentication and Authorization > Users

- Criar novos usuários
- Editar permissões
- Ativar/desativar contas
- Redefinir senhas

## 📝 Fluxo de Trabalho Recomendado

### Cadastrar um Novo Estabelecimento

1. Acesse **Core > Estabelecimentos > Adicionar estabelecimento**
2. Preencha todas as informações básicas (nome, categoria, descrição)
3. Adicione o endereço completo
4. Preencha informações de contato
5. Adicione a imagem principal
6. Se tiver, adicione fotos adicionais na seção inline
7. Configure horário de funcionamento
8. Marque como "Ativo"
9. Se for destaque, marque "Destaque"
10. Clique em "Salvar"

### Cadastrar um Evento

1. Acesse **Core > Eventos > Adicionar evento**
2. Preencha nome e tipo do evento
3. Adicione descrição detalhada
4. Defina data e hora de início
5. Informe o local
6. Adicione banner/imagem
7. Marque como "Ativo"
8. Clique em "Salvar"

### Moderar Avaliações

1. Acesse **Core > Avaliações**
2. Visualize a lista de avaliações
3. Filtre por estrelas ou estabelecimento
4. Para remover avaliação inadequada:
   - Selecione a avaliação
   - No menu "Ação", escolha "Excluir avaliações selecionadas"
   - Confirme

## 🎯 Dicas Importantes

### Para Estabelecimentos

1. **Imagens**: Use imagens de boa qualidade (mínimo 800x600px)
2. **Descrição**: Seja descritivo e atrativo
3. **Horário**: Use formato claro, ex:
   ```
   Segunda a Sexta: 08:00 às 18:00
   Sábado: 08:00 às 12:00
   Domingo: Fechado
   ```
4. **Coordenadas**: Para aparecer no mapa, adicione latitude e longitude
   - Use Google Maps para obter coordenadas
   - Clique com botão direito no local
   - Copie as coordenadas

### Para Eventos

1. **Banner**: Use imagem horizontal (16:9) para melhor visualização
2. **Datas**: Certifique-se de preencher datas futuras
3. **Descrição**: Inclua informações sobre ingresso, programação, etc.

### Gerenciamento de Categorias

1. **Ordem**: Números menores aparecem primeiro
   - Exemplo: Moda (1), Gastronomia (2), etc.
2. **Slugs**: Não use espaços ou caracteres especiais
   - Bom: "gastronomia", "moda-feminina"
   - Ruim: "Gastronomia", "moda feminina"

## 🔒 Segurança

### Boas Práticas

1. **Senhas**: Use senhas fortes e únicas
2. **Permissões**: Só marque usuários confiáveis como DEV
3. **Backup**: Faça backup regular do banco de dados
4. **Logs**: Monitore o arquivo de logs para atividades suspeitas

### Dar Acesso Admin para Outro Usuário

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from apps.core.models import Profile

user = User.objects.get(username='nome_do_usuario')
user.is_staff = True
user.is_superuser = True  # Opcional: dá acesso total
user.save()

user.profile.is_dev = True
user.profile.save()

exit()
```

## 📊 Relatórios e Estatísticas

Atualmente disponível no admin:

- Total de estabelecimentos por categoria
- Total de eventos
- Total de avaliações
- Média de avaliações por estabelecimento

Para relatórios personalizados, use o shell do Django:

```python
python manage.py shell

from apps.core.models import Estabelecimento, Evento, Avaliacao
from django.db.models import Count, Avg

# Estabelecimentos por categoria
Estabelecimento.objects.values('categoria__nome').annotate(total=Count('id'))

# Média geral de avaliações
Avaliacao.objects.aggregate(media=Avg('estrelas'))

# Estabelecimentos mais favoritados
Estabelecimento.objects.annotate(num_favoritos=Count('favoritos')).order_by('-num_favoritos')[:10]
```

## 🆘 Problemas Comuns

### "Você não tem permissão para acessar esta página"
- Verifique se seu usuário está marcado como `is_staff = True`
- Verifique se o perfil está marcado como `is_dev = True`

### Imagem não aparece no site
- Verifique se o arquivo foi enviado corretamente
- Certifique-se de que a pasta `media/` existe
- Verifique as configurações `MEDIA_URL` e `MEDIA_ROOT`

### Estabelecimento não aparece no mapa
- Adicione latitude e longitude
- Verifique se o estabelecimento está marcado como "Ativo"

---

**Minha Vitrine - Painel Administrativo** 🏪


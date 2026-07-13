# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [1.0.0] - 2024-10-12

### Adicionado

#### Funcionalidades Principais
- ✅ Sistema completo de autenticação (Login, Registro, Logout)
- ✅ Cadastro e gestão de estabelecimentos
- ✅ Cadastro e gestão de eventos
- ✅ Sistema de categorização
- ✅ Sistema de favoritos para usuários
- ✅ Sistema de avaliações com estrelas (1-5)
- ✅ Comentários em estabelecimentos
- ✅ Mapa interativo
- ✅ Busca de estabelecimentos
- ✅ Perfis de usuários

#### Interface
- ✅ Design moderno e responsivo
- ✅ Paleta de cores verde água (#17C3B2) e azul (#227C9D)
- ✅ Fontes modernas (Inter e Poppins)
- ✅ Ícones Font Awesome
- ✅ Animações suaves
- ✅ Menu mobile

#### Área Administrativa
- ✅ Painel admin customizado do Django
- ✅ Gestão completa de estabelecimentos
- ✅ Gestão completa de eventos
- ✅ Gestão de categorias
- ✅ Moderação de avaliações
- ✅ Gestão de usuários e perfis
- ✅ Upload de múltiplas imagens
- ✅ Sistema de permissões (apenas DEVs cadastram)

#### Páginas
- ✅ Página inicial com grid de estabelecimentos
- ✅ Página de login
- ✅ Página de registro
- ✅ Página de detalhes do estabelecimento
- ✅ Página de eventos
- ✅ Página de detalhes do evento
- ✅ Página de favoritos
- ✅ Página de busca
- ✅ Mapa interativo

#### Modelos de Dados
- ✅ Categoria
- ✅ Estabelecimento
- ✅ FotoEstabelecimento
- ✅ Avaliacao
- ✅ Evento
- ✅ Profile (perfil de usuário)

#### Recursos Técnicos
- ✅ Django 4.2.7
- ✅ Sistema de signals para criação automática de perfil
- ✅ Validação de CNPJ
- ✅ Upload de imagens com Pillow
- ✅ Sistema de mensagens
- ✅ AJAX para favoritos
- ✅ JavaScript vanilla para interatividade

#### Documentação
- ✅ README.md completo
- ✅ Guia de início rápido
- ✅ Guia do administrador
- ✅ Comentários no código
- ✅ Changelog

#### Utilitários
- ✅ Script de setup automatizado
- ✅ Comando customizado seed_data
- ✅ .gitignore configurado
- ✅ requirements.txt
- ✅ Dockerfile (opcional)
- ✅ docker-compose.yml (opcional)

### Características do MVP

- Apenas administradores/DEVs podem cadastrar estabelecimentos e eventos
- Usuários comuns podem:
  - Criar conta
  - Favoritar estabelecimentos
  - Avaliar estabelecimentos
  - Navegar por categorias
  - Usar mapa interativo
  - Buscar estabelecimentos

### Tecnologias Utilizadas

- **Backend**: Django 4.2.7, Python 3.11
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Banco de Dados**: SQLite (desenvolvimento)
- **Bibliotecas**: Pillow (imagens), Font Awesome (ícones)
- **Fontes**: Google Fonts (Inter, Poppins)

### Notas

Este é um **MVP (Minimum Viable Product)** desenvolvido para demonstração. Recursos adicionais podem ser implementados em versões futuras.

## [Futuro] - Melhorias Planejadas

### A Fazer
- [ ] Integração com Google Maps API
- [ ] Sistema de notificações em tempo real
- [ ] Chat online entre usuários e estabelecimentos
- [ ] Sistema de cupons e promoções
- [ ] Histórico de visualizações
- [ ] Recomendações personalizadas
- [ ] App mobile (React Native/Flutter)
- [ ] API REST (Django REST Framework)
- [ ] Testes automatizados
- [ ] Deploy em produção
- [ ] Sistema de pagamentos
- [ ] Newsletter
- [ ] Blog/Notícias
- [ ] Multi-idiomas
- [ ] Modo escuro

---

**Formato**: [Versão] - Data

**Tipos de mudanças**:
- `Adicionado` para novas funcionalidades
- `Modificado` para mudanças em funcionalidades existentes
- `Descontinuado` para funcionalidades que serão removidas
- `Removido` para funcionalidades removidas
- `Corrigido` para correções de bugs
- `Segurança` para vulnerabilidades


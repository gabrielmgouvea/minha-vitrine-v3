# 🤝 Contribuindo para o Minha Vitrine

Obrigado por considerar contribuir para o Minha Vitrine! Este documento fornece diretrizes para contribuir com o projeto.

## Como Contribuir

### Reportar Bugs

Se você encontrar um bug, por favor:

1. Verifique se o bug já não foi reportado nas Issues
2. Se não foi, crie uma nova Issue incluindo:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs comportamento atual
   - Screenshots (se aplicável)
   - Ambiente (SO, versão do Python, etc.)

### Sugerir Melhorias

Para sugerir uma nova funcionalidade:

1. Verifique se já não existe uma Issue similar
2. Crie uma nova Issue descrevendo:
   - O problema que você está tentando resolver
   - Sua solução proposta
   - Alternativas consideradas
   - Mockups ou exemplos (se aplicável)

### Pull Requests

1. **Fork** o repositório
2. **Clone** seu fork localmente
3. **Crie uma branch** para sua feature/correção:
   ```bash
   git checkout -b feature/minha-nova-feature
   ```
4. **Faça suas alterações** seguindo as diretrizes de código
5. **Commit** suas mudanças:
   ```bash
   git commit -m "feat: adiciona nova funcionalidade X"
   ```
6. **Push** para sua branch:
   ```bash
   git push origin feature/minha-nova-feature
   ```
7. **Abra um Pull Request** descrevendo suas mudanças

## Diretrizes de Código

### Python/Django

- Siga a PEP 8
- Use nomes descritivos para variáveis e funções
- Adicione docstrings em funções complexas
- Mantenha funções pequenas e focadas em uma tarefa
- Use type hints quando possível

Exemplo:
```python
def calcular_media_avaliacoes(estabelecimento_id: int) -> float:
    """
    Calcula a média de avaliações de um estabelecimento.
    
    Args:
        estabelecimento_id: ID do estabelecimento
        
    Returns:
        Média das avaliações (0-5)
    """
    # código aqui
```

### HTML/Templates

- Use indentação consistente (4 espaços)
- Adicione comentários para blocos complexos
- Use classes CSS descritivas
- Mantenha templates organizados e reutilizáveis

### CSS

- Use BEM ou nomenclatura consistente
- Organize por seções
- Adicione comentários para seções principais
- Use variáveis CSS para cores e tamanhos comuns

### JavaScript

- Use JavaScript moderno (ES6+)
- Adicione comentários para lógica complexa
- Mantenha funções pequenas e focadas
- Use nomes descritivos

## Padrões de Commit

Use commits semânticos:

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Mudanças na documentação
- `style:` Formatação, pontos e vírgulas, etc
- `refactor:` Refatoração de código
- `test:` Adicionar ou modificar testes
- `chore:` Tarefas de manutenção

Exemplos:
```
feat: adiciona sistema de notificações
fix: corrige erro ao favoritar estabelecimento
docs: atualiza README com instruções de deploy
style: formata código seguindo PEP 8
refactor: simplifica lógica de busca
test: adiciona testes para modelo Estabelecimento
chore: atualiza dependências
```

## Estrutura de Branches

- `main`: Código em produção
- `develop`: Código em desenvolvimento
- `feature/nome-da-feature`: Novas funcionalidades
- `fix/nome-do-bug`: Correções de bugs
- `docs/nome-da-doc`: Mudanças na documentação

## Testes

Antes de enviar um PR:

1. Execute os testes existentes:
   ```bash
   python manage.py test
   ```

2. Adicione testes para novas funcionalidades

3. Verifique o código com flake8:
   ```bash
   flake8 core/
   ```

## Documentação

- Atualize o README.md se necessário
- Adicione/atualize docstrings
- Atualize o CHANGELOG.md
- Adicione comentários em código complexo

## Revisão de Código

Todos os PRs passarão por revisão:

- Código limpo e legível
- Testes passando
- Documentação atualizada
- Sem conflitos com main
- Segue as diretrizes do projeto

## Código de Conduta

- Seja respeitoso e profissional
- Aceite feedback construtivo
- Foque no que é melhor para o projeto
- Seja paciente com iniciantes

## Dúvidas?

Se tiver dúvidas, sinta-se livre para:

- Abrir uma Issue
- Comentar em PRs existentes
- Entrar em contato com os mantenedores

---

**Obrigado por contribuir! 🎉**


# Análise de segurança de dados — Minha Vitrine

Este documento resume riscos e boas práticas com base na implementação atual do projeto (Django, SQLite, autenticação por sessão e e-mail de ativação).

## Pontos positivos

- **Proteção CSRF** em formulários POST (cadastro, login, feedback, favoritos, avaliações), via middleware e `{% csrf_token %}`.
- **Senhas** armazenadas com hash (PBKDF2 por padrão no Django), não em texto plano.
- **Conta inativa até confirmação de e-mail** (`is_active=False` até ativação por link com token), reduzindo cadastros com e-mail arbitrário sem verificação.
- **Tokens de ativação** baseados em `default_token_generator` (ligados ao utilizador e invalidados após alteração de password, conforme comportamento do gerador).
- **SQL injection**: o ORM do Django parametriza consultas, reduzindo esse risco em views que usam apenas o ORM.

## Riscos e melhorias recomendadas

### Configuração e segredos

- **`SECRET_KEY` fixa no repositório** (`config/settings.py`): em produção deve vir de variável de ambiente e ser única e secreta.
- **`DEBUG = True`**: em produção deve ser `False`; caso contrário expõe tracebacks e informações internas.
- **`ALLOWED_HOSTS` vazio**: em produção configure domínios explícitos para evitar ataques de cabeçalho Host.

### Transporte e cookies

- **HTTPS**: em produção use TLS em todo o site; sem isso, sessões e tokens podem ser interceptados.
- **`SESSION_COOKIE_SECURE` e `CSRF_COOKIE_SECURE`**: ative com HTTPS.
- **`SECURE_SSL_REDIRECT`**: redirecionar HTTP para HTTPS em produção.

### E-mail

- **Confirmação de e-mail** depende de SMTP (ou backend) bem configurado. O backend `console` só serve para desenvolvimento; mensagens não são enviadas a utilizadores reais.
- **Validação de “e-mail existe”**: o formulário valida formato e unicidade; **não** prova que a caixa de correio existe sem envio bem-sucedido ou serviço externo (API/MX).

### Dados e ficheiros

- **SQLite** em ficheiro local: adequado para desenvolvimento; em produção considere PostgreSQL com backups e permissões restritas ao ficheiro da base de dados.
- **Uploads** (`MEDIA`): garanta validação de tipo/tamanho no modelo ou formulário admin, armazenamento fora da raiz web servida diretamente sem controlo, e antivírus em anexos se aplicável.

### Privacidade e LGPD (Brasil)

- **Feedback e perfis** guardam dados pessoais: defina base legal, tempo de retenção, política de privacidade e procedimento para pedidos de eliminação/acesso.
- **Logs**: evite registar passwords ou tokens completos em logs.

### Limpeza de eventos

- A remoção de eventos **24 horas após o fim** é feita em pedidos que chamam `purge_eventos_expirados()`. Em tráfego baixo, considere também **cron** ou **Celery beat** para executar a limpeza periodicamente, para não depender apenas de visitas ao site.

### Cabeçalhos HTTP de segurança (produção)

- Configurar `SECURE_*`, `X_FRAME_OPTIONS`, CSP (Content-Security-Policy) e HSTS conforme o ambiente de alojamento.

---

*Documento gerado no contexto das atualizações da pasta `vitrine_virtual_atualizado`. Ajuste sempre à política da sua instituição e a um parecer jurídico quando necessário.*

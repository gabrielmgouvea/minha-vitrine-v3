# 📍 Como Adicionar Coordenadas GPS aos Estabelecimentos

## 🎯 Por que preciso adicionar coordenadas?

Os estabelecimentos só aparecem no **Mapa Interativo** se tiverem **latitude e longitude** cadastradas.

---

## 🗺️ Método 1: Obter Coordenadas pelo Google Maps (RECOMENDADO)

### **Passo a Passo:**

1. **Abra o Google Maps** no navegador
   - Acesse: https://www.google.com/maps

2. **Encontre o endereço** do seu estabelecimento
   - Digite o endereço na busca
   - Ou navegue até o local desejado

3. **Clique com botão direito** no ponto exato do mapa

4. **Clique nas coordenadas** que aparecem no topo do menu
   - Formato: `-23.550520, -46.633308`
   - As coordenadas serão copiadas automaticamente!

5. **Cole no Admin do Django**
   - Acesse: `http://127.0.0.1:8000/admin/`
   - Vá em **Core > Estabelecimentos**
   - Edite o estabelecimento
   - Cole a **primeira parte** (antes da vírgula) no campo **Latitude**
   - Cole a **segunda parte** (depois da vírgula) no campo **Longitude**

### **Exemplo:**

Se o Google Maps mostrar: `-23.550520, -46.633308`

- **Latitude:** `-23.550520`
- **Longitude:** `-46.633308`

---

## 💻 Método 2: Adicionar por Linha de Comando (Rápido)

Se você preferir adicionar via terminal:

```bash
# Ative o ambiente virtual
.\venv\Scripts\Activate.ps1

# Execute o comando Python
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'); import django; django.setup(); from apps.core.models import Estabelecimento; est = Estabelecimento.objects.get(id=1); est.latitude = -23.550520; est.longitude = -46.633308; est.save(); print(f'Coordenadas adicionadas ao {est.nome}!')"
```

**Importante:** Substitua:
- `id=1` pelo ID do estabelecimento
- `-23.550520` pela latitude real
- `-46.633308` pela longitude real

---

## 📋 Método 3: Pelo Admin Django (Interface Visual)

1. **Acesse o Admin:**
   ```
   http://127.0.0.1:8000/admin/
   ```

2. **Faça Login:**
   - Username: `admin`
   - Senha: `admin123`

3. **Navegue até Estabelecimentos:**
   - Clique em **"Core"**
   - Clique em **"Estabelecimentos"**

4. **Edite o estabelecimento:**
   - Clique no nome do estabelecimento

5. **Preencha as coordenadas:**
   - Role até os campos **"Latitude"** e **"Longitude"**
   - Cole os valores obtidos do Google Maps
   - Clique em **"Salvar"**

---

## ✅ Como Verificar se Funcionou

Após adicionar as coordenadas:

1. **Acesse o Mapa Interativo:**
   ```
   http://127.0.0.1:8000/mapa/
   ```

2. **Verifique:**
   - ✅ O estabelecimento deve aparecer na lista lateral
   - ✅ O mapa deve mostrar a localização
   - ✅ Ao clicar no card, o mapa deve focar naquele local

---

## 🌍 Coordenadas de Exemplo por Cidade

### **São Paulo - Centro**
- Latitude: `-23.550520`
- Longitude: `-46.633308`

### **Rio de Janeiro - Centro**
- Latitude: `-22.906847`
- Longitude: `-43.172896`

### **Brasília - Plano Piloto**
- Latitude: `-15.826691`
- Longitude: `-47.921822`

### **Belo Horizonte - Centro**
- Latitude: `-19.917299`
- Longitude: `-43.934559`

---

## 🚨 Avisos Importantes

### **Latitude:**
- Sempre começa com **sinal negativo** no Brasil (-)
- Intervalo típico: `-5` a `-35`
- Exemplo: `-23.550520`

### **Longitude:**
- Sempre começa com **sinal negativo** no Brasil (-)
- Intervalo típico: `-35` a `-75`
- Exemplo: `-46.633308`

### **Precisão:**
- Mais casas decimais = mais preciso
- Mínimo recomendado: 6 casas decimais
- Exemplo: `-23.550520` (6 casas)

---

## 🆘 Problemas Comuns

### **"Estabelecimento não aparece no mapa"**

**Causas possíveis:**
1. ❌ Latitude ou longitude não cadastradas
2. ❌ Estabelecimento marcado como inativo
3. ❌ Coordenadas com formato errado

**Solução:**
```bash
# Verificar estabelecimento
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'); import django; django.setup(); from apps.core.models import Estabelecimento; est = Estabelecimento.objects.get(id=1); print(f'Nome: {est.nome}'); print(f'Ativo: {est.ativo}'); print(f'Lat: {est.latitude}'); print(f'Long: {est.longitude}')"
```

---

## 📝 Checklist ao Cadastrar Novo Estabelecimento

Ao cadastrar um novo estabelecimento no admin, certifique-se de:

- [ ] Preencher nome
- [ ] Selecionar categoria
- [ ] Adicionar descrição
- [ ] Preencher endereço completo
- [ ] **Adicionar latitude** ← IMPORTANTE para o mapa
- [ ] **Adicionar longitude** ← IMPORTANTE para o mapa
- [ ] Upload de imagem principal
- [ ] Marcar como ativo

---

## 🎓 Dicas Profissionais

### **1. Use o Google Maps em modo Satélite**
Ajuda a identificar o ponto exato do estabelecimento

### **2. Salve as coordenadas em um arquivo**
Crie uma planilha com endereço e coordenadas

### **3. Teste sempre após adicionar**
Acesse o mapa interativo para verificar

### **4. Coordenadas precisas = Melhor UX**
Quanto mais preciso, melhor a experiência do usuário

---

## 📞 Precisa de Ajuda?

Se tiver dúvidas:
1. Consulte este guia
2. Verifique o arquivo `MODIFICACOES_GOOGLE_MAPS.md`
3. Teste no Google Maps primeiro

---

**Última atualização:** 12/10/2025  
**Projeto:** Vitrine Virtual


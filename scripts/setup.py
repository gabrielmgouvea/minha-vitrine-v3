"""
Script de configuração automatizada do projeto Minha Vitrine
Execute: python setup.py
"""

import os
import sys
import subprocess


def run_command(command, description):
    """Executa um comando e exibe o resultado"""
    print(f"\n{'='*60}")
    print(f"➡️  {description}")
    print(f"{'='*60}\n")

    try:
        result = subprocess.run(command, shell=True,
                                check=True, text=True, capture_output=True)
        print(result.stdout)
        print(f"✅ {description} - Concluído!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar: {description}")
        print(e.stderr)
        return False


def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║            🏪 MINHA VITRINE - CONFIGURAÇÃO 🏪             ║
    ║                                                           ║
    ║          Script de Configuração Automatizada              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    # Verificar se está no diretório correto
    if not os.path.exists('manage.py'):
        print("❌ Erro: Execute este script no diretório do projeto (onde está o manage.py)")
        sys.exit(1)

    print("Este script irá configurar o projeto automaticamente.\n")

    steps = [
        ("python manage.py makemigrations", "Criando migrações do banco de dados"),
        ("python manage.py migrate", "Aplicando migrações"),
        ("python manage.py seed_data", "Populando categorias iniciais"),
    ]

    for command, description in steps:
        if not run_command(command, description):
            print("\n⚠️  Houve um erro. Continuando com os próximos passos...\n")

    print(f"\n{'='*60}")
    print("📋 PRÓXIMOS PASSOS:")
    print(f"{'='*60}\n")

    print("1️⃣  Criar um superusuário:")
    print("   python manage.py createsuperuser\n")

    print("2️⃣  Marcar o usuário como DEV:")
    print("   python manage.py shell")
    print("   >>> from django.contrib.auth.models import User")
    print("   >>> from apps.core.models import Profile")
    print("   >>> user = User.objects.get(username='seu_username')")
    print("   >>> user.profile.is_dev = True")
    print("   >>> user.profile.save()")
    print("   >>> exit()\n")

    print("3️⃣  Iniciar o servidor:")
    print("   python manage.py runserver\n")

    print("4️⃣  Acessar:")
    print("   Site: http://127.0.0.1:8000/")
    print("   Admin: http://127.0.0.1:8000/admin/\n")

    print(f"{'='*60}")
    print("✨ Configuração básica concluída!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

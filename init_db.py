"""
Script para inicializar la base de datos y crear usuarios
Ejecutar: python init_db.py
"""

from app import create_app, db
from app.models.models import User, Vehicle, MonthlyClient
from datetime import datetime, timedelta

def init_database():
    app = create_app()
    
    with app.app_context():
        # Eliminar todas las tablas y recrearlas
        print("Eliminando tablas existentes...")
        db.drop_all()
        
        print("Creando nuevas tablas...")
        db.create_all()
        
        # Crear usuarios operadores
        print("Creando usuarios operadores...")
        users = [
            {'username': 'operador1', 'password': '1234', 'name': 'Juan Pérez'},
            {'username': 'operador2', 'password': '1234', 'name': 'María García'},
            {'username': 'operador3', 'password': '1234', 'name': 'Carlos López'},
            {'username': 'operador4', 'password': '1234', 'name': 'Ana Martínez'},
        ]
        
        for user_data in users:
            user = User(username=user_data['username'], name=user_data['name'])
            user.set_password(user_data['password'])
            db.session.add(user)
            print(f"  ✓ Usuario creado: {user_data['username']}")
        
        # Crear algunos clientes mensuales de ejemplo (opcional)
        print("\nCreando clientes mensuales de ejemplo...")
        monthly_clients = [
            {
                'plate': 'ABC123',
                'model': 'Toyota Corolla 2020',
                'phone': '3815551234',
                'vehicle_type': 'auto',
                'expiration_date': datetime.now() + timedelta(days=30)
            },
            {
                'plate': 'XYZ789',
                'model': 'Honda CG 150',
                'phone': '3815555678',
                'vehicle_type': 'moto',
                'expiration_date': datetime.now() + timedelta(days=15)
            },
        ]
        
        for client_data in monthly_clients:
            client = MonthlyClient(**client_data)
            db.session.add(client)
            print(f"  ✓ Cliente mensual creado: {client_data['plate']}")
        
        # Guardar cambios
        db.session.commit()
        
        print("\n✅ Base de datos inicializada correctamente!")
        print("\n📋 Credenciales de acceso:")
        print("=" * 50)
        for user_data in users:
            print(f"Usuario: {user_data['username']} | Contraseña: {user_data['password']}")
        print("=" * 50)
        print("\n🚀 Puede iniciar la aplicación con: python run.py")

if __name__ == '__main__':
    init_database()
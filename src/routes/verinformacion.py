from flask import Blueprint, render_template
from models import Remesa, Inventario, Proveedores, Ventas, Paciente, Pagos

verinformacion_bp = Blueprint('verinformacion', __name__)

@verinformacion_bp.route('/remesas', methods=['GET'])
def ver_remesas():
    remesas = Remesa.query.all()  # Obtener todos los registros de la tabla Remesa
    return render_template('verinformacion/remesa.html', datos=remesas)  # Pasar a la plantilla

@verinformacion_bp.route('/inventarios', methods=['GET'])
def ver_inventarios():
    inventarios = Inventario.query.all()  # Obtener todos los registros de la tabla Inventario
    return render_template('verinformacion/inventarios.html', datos=inventarios)  # Pasar a la plantilla

@verinformacion_bp.route('/proveedores', methods=['GET'])
def ver_proveedores():
    proveedores = Proveedores.query.all()
    print(proveedores)  # Obtener todos los registros de la tabla Proveedores
    return render_template('verinformacion/proveedores.html', datos=proveedores)  # Pasar a la plantilla

@verinformacion_bp.route('/ventas', methods=['GET'])
def ver_ventas():
    ventas = Ventas.query.all()  # Obtener todos los registros de la tabla Ventas
    return render_template('verinformacion/ventas.html', datos=ventas)  # Pasar a la plantilla

@verinformacion_bp.route('/pacientes', methods=['GET'])
def ver_pacientes():
    pacientes = Paciente.query.all()  # Obtener todos los registros de la tabla Paciente
    return render_template('verinformacion/paciente.html', datos=pacientes)  # Pasar a la plantilla

@verinformacion_bp.route('/pagos', methods=['GET'])
def ver_pagos():
    pagos = Pagos.query.all()  # Obtener todos los registros de la tabla Pagos
    return render_template('verinformacion/pagos.html', datos=pagos)  # Pasar a la plantilla

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ============================================
# PROTOTIPO INTERACTIVO DE SOLUCIONES OSBRA
# ============================================

class OSBRASolutionsGenerator:
    """Generador de soluciones automáticas para problemas ciudadanos"""
    
    def __init__(self):
        self.soluciones_db = self._cargar_base_soluciones()
        self.prioridades = self._definir_prioridades()
        self.recursos = self._calcular_recursos()
    
    def _cargar_base_soluciones(self):
        """Base de datos de soluciones por categoría"""
        return {
            'Salud': {
                'problemas_comunes': [
                    'falta de médicos', 'hospital sin personal', 'centro de salud cerrado',
                    'no hay medicamentos', 'ambulancia no llega', 'urgencias colapsadas'
                ],
                'soluciones_inmediatas': [
                    'Contratar médicos especialistas de forma urgente',
                    'Abrir turnos de 24 horas en centros de salud',
                    'Implementar sistema de telemedicina',
                    'Dotar de medicamentos esenciales'
                ],
                'soluciones_mediano_plazo': [
                    'Construir nuevos hospitales en zonas críticas',
                    'Capacitar personal sanitario local',
                    'Implementar sistema de citas digitales',
                    'Crear red de ambulancias municipales'
                ],
                'presupuesto_estimado': 500000000,  # 500 millones COP
                'tiempo_implementacion': '3-6 meses'
            },
            'Educación': {
                'problemas_comunes': [
                    'falta de profesores', 'escuela sin aulas', 'no hay materiales',
                    'colegio cerrado', 'profesores mal pagados', 'infraestructura deteriorada'
                ],
                'soluciones_inmediatas': [
                    'Contratar docentes de forma masiva',
                    'Rehabilitar aulas existentes',
                    'Dotar de materiales educativos básicos',
                    'Implementar clases virtuales de emergencia'
                ],
                'soluciones_mediano_plazo': [
                    'Construir nuevas escuelas y colegios',
                    'Capacitar docentes en nuevas tecnologías',
                    'Implementar programa de alimentación escolar',
                    'Crear bibliotecas digitales municipales'
                ],
                'presupuesto_estimado': 300000000,  # 300 millones COP
                'tiempo_implementacion': '6-12 meses'
            },
            'Seguridad': {
                'problemas_comunes': [
                    'delincuencia alta', 'policía no patrulla', 'calles oscuras',
                    'robos frecuentes', 'inseguridad nocturna', 'bandas delictivas'
                ],
                'soluciones_inmediatas': [
                    'Aumentar patrullaje policial 24/7',
                    'Instalar cámaras de seguridad en puntos críticos',
                    'Mejorar iluminación pública',
                    'Implementar botones de pánico comunitarios'
                ],
                'soluciones_mediano_plazo': [
                    'Crear comisarías de barrio',
                    'Implementar sistema de videovigilancia inteligente',
                    'Programas de prevención comunitaria',
                    'Centros de rehabilitación para jóvenes'
                ],
                'presupuesto_estimado': 400000000,  # 400 millones COP
                'tiempo_implementacion': '2-4 meses'
            },
            'Medio Ambiente': {
                'problemas_comunes': [
                    'basura en las calles', 'recolección irregular', 'contaminación del río',
                    'aire contaminado', 'no hay reciclaje', 'vertederos ilegales'
                ],
                'soluciones_inmediatas': [
                    'Aumentar frecuencia de recolección de basura',
                    'Implementar recolección selectiva',
                    'Limpiar puntos críticos de contaminación',
                    'Sancionar vertederos ilegales'
                ],
                'soluciones_mediano_plazo': [
                    'Crear plantas de reciclaje municipales',
                    'Implementar programa de compostaje comunitario',
                    'Reforestar áreas degradadas',
                    'Educación ambiental masiva'
                ],
                'presupuesto_estimado': 200000000,  # 200 millones COP
                'tiempo_implementacion': '4-8 meses'
            }
        }
    
    def _definir_prioridades(self):
        """Sistema de priorización automática"""
        return {
            'critica': {'score_min': 0.8, 'tiempo_respuesta': '24 horas', 'color': '#FF0000'},
            'alta': {'score_min': 0.6, 'tiempo_respuesta': '48 horas', 'color': '#FF8C00'},
            'media': {'score_min': 0.4, 'tiempo_respuesta': '1 semana', 'color': '#FFD700'},
            'baja': {'score_min': 0.0, 'tiempo_respuesta': '2 semanas', 'color': '#32CD32'}
        }
    
    def _calcular_recursos(self):
        """Cálculo de recursos necesarios"""
        return {
            'personal_requerido': {
                'Salud': {'medicos': 50, 'enfermeros': 100, 'administrativos': 25},
                'Educación': {'profesores': 200, 'coordinadores': 20, 'administrativos': 30},
                'Seguridad': {'policias': 80, 'vigilantes': 40, 'coordinadores': 15},
                'Medio Ambiente': {'recolectores': 60, 'supervisores': 20, 'educadores': 10}
            },
            'infraestructura': {
                'Salud': ['hospitales', 'centros_salud', 'ambulancias'],
                'Educación': ['escuelas', 'colegios', 'bibliotecas'],
                'Seguridad': ['comisarias', 'camaras', 'vehiculos'],
                'Medio Ambiente': ['plantas_reciclaje', 'vehiculos_recoleccion', 'centros_educacion']
            }
        }
    
    def analizar_problema(self, comentario, categoria, urgencia, ciudad):
        """Analiza un problema y genera soluciones automáticas"""
        print(f"\n{'='*80}")
        print(f"ANÁLISIS AUTOMÁTICO DE PROBLEMA CIUDADANO")
        print(f"{'='*80}")
        print(f"Comentario: '{comentario}'")
        print(f"Categoría: {categoria}")
        print(f"Urgencia: {urgencia}")
        print(f"Ciudad: {ciudad}")
        
        # Calcular prioridad
        prioridad = self._calcular_prioridad(categoria, urgencia, ciudad)
        
        # Generar soluciones
        soluciones = self._generar_soluciones(categoria, prioridad)
        
        # Calcular recursos
        recursos = self._calcular_recursos_necesarios(categoria, prioridad)
        
        # Generar plan de acción
        plan = self._generar_plan_accion(categoria, prioridad, ciudad)
        
        return {
            'prioridad': prioridad,
            'soluciones': soluciones,
            'recursos': recursos,
            'plan': plan
        }
    
    def _calcular_prioridad(self, categoria, urgencia, ciudad):
        """Calcula la prioridad del problema"""
        score = 0.5  # Base
        
        # Factor urgencia
        if urgencia == 'Urgente':
            score += 0.3
        else:
            score += 0.1
        
        # Factor ciudad (ciudades con más problemas)
        ciudades_prioritarias = ['Bogotá', 'Manizales', 'Medellín']
        if ciudad in ciudades_prioritarias:
            score += 0.2
        
        # Determinar nivel de prioridad
        for nivel, config in self.prioridades.items():
            if score >= config['score_min']:
                return {
                    'nivel': nivel,
                    'score': score,
                    'tiempo_respuesta': config['tiempo_respuesta'],
                    'color': config['color']
                }
        
        return {
            'nivel': 'baja',
            'score': score,
            'tiempo_respuesta': '2 semanas',
            'color': '#32CD32'
        }
    
    def _generar_soluciones(self, categoria, prioridad):
        """Genera soluciones específicas para la categoría"""
        if categoria not in self.soluciones_db:
            return {'error': 'Categoría no reconocida'}
        
        soluciones_cat = self.soluciones_db[categoria]
        
        if prioridad['nivel'] in ['critica', 'alta']:
            soluciones_aplicar = soluciones_cat['soluciones_inmediatas']
        else:
            soluciones_aplicar = soluciones_cat['soluciones_mediano_plazo']
        
        return {
            'inmediatas': soluciones_cat['soluciones_inmediatas'],
            'mediano_plazo': soluciones_cat['soluciones_mediano_plazo'],
            'aplicar_ahora': soluciones_aplicar,
            'presupuesto': soluciones_cat['presupuesto_estimado'],
            'tiempo': soluciones_cat['tiempo_implementacion']
        }
    
    def _calcular_recursos_necesarios(self, categoria, prioridad):
        """Calcula recursos necesarios para implementar soluciones"""
        if categoria not in self.recursos['personal_requerido']:
            return {'error': 'Categoría no reconocida'}
        
        personal = self.recursos['personal_requerido'][categoria].copy()
        infraestructura = self.recursos['infraestructura'][categoria].copy()
        
        # Ajustar según prioridad
        multiplicador = 1.0
        if prioridad['nivel'] == 'critica':
            multiplicador = 1.5
        elif prioridad['nivel'] == 'alta':
            multiplicador = 1.2
        
        for cargo in personal:
            personal[cargo] = int(personal[cargo] * multiplicador)
        
        return {
            'personal': personal,
            'infraestructura': infraestructura,
            'multiplicador': multiplicador
        }
    
    def _generar_plan_accion(self, categoria, prioridad, ciudad):
        """Genera un plan de acción detallado"""
        return {
            'fase_1_inmediata': {
                'tiempo': '0-48 horas',
                'acciones': [
                    'Evaluación de la situación actual',
                    'Asignación de recursos de emergencia',
                    'Comunicación con autoridades locales',
                    'Implementación de medidas temporales'
                ]
            },
            'fase_2_corto_plazo': {
                'tiempo': '1-4 semanas',
                'acciones': [
                    'Contratación de personal especializado',
                    'Adquisición de equipos necesarios',
                    'Capacitación del personal',
                    'Implementación de soluciones inmediatas'
                ]
            },
            'fase_3_mediano_plazo': {
                'tiempo': '1-6 meses',
                'acciones': [
                    'Construcción de infraestructura',
                    'Implementación de programas permanentes',
                    'Monitoreo y evaluación continua',
                    'Ajustes basados en resultados'
                ]
            },
            'responsables': {
                'coordinador_general': 'Alcaldía Municipal',
                'coordinador_tecnico': f'Secretaría de {categoria}',
                'supervisor_campo': 'Funcionario designado',
                'evaluador': 'Comité ciudadano'
            }
        }
    
    def generar_reporte_completo(self, problemas_analizados):
        """Genera un reporte completo con todas las soluciones"""
        print(f"\n{'='*80}")
        print(f"REPORTE COMPLETO DE SOLUCIONES OSBRA")
        print(f"{'='*80}")
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Problemas analizados: {len(problemas_analizados)}")
        
        # Resumen por categoría
        resumen_categorias = {}
        for problema in problemas_analizados:
            cat = problema['categoria']
            if cat not in resumen_categorias:
                resumen_categorias[cat] = {'total': 0, 'criticos': 0, 'presupuesto': 0}
            resumen_categorias[cat]['total'] += 1
            if problema['prioridad']['nivel'] in ['critica', 'alta']:
                resumen_categorias[cat]['criticos'] += 1
            resumen_categorias[cat]['presupuesto'] += problema['soluciones']['presupuesto']
        
        print(f"\nRESUMEN POR CATEGORÍA:")
        for cat, datos in resumen_categorias.items():
            print(f"  {cat}: {datos['total']} problemas ({datos['criticos']} críticos)")
            print(f"    Presupuesto estimado: ${datos['presupuesto']:,} COP")
        
        # Presupuesto total
        presupuesto_total = sum(datos['presupuesto'] for datos in resumen_categorias.values())
        print(f"\nPRESUPUESTO TOTAL ESTIMADO: ${presupuesto_total:,} COP")
        
        return resumen_categorias

def crear_dashboard_soluciones():
    """Crea un dashboard visual de las soluciones generadas"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('OSBRA - PROTOTIPO DE SOLUCIONES AUTOMÁTICAS', fontsize=16, fontweight='bold')
    
    # Datos de ejemplo
    categorias = ['Salud', 'Educación', 'Seguridad', 'Medio Ambiente']
    problemas = [2515, 2509, 2540, 2436]
    presupuestos = [500, 300, 400, 200]  # millones COP
    prioridades = [45, 35, 60, 25]  # % críticos
    
    # 1. Distribución de problemas
    axes[0,0].bar(categorias, problemas, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    axes[0,0].set_title('Problemas por Categoría', fontweight='bold')
    axes[0,0].set_ylabel('Número de Reportes')
    for i, v in enumerate(problemas):
        axes[0,0].text(i, v + 20, str(v), ha='center', va='bottom', fontweight='bold')
    
    # 2. Presupuesto requerido
    axes[0,1].bar(categorias, presupuestos, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    axes[0,1].set_title('Presupuesto Estimado (Millones COP)', fontweight='bold')
    axes[0,1].set_ylabel('Presupuesto (Millones)')
    for i, v in enumerate(presupuestos):
        axes[0,1].text(i, v + 10, f'${v}M', ha='center', va='bottom', fontweight='bold')
    
    # 3. Prioridad de problemas
    colors_prioridad = ['#FF0000', '#FF8C00', '#FFD700', '#32CD32']
    axes[1,0].pie(prioridades, labels=categorias, autopct='%1.1f%%', colors=colors_prioridad)
    axes[1,0].set_title('Problemas Críticos por Categoría', fontweight='bold')
    
    # 4. Timeline de implementación
    fases = ['Inmediata\n(0-48h)', 'Corto Plazo\n(1-4 sem)', 'Mediano Plazo\n(1-6 mes)']
    cobertura = [80, 60, 40]  # % de problemas cubiertos
    axes[1,1].bar(fases, cobertura, color=['#FF4444', '#FFAA44', '#44AA44'])
    axes[1,1].set_title('Cobertura por Fase de Implementación', fontweight='bold')
    axes[1,1].set_ylabel('Problemas Cubiertos (%)')
    axes[1,1].set_ylim(0, 100)
    for i, v in enumerate(cobertura):
        axes[1,1].text(i, v + 2, f'{v}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('prototipo_soluciones_osbra.png', dpi=300, bbox_inches='tight')
    print("[OK] Dashboard de soluciones guardado: prototipo_soluciones_osbra.png")

def demostrar_prototipo():
    """Demuestra el funcionamiento del prototipo de soluciones"""
    print("[INICIANDO] DEMOSTRACION DEL PROTOTIPO OSBRA")
    print("="*80)
    
    # Inicializar generador de soluciones
    osbra = OSBRASolutionsGenerator()
    
    # Problemas de ejemplo para demostrar
    problemas_demo = [
        {
            'comentario': 'necesitamos más médicos en el hospital, hay mucha gente esperando',
            'categoria': 'Salud',
            'urgencia': 'Urgente',
            'ciudad': 'Bogotá'
        },
        {
            'comentario': 'no hay suficientes profesores en la escuela del barrio',
            'categoria': 'Educación',
            'urgencia': 'No urgente',
            'ciudad': 'Medellín'
        },
        {
            'comentario': 'hay mucha delincuencia en el barrio, necesitamos más policía',
            'categoria': 'Seguridad',
            'urgencia': 'Urgente',
            'ciudad': 'Manizales'
        },
        {
            'comentario': 'las calles están llenas de basura, no recogen los desechos',
            'categoria': 'Medio Ambiente',
            'urgencia': 'No urgente',
            'ciudad': 'Cali'
        }
    ]
    
    # Analizar cada problema
    resultados = []
    for i, problema in enumerate(problemas_demo, 1):
        print(f"\n[ANALISIS] {i}/4")
        resultado = osbra.analizar_problema(
            problema['comentario'],
            problema['categoria'],
            problema['urgencia'],
            problema['ciudad']
        )
        
        # Mostrar resultados
        print(f"\n[PRIORIDAD] {resultado['prioridad']['nivel'].upper()}")
        print(f"   Score: {resultado['prioridad']['score']:.2f}")
        print(f"   Tiempo de respuesta: {resultado['prioridad']['tiempo_respuesta']}")
        
        print(f"\n[SOLUCIONES INMEDIATAS]:")
        for j, solucion in enumerate(resultado['soluciones']['aplicar_ahora'], 1):
            print(f"   {j}. {solucion}")
        
        print(f"\n[PRESUPUESTO] ${resultado['soluciones']['presupuesto']:,} COP")
        print(f"[TIEMPO] {resultado['soluciones']['tiempo']}")
        
        print(f"\n[RECURSOS NECESARIOS]:")
        for cargo, cantidad in resultado['recursos']['personal'].items():
            print(f"   {cargo.title()}: {cantidad} personas")
        
        print(f"\n[PLAN DE ACCION]:")
        for fase, detalles in resultado['plan'].items():
            if fase.startswith('fase_'):
                print(f"   {fase.replace('_', ' ').title()}: {detalles['tiempo']}")
                for accion in detalles['acciones'][:2]:  # Mostrar solo 2 acciones
                    print(f"     • {accion}")
        
        resultados.append({
            'categoria': problema['categoria'],
            'prioridad': resultado['prioridad'],
            'soluciones': resultado['soluciones'],
            'recursos': resultado['recursos'],
            'plan': resultado['plan']
        })
    
    # Generar reporte completo
    osbra.generar_reporte_completo(resultados)
    
    # Crear dashboard visual
    crear_dashboard_soluciones()
    
    print(f"\n[COMPLETADO] DEMOSTRACION COMPLETADA")
    print(f"[ARCHIVOS] Archivos generados:")
    print(f"   • prototipo_soluciones_osbra.png")
    print(f"   • Reporte completo en consola")

if __name__ == "__main__":
    demostrar_prototipo()

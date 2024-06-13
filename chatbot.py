
import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hola', ['hola', 'saludos', 'buenas'], single_response=True)
    response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
    response('Claro\n\n'
             'Dia Miercoles\n'+
             'Horario:    2:00-3:40 \n'+
             'Docente:    Hugo Espetia Huamanga \n'+
             'Salon:      301 \n'+
             'Dia Jueves\n'+
             'Horario:    2:00-5:09 \n'+
             'Docente:    Hugo Espetia Huamanga \n'+
             'Salon:      801 \n'
             ,['horario','cual'],required_words=['horario'])
    response('Los examenes son en las semanas: \n'+
             'Semana:  4 ' + ' Semana:  7 \n'+
             'Semana:  8 ' + ' Semana:  12 \n'+
             'Semana:  15' + ' Semana:  16 \n'
             ,['semana','examen','que','fecha'],required_words=['examenes'])
    response('El total de creditos es: 4',['creditos','total','cuantos'],required_words=['creditos'])
    response('Construcción de Software es una asignatura obligatoria de especialidad, desarrolla en un nivel intermedio las competencias transversales Gestión de Proyectos y Experimentación',['introduccion','curso','puedes'],required_words=['introduccion'])
    response('El total de horas son: \n'+
             'Horas teoricas:  4 \n'+
             'Horas practicas: 2 \n',['cuantas','horas','tienes'],required_words=['horas'])
    response('Al finalizar la asignatura, el estudiante será capaz de aplicar los principios fundamentales de la construcción de software empleando metodologías y herramientas de construcción de software'
             ,['resultado','resultados','cual'],required_words=['resultado'])
    """""
    response('La unidad 1 tiene como ejes tematicos'+
            '1. Minimización de la complejidad'+
             '2. Anticipación a los cambios'+
             '3. Construcción para verificación'+
             '4. Reutilización'+
             '5. Estándares en la construcción',['unidad1'],required_words=['unidad1'])
    response('Unidad 2: Gestión de la construcción de software'+
             '1. Modelos de construcción'
             '2. Plan de construcción'
             '3. Métricas de la construcción',['unidad2'],required_words=['unidad2'])
    response('Unidad 3: Prácticas de código completo y código limpio'+
             '1. Diseño de la construcción'+
             '2. Lenguajes de construcción'+
             '3. Codificación'+
             '4. Pruebas de construcción'+
             '5. Construcción para reutilización'+
             '6. Construcción con reutilización'+
             '7. Calidad de construcción'+
             '8. Integración',['unidad3'],required_words=['unidad3'])
    response('Unidad 4: Tecnologías y Herramientas para la construcción de software'+
             '1. Diseño y uso API'+
             '2. Problemas de tiempo de ejecución orientado a objetos'+
             '3. Parametrización y genéricos'+
             '4. Afirmaciones, diseño por contrato y programación defensiva'+
             '5. Control de errores, control de excepciones, y la tolerancia a fallos'+
             '6. Modelos ejecutables'+
             '7. Técnicas de construcción basadas en estados y tablas'+
             '8. Configuración de tiempo de ejecución y la internacionalización'+
             '9. Procesamiento de entrada basada en gramática'+
             '10. Middleware'+
             '11. Métodos de construcción para software distribuido'+
             '12. Construcción de sistemas heterogéneos'+
             '13. Entornos de desarrollo'+
             '14. Constructores GUI'+
             '15. Herramientas de prueba de unidad',['unidad4','cuales','ejes','tematicos'],required_words=['unidad4'])
             """
    best_match = max(highest_prob, key=highest_prob.get)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Búscalo en google a ver que tal'][random.randrange(3)]
    return response
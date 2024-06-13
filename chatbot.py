
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
             'Curso:    Construcción de Software \n'+
             'Horario:    2:00-3:40 \n'+
             'Docente:    Hugo Espetia Huamanga \n'+
             'Salon:      301 \n\n'+
             'Dia Jueves\n'+
             'Curso:    Construcción de Software \n'+
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
    
    response('La unidad 1 tiene como ejes tematicos\n'+
            '1. Minimización de la complejidad\n'+
             '2. Anticipación a los cambios\n'+
             '3. Construcción para verificación\n'+
             '4. Reutilización\n'+
             '5. Estándares en la construcción\n',['primera','1'],required_words=['primera'])
    response('Unidad 2: Gestión de la construcción de software\n'+
             '1. Modelos de construcción\n'+
             '2. Plan de construcción\n'+
             '3. Métricas de la construcción',['eje','2'],required_words=['segunda'])
    response('Unidad 3: Prácticas de código completo y código limpio'+
             '1. Diseño de la construcción\n'+
             '2. Lenguajes de construcción\n'+
             '3. Codificación\n'+
             '4. Pruebas de construcción\n'+
             '5. Construcción para reutilización\n'+
             '6. Construcción con reutilización\n'+
             '7. Calidad de construcción\n'+
             '8. Integración',['temas','3'],required_words=['tercera'])
    response('Unidad 4: Tecnologías y Herramientas para la construcción de software\n'+
             '1. Diseño y uso API\n'+
             '2. Problemas de tiempo de ejecución orientado a objetos\n'+
             '3. Parametrización y genéricos\n'+
             '4. Afirmaciones, diseño por contrato y programación defensiva\n'+
             '5. Control de errores, control de excepciones, y la tolerancia a fallos\n'+
             '6. Modelos ejecutables\n'+
             '7. Técnicas de construcción basadas en estados y tablas\n'+
             '8. Configuración de tiempo de ejecución y la internacionalización\n'+
             '9. Procesamiento de entrada basada en gramática\n'+
             '10. Middleware\n'+
             '11. Métodos de construcción para software distribuido\n'+
             '12. Construcción de sistemas heterogéneos\n'+
             '13. Entornos de desarrollo\n'+
             '14. Constructores GUI\n'+
             '15. Herramientas de prueba de unidad',['contenido','4'],required_words=['cuarta'])
    
    response('Soy Glados , un chatbot de soporte para el curso de Construccion de Software\nEntre la informacion que te puedo brindar esta: \n'+
             '1. Horario de clases\n'+
             '2. Silabo del curso\n'+
             '3. Cantidad de creditos del curso\n'+
             '4. Fechas de examenes\n'+
             '5. Tus resultados al final del curso\n'+
             '6. Proximamente mas funcionalidades',['que','eres','realizas','como','ayudar','ayudarme'],required_words=['eres'])
             
    best_match = max(highest_prob, key=highest_prob.get)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Búscalo en google a ver que tal'][random.randrange(3)]
    return response
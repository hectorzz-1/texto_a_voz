# Este es el main aqui se va a consentrar todo el codigo de los demas scripts

# Clases Locales
import decoration
import audio_config
import text_providers
import interfaz
import text_validators

# Clases Externas
import time


# Instancias del script decoration.py
offline = decoration.OfflineData()
online = decoration.OnlineData()
mode_decoration = decoration.ModeDecorator(offline, online)
change_voice = decoration.VoicesData()
change_language = decoration.LanguageData()
start_write = decoration.WriteData()
opcions_offline = decoration.OpcionsDecorator(change_language, start_write)
opcions_online = decoration.OpcionsDecorator(change_voice, start_write)
file_option = decoration.FileData()
text_option = decoration.TextData()
opcions_get_text = decoration.OpcionsDecorator(text_option, file_option)
list_show = decoration.ListShow()

# Intancias del script audio_config.py
language_config = audio_config.LanguageConfig()
voice_config = audio_config.VoiceConfig()

# Intancias del script interfaz.py
file_interfaz = interfaz.GUIFileSelector()

# Intancias del script text_providers.py
text_provider = text_providers.ConsoleTextProvider()
file_provider = text_providers.FileProvider(file_interfaz)
get_file_text = text_providers.GetFileText()

# Intancias del script text_validators.py
if_empty = text_validators.TextValidatorIfEmpty()
if_characters = text_validators.TextValidatorValid()
if_onlyespace = text_validators.TextValidatorEspace()
if_Long = text_validators.TextValidatorLong()
validator = text_validators.Validator(if_empty, if_characters ,if_onlyespace ,if_Long)


for i in range(3):
    # Pedir en que modo quiere el audio si online u offline
    mode = mode_decoration.consultation()

    # Si prefiere offline
    if mode == 1:
        for i in range(3):
            # Dar opciones si quiere cambiar el idioma o escribir directamente
            selection = opcions_offline.consultation()

            # Si quiere cambiar el idioma
            if selection == 1:
                for i in range(5):
                    # Mostrar la lista de idiomas disponibles
                    print(list_show.show(language_config.list_language))
                    
                    language = language_config.config()

                    # Si la respuesta es correcta
                    if language != False:
                        break
                    
                    # Si no dio una respuesta correcta
                    else:
                        print("Por favor escribra el nombre del idioma que quiera")

                        if i == 2:
                            print("se usará el pre determinado (ingles)")
                            language = "en"
                            break

                        continue

            elif selection != 2:
                print("Por favor ponga el indice de la opcion o la opcion que quiera")
                time.sleep(1)
                continue

            break

    # Si prefiere online
    elif mode == 2:
        for i in range(3):
            # Dar opciones si quiere cambiar la voz o escribir directamente
            selection = opcions_offline.consultation()

            # Si quiere cambiar la voz
            if selection == 1:
                for i in range(5):
                    # Mostrar la lista de idiomas disponibles
                    print(list_show.show(voice_config.voices_list))
                    
                    voice = voice_config.config()

                    # Si la respuesta es correcta
                    if voice != False:
                        break
                    
                    # Si no dio una respuesta correcta
                    else:
                        print("Por favor escribra el nombre de la voz que quiera")

                        if i == 2:
                            print("se usará el pre determinado (alloy)")
                            voice = "alloy"
                            break

                        continue

            elif selection != 2:
                print("Por favor ponga el indice de la opcion o la opcion que quiera")
                time.sleep(1)
                continue

            break

    # Si no puso una respuesta correcta
    else:
        print("Por favor ponga el indice de la opcion o la opcion que quiera")
        time.sleep(3)
        continue

    break

# Manejar el texto para convertirlo a audio
for i in range(3):
    # Preguntar si desea pasar el texto por un file o escribir el texto
    print("Como desea dar el texto")
    get_text = opcions_get_text.consultation()

    # Si quiere escribir
    if get_text == 1:
        for i in range(3):
            # Inicialisar la lista de errores
            fails = []

            # Pedirá el texto al usuario
            text = text_provider.get_text()

            # Validar que el texto sea valido para convertir a audio
            validate = validator.validate(text)

            # Calcula cuantos errores hubo si es que hubo
            for i in validate:
                if i["check"] == True:
                    pass
                else:
                    fails.append(i["error"])

            # Si no hay errores saldrá del for 
            # y significará que el texto es valido
            if not fails:
                break
            # Si hay algun error lo imprimirá por pantalla
            # y le volverá a pedir un texto 
            else:
                for i in fails:
                    print("Error:",i)
                
                continue
                        
        break

    # Si quiere pasar un file
    elif get_text == 2:
        print(2)
        break

    # Si no dio una respuesta correcta
    else:
        print("Por favor ponga el indice de la opcion o la opcion que quiera")
        time.sleep(1)
        continue
# Este es el main aqui se va a consentrar todo el codigo de los demas scripts

# Clases Locales
import decoration
import audio_config
import text_providers
import interfaz
import text_validators
import files_validators
import limit_online

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
name_config = audio_config.NameConfig()

# Intancias del script interfaz.py
file_interfaz = interfaz.GUIFileSelector()
save_interfaz = interfaz.FolderSelector()

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

# Intancias del script files_validators.py
file_validator = files_validators.ValidTextFile()

# Intancias del script limit_online.py
check_limit_day = limit_online.DayLimit()
limit_Use_online = limit_online.UseLimit()



name = name_config.config()
if name != None:
    path_save = save_interfaz.select_folder()
    print(f"{path_save}/{name}")


if __name__ == "__mai__":   
    # Definir la variable que valida si se puede proseder a hacer el audio
    checkout= False

    for i in range(3):
        # Pedir en que modo quiere el audio si online u offline
        mode = mode_decoration.consultation()
        # si es un nuevo dia renueva los usos online diarios
        check_limit_day.limitador()
    
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
            # Verifica si puedes usar el modo online
            online_use = limit_Use_online.count_usage_limiter()
            if online_use == False:
                print("Ya no tienes usos Online por hoy")
                break
            
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
                # Pedirá el texto al usuario
                text = text_provider.get_text()
    
                # Validar que el texto sea valido para convertir a audio
                validate = validator.validate(text)
    
                # Calcula los errores que hubo si es que hubo
                for i in validate:
                    if i["check"] == True:
                        checkout = True
                        pass
                    
                    # Si hay algun error lo imprimirá por pantalla
                    # y le volverá a pedir un texto 
                    else:
                        print("Error:", i["error"])
                        checkout = False
                        break
                    
                # Si todas las validaciones fueron correctas saldrá del for
                if checkout == True:
                    break                       
                
        # Si quiere pasar un file
        elif get_text == 2:
                
            for i in range(3):
                # Obtiene el path del file
                file = file_provider.get_text()
    
                # Valida que el file sea de texto plano
                file_validation = file_validator.file_valid()
                
                # Si es valido extraerá el texto del file
                if file_validation == True:
                    text = get_file_text.get_text_of_file()
    
                # Si no es valido lo volverá a pedir 
                else:
                    print("Por favor introduzca un file valido (que sea de texto plano)")
                    continue
                
                # Validar que el texto sea valido para convertir a audio
                validate = validator.validate(text)
    
                # Calcula los errores que hubo si es que hubo
                for i in validate:
                    if i["check"] == True:
                        checkout = True
                        pass
                    
                    # Si hay algun error lo imprimirá por pantalla
                    # y le volverá a pedir un texto 
                    else:
                        print("FileError:", i["error"])
                        checkout = False
                        break
                    
                # Si todas las validaciones fueron correctas saldrá del for
                if checkout == True:
                    break  
                
        # Si no dio una respuesta correcta
        else:
            print("Por favor ponga el indice de la opcion o la opcion que quiera")
            time.sleep(1)
            continue
        
        break
    
    # Valida que todo esté correcto para generar el audio
    if checkout == True:
        # Crear un nombre
        name = name_config.config()
        path_save = save_interfaz
        path_save = ""
        # Generar el audio offline
        if mode == 1:
            pass
        
        # Generar el audio Online
        else:
            pass    
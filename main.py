from interfaz import GUIFileSelector
from text_providers import GetFileText, FileProvider
from files_validators import ValidTextFile


i = GUIFileSelector()

get_file = FileProvider(i)
file_validator = ValidTextFile()
get_ft = GetFileText()


file = get_file.get_text()

if file_validator.file_valid(file):
    file = get_ft.get_text_of_file(file)
    print(file)
else:
    print("Error")
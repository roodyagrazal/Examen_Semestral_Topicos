## Examen Semestral ##
Para correr el proyecto debe ejecutar primero el script ## docker_build.sh ## 
Debe estar en la raiz del proyecto para ejecutar el siguiente comando.
~/Examen/Examen_Semestral_Topicos ./scripts/docker_build.sh  
Esto generara la imagen del proyecto.

Luego debemos ejecutar el proyecto con el script ## docker_run.sh ##
~/Examen/Examen_Semestral_Topicos ./scripts/docker_run.sh

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


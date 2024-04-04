import subprocess
import webbrowser
import time

def ejecutar_pruebas_behave():
    # Ejecutar las pruebas de Behave y generar el informe de Allure en formato json
    subprocess.run(['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o', 'allure-results'])

def generar_informe_web():

    subprocess.Popen(['allure', 'serve', 'allure-results'], shell=True)

if __name__ == "__main__":
    # Ejecutar las pruebas de Behave
    ejecutar_pruebas_behave()
    
    # Tiempo de espera para generar los resultados de las pruebas
    time.sleep(2)
    
    # Generar el informe de Allure y lo abre en el navegador
    generar_informe_web()

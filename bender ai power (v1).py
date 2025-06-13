import threading
import speech_recognition as sr
import pyautogui
from colorama import init, Fore

# Inicializa o colorama para suporte a cores no Windows
init()

# Configurações
reconhecedor = sr.Recognizer()
pyautogui.PAUSE = 0.01  # Reduz o atraso entre ações do pyautogui

# Arte ASCII e informações iniciais com cores
print(f"""
{Fore.CYAN}       
                     $$$                       
                    $   $                      
                     $$$                       
                     $ $                       
                     $ $                       
                   $$$ $$$                     
                 $$  $$$  $$$                  
               $$  $$$$$$$   $                 
              $               $                
             $                 $               
             $                 $               
             $     $$$$$$$$$$$$$$$             
             $    $               $            
             $    $   $$$$$$$$$$$$$            
             $   $   $           $$$           
             $   $   $ $$$   $$$  $$           
             $   $   $ $$$   $$$  $$           
             $   $   $           $$$           
             $    $   $$$$$$$$$$$$$            
             $     $$$$$$$$$$$$$$              
             $                 $               
             $    $$$$$$$$$$$$$$               
             $   $  $  $  $  $                 
             $  $$$$$$$$$$$$$$                 
             $  $   $  $  $  $                 
             $   $$$$$$$$$$$$$$$               
            $$$                 $$$            
          $$   $$$         $$$$$   $$          
        $$        $$$$$$$$$          $$$       
       $  $$                     $$$$   $$     
    $$$$$   $$$$$$$$      $$$$$$$       $ $    
  $      $$         $$$$$$              $ $$   
 $    $    $                            $ $ $  
 $     $   $              $$$$$$$$$$$   $ $ $$ 
 $$$    $   $  $$$$$$$$$$$$          $   $ $ $$
$   $$$$    $  $                     $   $ $$ $
$$$    $   $$  $                     $$  $ $  $
$   $  $  $$   $                      $  $$$  $
$     $$ $$    $               $$$    $  $ $  $
    {Fore.RESET}
                        
{Fore.GREEN}Bender AI Power - Versão 1.0{Fore.RESET}

{Fore.YELLOW}Comandos de voz disponíveis:
- 'slide passar', 'pode passar', 'slider passa': Avança o slide
- 'slide voltar', 'pode botar', 'slider vota': Volta o slide
- 'pode descer', 'slide descer': Desce a página
- 'subir slide', 'pode subir': Sobe a página{Fore.RESET}

{Fore.MAGENTA}Criado por: DevKauan{Fore.RESET}
""")

def escutar_comandos():
    with sr.Microphone() as mic:
        reconhecedor.adjust_for_ambient_noise(mic, duration=0.5)  # Reduz tempo de ajuste
        while True:
            try:
                audio = reconhecedor.listen(mic, timeout=5)  # Timeout reduzido
                comando = reconhecedor.recognize_google(audio, language="pt-BR").lower()
                
                # Processa comandos se contiver "pode", "slide" ou "slider"
                if "pode" in comando or "slide" in comando or "slider" in comando:
                    if "passar" in comando or "passa" in comando:
                        pyautogui.press('right')  # Avança o slide
                    elif "volta" in comando or "voltar" in comando or "vota" in comando or "votar" in comando or "botar" in comando or "bota" in comando:
                        pyautogui.press('left')  # Volta o slide
                    elif "descer" in comando:
                        pyautogui.scroll(-500)  # Desce o scroll (valor maior)
                    elif "subir" in comando:
                        pyautogui.scroll(500)   # Sobe o scroll (valor maior)
            except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
                pass  # Ignora erros silenciosamente

# Inicia a thread de voz
thread_voz = threading.Thread(target=escutar_comandos)
thread_voz.daemon = True
thread_voz.start()

# Mantém o programa rodando
while True:
    pass
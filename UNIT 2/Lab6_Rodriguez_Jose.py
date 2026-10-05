from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod

# Intentamos importar PIL, si falla, permitimos que el programa siga funcionando
try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# ================================
# LÓGICA DE NEGOCIO (POLIMORFISMO)
# ================================

class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")
    
    def turn_on(self):
        return f"{self.name}: Set the brightness to 100%"

class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Speaker")
    
    def turn_on(self):
        return f"{self.name}: Play The Rose music at volume 60%"

class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Hisense Inverter")  # Corregido el nombre a Hisense
     
    def turn_on(self):
        return f"{self.name}: Set the temperature to 72 degrees Fahrenheit"


# ================================
# INTERFAZ GRÁFICA (GUI)
# ================================

class SmartHomeApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab 6. Smart Home Controller (polymorphism)")
        self.geometry("450x420") 
        
        # Opciones para permitir maximizar y minimizar
        self.resizable(True, True) 
        
        self.devices = {
            "Light": SmartLight(),
            "Speaker": SmartSpeaker(),
            "AC": SmartAC()
        }
        
        self.build_ui()
          
    def build_ui(self):
        # 1. Cargar y mostrar el icono (Solo si PIL está instalado)
        if HAS_PIL:
            try:
                # Nombre exacto de tu archivo
                img_original = Image.open("Gemini_Generated_Image_9pfzrp9pfzrp9pfz_2.jpg")
                # Image.LANCZOS es más compatible con versiones anteriores de Pillow
                img_resized = img_original.resize((60, 60), getattr(Image, 'Resampling', Image).LANCZOS)
                
                self.home_icon = ImageTk.PhotoImage(img_resized)
                icon_label = ttk.Label(self, image=self.home_icon)
                icon_label.pack(pady=(15, 0))
            except Exception as e:
                print(f"No se pudo cargar la imagen: {e}")
        else:
            print("Pillow (PIL) no está instalado. El icono no se mostrará, pero la app funcionará.")

        # 2. Header (Título)
        title_label = ttk.Label(
            self, text="Smart Home Controller", 
            font=("Arial", 16, "bold"),
            foreground="blue"
        )
        title_label.pack(pady=(5, 20))
        
        # 3. Contenedor de dispositivos
        group_box = ttk.LabelFrame(
            self,
            text="Select device",
            padding=(20, 5) 
        )
        group_box.pack(pady=10, padx=20, fill="x")
        
        # Variable para almacenar la selección
        first_key = list(self.devices.keys())[0]
        self.selected_device = StringVar(value=first_key) 
        
        # Crear los Radiobuttons dinámicamente
        for device_name in self.devices.keys():
            rb = ttk.Radiobutton(
                group_box, 
                text=device_name, 
                value=device_name, 
                variable=self.selected_device
            )
            rb.pack(anchor="w", pady=5)
            
        # 4. Botón de encendido
        action_btn = ttk.Button(
            self, 
            text="Turn On", 
            command=self.activate_device
        )
        action_btn.pack(pady=15)
        
        # 5. Etiqueta para mostrar el resultado
        self.result_label = ttk.Label(
            self, 
            text="Waiting for command...", 
            font=("Arial", 11, "italic"),
            foreground="gray",
            wraplength=400,
            justify="center"
        )
        self.result_label.pack(pady=10)

    # Método de comportamiento polimórfico
    def activate_device(self):
        selected_key = self.selected_device.get()
        device_obj = self.devices[selected_key]
        
        # Llamada polimórfica al método turn_on()
        action_message = device_obj.turn_on()
        
        self.result_label.config(text=action_message, foreground="black")

# Ejecución
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
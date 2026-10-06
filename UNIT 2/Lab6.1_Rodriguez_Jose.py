from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod
import datetime

# ================================
# LÓGICA DE NEGOCIO (POLIMORFISMO)
# ================================

class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("💡 Living Room Smart Light")
    
    def turn_on(self):
        return f"{self.name}: Set the brightness to 100%"
        
    def turn_off(self):
        return f"{self.name}: Light turned off"

class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("🔊 Alexa Speaker")
    
    def turn_on(self):
        return f"{self.name}: Play The Rose music at volume 60%"
        
    def turn_off(self):
        return f"{self.name}: Stopped playback and sleeping"

class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("❄️ Hisense Inverter")
     
    def turn_on(self):
        return f"{self.name}: Set the temperature to 72 degrees Fahrenheit"
        
    def turn_off(self):
        return f"{self.name}: AC powered off"

# Nuevo dispositivo para probar escalabilidad
class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("📺 Samsung Smart TV")
        
    def turn_on(self):
        return f"{self.name}: Turning on and opening Netflix"
        
    def turn_off(self):
        return f"{self.name}: Screen turned off"


# ================================
# INTERFAZ GRÁFICA (GUI)
# ================================

class SmartHomeApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab 6.1 Smart Home Controller Upgrade")
        self.geometry("550x450") 
        self.resizable(True, True) 
        
        self.devices = {
            "💡 Light": SmartLight(),
            "🔊 Speaker": SmartSpeaker(),
            "❄️ AC": SmartAC(),
            "📺 TV": SmartTV()
        }
        
        self.build_ui()
          
    def build_ui(self):
        # 1. Header (Título)
        title_label = ttk.Label(
            self, text="Smart Home Controller", 
            font=("Arial", 16, "bold"),
            foreground="blue"
        )
        title_label.pack(pady=(15, 10))
        
        # 2. Contenedor de dispositivos
        group_box = ttk.LabelFrame(
            self,
            text="Select device",
            padding=(20, 5) 
        )
        group_box.pack(pady=10, padx=20, fill="x")
        
        first_key = list(self.devices.keys())[0]
        self.selected_device = StringVar(value=first_key) 
        
        for device_name in self.devices.keys():
            rb = ttk.Radiobutton(
                group_box, 
                text=device_name, 
                value=device_name, 
                variable=self.selected_device
            )
            rb.pack(anchor="w", pady=2)
            
        # 3. Botones de acción (Turn On / Turn Off)
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        
        on_btn = ttk.Button(
            btn_frame, 
            text="Turn On", 
            command=self.activate_device_on
        )
        on_btn.grid(row=0, column=0, padx=10)
        
        off_btn = ttk.Button(
            btn_frame, 
            text="Turn Off", 
            command=self.activate_device_off
        )
        off_btn.grid(row=0, column=1, padx=10)

        # 4. Activity Log (Listbox + Scrollbar)
        log_frame = ttk.LabelFrame(self, text="Activity Log", padding=(10, 10))
        log_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(log_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.activity_log = Listbox(
            log_frame, 
            yscrollcommand=self.scrollbar.set,
            font=("Arial", 10),
            height=8
        )
        self.activity_log.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.activity_log.yview)

    # Métodos de comportamiento polimórfico
    def activate_device_on(self):
        selected_key = self.selected_device.get()
        device_obj = self.devices[selected_key]
        action_message = device_obj.turn_on()
        self.log_action(action_message)
        
    def activate_device_off(self):
        selected_key = self.selected_device.get()
        device_obj = self.devices[selected_key]
        action_message = device_obj.turn_off()
        self.log_action(action_message)

    def log_action(self, message):
        # Agrega la hora actual al log
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        
        self.activity_log.insert(END, log_entry)
        self.activity_log.yview(END)

# Ejecución
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
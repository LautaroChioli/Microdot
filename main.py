def connect_to(ssid, passwd):
    #Conectar el micro a la red WIFI
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            pass
    return sta_if.ifconfig()[0]
        
from microdot import Microdot, send_file

# Creo una instancia de Microdot
app = Microdot()

@app.route("/")
def index(request):
    return send_file("index.html")


@app.route("/assets/<dir>/<file>")
def assets(request, dir, file):
    return send_file("/assets/" + dir + "/" + file)

@app.route("/data/update")
def data_update(request):
    # ADC para sensores analogicos
    from machine import ADC
    import machine, onewire, ds18x20, time
    # Instancia para el ds18
    ds_pin = machine.Pin(21)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    roms = ds_sensor.scan()
    if roms:
        rom = roms[0]
        ds_sensor.convert_temp()
        time.sleep_ms(750)
        cpu_temp = ds_sensor.read_temp(rom)
        print("CPU Temperature:", cpu_temp)
        return {"cpu_temp": cpu_temp}
    else:
        print(" noooooooooooooo")
        return {"cpu_temp": None}

if __name__ == "__main__":
    
    try:
        ip = connect_to("Red Alumnos", "")
        print("Microdot corriendo en IP/Puerto: " + ip + ":5000")
        # Inicio la aplicacion
        app.run()
    
    except KeyboardInterrupt:
        # Control + c para terminar programa :)
        print("Aplicacion terminada")

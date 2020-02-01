from infi.systray import SysTrayIcon
import yeelight as y

def toggle(systray):
    var = y.discover_bulbs()

    if len(var) < 1:
        var = "192.168.1.3"
    else:
        var = var[0]["ip"]

    bulb = y.Bulb(var)
    bulb.toggle()


menu = (("Toggle", None, toggle),)
systray = SysTrayIcon("yeelightico.ico", "Yeelight", menu)
systray.start()

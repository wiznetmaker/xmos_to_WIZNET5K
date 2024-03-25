from machine import Pin


class XmosStatusCmdAction_Pico:
    def __init__(self, led_pin=None):

        self.xmos_status = False
        self.xmos_led = Pin(xmos_led_pin, Pin.OUT) if xmos_led_pin is not None else None      
    
    def on_xmos_cyberon(self):
        if not self.xmos_status and self.xmos_led:
            print("Xmos Device turned on.")
            self.xmos_led.high()  # Send HIGH signal to turn on.
            self.xmos_status = True

    def off_xmos_cyberon(self):
        if self.xmos_status and self.xmos_led:
            print("Xmos Device turned off.")
            self.xmos_led.low()  # Send LOW signal to turn off.
            self.xmos_status = False    

class XmosTVCmdAction_Pico:
    def __init__(self, tv_pin=None, 
                 max_channel=10, min_channel=1, max_volume=20, min_volume=0):
        
        self.tv_status = False
        
        self.current_channel = 1  # Initialize TV channel to 1.
        self.max_channel = max_channel
        self.min_channel = min_channel

        self.current_volume = 0  # Initialize volume to 0
        self.max_volume = max_volume
        self.min_volume = min_volume
        
        self.tv_switch = Pin(tv_pin, Pin.OUT) if tv_pin is not None else None
        
        if self.xmos_led: self.xmos_led.low()
        if self.tv_switch: self.tv_switch.low()


    def switch_on_tv(self):
        if not self.tv_status and self.tv_switch:
            print("TV turned on.")
            self.tv_switch.high()  # Send HIGH signal to turn on.
            self.tv_status = True        

    def switch_off_tv(self):
        if self.tv_status and self.tv_switch:
            print("TV turned off.")
            self.tv_switch.low()  # Send LOW signal to turn off.
            self.tv_status = False

    def channel_up(self):
        if self.tv_status:
            self.current_channel += 1
            if self.current_channel > self.max_channel:
                self.current_channel = self.min_channel  # Wrap around.
            print(f"Channel changed to {self.current_channel}.")

    def channel_down(self):
        if self.tv_status:
            self.current_channel -= 1
            if self.current_channel < self.min_channel:
                self.current_channel = self.max_channel  # Wrap around.
            print(f"Channel changed to {self.current_channel}.")

    def volume_up(self):
        if self.tv_status and self.current_volume < self.max_volume:
            self.current_volume += 1
            print(f"Volume increased to {self.current_volume}.")

    def volume_down(self):
        if self.tv_status and self.current_volume > self.min_volume:
            self.current_volume -= 1
            print(f"Volume decreased to {self.current_volume}.")
            

from machine import Pin, ADC, PWM
import machine
import time
import math
import neopixel


num_LEDs = 5
Pin = macnum_LEDs = 5
pin_neopixel = machine.Pin(22, machine.Pin.OUT)
strip = neopixel.NeoPixel(pin_neopixel, num_LEDs)
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_counter = 0
buzzer = machine.Pin(18, machine.Pin.OUT)
buzza = PWM(buzzer)
buzza.duty_u16(0)
current_time = time.ticks_ms()
selectMode = 0
confirmMode = 0


def modeOne():
 while True:
         sound_detector()
         if decibels >= 75:
            strip[0] = (255, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 0)
            strip.write()

def modeTwo():
 while True:
        sound_detector()
        if decibels >= 80:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 255, 0)
            strip[2] = (0, 0, 0)
            strip.write()
def modeThree():
 while True:
        sound_detector()
        if decibels >= 85:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 255)
            strip.write()

def buzza_process():
            buzza.freq(1000)
            buzza.duty_u16(32000)
            buzzer_end_time = time.ticks_add(current_time, 2000)
            buzza.duty_u16(0)

def sound_detector():
        # If the button is NOT pressed, run the microphone logic
        # 1. Capture the amplitude of the audio wave
        amplitude = sample_peak_to_peak(50)

        # 2. Prevent mathematical domain errors if amplitude is zero or below baseline
        if amplitude < ADC_BASELINE:
            amplitude = ADC_BASELINE

        # 3. Logarithmic formula: dB = Baseline_dB + 20 * log10(Current_Amplitude / Baseline_Amplitude)
        decibels = DB_BASELINE + (20 * math.log10(amplitude / ADC_BASELINE))


if button1.value(1):
    button_counter = button_counter + 1

# Initialize ADC on GP26 (ADC 0)
adc = machine.ADC(26)

# Calibration values (Adjust these based on your room noise)
# Cheap microphone modules lack factory calibration, so we establish a baseline.
DB_BASELINE = 40.0   # Decibel estimation for a dead-silent room
ADC_BASELINE = 10.0  # Minimum raw amplitude variation in a dead-silent room


def sample_peak_to_peak(duration_ms=50):
    """
    Samples the microphone rapidly for a fixed window to find the max wave amplitude.
    """
    max_val = 0
    min_val = 65535

    start_time = time.ticks_ms()
    # Read as fast as possible for the duration window (default 50ms)
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        sample = adc.read_u16()
        if sample > max_val:
            max_val = sample
        if sample < min_val:
            min_val = sample

    # Calculate peak-to-peak amplitude difference
    peak_to_peak = max_val - min_val
    return peak_to_peak


print("Calibrating/Starting Decibel Meter...")
time.sleep(1)

# SINGLE MAIN LOOP FOR BOTH FEATURES
while True:
    if button1.value(1):
       selectMode = selectMode + 1
    if selectMode > 3:
           selectMode = 1
    if button2.value(1):
       confirmMode = selectMode
       
    if selectMode == 1:
      strip[0] = (255, 0, 0)
      strip[1] = (0, 0, 0)
      strip[2] = (0, 0, 0)
      strip.write()
    elif selectMode == 2:
      strip[0] = (0, 0, 0)
      strip[1] = (0, 255, 0)
      strip[2] = (0, 0, 0)
      strip.write()    
    elif selectMode == 3:
      strip[0] = (0, 0, 0)
      strip[1] = (0, 0, 0)
      strip[2] = (0, 0, 255)
      strip.write()    
    elif confirmMode == 1:
      modeOne()
    elif confirmMode ==2:
      modeTwo()
    elif confirmMode == 3:
      modeThree()
    else:

        # Print the values so Thonny's Plotter can see them
    print(f"Raw Amplitude: {amplitude} | Estimated dB: {decibels:.1f}")
import RPi.GPIO as GPIO
import time

class RotaryEncoder:
    def __init__(self, pinA, pinB, name, callback):
        self.pinA = pinA
        self.pinB = pinB
        self.name = name
        self.callback = callback
        self.last_state = 0
        self.state = 0
        self.last_event_time = 0
        self.debounce_time = 0.05  # 50ms debounce
        self.event_accumulator = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Watch both for better direction accuracy
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self._handle_turn)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self._handle_turn)

    def _handle_turn(self, channel):
        now = time.time()
        if now - self.last_event_time < self.debounce_time:
            return
        self.last_event_time = now

        a = GPIO.input(self.pinA)
        b = GPIO.input(self.pinB)

        encoded = (a << 1) | b
        transition = (self.state << 2) | encoded

        # Lookup table based on valid quadrature transitions
        transition_table = {
            0b0001: 1,
            0b0011: -1,
            0b0010: -1,
            0b0110: 1,
            0b0111: -1,
            0b0101: 1,
            0b1110: -1,
            0b1100: 1,
            0b1000: -1,
            0b1001: 1,
            0b1011: -1,
            0b1111: 1
        }

        direction = transition_table.get(transition, 0)
        self.state = encoded

        if direction != 0:
            if "knob" in self.name.lower():
                event = "knob_up" if direction == 1 else "knob_down"
            else:
                event = "dial_up" if direction == 1 else "dial_down"

            print(f"[{self.name.upper()}] Detected {'up' if direction == 1 else 'down'} turn")
            self.callback(event)
#Embedded file name: /Users/versonator/Jenkins/live/Projects/AppLive/Resources/MIDI Remote Scripts/_Framework/SysexValueControl.py
from _Framework.InputControlElement import InputControlElement, MIDI_SYSEX_TYPE

class SysexValueControl(InputControlElement):
    """
    Sysex value control receives a sysex message, identified by a
    prefix.  The value can be requested with a value_enquiry MIDI
    message to the controller.
    """

    def __init__(self, message_prefix = None, value_enquiry = None, *a, **k):
        super(SysexValueControl, self).__init__(msg_type=MIDI_SYSEX_TYPE, sysex_identifier=message_prefix, *a, **k)
        self._value_enquiry = value_enquiry

    def send_value(self, value_bytes):
        self.send_midi(self.message_sysex_identifier() + value_bytes + (247,))

    def enquire_value(self):
        raise self._value_enquiry != None or AssertionError
        self.send_midi(self._value_enquiry)

    def reset(self):
        pass
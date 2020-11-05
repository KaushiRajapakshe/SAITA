import win32com.client
from SAITA.IT16178700.data.variables import say_speed, say_voice


class SayText(object):
    enable = True
    speaker = None
    __seyText = None

    @staticmethod
    def get_say_text():
        if SayText.__seyText is None:
            SayText()

        return SayText.__seyText

    def __init__(self):
        if SayText.__seyText is None:
            self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
            self.speaker.Voice = self.speaker.GetVoices().Item(say_voice)
            self.speaker.Rate = say_speed
        SayText.__seyText = self

    def say(self, txt):
        if self.enable == 1:
            self.speaker.Speak(txt)

    def set_enable(self, val=True):
        self.enable = val

    def get_enable(self):
        return self.enable

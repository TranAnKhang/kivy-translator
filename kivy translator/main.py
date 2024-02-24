from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
# from languages import *

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',}

keys = [keys for keys in LANGUAGES.keys()]
values = [values for values in LANGUAGES.values()]



class Home(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initUI()
        self.connects()

    def initUI(self):
        row = BoxLayout()
        collum_1 = BoxLayout(orientation = "vertical")
        collum_2 = BoxLayout(orientation = "vertical")
        self.label = Label(text = "Translater 2.0")
        self.dropdown_1 = DropDown()
        self.dropdown_2 = DropDown()
        self.translate_bt = Button(text="translate now", font_size = 10, size = (50,100))
        self.clear_bt = Button(text = "clear", font_size = 10, size = (50,100))
        self.textinput_1 = TextInput()
        self.textinput_2 = TextInput()
        self.reverse_bt = Button(text = "reverse", font_size = 10, size = (50,100))
        self.dropdown_bt = Button(text = "drop down")
        collum_1.add_widget(self.label)
        collum_1.add_widget(self.dropdown_1)
        collum_1.add_widget(self.dropdown_2)
        collum_1.add_widget(self.translate_bt)
        collum_1.add_widget(self.clear_bt)
        collum_1.add_widget(self.dropdown_bt)
        collum_2.add_widget(self.textinput_1)
        collum_2.add_widget(self.reverse_bt)
        collum_2.add_widget(self.textinput_2)
        row.add_widget(collum_1)
        row.add_widget(collum_2)
        self.add_widget(row)

    def connects(self):
        self.dropdown_bt.bind(on_release = lambda btn: self.dropdown_1.open(self.add_languages(values)))
        self.dropdown_1.bind(on_select=lambda x: setattr(self.dropdown_bt,"text",x))

    def add_languages(self, languages):
        i = 0
        for l in languages:
            l = Button(text = values[i])
            self.dropdown_1.add_widget(l)
            i += 1






class Myapp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Home(name = "home"))
        return manager

my_app = Myapp()
my_app.run()
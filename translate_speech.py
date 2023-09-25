import speech_recognition as spr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

import csv

from grammar_correction import correct_sentence

def translate_speech(english_speech):

    d = {}
    with open('trial.csv', mode='r', encoding="utf8") as f:
        data = csv.reader(f)
        d = {rows[0]:rows[1:] for rows in data}
    recog1 = spr.Recognizer()


    from_lang = 'en'
    to_lang = 'hi'
    try:

        corrected_input = correct_sentence(english_speech)

        text_to_translate = GoogleTranslator(source='en', target='hi').translate(corrected_input)
        text = text_to_translate
        text1 = text.split()
        test = []
        for i in text1:
            test.append(i)
        key_list = list(d.keys())
        val_list = list(d.values())
        list2 = []
        for n in test:
            f = 0
            k = 0
            for i in val_list:
                for j in i:
                    if(j == n):
                        position = k
                        f = 1
                k += 1
            if f == 0:
                list2.append(n)
            else:
                list2.append(key_list[position])
        pai = ' '.join(list2)
        speak = gTTS(text=pai, lang=to_lang, slow=False)
        speak.save("/home/chaithanyakumar/mysite/static/captured_voicenew.mp3")
        os.system("start captured_voice.mp3")
        return pai
    except spr.UnknownValueError:
        return "Unable to Understand the Input"
    except spr.RequestError as e:
        return "Unable to provide Required Output".format(e)

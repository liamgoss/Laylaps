from AppKit import NSSpeechSynthesizer
import pyttsx3
def getvoicenames():
    """I am returning the names of the voices available on Mac OS X."""
    voices = NSSpeechSynthesizer.availableVoices()
    voicenames = []
    for voice in voices:
        voiceattr = NSSpeechSynthesizer.attributesForVoice_(voice)
        voicename = voiceattr['VoiceName']
        if voicename not in voicenames:
            voicenames.append(voicename)
    return voicenames





availableVoices = [ 
    "Alex", 
    "Alice",
    "Alva",
    "Amelie",
    "Anna",
    "Carmit",
    "Damayanti",
    "Daniel",
    "Diego",
    "Ellen",
    "Fiona",
    "Fred",
    "Ioana",
    "Joana",
    "Jorge",
    "Juan",
    "Kanya",
    "Karen",
    "Kyoko",
    "Laura",
    "Lekha",
    "Luca",
    "Luciana",
    "Maged",
    "Mariska",
    "Mei-Jia",
    "Melina",
    "Milena",
    "Moira",
    "Monica",
    "Nora",
    "Paulina",
    "Rishi",
    "Samantha",
    "Sara",
    "Satu",
    "Sin-ji",
    "Tessa",
    "Thomas",
    "Ting-Ting",
    "Veena",
    "Victoria",
    "Xander",
    "Yelda",
    "Yuna",
    "Yuri",
    "Zosia",
    "Zuzana",
]
def testAllVoices():
    engine=pyttsx3.init('nsss')
    for voice in availableVoices:
        if voice == 'Fred':
            engine.setProperty('voice', f'com.apple.speech.synthesis.voice.{voice}')    
        else:
            engine.setProperty('voice', f'com.apple.speech.synthesis.voice.{voice.lower()}')
        print(f"My name is {voice}")
        engine.say(f"My name is {voice}")
        engine.runAndWait()

if __name__ == '__main__':
    testAllVoices()






'''
<Voice id=com.apple.speech.synthesis.voice.Alex
          name=Alex
          languages=['en_US']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.alice
          name=Alice
          languages=['it_IT']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.alva
          name=Alva
          languages=['sv_SE']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.amelie
          name=Amelie
          languages=['fr_CA']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.anna
          name=Anna
          languages=['de_DE']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.carmit
          name=Carmit
          languages=['he_IL']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.damayanti
          name=Damayanti
          languages=['id_ID']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.daniel
          name=Daniel
          languages=['en_GB']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.diego
          name=Diego
          languages=['es_AR']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.ellen
          name=Ellen
          languages=['nl_BE']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.fiona
          name=Fiona
          languages=['en-scotland']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.Fred
          name=Fred
          languages=['en_US']
          gender=VoiceGenderMale
          age=30>
<Voice id=com.apple.speech.synthesis.voice.ioana
          name=Ioana
          languages=['ro_RO']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.joana
          name=Joana
          languages=['pt_PT']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.jorge
          name=Jorge
          languages=['es_ES']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.juan
          name=Juan
          languages=['es_MX']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.kanya
          name=Kanya
          languages=['th_TH']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.karen
          name=Karen
          languages=['en_AU']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.kyoko
          name=Kyoko
          languages=['ja_JP']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.laura
          name=Laura
          languages=['sk_SK']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.lekha
          name=Lekha
          languages=['hi_IN']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.luca
          name=Luca
          languages=['it_IT']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.luciana
          name=Luciana
          languages=['pt_BR']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.maged
          name=Maged
          languages=['ar_SA']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.mariska
          name=Mariska
          languages=['hu_HU']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.meijia
          name=Mei-Jia
          languages=['zh_TW']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.melina
          name=Melina
          languages=['el_GR']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.milena
          name=Milena
          languages=['ru_RU']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.moira
          name=Moira
          languages=['en_IE']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.monica
          name=Monica
          languages=['es_ES']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.nora
          name=Nora
          languages=['nb_NO']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.paulina
          name=Paulina
          languages=['es_MX']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.rishi
          name=Rishi
          languages=['en_IN']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.samantha
          name=Samantha
          languages=['en_US']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.sara
          name=Sara
          languages=['da_DK']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.satu
          name=Satu
          languages=['fi_FI']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.sinji
          name=Sin-ji
          languages=['zh_HK']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.tessa
          name=Tessa
          languages=['en_ZA']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.thomas
          name=Thomas
          languages=['fr_FR']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.tingting
          name=Ting-Ting
          languages=['zh_CN']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.veena
          name=Veena
          languages=['en_IN']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.Victoria
          name=Victoria
          languages=['en_US']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.xander
          name=Xander
          languages=['nl_NL']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.yelda
          name=Yelda
          languages=['tr_TR']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.yuna
          name=Yuna
          languages=['ko_KR']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.yuri
          name=Yuri
          languages=['ru_RU']
          gender=VoiceGenderMale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.zosia
          name=Zosia
          languages=['pl_PL']
          gender=VoiceGenderFemale
          age=35>
<Voice id=com.apple.speech.synthesis.voice.zuzana
          name=Zuzana
          languages=['cs_CZ']
          gender=VoiceGenderFemale
          age=35>

'''
"""
Text Translator
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Create instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate text from English to French
    """
    if english_text is None:
        return None    
    else:
        french_translation = language_translator.translate(text=english_text,model_id='en-fr')
        french_res = french_translation.get_result()
        french_text = french_res['translations'][0]['translation']
        return french_text


def french_to_english(french_text):
    """
    Translate text from French to English
    """
    if french_text is None:
        return None
    else:
        english_translation = language_translator.translate(text=french_text,model_id='fr-en')
        english_res = english_translation.get_result()
        english_text = english_res['translations'][0]['translation']
        return english_text

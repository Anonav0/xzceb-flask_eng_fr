import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey= os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-07-14',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Function to convert incoming english text to french text.
    
    """
    if english_text is None:
        return None
    
    result = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = result['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Function to convert incoming French text to English text.
    
    """
    if french_text is None:
        return None
    
    result = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text = result['translations'][0]['translation']
    return english_text

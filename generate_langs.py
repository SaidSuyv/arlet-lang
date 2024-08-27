import os
import json

langs = ['es','en']
prefixes = ['PE','ES','US']

for lang in langs:
    
    # Opens main langs
    prefix = open('./common/{0}.json'.format(lang),'r',encoding='utf-8')

    # Reads content
    text = prefix.read()

    # Translates to JSON
    j_obj = json.loads(text)
    print(j_obj)

    for pref in prefixes:
        # Update lang property
        j_obj['lang'] = "{0}-{1}".format(lang,pref)
        
        # Dumps it to text
        text = json.dumps(j_obj)

        # Opens new prefix language
        file = open("./common/{0}-{1}.json".format(lang,pref),'w',encoding='utf-8')
        file.write(text)
        file.close()

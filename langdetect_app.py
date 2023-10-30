from langdetect import detect_langs, detect

text = "Dies ist ein Beispieltext in Deutsch."
detected_languages = detect_langs(text)

for language in detected_languages:
    print(f"Language: {language.lang}, Confidence: {language.prob}")

text = "Perang memusnahkan harta benda dan menyebabkan banyak kematian jiwa seperti warga emas, kanak-kanak, dan wanita yag tidak berdosa"
detected_languages = detect_langs(text)
for language in detected_languages:
    print(f"Language: {language.lang}, Confidence: {language.prob}")

text = "Ini adalah contoh teks dalam Bahasa Malaysia."
detected_language = detect(text)
print(f"The detected language is: {detected_language}")

text = "hari esok hari minggu, jadi, saya nak habiskan masa membeli belah di sebuah pasaraya terkemuka di kuala lumpur."
detected_languages = detect_langs(text)
for language in detected_languages:
    print(f"Language: {language.lang}, Confidence: {language.prob}")

e = 1

# make content groups from back cover text (takzir)
# example book - https://www.e-vrit.co.il/Product/18533/האריות_מסיציליה

text = '''
סאגה סוחפת של סודות אפלים, סיפורי אהבה, בגידות ומעשי נקם אכזריים
 
רומן היסטורי מרתק המבוסס על חייהם האמיתיים של ג'וזפינה פלוריו וגיסה המאוהב בה בסתר איגנציו, וינצ'נצו השאפתן והיצירתי, ג'וליה פורטלופי הסוערת והנבונה ושאר בני משפחת פלוריו, המלכים הלא־מוכתרים של סיציליה, אנשים ערמומיים ושאפתנים, הנחושים להיות עשירים ורבי־עוצמה יותר מכל אדם אחר.
 
לאחר רעידת אדמה שהחריבה את ביתה מגיעה משפחת פלוריו לסיציליה בחוסר כול. כנגד כל הסיכויים, ולמרות המלחמות הנפוליאוניות והמגיפות המשחרות לפתח, הם מצליחים לפתוח דף חדש.
 
כאשר איזבלה האריסטוקרטית דוחה את וינצ'נצו שמחזר אחריה בלהט, הוא נשבע לנקום את חילול כבודו ולהיהפך לאיש העשיר ביותר באיטליה. כשהוא מעלה על המזבח גם את האהבה וגם את בני משפחתו, וינצ'נצו שואף לרכוש בכסף את אשר לא זכה לו מלידה. גם נשות המשפחה נלחמות על מעמדן ומנסות להיחלץ מהכבלים שמרתקים אותן למקומן: ג'וליה הפיקחית, שלמרות היותה רק פילגש מנהלת את האימפריה מאחורי הקלעים ביד רמה, או אנג'לינה, שנולדה ממזרה, אך מתווה לעצמה עתיד שונה לחלוטין מזה שייעד לה אביה.
'''

book_name = "האריות מסציליה"
# author_name = ""
# publisher = ""
category = ["פרוזה מקור", "מדינות וערים"]
# print()
print(book_name)

proza_makor = [
    [{"פרוזה מקור": []}], [{"ספרים מצחיקים": ["משעשע", "מבדר", "מצחיק"]}],
    [{"מבוסס על סיפור אמיתי": ["המבוסס על חייהם", "סיפורה האמיתי"]}],
    [{"רומן היסטורי": ["הרומן ההיסטורי"]}],
    [{'להטב״ק': []}],
    [{"אימוץ": ["לאמץ תינוק", "הורים מאמצים",]}],
]

romatica=[
    [{"רומן רומנטי": []}], [{"רומנטיקת נקמה": []}],
    [{"יוונים רומנטיים": ["יוון", ]}],
]

places=[
    [{"מדינות וערים": []}], [{"איטליה": ["סיציליה",]}],
    [{"ניו יורק": ["מנהטן"]}],
]

biography=[
    [{"ביוגרפיה": []}], [{"ביוגרפיות": []}], [{"אוטוביוגרפיה": ["אוטוביוגרפי"]}],
]

all_groups = [proza_makor, romatica, places, biography]
all_groups_str=["פרוזה מקור", "רומן רומנטי", "מדינות וערים", "ביוגרפיה"]
# all_groups2=[]

# print(text)

# make list of words from text
texts = text.split()
# print(texts)

# make phrases because split()
texts_len = len(texts)
for word in range(texts_len-1):
    if texts[word] =="רומן" and texts[word+1]=="היסטורי":
     texts[word]=str(texts[word] + " " + texts[word+1])
    if texts[word] =="הרומן" and texts[word+1]=="ההיסטורי":
     texts[word]=str(texts[word] + " " + texts[word+1])
    if texts[word] == "סיפור" and texts[word + 1] == "אמיתי":
         texts[word] = str(texts[word] + " " + texts[word + 1])
    if texts[word] == "סיפורה" and texts[word + 1] == "האמיתי":
         texts[word] = str(texts[word] + " " + texts[word + 1])
     #texts[word+1]=""
    if texts[word] =="מבוסס" and texts[word+1]=="על" and texts[word+2]=="חייהם":
     texts[word]=str(texts[word] + " " + texts[word+1] + " " + texts[word+2])
    if texts[word] =="לאמץ" and texts[word+1]=="תינוק":
     texts[word]=str(texts[word] + " " + texts[word+1])
    if texts[word] =="רומן" and texts[word+1]=="רומנטי":
     texts[word]=str(texts[word] + " " + texts[word+1])
    if texts[word] == "ספרים" and texts[word + 1] == "מצחיקים":
     texts[word] = str(texts[word] + " " + texts[word + 1])

#print(texts)

# choose on what category to run from all_groups list (the smart way is to find keys..) ->
# then run over the category group (holder) and find words in keys values
print()
# len_all_category=len(category)
len_all_groups_str=len(all_groups_str)
for groupi in all_groups_str:
 for cat in category:
        #print(cat, groupi)
     if cat==groupi:
        print (groupi, all_groups_str.index(cat))
        tempr=all_groups_str.index(cat)
        holder = all_groups[tempr]
        # the actual code - finds the words
        len_holder = len(holder)
        for group in range(len_holder):
            for item in holder[group]:
                # print(item)
                for key, val in item.items():
                    # print(key, val)
                    for word in texts:
                        if key in word:
                            print(key, " - ", word)
                    for valey in val:
                        # print(valey)
                        for word in texts:
                            if valey in word:
                                print(word, " - ", key)






from junja2 import Template

gematria = [
    ["alef" , "U+05D0" , 1, "א‎"],
    ["bet" , "U+05D1" , 2, "ב‎"],
    ["guimel" , "U+05D2" , 3, "ג‎"],
    ["dalet" , "U+05D3" , 4, "ד‎"],
    ["he" , "U+05D4" , 5, "ה‎"],
    ["vav" , "U+05D5" , 6, "ו‎"],
    ["tzain" , "U+05D6" , 7, "ז‎"],
    ["jet" , "U+05D7" , 8, "ח‎"],
    ["tet" , "U+05D8" , 9, "ט‎"],
    ["yod" , "U+05D9" , 10, "י‎"],
    ["kaf" , "U+05DB" , 20, "כ"],
    ["lamed" , "U+05DC" , 30, "ל‎"],
    ["mem" , "U+05DE" , 40, "מ"],
    ["nun" , "U+05DF" , 50, "נ"],
    ["samej" , "U+05E1" , 60, "ס‎"],
    ["ayin" , "U+05E2" , 70, "ע‎"],
    ["pe" , "U+05E4" , 80, "פ"],
    ["tzadic" , "U+05E6" , 90, "צ"],
    ["kof" , "U+05E7" , 100, "ק‎"],
    ["resh" , "U+05E8" , 200, "ר‎"],
    ["shin" , "U+05E9" , 300, "ש‎"],
    ["tav" , "U+05EA" , 400, "ת‎"],
    ["kaf_sofit" , "U+05DA" , 500, "ך‎"],
    ["mem_sofit" , "U+05DD" , 600, "ם‎"],
    ["nun_sofit" , "U+05DF" , 700, "ן‎"],
    ["pe_sofit" , "U+05E3" , 800, "ף‎"],
    ["tzadi_sofit" , "U+05E5" , 900, "ץ‎"]
]

t = Template("Hola {{ propiedad }} ")
t.render(propiedad="SERGIOOOO")

t = Template("""

Hola {% for n in range(1,10) %} {{ n }}

""")
t.render(propiedad="SERGIOOOO")
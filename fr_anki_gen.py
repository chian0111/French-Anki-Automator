import genanki
from gtts import gTTS
import os

# 視覺設計保持不變 (維持妳喜歡的藝術館風格)
style = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,700&family=Raleway:wght@300;400&display=swap');
.card {
    font-family: 'Raleway', sans-serif;
    background: linear-gradient(135deg, rgba(244,241,234,0.9) 0%, rgba(244,241,234,1) 50%, rgba(244,241,234,0.9) 100%),
                linear-gradient(90deg, rgba(0,85,164,0.015) 0%, rgba(255,255,255,0) 33%, rgba(255,255,255,0) 66%, rgba(239,65,53,0.015) 100%);
    margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh;
}
.container {
    background: #ffffff; padding: 60px 40px; border-radius: 2px;
    box-shadow: 20px 20px 60px #d9d6cf, -20px -20px 60px #ffffff;
    border-left: 5px solid #354f52; width: 320px; position: relative; overflow: hidden;
}
.container::after {
    content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 3px;
    background: linear-gradient(90deg, #0055A4 0%, #0055A4 33%, #FFFFFF 33%, #FFFFFF 66%, #EF4135 66%, #EF4135 100%);
    opacity: 0.6;
}
.word { font-family: 'Playfair Display', serif; font-size: 52px; font-weight: 700; color: #354f52; margin-bottom: 10px; }
.translation { font-size: 20px; letter-spacing: 2px; text-transform: uppercase; color: #84a59d; font-weight: 300; }
.audio-icon { margin-top: 40px; font-size: 12px; color: #cad2c5; }
"""

my_model = genanki.Model(
    1607392319, 'French Modern Model v2',
    fields=[{'name': 'French'}, {'name': 'Chinese'}, {'name': 'Audio'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="card"><div class="container"><div class="word">{{French}}</div></div></div>',
        'afmt': '<div class="card"><div class="container"><div class="word">{{French}}</div><div class="translation">{{Chinese}}</div><div class="audio-icon">ÉCOUTER: {{Audio}}</div></div></div>',
    }],
    css=style
)

# --- 這裡就是妳可以自由修改單字的地方 ---
words = [
    {"fr": "La Vie en rose", "zh": "玫瑰色的人生"},
    {"fr": "Épanouissement", "zh": "自我實現/綻放"},
    {"fr": "Sagesse", "zh": "智慧"},
    {"fr": "Dégustation", "zh": "品嚐"},
    {"fr": "Esthétique", "zh": "美學"},
    {"fr": "Gratitude", "zh": "感激"},
    {"fr": "Inspiration", "zh": "靈感"},
    {"fr": "Sérénité", "zh": "寧靜"}
]
# ---------------------------------------

my_deck = genanki.Deck(2059400111, 'My French Collection')
media_files = []
for item in words:
    f = f"{item['fr'].replace(' ', '_')}.mp3" # 處理空格避免路徑出錯
    if not os.path.exists(f):
        gTTS(item['fr'], lang='fr').save(f)
    media_files.append(f)
    my_deck.add_note(genanki.Note(model=my_model, fields=[item['fr'], item['zh'], f"[sound:{f}]"]))

package = genanki.Package(my_deck)
package.media_files = media_files
package.write_to_file('my_french_vocab.apkg')
print(f"✅ 成功生成 {len(words)} 個單字！檔案：my_french_vocab.apkg")

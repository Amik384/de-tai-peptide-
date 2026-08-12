from flask import Flask, render_template_string, abort

app = Flask(__name__)


# Дополнительные материалы, переданные пользователем.
SIAMI_TEXT = {
    "title": "СИАМИПЕЙ",
    "subtitle": "Двойное пептидное питание + тройной пребиотический комплекс",
    "intro": "Формула, объединяющая два источника пищевых пептидов с тремя пребиотическими компонентами.",
    "components": [
        ("🧬", "Пептиды коллагена из костной ткани яка", "Пептидное направление",
         "Источник пептидов и аминокислот. В предоставленных материалах компонент связывается с пищевой поддержкой тканей и нормальной работой пищеварительной системы."),
        ("🌾", "Олигопептиды проса", "Пептидное направление",
         "Небольшие пептидные фрагменты из белка проса. В материалах DeTai компонент связывается с поддержкой слизистой ЖКТ, моторики, пищеварения и усвоения питательных веществ."),
        ("🍄", "Полисахариды тремеллы", "Пребиотическое направление",
         "Компонент пребиотической части формулы. В предоставленном тексте связывается с поддержкой кишечной микрофлоры, пищеварения и усвоения питательных веществ."),
        ("🌿", "Инулин", "Пребиотическое направление",
         "Природная растительная клетчатка и пребиотик. В тексте описывается как пищевой субстрат для определённых микроорганизмов кишечника."),
        ("🌱", "Раффиноза", "Пребиотическое направление",
         "Природный сложный углевод. Не является пробиотиком и не содержит живых бактерий; в предоставленном тексте описывается как пищевой субстрат для кишечной микрофлоры.")
    ]
}

FOUNDER_TEXT = {
    "name": "У Циньлин",
    "title": "Основатель De tai — «Человек мира»",
    "paragraphs": [
        "По предоставленному пользователем тексту, история De tai связана с её основателем — У Циньлином (Wu Qinling), которого материалы представляют как предпринимателя, исследователя и мецената.",
        "В тексте философия компании описывается через сочетание древней восточной мудрости и современных биотехнологий, а также через идею целостного подхода к человеку.",
        "В материалах также заявляются 12-ступенчатые технологии низкотемпературного ферментативного гидролиза, низкомолекулярные пептидные соединения, международное сотрудничество и социальные проекты."
    ],
    "quote": "«Здоровье человека — это не просто отсутствие болезней, это гармония каждой клетки нашего тела с окружающим миром...»"
}

PRODUCTS = [
    {
        "id": "yak",
        "category": "Пептиды",
        "title": "Пептиды яка",
        "subtitle": "Yak Peptide Solid Drink",
        "weight": "160 г · 8 г × 20 пакетов",
        "ingredients": [
            "Коллагеновые пептиды из костей яка",
            "Пептиды костного мозга яка",
            "Альбуминовые пептиды",
            "Олигопептиды женьшеня",
            "Пептиды морского огурца",
            "Культура снежного лотоса",
        ],
        "properties": [
            "Поддержка костной ткани и суставов",
            "Поддержка иммунной функции",
            "Поддержка кроветворения",
            "Поддержка водно-солевого баланса",
            "Поддержка энергетического обмена",
        ],
        "note": "В презентации указано, что продукт не является лекарственным средством и не заменяет медикаменты."
    },
    {
        "id": "double",
        "category": "Пептиды",
        "title": "Двойное пептидное питание",
        "subtitle": "Double Compound Small Molecule Peptide Special Diet",
        "weight": "240 г · 8 г × 30 пакетов",
        "ingredients": [
            "Пептиды коллагена из якостной кости",
            "Олигопептиды проса",
            "Полисахариды тремеллы",
            "Инулин",
            "Раффиноза",
        ],
        "properties": [
            "Поддержка моторики ЖКТ",
            "Поддержка слизистой желудка",
            "Поддержка кишечной микрофлоры",
            "Пребиотическая поддержка",
            "Поддержка усвоения питательных веществ",
        ],
        "note": "Сведения на этой странице переданы по материалам загруженной презентации."
    },
    {
        "id": "walnut",
        "category": "Мозг",
        "title": "Пептиды грецкого ореха",
        "subtitle": "Walnut Small Molecular Peptide Special Diet",
        "weight": "100 г · 5 г × 20 пакетов",
        "ingredients": [
            "Олигопептиды из грецкого ореха",
            "Пептиды мозгового белка",
            "Фосфатидилсерин (PS)",
            "L-α-глицерофосфорилхолин",
            "Таурин",
            "Экстракт мяты колосистой",
            "Экстракт гуараны",
            "Дрожжевой порошок",
        ],
        "properties": [
            "Поддержка памяти и внимания",
            "Поддержка когнитивных функций",
            "Поддержка умственной работоспособности",
            "Поддержка нервной ткани",
        ],
        "note": "Приведённые свойства являются формулировками из презентации, а не независимой медицинской оценкой."
    },
    {
        "id": "collagen",
        "category": "Коллаген",
        "title": "Коллагеновые пептиды",
        "subtitle": "Collagen Peptide Solid Beverages",
        "weight": "180 г · 6 г × 30 пакетов",
        "ingredients": [
            "Пептиды рыбного коллагена",
            "Пептиды ямса",
            "7 видов фруктовых порошков",
            "Витамин C",
            "Инулин",
        ],
        "properties": [
            "Питание кожи",
            "Поддержка увлажнённости и упругости кожи",
            "Источник коллагеновых пептидов",
            "Дополнительная клетчатка и витамин C",
        ],
        "note": "В презентации продукт позиционируется как пищевой продукт, а не лекарственное средство."
    },
    {
        "id": "gold",
        "category": "Косметология",
        "title": "Золотое сияние",
        "subtitle": "Пептидный антивозрастной уход",
        "weight": "Премиальный набор ухода",
        "ingredients": [
            "Пептид морского улиточного яда",
            "Пептид овса",
            "Пептид змеиного яда",
            "Ацетилгексапептид-8",
            "Ацетилтетрапептид-9",
            "Трипептид-1",
            "Гексапептид-9",
            "Олигопептиды-1, 2, 5",
            "Пальмитоилтрипептид-1",
            "Пальмитоилпентапептид-4",
            "Пальмитоилтрипептид-5",
            "Пальмитоилтетрапептид-7",
        ],
        "properties": [
            "Уход за кожей",
            "Поддержка упругости и эластичности",
            "Антиоксидантный уход",
            "Увлажнение и восстановление кожного барьера",
        ],
        "note": "Список и описания пептидов перенесены из загруженной презентации."
    },
    {
        "id": "mask",
        "category": "Косметология",
        "title": "Pro-Xylane увлажняющая маска",
        "subtitle": "Pro-Xylane To Compact Moisturizing Mask",
        "weight": "150 г · 30 г × 5 масок",
        "ingredients": [
            "Медный пептид",
            "Pro-Xylane",
            "Гидролизованный коллаген",
            "Рекомбинантный коллаген человека типа III",
            "Гиалуронат натрия",
            "Экстракты ромашки и бессмертника",
        ],
        "properties": [
            "Увлажнение кожи",
            "Уход за кожным барьером",
            "Поддержка упругости",
            "Антиоксидантный уход",
        ],
        "note": "Процентные значения и эффекты приведены так, как они представлены в исходных слайдах."
    },
    {
        "id": "serum",
        "category": "Косметология",
        "title": "Антивозрастная сыворотка",
        "subtitle": "Anti-Wrinkle Serum",
        "weight": "Профессиональный SPA-уход",
        "ingredients": [
            "Ацетилтетрапептид-11",
            "Ацетилтетрапептид-9",
            "Декапептид-4",
            "Пептид морской улитки",
            "Масло семян лимнантеса",
            "Масло жожоба",
            "Экстракт морской водоросли",
        ],
        "properties": [
            "Антивозрастной уход",
            "Уход за плотностью и эластичностью кожи",
            "Увлажнение",
            "Поддержка внешнего вида кожи",
        ],
        "note": "Заявленные эффекты основаны на тексте презентации и не являются медицинской рекомендацией."
    },
    {
        "id": "spray",
        "category": "Косметология",
        "title": "Лифтинг-спрей для лица",
        "subtitle": "Anti Wrinkle Spray",
        "weight": "Спрей для ухода за кожей лица",
        "ingredients": [
            "Трипептид-1",
            "Пальмитоилтрипептид-1",
            "Пальмитоилтетрапептид-7",
            "Гексапептид-9",
            "Пальмитоилтрипептид-5",
            "Пальмитоилпентапептид-4",
        ],
        "properties": [
            "Интенсивное увлажнение",
            "Уход за упругостью кожи",
            "Антивозрастной уход",
            "Поддержка внешнего вида кожи",
        ],
        "note": "Информация основана на загруженных слайдах."
    },
    {
        "id": "gel",
        "category": "Уход",
        "title": "Relieve Pain Health Care Gel",
        "subtitle": "Гель с роликовым SPA-аппликатором",
        "weight": "80 г",
        "ingredients": [
            "6 видов традиционных китайских трав",
            "20 видов растительных экстрактов",
            "Всего заявлено 26 растительных экстрактов",
        ],
        "properties": [
            "Массаж акупунктурных точек",
            "Роликовый аппликатор с 6 шариками",
            "Т-образная насадка для гуаша-массажа",
            "Силиконовые выступы для мягкого массажа",
        ],
        "note": "Презентация отдельно указывает, что полный состав следует смотреть в формуле продукта."
    },
]

CATEGORIES = ["Все", "Пептиды", "Мозг", "Коллаген", "Косметология", "Уход"]

TEMPLATE = r"""
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Peptide Catalog</title>
<style>
:root{
 --bg:#080b12; --panel:#111725; --panel2:#171e2d; --text:#f4f7fb;
 --muted:#9ba8bb; --accent:#75e6c2; --accent2:#7aa7ff; --line:#273247;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(circle at 20% 0%,#14243b 0,#080b12 42%);color:var(--text);font-family:Inter,Segoe UI,Arial,sans-serif}
a{text-decoration:none;color:inherit}
.container{max-width:1180px;margin:auto;padding:0 22px}
header{position:sticky;top:0;z-index:10;background:rgba(8,11,18,.86);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}
.nav{height:70px;display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-weight:900;letter-spacing:.8px}.logo span{color:var(--accent)}
.navlinks{display:flex;gap:18px;color:var(--muted);font-size:14px}.navlinks a:hover{color:white}
.hero{padding:76px 0 54px}
.badge{display:inline-block;padding:8px 12px;border:1px solid #31506a;border-radius:999px;color:var(--accent);font-size:12px;text-transform:uppercase;letter-spacing:1px}
h1{font-size:clamp(38px,6vw,72px);line-height:.98;margin:18px 0 20px;max-width:900px}
.hero p{color:var(--muted);font-size:18px;line-height:1.65;max-width:800px}
.notice{margin-top:25px;padding:15px 17px;border:1px solid #51472c;background:#17160f;border-radius:14px;color:#d9d0ae;font-size:13px;line-height:1.55}
.controls{display:flex;gap:10px;flex-wrap:wrap;margin:25px 0 32px}
.filter{cursor:pointer;background:var(--panel);color:var(--muted);border:1px solid var(--line);padding:11px 15px;border-radius:12px}
.filter.active,.filter:hover{color:#08110f;background:var(--accent);border-color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:17px;padding-bottom:65px}
.card{background:linear-gradient(145deg,var(--panel),#0d121c);border:1px solid var(--line);border-radius:20px;padding:22px;min-height:250px;display:flex;flex-direction:column;transition:.2s transform,.2s border-color}
.card:hover{transform:translateY(-4px);border-color:#46617d}
.card.hidden{display:none}
.tag{color:var(--accent2);font-size:12px;text-transform:uppercase;letter-spacing:.9px}
.card h2{font-size:22px;margin:9px 0 7px}.sub{color:var(--muted);font-size:13px;min-height:38px}
.weight{margin:18px 0;color:#d8e0ea;font-size:13px}
.card button{margin-top:auto;width:100%;padding:12px;border-radius:12px;border:0;background:#edf3fa;color:#101620;font-weight:800;cursor:pointer}
.card button:hover{background:var(--accent)}
.section{padding:65px 0;border-top:1px solid var(--line)}
.section h2{font-size:34px;margin:0 0 10px}.section>p{color:var(--muted)}
.product{background:var(--panel);border:1px solid var(--line);border-radius:22px;padding:26px;margin-top:22px;scroll-margin-top:90px}
.product h3{font-size:28px;margin:0 0 5px}.product .sub{margin-bottom:18px}
.columns{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.box{background:var(--panel2);border:1px solid var(--line);border-radius:16px;padding:18px}
.box h4{margin:0 0 12px;color:var(--accent)}
ul{margin:0;padding-left:20px;color:#cbd5e1;line-height:1.8}
.small{color:var(--muted);font-size:12px;line-height:1.55;margin-top:17px}
footer{padding:35px 0 55px;color:#738095;font-size:12px}
@media(max-width:850px){.grid{grid-template-columns:1fr 1fr}.columns{grid-template-columns:1fr}}
@media(max-width:560px){.navlinks{display:none}.grid{grid-template-columns:1fr}h1{font-size:44px}}
</style>
</head>
<body>
<header>
 <div class="container nav">
  <div class="logo">PEPTIDE<span>CATALOG</span></div>
  <div class="navlinks"><a href="#catalog">Каталог</a><a href="/siami">СИАМИПЕЙ</a><a href="/founder">Основатель</a><a href="#about">О проекте</a></div>
 </div>
</header>

<main>
<section class="hero">
 <div class="container">
  <span class="badge">Python · Flask · один файл</span>
  <h1>Каталог продуктов<br>с пептидами</h1>
  <p>Интерактивный сайт по материалам загруженной презентации: категории, состав, свойства и отдельные карточки продуктов.</p>
  <div class="notice">
   <b>Важно:</b> формулировки о свойствах ниже перенесены из презентации. Это не независимая медицинская проверка эффективности. В самой презентации для ряда продуктов указано, что они не являются лекарственными средствами.
  </div>
 </div>
</section>

<section id="catalog" class="section">
<div class="container">
 <h2>Каталог</h2>
 <p>Нажми на категорию или кнопку «Подробнее».</p>
 <div class="controls">
  {% for c in categories %}
   <button class="filter {% if c == 'Все' %}active{% endif %}" onclick="filterCards('{{ c }}', this)">{{ c }}</button>
  {% endfor %}
 </div>

 <div class="grid" id="cards">
 {% for p in products %}
 <article class="card" data-category="{{ p.category }}">
  <div class="tag">{{ p.category }}</div>
  <h2>{{ p.title }}</h2>
  <div class="sub">{{ p.subtitle }}</div>
  <div class="weight">{{ p.weight }}</div>
  <button onclick="document.getElementById('p-{{ p.id }}').scrollIntoView({behavior:'smooth'})">Подробнее →</button>
 </article>
 {% endfor %}
 </div>
</div>
</section>

<section id="details" class="section">
<div class="container">
 <h2>Состав и свойства</h2>
 <p>Нажми «Подробнее» в каталоге — страница прокрутится к нужному продукту.</p>
 {% for p in products %}
 <article class="product" id="p-{{ p.id }}">
  <div class="tag">{{ p.category }}</div>
  <h3>{{ p.title }}</h3>
  <div class="sub">{{ p.subtitle }} · {{ p.weight }}</div>
  <div class="columns">
   <div class="box">
    <h4>Компоненты</h4>
    <ul>{% for x in p.ingredients %}<li>{{ x }}</li>{% endfor %}</ul>
   </div>
   <div class="box">
    <h4>Заявленные свойства</h4>
    <ul>{% for x in p.properties %}<li>{{ x }}</li>{% endfor %}</ul>
   </div>
  </div>
  <div class="small">{{ p.note }}</div>
 </article>
 {% endfor %}
</div>
</section>

<section id="about" class="section">
<div class="container">
 <h2>О проекте</h2>
 <p>Сайт сделан полностью на Python с Flask: данные продуктов, маршруты и шаблон находятся внутри Python-файла. Отдельные HTML/CSS/JS-файлы не обязательны.</p>
</div>
</section>
</main>

<footer><div class="container">Материалы каталога основаны на загруженном PDF. © Peptide Catalog</div></footer>

<script>
function filterCards(category, btn){
 document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));
 btn.classList.add('active');
 document.querySelectorAll('.card').forEach(card=>{
   card.classList.toggle('hidden', category !== 'Все' && card.dataset.category !== category);
 });
}
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, products=PRODUCTS, categories=CATEGORIES)

@app.route("/product/<product_id>")
def product(product_id):
    p = next((x for x in PRODUCTS if x["id"] == product_id), None)
    if not p:
        abort(404)
    return render_template_string(
        TEMPLATE.replace(
            '<section id="catalog"',
            '<section id="catalog"'
        ),
        products=[p], categories=["Все"]
    )


@app.route("/siami")
def siami():
    return render_template_string("""
<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>СИАМИПЕЙ · DE TAI</title>
<style>
body{margin:0;background:#080c12;color:#f3f6fa;font-family:Arial,sans-serif}
.wrap{max-width:1000px;margin:auto;padding:35px 22px}
h1{font-size:52px;margin-bottom:8px}h2{margin-top:38px}
.sub{color:#75e5c0}.intro,.card{background:#111a26;border:1px solid #263246;border-radius:18px;padding:22px;margin:18px 0;line-height:1.65}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.icon{font-size:30px}.type{color:#8aaeff;font-size:12px;text-transform:uppercase}
a{color:#75e5c0}.flow{font-size:20px;line-height:2;text-align:center;background:#111a26;padding:24px;border-radius:18px}
@media(max-width:650px){.grid{grid-template-columns:1fr}h1{font-size:40px}}
</style></head><body><div class="wrap">
<a href="/">← Вернуться в каталог</a>
<h1>{{data.title}}</h1><div class="sub">{{data.subtitle}}</div>
<div class="intro">{{data.intro}}</div>
<h2>5 ключевых компонентов</h2>
<div class="grid">{% for c in data.components %}
<div class="card"><div class="icon">{{c[0]}}</div><div class="type">{{c[2]}}</div><h3>{{c[1]}}</h3><p>{{c[3]}}</p></div>
{% endfor %}</div>
<h2>Логика формулы</h2>
<div class="flow">ПИЩА → ПИЩЕВАРЕНИЕ → УСВОЕНИЕ → КИШЕЧНЫЙ БАРЬЕР → МИКРОБИОТА</div>
<div class="intro"><b>Важно:</b> описания свойств приведены по предоставленным материалам и не являются независимой медицинской оценкой.</div>
</div></body></html>
""", data=SIAMI_TEXT)

@app.route("/founder")
def founder():
    return render_template_string("""
<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Основатель De tai</title>
<style>
body{margin:0;background:#080c12;color:#f3f6fa;font-family:Arial,sans-serif}
.wrap{max-width:900px;margin:auto;padding:45px 22px}.box{background:#111a26;border:1px solid #263246;border-radius:20px;padding:28px;line-height:1.7}
h1{font-size:48px}h2{margin-top:32px}.green{color:#75e5c0}.quote{border-left:3px solid #75e5c0;padding:15px 20px;background:#0c131d;margin-top:25px}
a{color:#75e5c0}@media(max-width:600px){h1{font-size:38px}}
</style></head><body><div class="wrap">
<a href="/">← Вернуться в каталог</a>
<h1>{{data.title}}</h1><div class="box"><h2 class="green">{{data.name}}</h2>
{% for p in data.paragraphs %}<p>{{p}}</p>{% endfor %}
<div class="quote">{{data.quote}}<br><br><b>— У Циньлин, основатель компании De tai</b></div>
<p><small>Этот раздел составлен по предоставленному пользователем тексту; приведённые сведения не были независимо проверены.</small></p>
</div></div></body></html>
""", data=FOUNDER_TEXT)

if __name__ == "__main__":
    print("Открой в браузере: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

#!/usr/bin/env python3
"""Generate the static site in docs/. Run from the repo root: python3 build.py"""

from pathlib import Path

CATALOG = "https://bta-ind.methone.opalsinfo.net/bin/home#0"
FACEBOOK = "https://www.facebook.com/BibliotecaSanBenitoTA"
INSTAGRAM = "https://www.instagram.com/biblioteca_sanbenito_ta/"
GOFUNDME = "https://gofund.me/43acea0a"
WHATSAPP = "https://wa.me/50763726705"
MAPS_RECYCLE = "https://maps.app.goo.gl/LJGcCsMTsH7ngxLy9"

ICON_FB = """<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#044e7f" d="M13.4 20v-7.2h2.4l.4-2.8h-2.8V8.4c0-.8.2-1.4 1.4-1.4H16.4V4.5c-.2 0-1.1-.1-2.1-.1-2.1 0-3.5 1.3-3.5 3.6v2h-2.4v2.8h2.4V20h2.6z"/></svg>"""
ICON_IG = """<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="12" fill="currentColor"/><path fill="#044e7f" d="M12 8.2A3.8 3.8 0 1 0 12 15.8 3.8 3.8 0 0 0 12 8.2zm0 6.3a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5zm4-6.6a.9.9 0 1 1-1.8 0 .9.9 0 0 1 1.8 0zM12 6.4c-1.1 0-1.3 0-1.8.1-.5 0-.8.1-1.1.2-.3.2-.6.3-.8.6-.3.2-.4.5-.6.8-.1.3-.2.6-.2 1.1 0 .5-.1.7-.1 1.8s0 1.3.1 1.8c0 .5.1.8.2 1.1.2.3.3.6.6.8.2.3.5.4.8.6.3.1.6.2 1.1.2.5 0 .7.1 1.8.1s1.3 0 1.8-.1c.5 0 .8-.1 1.1-.2.3-.2.6-.3.8-.6.3-.2.4-.5.6-.8.1-.3.2-.6.2-1.1 0-.5.1-.7.1-1.8s0-1.3-.1-1.8c0-.5-.1-.8-.2-1.1-.2-.3-.3-.6-.6-.8-.2-.3-.5-.4-.8-.6-.3-.1-.6-.2-1.1-.2-.5 0-.7-.1-1.8-.1zm0 1.2c1.1 0 1.3 0 1.7.1.4 0 .7.1.8.2.2.1.4.2.5.4.1.1.3.3.4.5.1.2.2.4.2.8 0 .5.1.6.1 1.7s0 1.3-.1 1.7c0 .4-.1.7-.2.8-.1.2-.2.4-.4.5-.1.1-.3.3-.5.4-.2.1-.4.2-.8.2-.5 0-.6.1-1.7.1s-1.3 0-1.7-.1c-.4 0-.7-.1-.8-.2-.2-.1-.4-.2-.5-.4-.1-.1-.3-.3-.4-.5-.1-.2-.2-.4-.2-.8 0-.5-.1-.6-.1-1.7s0-1.3.1-1.7c0-.4.1-.7.2-.8.1-.2.2-.4.4-.5.1-.1.3-.3.5-.4.2-.1.4-.2.8-.2.4 0 .6-.1 1.7-.1z"/></svg>"""

HOURS_ES = """\
<ul>
<li>martes, 1 p.m. a 5 p.m.</li>
<li>miércoles, 10 a.m. a 2 p.m.</li>
<li>jueves, 1 p.m. a 5 p.m.</li>
<li>viernes, 9 a.m. a 12 p.m.</li>
<li>sábado, 10 a.m. a 3 p.m.</li>
<li>cerrado domingo y lunes</li>
</ul>"""

HOURS_EN = """\
<ul>
<li>Tuesday, 1 p.m. to 5 p.m.</li>
<li>Wednesday, 10 a.m. to 2 p.m.</li>
<li>Thursday, 1 p.m. to 5 p.m.</li>
<li>Friday, 9 a.m. to 12 p.m.</li>
<li>Saturday, 10 a.m. to 3 p.m.</li>
<li>Closed Sunday and Monday</li>
</ul>"""

NAV_ES = [
    ("index.html", "Inicio"),
    ("noticias-y-actualizaciones.html", "Noticias y actualizaciones"),
    ("donaciones.html", "Donaciones"),
    ("sobre-nosotros.html", "Sobre Nosotros"),
    ("organigrama.html", "Organigrama"),
]

NAV_EN = [
    ("en.html", "Home"),
    ("en/news-and-updates.html", "News & Updates"),
    ("en/donations.html", "Donations"),
    ("en/about-us.html", "About Us"),
    ("en/governance.html", "Governance"),
]

PAIR = {
    "index.html": "en.html",
    "calendario-comunitario.html": "en/community-calendar.html",
    "membresia-anual.html": "en/application-for-a-library-card.html",
    "noticias-y-actualizaciones.html": "en/news-and-updates.html",
    "donaciones.html": "en/donations.html",
    "donaciones-de-libros.html": "en/book-donations.html",
    "sobre-nosotros.html": "en/about-us.html",
    "organigrama.html": "en/governance.html",
    "preguntas-frecuentes.html": "en/frequently-asked-questions.html",
    "politicas-de-la-biblioteca.html": "en/library-policies.html",
    "historias-de-voluntarios.html": "en/volunteer-stories.html",
    "agradecimiento-a-nuestros-donantes.html": "en/thank-you-to-our-corporate-donors.html",
    "progreso-de-renovaciones.html": "en/renovation-progress-2024.html",
    "informe-anual-2024.html": "en/annual-reports.html",
}
PAIR.update({v: k for k, v in list(PAIR.items())})


def prefix_for(path):
    return "../" if path.startswith("en/") else ""


def href(path, target):
    p = prefix_for(path)
    if target.startswith("http"):
        return target
    if path.startswith("en/"):
        if target.startswith("en/"):
            return target[3:]
        return "../" + target
    return target


def page(path, title, description, body, home=False):
    lang = "en" if path == "en.html" or path.startswith("en/") else "es"
    p = prefix_for(path)
    nav = NAV_EN if lang == "en" else NAV_ES
    other = PAIR[path]
    menu = "Menu" if lang == "en" else "Menú"
    skip = "Skip to content" if lang == "en" else "Saltar al contenido"
    hours_title = "Hours" if lang == "en" else "Horario"
    hours = HOURS_EN if lang == "en" else HOURS_ES
    catalog_label = "Search the online catalogue" if lang == "en" else "Buscar en el catálogo en línea"
    follow = "Follow us" if lang == "en" else "Síganos"
    more = "More" if lang == "en" else "Más"
    foundation = "Fundación Arte y Cultura de Tierras Altas"
    lang_label = "Español" if lang == "en" else "English"
    body_class = ' class="home"' if home else ""

    links = []
    for target, label in nav:
        current = ' aria-current="page"' if target == path else ""
        extra = ' class="lang"' if False else ""
        links.append(f'<a href="{href(path, target)}"{current}{extra}>{label}</a>')
    links.append(f'<a class="lang" href="{href(path, other)}" lang="{"es" if lang == "en" else "en"}">{lang_label}</a>')

    extra_es = [
        ("calendario-comunitario.html", "Calendario"),
        ("membresia-anual.html", "Carnet"),
        ("donaciones-de-libros.html", "Donaciones de libros"),
        ("politicas-de-la-biblioteca.html", "Políticas"),
        ("preguntas-frecuentes.html", "Preguntas frecuentes"),
    ]
    extra_en = [
        ("en/community-calendar.html", "Calendar"),
        ("en/application-for-a-library-card.html", "Library card"),
        ("en/book-donations.html", "Book donations"),
        ("en/library-policies.html", "Policies"),
        ("en/frequently-asked-questions.html", "FAQ"),
    ]
    more_links = "\n".join(
        f'<li><a href="{href(path, t)}">{lab}</a></li>' for t, lab in (extra_en if lang == "en" else extra_es)
    )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{p}img/favicon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Oswald:wght@500;700&display=swap">
<link rel="stylesheet" href="{p}css/style.css">
</head>
<body{body_class}>
<a class="skip" href="#content">{skip}</a>
<header class="site-header">
<div class="header-inner">
<a class="brand" href="{href(path, 'en.html' if lang == 'en' else 'index.html')}">
<img src="{p}img/header.png" alt="Biblioteca San Benito, Tierras Altas, Panamá">
</a>
<input type="checkbox" id="nav-toggle">
<label class="nav-button" for="nav-toggle" aria-label="{menu}"><span></span></label>
<nav class="nav">
{chr(10).join(links)}
</nav>
</div>
</header>
<main id="content">
<div class="wrap">
{body}
</div>
</main>
<footer class="site-footer">
<div class="footer-inner">
<section>
<h2>{hours_title}</h2>
{hours}
<p><a href="{CATALOG}">{catalog_label}</a></p>
</section>
<section>
<h2>{more}</h2>
<ul>
{more_links}
</ul>
</section>
<section>
<h2>{follow}</h2>
<p class="social">
<a href="{FACEBOOK}" aria-label="Facebook">{ICON_FB}</a>
<a href="{INSTAGRAM}" aria-label="Instagram">{ICON_IG}</a>
</p>
<ul>
<li><a href="{WHATSAPP}">WhatsApp 6372-6705</a></li>
</ul>
<p>{foundation}</p>
</section>
</div>
</footer>
</body>
</html>
"""


def person(img_prefix, file, name, role, bio, alt):
    img = f'<img src="{img_prefix}img/{file}" alt="{alt}">' if file else ""
    return f"""<article class="person">
{img}
<div>
<h2>{name}</h2>
<p class="role">{role}</p>
{bio}
</div>
</article>"""


def write_pages(docs: Path):
    pages = {}

    pages["index.html"] = page(
        "index.html",
        "Biblioteca San Benito, Tierras Altas, Panamá",
        "Biblioteca y centro comunitario de Tierras Altas, Panamá: horario, catálogo, carnet y donaciones.",
        f"""<h1>Home</h1>
<section class="tiles">
<a class="tile" href="{CATALOG}"><img src="img/icons/catalogo.png" alt="Busque lo que necesita aquí en nuestro catálogo en línea"></a>
<a class="tile" href="calendario-comunitario.html"><img src="img/icons/calendario.png" alt="Calendario comunitario y eventos"></a>
<div class="tile"><img src="img/icons/horario.png" alt="Horario de la biblioteca"></div>
<a class="tile" href="membresia-anual.html"><img src="img/icons/membresia.png" alt="Información de solicitud de membresía"></a>
<a class="tile" href="preguntas-frecuentes.html"><img src="img/icons/faq-es.jpg" alt="Preguntas frecuentes"></a>
<a class="tile" href="politicas-de-la-biblioteca.html"><img src="img/icons/politicas.png" alt="Política de biblioteca"></a>
</section>
<p class="home-catalog"><a href="{CATALOG}">Busque lo que necesita aquí en nuestro catálogo en línea</a></p>
<section class="home-hours">
<h2>HORARIO:</h2>
{HOURS_ES}
</section>""",
        home=True,
    )

    pages["calendario-comunitario.html"] = page(
        "calendario-comunitario.html",
        "Calendario comunitario — Biblioteca San Benito",
        "Charlas, hora del cuento, Spanglish y otros eventos en Tierras Altas.",
        f"""<h1>Calendario comunitario de Tierras Altas</h1>
<article class="event">
<h2>Nuestro vecino, el Volcán Barú</h2>
<p class="meta">9 de septiembre de 2026, 5:00 p.m. · inglés con traducción al español</p>
<p>Únase a nosotros para descubrir la historia de las rocas, fallas y fuerzas invisibles del oeste de Panamá que dan forma a nuestro entorno. Presentado por Carolyn Lang, geóloga cuya investigación abarca desde los mecanismos profundos de la Tierra hasta las posibilidades de vida en el cosmos.</p>
</article>
<h2>Eventos semanales de la biblioteca</h2>
<ul>
<li><strong>Spanglish</strong> — martes, 3:30 p.m. en la biblioteca</li>
<li><strong>Conversación en español</strong> — sábados, 9:00 a.m. principiantes y 10:00 a.m. nivel básico, en el aula frente a Land's End, Complejo San Benito</li>
<li><strong>Hora del cuento</strong> — sábados, 10:30 a.m. en la biblioteca (bilingüe)</li>
</ul>
<h2>Otros eventos comunitarios</h2>
<ul>
<li><strong>Mercado de los viernes</strong> — 9:00 a.m. a 1:00 p.m. en el Club de Leones</li>
<li><strong>Reciclaje</strong> — viernes y sábados, 9:00 a.m. a 12:00 p.m. detrás de la Junta Comunal de Volcán (<a href="{MAPS_RECYCLE}">mapa</a>)</li>
<li><strong>Clínica de esterilización</strong> — mismo lugar que el reciclaje. Fechas 2026: 20 de septiembre, 18 de octubre, 15 de noviembre. No hay clínica en diciembre.</li>
</ul>
<h2>Charlas de la biblioteca</h2>
<figure class="figure">
<img src="img/charla-carolyn.jpeg" alt="Afiche de la charla de Carolyn Lang sobre el Volcán Barú, 9 de septiembre de 2026">
</figure>
<article class="event">
<h2>Habilidades tecnológicas, cómo protegerse de estafadores astutos, y lo básico de WhatsApp con Cristhian Vega</h2>
<p class="meta">14 de octubre de 2026, 5:00 p.m. · inglés y español</p>
<p>Cristhian responderá preguntas sobre todo lo relacionado con la tecnología informática (siéntase libre de enviar sus preguntas), cómo mantenerse alerta ante los estafadores, y cómo sacarle el máximo provecho a WhatsApp.</p>
</article>
<h2>Eventos pasados</h2>
<ul>
<li>12 de agosto de 2026: La vida secreta de las orquídeas, Jorge Acosta</li>
<li>8 de julio de 2026: Tai Chi, Helen Horn</li>
<li>10 de junio de 2026: Charla de voluntariado</li>
<li>13 de mayo de 2026: Historias de café</li>
<li>2 de mayo de 2026: Café y economía</li>
<li>8 de abril de 2026: Historia de los volcanes, Abdiel Torres</li>
<li>26 de marzo de 2026: Prepárate, Boquete Health and Hospice</li>
<li>11 de marzo de 2026: Pesca en las aguas del Pacífico de Chiriquí, Monty López</li>
<li>11 de febrero de 2026: Explorando China: un millón de pasos, Tracey Eaton</li>
<li>14 de enero de 2026: Siéntete mejor con tu cuerpo, Steph Lozen</li>
<li>12 de diciembre de 2025: Conviviendo con serpientes, Mike Hill</li>
<li>14 de noviembre de 2025: La vida de los Ngäbe-Buglé, Reynaldo Quintera</li>
<li>10 de octubre de 2025: Preparar el jardín para la temporada de vientos</li>
<li>12 de septiembre de 2025: Una carrera por la paz, Mulget Amaru</li>
<li>8 de agosto de 2025: Un poco de todo, Jenna Glasz</li>
<li>26 de julio de 2025: RCP, Jim Myers</li>
<li>3 de julio de 2025: Heliconias, Carla Black</li>
</ul>""",
    )

    pages["membresia-anual.html"] = page(
        "membresia-anual.html",
        "Carnet de biblioteca — Biblioteca San Benito",
        "Cómo solicitar un carnet familiar o juvenil en la Biblioteca San Benito.",
        """<h1>Carnet de biblioteca</h1>
<p>Quien vive en Tierras Altas (Volcán, Cerro Punta, Paso Ancho, Nueva California, Cuesta de Piedra, Tisingal o Caisán) puede solicitar un carnet y llevar libros.</p>
<h2>Tipos de membresía</h2>
<ul>
<li><strong>Carnet familiar, B/. 5</strong> — cubre a un adulto y su familia que vive en el mismo hogar.</li>
<li><strong>Carnet juvenil, B/. 3</strong> — para jóvenes de 12 a 18 años que quieren su propio carnet.</li>
</ul>
<h2>Requisitos</h2>
<ul>
<li>Cédula o pasaporte</li>
<li>Comprobante de domicilio en Tierras Altas: recibo de luz, agua, teléfono o copia del contrato de arrendamiento</li>
</ul>
<p>Venga durante el horario de atención o descargue el formulario. El carnet tarda una o dos semanas, pero puede llevar libros de inmediato. Un padre o acudiente debe acompañar al joven que solicita carnet.</p>
<div class="actions">
<a class="button" href="files/formulario-carnet.pdf">Descargar el formulario</a>
<a class="button secondary" href="politicas-de-la-biblioteca.html">Ver políticas de préstamo</a>
</div>""",
    )

    pages["preguntas-frecuentes.html"] = page(
        "preguntas-frecuentes.html",
        "Preguntas frecuentes — Biblioteca San Benito",
        "Horario, renovación de libros y cómo obtener un carnet.",
        f"""<h1>Preguntas frecuentes</h1>
<dl class="faq">
<dt>¿Cuál es el horario?</dt>
<dd>{HOURS_ES}</dd>
<dt>¿Cómo renuevo un libro?</dt>
<dd>En persona o por <a href="{WHATSAPP}">WhatsApp +507 6372-6705</a>. Puede renovar una vez.</dd>
<dt>¿Cómo obtengo un carnet?</dt>
<dd>Traiga identificación y un comprobante de domicilio en Tierras Altas. Hay carnet familiar (B/. 5) y juvenil (B/. 3). Detalles en <a href="membresia-anual.html">membresía anual</a>.</dd>
<dt>¿Hay multa por atraso?</dt>
<dd>No cobramos cargos por demora. Pedimos devolver los libros a tiempo para que otras personas puedan leerlos.</dd>
</dl>""",
    )

    pages["politicas-de-la-biblioteca.html"] = page(
        "politicas-de-la-biblioteca.html",
        "Políticas de la biblioteca — Biblioteca San Benito",
        "Carnet, préstamo de libros, internet y normas de la sala.",
        """<h1>Políticas de la biblioteca</h1>
<p>Nuestra biblioteca es un espacio para el aprendizaje, la curiosidad y la comunidad. Para que todas las visitas sean agradables, estas son las normas.</p>
<h2>Cómo obtener un carnet</h2>
<p>Si vive en Tierras Altas (Volcán, Cerro Punta, Paso Ancho, Nueva California, Cuesta de Piedra, Tisingal o Caisán), puede obtener un carnet y pedir libros prestados.</p>
<ul>
<li>Traiga una copia de un comprobante de domicilio (recibo de luz, agua, internet, teléfono o contrato de arrendamiento).</li>
<li>Traiga una copia de su cédula o pasaporte (también para niños).</li>
<li>Complete la solicitud de carnet.</li>
<li>Para menores de 12 a 18 años: un padre o acudiente debe firmar el formulario y presentar identificación.</li>
</ul>
<p><strong>B/. 5 carnet familiar</strong> — un adulto y su familia en el mismo hogar.<br>
<strong>B/. 3 carnet juvenil</strong> — jóvenes de 12 a 18 años que quieren su propio carnet.</p>
<p>Los carnets son personales e intransferibles. Usted es responsable de lo prestado con su carnet. Se renuevan cada año. Un carnet perdido cuesta B/. 2.</p>
<h2>Préstamo de libros</h2>
<ul>
<li>Puede prestar dos libros a la vez por dos semanas.</li>
<li>Puede renovar una sola vez, en persona o por WhatsApp.</li>
<li>No cobramos cargos por demora; pedimos devolver los libros a tiempo.</li>
<li>Los niños pueden pedir libros con el carnet de su padre, madre o tutor, y el hogar puede llevar más de dos libros.</li>
<li>Si pierde un libro y no lo devuelve en un mes, pedimos cubrir el costo (hasta B/. 10, salvo libros publicados en los últimos 4 años).</li>
</ul>
<h2>Internet y tecnología</h2>
<p>Hay Wi-Fi gratuito en toda la biblioteca.</p>
<ul>
<li>Los padres o acudientes supervisan el uso de internet de sus hijos.</li>
<li>Computadoras públicas: no más de dos personas por computadora.</li>
<li>Si reproduce música o juega en un dispositivo personal, use auriculares.</li>
</ul>
<h2>Dentro de la biblioteca</h2>
<ul>
<li>No se permite comer. Bebidas en envases con tapa sí.</li>
<li>Espacio libre de humo y zona tranquila.</li>
<li>Deje las mochilas con el bibliotecario.</li>
<li>Se permite cargar teléfonos.</li>
<li>No correr ni gritar.</li>
<li>Puede leer, estudiar o relajarse sin carnet; solo quienes tienen carnet piden libros prestados.</li>
<li>Trate con cuidado los libros, juguetes y rompecabezas, y devuélvalos al terminar.</li>
</ul>
<p>La biblioteca puede pedir que se retire quien no cumpla estas normas.</p>""",
    )

    pages["donaciones.html"] = page(
        "donaciones.html",
        "Donaciones — Biblioteca San Benito",
        "Cómo donar a la Fundación Arte y Cultura de Tierras Altas.",
        f"""<h1>Donaciones</h1>
<p>Las donaciones mantienen la biblioteca abierta. Puede depositar directamente en la cuenta de la Fundación o, si está en Estados Unidos, aportar por GoFundMe.</p>
<div class="bank">
<p><strong>Banco:</strong> Banistmo</p>
<p><strong>Nombre de la cuenta:</strong> Fundacion Arte y Cultura de Tierras Altas</p>
<p><strong>Número de cuenta:</strong> 011 984 7755</p>
<p><strong>Tipo:</strong> corriente</p>
<p><strong>Código SWIFT:</strong> MIDLPAPAXXX</p>
</div>
<div class="actions">
<a class="button" href="{GOFUNDME}">GoFundMe</a>
<a class="button secondary" href="donaciones-de-libros.html">Donar libros</a>
</div>""",
    )

    pages["donaciones-de-libros.html"] = page(
        "donaciones-de-libros.html",
        "Donaciones de libros — Biblioteca San Benito",
        "Qué libros aceptamos y cómo donarlos.",
        """<h1>Donaciones de libros</h1>
<p>Agradecemos las ofertas de libros. Si desea donar, escriba a la bibliotecaria Chris Thomas: <a href="mailto:chrisbardolf@gmail.com">chrisbardolf@gmail.com</a>.</p>
<h2>Lo que necesitamos</h2>
<p>Libros en español e inglés. La meta es una colección de 10.000 libros y otros materiales, idealmente 60% en español y 40% en inglés, para niños y adultos.</p>
<h2>Lo que no podemos aceptar</h2>
<ul>
<li>Libros dañados por insectos, con páginas rotas, moho o escritura</li>
<li>No ficción de más de 10 años</li>
<li>Enciclopedias</li>
<li>Revistas de más de 3 años</li>
<li>Casetes, cintas VHS o Betamax, o películas</li>
</ul>""",
    )

    pages["sobre-nosotros.html"] = page(
        "sobre-nosotros.html",
        "Sobre nosotros — Biblioteca San Benito",
        "Historia, visión y misión de la Biblioteca San Benito en Tierras Altas.",
        """<h1>Sobre nosotros</h1>
<h2>Visión</h2>
<p>Enriquecer la vida de las personas de Tierras Altas creando un lugar que inspire la alfabetización, el arte, la educación y el compromiso social.</p>
<h2>Misión</h2>
<p>La biblioteca ofrece un ambiente acogedor y de apoyo donde:</p>
<ul>
<li>los libros despiertan la imaginación, fomentan la alfabetización y el amor por la lectura</li>
<li>las personas descubren, crean y comparten información e ideas</li>
<li>familias y amigos se reúnen para actividades culturales y comunitarias</li>
</ul>
<p>La Fundación Arte y Cultura de Tierras Altas fue fundada por un grupo de amantes de los libros que trabajan para establecer una biblioteca y centro comunitario para los residentes de Tierras Altas. Esta área tuvo una biblioteca y centro comunitario muy queridos, fundados en 1961 por el hermano benedictino Elred Wetli.</p>
<p>Quienes recuerdan la biblioteca original hablan del Brother Elred y de cómo las clases de inglés y otras materias les cambiaron la vida. El centro era el lugar donde las familias se reunían. Además de libros, prestaban juguetes los fines de semana.</p>
<figure class="figure">
<img src="img/antigua-biblioteca.jpg" alt="La antigua Biblioteca San Benito">
<figcaption>La antigua Biblioteca San Benito</figcaption>
</figure>
<p>La biblioteca se cerró poco después de la muerte del Brother Elred. Al cerrar en 2013, los libros quedaron adentro y sufrieron el clima. Algunos se pudieron salvar; otros, amarillentos o comidos por polilla, solo sirven para reciclar. Muchos de los libros originales vinieron de bibliotecas de la Zona del Canal. Esa colección necesita actualizarse.</p>
<p>La nueva biblioteca sirve al distrito de Tierras Altas (unos 40.000 habitantes, 8.000 menores de 15 años): Volcán, Cerro Punta, Nueva California, Cuesta de Piedra y Paso Ancho. No hay otra biblioteca en estos lugares. Los libros son inalcanzables para la mayoría. Una biblioteca hace posible leer para todos.</p>""",
    )

    pages["organigrama.html"] = page(
        "organigrama.html",
        "Organigrama — Biblioteca San Benito",
        "Miembros de la junta directiva de la Fundación Arte y Cultura de Tierras Altas.",
        "<h1>Junta directiva</h1>"
        + person(
            "",
            "tony-leung.jpg",
            "Anthony Tak On Leung",
            "Presidente, jubilado",
            "<p>Nació y creció en Hong Kong; estudió en la Universidad de Wisconsin. Fue empresario y trabajó para la Organización Internacional para las Migraciones como oficial de administración y finanzas en Manila. Ha sido voluntario en varias ONG en Hong Kong, incluyendo Refugee Concern, la Asociación Hong Chi, la Fundación Pam Baker, y presidió The Leprosy Project en Sichuan, China. Fue rotario activo por más de 30 años.</p>",
            "Anthony Leung, presidente",
        )
        + person(
            "",
            "linda-chang.jpg",
            "Linda Kristina Chang Quintero",
            "Vicepresidenta y representante legal, abogada",
            "<p>Miembro fundador. Nació en la ciudad de Panamá. Título en Derecho y Ciencias Políticas de la Universidad Metropolitana de Panamá; conciliadora y mediadora por la Universidad Latina, con especialización en derecho comercial y migratorio. Socia de Magallan y Chang; asesora legal de la Cámara de Turismo, Comercio e Industria de Tierras Altas.</p>",
            "Linda Chang, vicepresidenta",
        )
        + person(
            "",
            "alan-baumbach.jpg",
            "Alan John Baumbach",
            "Tesorero, jubilado",
            "<p>Miembro fundador. Nació en Colorado. Título de la Universidad de Denver y certificación de contador público de Alaska, en Arthur Young and Company. Participó en vivienda de bajo costo y proyectos médicos en Centroamérica, y en el Instituto Osher de Aprendizaje de la Universidad de Denver.</p>",
            "Alan Baumbach",
        )
        + person(
            "",
            "laurie-leung.jpg",
            "Laurie Lemmlie-Leung",
            "Secretaria, jubilada",
            "<p>Miembro fundador; también trabaja con el comité de recaudación. Nació en Estados Unidos y se graduó de Cornell College. Sirvió en el Cuerpo de Paz en Filipinas, trabajó para el programa estadounidense de refugiados en Manila y en KPMG en Hong Kong. En Volcán es voluntaria de Tierras Altas Recicla.</p>",
            "Laurie Lemmlie-Leung, secretaria",
        )
        + person(
            "",
            "chris-thomas.jpg",
            "Christine Bardolf Thomas",
            "Bibliotecaria, jubilada",
            "<p>Miembro fundador. Título de Clemson University y maestría en educación de Framingham. Enseñó inglés y ciencias en Costa Rica y fue bibliotecaria de primaria 23 años en una escuela internacional. Trabaja con la Fundación Humanitaria de Costa Rica y como consultora de Wells Mountain Foundation y Tropical Forest Management Foundation. Ha vivido entre Costa Rica y Panamá 42 años.</p>",
            "Chris Thomas, bibliotecaria",
        )
        + person(
            "",
            "chris-arias.jpg",
            "Chris Arias",
            "Instructora de español para extranjeros",
            "<p>Miembro fundador, bilingüe inglés/español. Nació en Honduras. Título en tecnología de alimentos y en alta dirección bancaria. Fue presidenta de AHIBA en el litoral atlántico y vicepresidenta de la Cámara de Comercio de Atlántida. Ha servido en juntas de Adelante Foundation, RBC en Roatán y HALA.</p>",
            "Chris Arias",
        )
        + person(
            "",
            "estela-ritter.jpg",
            "Estela Ritter Pangtay",
            "Tercera vocal, jubilada",
            "<p>Nació en la ciudad de Panamá. Arquitecta por la Universidad de São Paulo. Trabajó como urbanista para el gobierno de Panamá y como operadora CAD en Canadá. Miembro activo de Tierras Altas Recicla.</p>",
            "Estela Ritter",
        )
        + person(
            "",
            "rossana-tarantini.jpeg",
            "Rossana Saccucci Tarantini (Roxx)",
            "Tesorera, editora",
            "<p>Nació en Canadá, de ascendencia italiana. Licenciada en idiomas (francés, italiano y español) por York University, Toronto. Certificaciones en contabilidad, gestión de instalaciones y edición. Este es su primer cargo en la junta de una fundación sin fines de lucro.</p>",
            "Rossana Saccucci Tarantini, tesorera",
        )
        + person(
            "",
            "nahomi-soto.jpg",
            "Nahomi Soto",
            "Asesora, estudiante de ingeniería",
            "<p>Nació en la ciudad de Panamá. Estudia Ingeniería Industrial Administrativa. Apoya redes sociales y la promoción de actividades de la biblioteca.</p>",
            "Nahomi Soto",
        )
        + """
<h2>Otros miembros</h2>
<ul>
<li>Cheryl Roe Michel, jubilada</li>
<li>Stephanie Llean Charpentier Santamaría, arquitecta</li>
<li>Miguel Eduardo Samudio Ledezma, servicio civil</li>
<li>Ana Iris Tribaldos Jarquin, administración</li>
</ul>
<h2>Miembros anteriores de la junta directiva</h2>"""
    )

    pages["noticias-y-actualizaciones.html"] = page(
        "noticias-y-actualizaciones.html",
        "Noticias y actualizaciones — Biblioteca San Benito",
        "Novedades de la Biblioteca San Benito.",
        """<h1>Noticias y actualizaciones</h1>
<ul class="news">
<li><a href="historias-de-voluntarios.html">Historias de voluntarios</a><br><span class="meta">14 de febrero de 2025</span></li>
<li><a href="agradecimiento-a-nuestros-donantes.html">Agradecimiento a nuestros donantes</a><br><span class="meta">15 de enero de 2025</span></li>
<li><a href="progreso-de-renovaciones.html">Progreso de renovaciones</a><br><span class="meta">15 de enero de 2025</span></li>
<li><a href="informe-anual-2024.html">Informe anual 2024</a><br><span class="meta">9 de enero de 2025</span></li>
</ul>""",
    )

    pages["historias-de-voluntarios.html"] = page(
        "historias-de-voluntarios.html",
        "Historias de voluntarios — Biblioteca San Benito",
        "Jill Dubler cuenta cómo se catalogan los libros de la biblioteca.",
        """<h1>Historias de voluntarios</h1>
<p class="meta">14 de febrero de 2025</p>
<h2>Jill Dubler</h2>
<p>Mi esposo y yo llegamos a Volcán hace tres años. Hace dos años me involucré en ayudar a la Biblioteca San Benito. He hecho muchas de las tareas para restaurar los libros que se salvaron de la antigua biblioteca, pero descubrí que mi verdadera pasión es la catalogación. Comparto este trabajo con Ed Simmons.</p>
<h2>Catalogación</h2>
<p>Cada libro debe ingresarse en nuestro sistema para que se pueda buscar de varias maneras. Trabajo desde casa, así que mi esposo y yo trasladamos cajas desde la “oficina” de la biblioteca. He llegado a tener entre 7 y 10 cajas grandes a la vez.</p>
<p>Tenemos acceso a las bases de datos de cuatro bibliotecas asociadas. Primero busco el libro por título, autor, editorial, ISBN, etc. Si aparece, usamos parte de esa información y la revisamos. El formulario incluye ISBN, autor, título, lugar y fecha de publicación, editorial, páginas, ilustraciones y mapas. Medimos el libro en centímetros, anotamos si es parte de una serie, el idioma, un resumen, premios, temas e ilustrador.</p>
<p>La segunda página indica dónde se coloca en nuestros estantes: clasificación Dewey, ficción, literatura infantil o juvenil, referencia, biografía, código de barras y costo estimado de reemplazo.</p>
<figure class="figure">
<img src="img/jill-dubler.jpg" alt="Jill Dubler, voluntaria que cataloga libros para la Biblioteca San Benito">
<figcaption>Jill Dubler cataloga libros para la Biblioteca San Benito.</figcaption>
</figure>
<h2>¿Y si no está en las otras bibliotecas?</h2>
<p>Hay que crear toda la información desde cero. Muchos registros no tienen foto de portada; usamos Google, Amazon, eBay y otras fuentes. Un libro puede tomar entre 5 y 20 minutos.</p>
<h2>¿Hay diferencia entre español e inglés?</h2>
<p>Los libros en español rara vez están en las bibliotecas asociadas, así que casi siempre hay que empezar de cero y traducir el formulario a ambos idiomas. He leído que los libros infantiles ayudan a aprender un idioma. ¡Tienen razón!</p>
<p>Vamos a tener una selección increíble en la nueva Biblioteca San Benito, y estoy muy agradecida de seguir formando parte de este proyecto.</p>""",
    )

    pages["agradecimiento-a-nuestros-donantes.html"] = page(
        "agradecimiento-a-nuestros-donantes.html",
        "Agradecimiento a nuestros donantes — Biblioteca San Benito",
        "Gracias a Grupo ENX, Naturgy y Janson Coffee Farm por apoyar las renovaciones de 2024.",
        """<h1>Agradecimiento a nuestros donantes</h1>
<p class="meta">31 de enero de 2025</p>
<figure class="figure">
<img src="img/enx-photo.jpg" alt="Tony Leung, Moisés Vega, Nery Esquivel y Linda Chang">
<figcaption>De izquierda a derecha: Tony Leung, presidente de la Fundación; Moisés Vega, CEO de Grupo ENX; Nery Esquivel, coordinador de asistencia social de Chiriquí; y Linda Chang, vicepresidenta de la Fundación.</figcaption>
</figure>
<div class="logos"><img src="img/enx-logo.jpg" alt="Logo de Grupo ENX"></div>
<figure class="figure">
<img src="img/naturgy-signing.jpg" alt="Entrega de cheque de Naturgy">
<figcaption>De izquierda a derecha: Mymara Crespo Baiz, directora de comunicaciones de Naturgy; el gerente regional Javier Sánchez; y Tony Leung.</figcaption>
</figure>
<div class="logos"><img src="img/naturgy-logo.jpg" alt="Logo de Naturgy"></div>
<figure class="figure">
<img src="img/janson-family.jpg" alt="Familia Janson con miembros de la Fundación">
<figcaption>De izquierda a derecha: Zahida de Janson, Janeth Janson, Haydee y Carl Janson de Janson Coffee Farm, con Tony Leung, Laurie Lemmlie-Leung y Linda Chang.</figcaption>
</figure>
<div class="logos"><img src="img/janson-logo.png" alt="Logo de Janson Coffee Farm"></div>
<p>Ninguna de las <a href="progreso-de-renovaciones.html">renovaciones de 2024</a> habría sido posible sin el apoyo de nuestros donantes. Un agradecimiento de corazón a Moisés Vega de Grupo ENX, Javier Sánchez, gerente regional de Naturgy, y Haydee Janson de Janson Coffee Farm, quien también donó el inodoro y las barras de seguridad para el baño accesible.</p>""",
    )

    pages["progreso-de-renovaciones.html"] = page(
        "progreso-de-renovaciones.html",
        "Progreso de renovaciones — Biblioteca San Benito",
        "Mejoras al edificio de la biblioteca en 2024.",
        """<h1>Progreso de renovaciones</h1>
<p class="meta">31 de enero de 2025</p>
<p>Al mirar atrás a 2024, nos emociona el progreso logrado juntos. Gracias a su generosidad y a la de nuestros <a href="agradecimiento-a-nuestros-donantes.html">donantes corporativos</a>, recaudamos fondos para comenzar las renovaciones. Estas mejoras crean un espacio más acogedor, accesible y funcional.</p>
<div class="gallery">
<img src="img/reno-walkway.jpg" alt="Ampliación de la acera">
<img src="img/reno-door.jpg" alt="Puerta ensanchada entre las salas">
<img src="img/reno-roof.jpg" alt="Reparación del techo">
<img src="img/reno-electrical.jpg" alt="Sistema eléctrico">
<img src="img/reno-ceiling.jpg" alt="Cielorraso nuevo">
<img src="img/reno-glass-door.jpg" alt="Nueva entrada principal con puertas de vidrio">
</div>""",
    )

    pages["informe-anual-2024.html"] = page(
        "informe-anual-2024.html",
        "Informe anual 2024 — Biblioteca San Benito",
        "Recaudación, obras, libros y clases de idiomas en 2024.",
        """<h1>Informe anual 2024</h1>
<p class="meta">9 de enero de 2025</p>
<h2>Junta directiva</h2>
<p>El 29 de enero de 2023 se eligió la junta:</p>
<ul>
<li>Presidente: Tony Leung</li>
<li>Vicepresidenta: Linda Chang</li>
<li>Secretaria: Laurie Lemmlie-Leung</li>
<li>Tesorero: Alan Baumbach</li>
<li>Fiscal: Cher Michel</li>
<li>Miembros: Stephanie, Gregorio Filis, Estela Ritter</li>
<li>Asesores: Ana Tribaldos, Miguel Samudio</li>
</ul>
<h2>Recaudación de fondos</h2>
<ul>
<li><strong>Food truck de Año Nuevo:</strong> Beth Harrison instaló su food truck en casa de Azel Ames durante el picnic comunitario. Todas las ganancias fueron para la biblioteca.</li>
<li><strong>Fiestas comunitarias:</strong> Black and White Bash en agosto, Halloween en octubre y fiesta de suéteres feos en diciembre.</li>
<li><strong>Campaña “Sé una luz”:</strong> financió las luces nuevas en dos días e inspiró a un donante anónimo a aportar cada mes.</li>
<li><strong>Parada de las Flores:</strong> mostramos las mejoras del edificio, alquilamos los baños, vendimos ropa donada y distribuimos libros.</li>
<li><strong>Bazar de diciembre:</strong> más de 30 vendedores. Beth Harrison donó de nuevo el food truck; Lyn Bishop organizó “BonBons for Books”. Hubo autos clásicos (Anyansi de Angel), desfile de perros, cuentacuentos y manualidades (Natalie Richie), pintacaritas (Jenna Glasz) y globos (Terry Newcombe).</li>
</ul>
<p>Agradecemos a Marianne Brown y The Quilt House por la colcha rifada en agosto, y a Alan Baumbach por la motocicleta rifada en la fiesta de Navidad.</p>
<p>Apreciamos las contribuciones de Moisés Vega (Grupo ENX), Javier Sánchez (Naturgy) y Haydee Janson (Janson Coffee Farm). La familia Janson también donó el inodoro y las barras del baño accesible. Gracias a Linda Chang por gestionar estas donaciones.</p>
<h2>Mejoras en el edificio</h2>
<ul>
<li>Acera ampliada alrededor del edificio</li>
<li>Puerta ensanchada entre las salas principales</li>
<li>Techo reparado y cielorrasos nuevos con luces y ventiladores</li>
<li>Ambos baños renovados; uno accesible gracias a la familia Janson</li>
<li>Nueva entrada con puertas dobles de vidrio, a tiempo para el bazar de Navidad</li>
</ul>
<h2>Libros</h2>
<p>Chris Thomas y un equipo de voluntarios catalogaron más de 7.000 libros para la inauguración.</p>
<h2>Clases de idiomas</h2>
<p><strong>Inglés.</strong> Natalie Richie relanzó clases en enero para niños (7–12), adolescentes (13–18) y adultos.</p>
<p><strong>Español.</strong> Las clases a bajo costo de Arelis Mendoza pasaron de un grupo mixto a tres niveles.</p>
<p>Este informe resume el trabajo de la Fundación Arte y Cultura de Tierras Altas en 2024.</p>""",
    )

    # English
    pages["en.html"] = page(
        "en.html",
        "San Benito Library, Tierras Altas, Panama",
        "Community library in Tierras Altas, Panama: hours, catalogue, library cards, and donations.",
        f"""<h1>Home</h1>
<section class="tiles">
<a class="tile" href="{CATALOG}"><img src="img/icons/catalog-en.png" alt="Search the online catalogue"></a>
<a class="tile" href="en/community-calendar.html"><img src="img/icons/calendar-en.png" alt="Community calendar"></a>
<div class="tile"><img src="img/icons/hours-en.png" alt="Library hours"></div>
<a class="tile" href="en/application-for-a-library-card.html"><img src="img/icons/card-en.png" alt="Application for a library card"></a>
<a class="tile" href="en/frequently-asked-questions.html"><img src="img/icons/faq-en.jpg" alt="Frequently asked questions"></a>
<a class="tile" href="en/library-policies.html"><img src="img/icons/policies-en.png" alt="Library policies"></a>
</section>
<p class="home-catalog"><a href="{CATALOG}">Search the online library catalogue here</a></p>
<section class="home-hours">
<h2>OPENING HOURS:</h2>
{HOURS_EN}
</section>""",
        home=True,
    )

    pages["en/community-calendar.html"] = page(
        "en/community-calendar.html",
        "Community calendar — San Benito Library",
        "Talks, story time, Spanglish, and other events in Tierras Altas.",
        f"""<h1>Tierras Altas community calendar</h1>
<h2>Weekly library events</h2>
<ul>
<li><strong>Spanglish</strong> — Tuesdays, 3:30 p.m. at the library</li>
<li><strong>Spanish conversation</strong> — Saturdays, 9:00 a.m. beginners and 10:00 a.m. basic, in the classroom across from Land's End in the San Benito compound</li>
<li><strong>Story time</strong> — Saturdays, 10:30 a.m. in the library (bilingual)</li>
</ul>
<h2>Other community events</h2>
<ul>
<li><strong>Friday market</strong> — 9:00 a.m. to 1:00 p.m. at the Lion’s Club</li>
<li><strong>Recycling</strong> — Fridays and Saturdays, 9:00 a.m. to 12:00 p.m. behind the Junta Comunal de Volcán (<a href="{MAPS_RECYCLE}">map</a>)</li>
<li><strong>Spay and neuter clinic</strong> — same location as recycling. 2026 dates: 20 September, 18 October, 15 November. None in December.</li>
</ul>
<article class="event">
<h2>Tech skills, staying safe from savvy scammers, and the basics of WhatsApp with Cristhian Vega</h2>
<p class="meta">14 October 2026 · bilingual</p>
<p>Cristhian will answer questions on all things related to computer technology (feel free to submit questions), staying ahead of the scammers, and how to get the most out of WhatsApp.</p>
</article>
<h2>Speaker series</h2>
<figure class="figure">
<img src="../img/charla-carolyn.jpeg" alt="Poster for Carolyn Lang’s 9 September 2026 talk on Volcán Barú">
</figure>
<article class="event">
<h2>Our Neighbor, Volcán Barú: Shifting Plates, Hidden Geology, and What Comes Next with Carolyn Lang</h2>
<p class="meta">9 September 2026, 5:00 p.m. · English with Spanish translation</p>
<p>Join us to uncover the story of western Panama’s rocks, faults, and unseen forces that shape our surroundings. Presented by Carolyn Lang, a geologist whose research spans from the deep mechanisms of Earth to the possibilities of life in the cosmos.</p>
</article>
<h2>Past events</h2>
<ul>
<li>12 August 2026: The Secret Life of Orchids, Jorge Acosta</li>
<li>8 July 2026: Tai Chi, Helen Horn</li>
<li>10 June 2026: Volunteer talks</li>
<li>13 May 2026: Coffee stories, Ratibor Hartman</li>
<li>2 May 2026: Coffee and the economy, Lucho Moran</li>
<li>8 April 2026: Volcano history, Abdiel Torres</li>
<li>26 March 2026: Be Prepared, Boquete Health and Hospice</li>
<li>11 March 2026: Fishing in the Pacific waters of Chiriquí, Monty López</li>
<li>11 February 2026: Exploring China: One Million Steps, Tracey Eaton</li>
<li>14 January 2026: Feel Better in Your Body, Steph Lozen</li>
<li>12 December 2025: Living with snakes, Mike Hill</li>
<li>14 November 2025: Ngäbe-Buglé life, Reynaldo Quintera</li>
<li>10 October 2025: Preparing your garden for the windy season</li>
<li>12 September 2025: A Run for Peace, Mulget Amaru</li>
<li>8 August 2025: Buggin’ out, Jenna Glasz</li>
<li>26 July 2025: CPR, Jim Myers</li>
<li>3 July 2025: Heliconias, Carla Black</li>
</ul>""",
    )

    pages["en/application-for-a-library-card.html"] = page(
        "en/application-for-a-library-card.html",
        "Library card — San Benito Library",
        "How to apply for a family or teen library card.",
        """<h1>Library card</h1>
<p>If you live in Tierras Altas (Volcán, Cerro Punta, Paso Ancho, Nueva California, Cuesta de Piedra, Tisingal, or Caisán), you can get a card and borrow books.</p>
<h2>Types of membership</h2>
<ul>
<li><strong>Family card, B/. 5</strong> — covers an adult and their immediate family in the same household.</li>
<li><strong>Teen card, B/. 3</strong> — for ages 12–18 who want their own card.</li>
</ul>
<h2>Requirements</h2>
<ul>
<li>Cédula or passport</li>
<li>Proof of residence in Tierras Altas: electric, water, or phone bill, or a copy of the lease</li>
</ul>
<p>Visit during opening hours or download the form. The card is ready in one to two weeks, but you can check out books immediately. A parent or guardian must accompany a teen applying for a card.</p>
<div class="actions">
<a class="button" href="../files/library-card-application.pdf">Download the application</a>
<a class="button secondary" href="library-policies.html">Borrowing policies</a>
</div>""",
    )

    pages["en/frequently-asked-questions.html"] = page(
        "en/frequently-asked-questions.html",
        "FAQ — San Benito Library",
        "Hours, renewals, and how to get a library card.",
        f"""<h1>Frequently asked questions</h1>
<dl class="faq">
<dt>What are the hours?</dt>
<dd>{HOURS_EN}</dd>
<dt>How do I renew a book?</dt>
<dd>In person or by <a href="{WHATSAPP}">WhatsApp +507 6372-6705</a>. You may renew once.</dd>
<dt>How do I get a library card?</dt>
<dd>Bring ID and proof of address in Tierras Altas. Family cards are B/. 5 and teen cards are B/. 3. See <a href="application-for-a-library-card.html">library cards</a>.</dd>
<dt>Are there late fees?</dt>
<dd>No. Please return books on time so others can read them too.</dd>
</dl>""",
    )

    pages["en/library-policies.html"] = page(
        "en/library-policies.html",
        "Library policies — San Benito Library",
        "Cards, borrowing, internet, and house rules.",
        """<h1>Library policies</h1>
<p>Our library is a space for learning, curiosity, and community. Please take a moment to review these policies.</p>
<h2>Getting a library card</h2>
<p>If you live in Tierras Altas (including Volcán, Cerro Punta, Paso Ancho, Nueva California, Cuesta de Piedra, Tisingal, or Caisán), you may get a card and borrow books.</p>
<ul>
<li>Bring a copy of a utility bill, lease, or other document with your local address.</li>
<li>Bring a copy of your cédula or passport (this also applies to children).</li>
<li>Fill out a library card application.</li>
<li>For ages 12–18: a parent or guardian must sign and also provide ID and proof of residency.</li>
</ul>
<p><strong>B/. 5 family card</strong> — an adult and immediate family in the same household.<br>
<strong>B/. 3 teen card</strong> — ages 12–18 who want their own card.</p>
<p>Cards are personal and non-transferable. You are responsible for items checked out on your card. Renew each year. A replacement card costs B/. 2.</p>
<h2>Borrowing books</h2>
<ul>
<li>Two books at a time for two weeks.</li>
<li>Renew once, in person or via WhatsApp.</li>
<li>No late fees; please return books on time.</li>
<li>Children may borrow on a parent or guardian’s card, so a household can take more than two books.</li>
<li>If a book is lost and not returned within a month of the due date, we ask you to cover the cost (up to B/. 10, more if published in the last four years).</li>
</ul>
<h2>Internet and technology</h2>
<p>Free Wi-Fi throughout the library.</p>
<ul>
<li>Parents or guardians supervise children’s internet use.</li>
<li>Public computers: no more than two people per computer.</li>
<li>Use earphones for music or games on a personal device.</li>
</ul>
<h2>Inside the library</h2>
<ul>
<li>No food. Drinks with a secure cap are permitted.</li>
<li>Smoke-free and quiet.</li>
<li>Leave backpacks with the librarian, on the porch, or on the bookcase at the entrance.</li>
<li>Phone charging is allowed.</li>
<li>No running or shouting.</li>
<li>You may read, study, or relax without a card; only cardholders check out books.</li>
<li>Treat books, toys, and puzzles with care and put them back.</li>
</ul>
<p>The library may ask anyone who is not following these policies to leave.</p>""",
    )

    pages["en/donations.html"] = page(
        "en/donations.html",
        "Donations — San Benito Library",
        "How to donate to the Foundation for Art and Culture of Tierras Altas.",
        f"""<h1>Donations</h1>
<p>Donations keep this small library going. You can deposit directly into the Foundation account or, from the United States, give through GoFundMe.</p>
<div class="bank">
<p><strong>Bank:</strong> Banistmo</p>
<p><strong>Account name:</strong> Fundacion Arte y Cultura de Tierras Altas</p>
<p><strong>Account number:</strong> 011 984 7755</p>
<p><strong>Account type:</strong> checking</p>
<p><strong>SWIFT:</strong> MIDLPAPAXXX</p>
</div>
<div class="actions">
<a class="button" href="{GOFUNDME}">GoFundMe</a>
<a class="button secondary" href="book-donations.html">Donate books</a>
</div>""",
    )

    pages["en/book-donations.html"] = page(
        "en/book-donations.html",
        "Book donations — San Benito Library",
        "What books we can accept and how to donate them.",
        """<h1>Book donations</h1>
<h2>What we need</h2>
<p>Books in Spanish and English. The goal is a collection of 10,000 books and other materials, ideally 60% Spanish and 40% English, for children and adults.</p>
<h2>What we cannot accept</h2>
<ul>
<li>Books with insect damage, torn pages, mold, or writing</li>
<li>Non-fiction more than 10 years old</li>
<li>Encyclopedias</li>
<li>Magazines more than 3 years old</li>
<li>Cassettes, VHS or Betamax tapes, or film</li>
</ul>
<p>We are glad of book offers. If you have books to donate, please email librarian Chris Thomas: <a href="mailto:chrisbardolf@gmail.com">chrisbardolf@gmail.com</a>.</p>""",
    )

    pages["en/about-us.html"] = page(
        "en/about-us.html",
        "About us — San Benito Library",
        "History, vision, and mission of San Benito Library in Tierras Altas.",
        """<h1>About us</h1>
<h2>Vision</h2>
<p>To enrich the lives of people in our community by creating a place that inspires literacy, art, education, and social engagement.</p>
<h2>Mission</h2>
<p>The library offers a welcoming, supportive environment where:</p>
<ul>
<li>books spark the imagination and a lifelong love of reading</li>
<li>people discover, create, and share information and ideas</li>
<li>families and friends gather for cultural and community activities</li>
</ul>
<p>The Foundation for Art and Culture of Tierras Altas was established by civic-minded booklovers working to reopen the library and community center for the western highlands of Panama. The area once had a popular library founded in 1961 by Oblate Benedictine monk Brother Elred Wetli. Long-time residents remember both the library and Brother Elred fondly.</p>
<figure class="figure">
<img src="../img/old-san-benito.jpg" alt="The old San Benito Library around 1960">
<figcaption>The old San Benito Library, around 1960</figcaption>
</figure>
<p>Many residents credit English classes and other teaching at the library with changing their lives. Families gathered there. Besides books, the library lent toys on weekends.</p>
<p>The library did not survive Brother Elred’s passing. It closed in 2013 and the books were left inside. Some are still usable; others yellowed or eaten by insects and can only be recycled. Many original books came from Canal Zone libraries and the collection needs updating.</p>
<p>The new library serves the District of Tierras Altas (population about 40,000, of whom 8,000 are under 15): Volcán, Cerro Punta, Cuesta de Piedra, Nueva California, and Paso Ancho. There are no other libraries in the district, or even in the schools. Books are out of reach for most people. A library makes reading possible and improves students’ prospects.</p>
<p>After three years of fundraising and rebuilding, Biblioteca San Benito opened on 30 June 2025. Because we still depend on volunteers, hours are limited. Recurring donations would let us hire staff and open six days a week.</p>
<p><a href="governance.html">Meet the board</a></p>""",
    )

    p = "../"
    pages["en/governance.html"] = page(
        "en/governance.html",
        "Governance — San Benito Library",
        "Board of the Foundation for Art and Culture of Tierras Altas.",
        "<h1>Current board members</h1>"
        + person(
            p,
            "tony-leung.jpg",
            "Anthony Tak On Leung",
            "Chairman, retired",
            "<p>Born and raised in Hong Kong; B.A. from the University of Wisconsin. Former business owner. Administration and Finance Officer for the International Organization for Migration in Manila. Volunteered with Refugee Concern, the Hong Chi Association, the Pam Baker Foundation, and chaired The Leprosy Project in Sichuan, China. Active Rotarian for over 30 years.</p>",
            "Anthony Leung, chairman",
        )
        + person(
            p,
            "linda-chang.jpg",
            "Linda Kristina Chang Quintero",
            "Vice president and legal representative, attorney",
            "<p>Founding member. Born in Panama City. Law degree from Metropolitan University of Panama; conciliator and mediator (Universidad Latina) with a specialty in commercial and immigration law. Partner at Magallan y Chang; legal adviser to the Chamber of Tourism, Commerce and Industry in Tierras Altas.</p>",
            "Linda Chang, vice president",
        )
        + person(
            p,
            "alan-baumbach.jpg",
            "Alan John Baumbach",
            "Treasurer, retired",
            "<p>Born in Colorado. B.S.B.A. from the University of Denver; CPA (Alaska) while at Arthur Young and Company. Active in low-income housing and medical projects in Central America and in the Osher Lifelong Learning Institute at the University of Denver.</p>",
            "Alan Baumbach",
        )
        + person(
            p,
            "laurie-leung.jpg",
            "Laurie Diane Lemmlie-Leung",
            "Secretary, retired",
            "<p>Founding member; also works with the fundraising committee. Born in the United States; bachelor’s degree from Cornell College. Peace Corps Volunteer in the Philippines; U.S. Refugee Program in Manila; KPMG in Hong Kong. In Volcán she volunteers with Tierras Altas Recicla.</p>",
            "Laurie Lemmlie-Leung, secretary",
        )
        + person(
            p,
            "chris-thomas.jpg",
            "Christine Bardolf Thomas",
            "Librarian, retired",
            "<p>Founding member. B.A. from Clemson University; M.Ed. from Framingham. Taught ESL, science, and biology in Costa Rica and was elementary librarian at an American international school for 23 years. Works with the Costa Rican Humanitarian Foundation and reviews for Wells Mountain Foundation. Has lived between Panama and Costa Rica for 42 years.</p>",
            "Chris Thomas, librarian",
        )
        + person(
            p,
            "chris-arias.jpg",
            "Chris Arias",
            "Spanish tutor",
            "<p>Founding member, fully bilingual. Born in Honduras. Degrees in food technology and senior banking management. Former president of AHIBA’s North Coast chapter and vice president of the Atlántida Chamber of Commerce. Board work with Adelante Foundation, RBC in Roatán, and HALA.</p>",
            "Chris Arias",
        )
        + person(
            p,
            "estela-ritter.jpg",
            "Estela Ritter Pangtay",
            "Third vocal, retired",
            "<p>Born in Panama. Architecture degree from the University of São Paulo. Urbanist and regional planner for the government of Panama; CAD operator in Canada. Active with Tierras Altas Recicla.</p>",
            "Estela Ritter",
        )
        + person(
            p,
            "rossana-tarantini.jpeg",
            "Rossana Saccucci Tarantini (Roxx)",
            "Treasurer, editor",
            "<p>Born in Canada, of Italian heritage. Degree in languages (French, Italian, and Spanish) from York University, Toronto. Certifications in accounting, facilities management, and editing. This is her first board role at a nonprofit foundation.</p>",
            "Rossana Saccucci Tarantini, treasurer",
        )
        + person(
            p,
            "nahomi-soto.jpg",
            "Nahomi Soto",
            "Advisor, engineering student",
            "<p>Born and raised in Panama City. Studies Administrative Industrial Engineering. Supports social media and helps promote library programs.</p>",
            "Nahomi Soto",
        )
        + """
<h2>Other members</h2>
<ul>
<li>Cheryl Roe Michel, retired</li>
<li>Stephanie Llean Charpentier Santamaría, architect</li>
<li>Miguel Eduardo Samudio Ledezma, civil service</li>
<li>Ana Iris Tribaldos Jarquin, administration</li>
</ul>
<h2>Former board members</h2>"""
    )

    pages["en/news-and-updates.html"] = page(
        "en/news-and-updates.html",
        "News and updates — San Benito Library",
        "News from San Benito Library.",
        """<h1>News and updates</h1>
<ul class="news">
<li><a href="volunteer-stories.html">Volunteer stories</a><br><span class="meta">15 February 2025</span></li>
<li><a href="thank-you-to-our-corporate-donors.html">Thank you to our corporate donors</a><br><span class="meta">15 January 2025</span></li>
<li><a href="renovation-progress-2024.html">Renovation progress</a><br><span class="meta">15 January 2025</span></li>
<li><a href="annual-reports.html">Annual report 2024</a><br><span class="meta">9 January 2025</span></li>
</ul>""",
    )

    pages["en/volunteer-stories.html"] = page(
        "en/volunteer-stories.html",
        "Volunteer stories — San Benito Library",
        "Jill Dubler on cataloguing books for the library.",
        """<h1>Volunteer stories</h1>
<p class="meta">15 February 2025</p>
<h2>Jill Dubler</h2>
<p>My husband and I arrived in Volcán about three years ago. Two years ago I began helping Biblioteca San Benito. I have done many of the jobs needed to restore books saved from the old library, but cataloguing is my real passion. I share this work with Ed Simmons.</p>
<figure class="figure">
<img src="../img/jill-dubler.jpg" alt="Volunteer Jill Dubler cataloguing books for San Benito Library">
<figcaption>Volunteer Jill Dubler</figcaption>
</figure>
<h2>Cataloguing</h2>
<p>Each book is entered into our system so it can be searched in several ways. I work at home, so my husband and I move boxes from the library “office.” I have had as many as 7–10 large boxes at once.</p>
<p>Four partner libraries let us use their databases. I first search by title, author, publisher, ISBN, and so on. If the book is there, we reuse some of that data and check it. The form includes ISBN, author, title, place and date of publication, publisher, pages, illustrations, and maps. We measure the book in centimetres and note series, language, a summary, awards, subjects, and the illustrator.</p>
<p>The second page is how we shelve it: Dewey Decimal class, fiction, juvenile, early reader, adolescent, reference, biography, barcode, and estimated replacement cost.</p>
<h2>What if the book is not in those libraries?</h2>
<p>We create the record from scratch. Many records have no cover photo, so we look on Google, Amazon, eBay, and elsewhere. One book can take 5 to 20 minutes.</p>
<h2>Spanish versus English</h2>
<p>Spanish books are seldom in the partner libraries, so they usually start from a blank form and we translate the record into both languages. People say children’s books help you learn a language. They are right!</p>
<p>We are going to have an amazing selection in Volcán’s new Biblioteca San Benito, and I am grateful to be part of it.</p>""",
    )

    pages["en/thank-you-to-our-corporate-donors.html"] = page(
        "en/thank-you-to-our-corporate-donors.html",
        "Thank you to our donors — San Benito Library",
        "Thanks to Grupo ENX, Naturgy, and Janson Coffee Farm for 2024 renovations.",
        """<h1>Thank you to our corporate donors</h1>
<p class="meta">31 January 2025</p>
<figure class="figure">
<img src="../img/enx-photo.jpg" alt="Tony Leung, Moisés Vega, Nery Esquivel, and Linda Chang">
<figcaption>From left: Tony Leung, Foundation president; Moisés Vega, CEO of Grupo ENX; Nery Esquivel, coordinator of social assistance for Chiriquí; and Linda Chang, Foundation vice president.</figcaption>
</figure>
<p>None of the <a href="renovation-progress-2024.html">2024 renovations</a> would have been possible without our donors. Heartfelt thanks to Moisés Vega of Grupo ENX; Javier Sánchez, regional manager of Naturgy; and Haydee Janson of Janson Coffee Farm, who also donated the toilet and safety bars for the accessible bathroom. We are grateful to Linda Chang for securing these gifts.</p>
<div class="logos"><img src="../img/enx-logo.jpg" alt="Grupo ENX logo"></div>
<figure class="figure">
<img src="../img/naturgy-signing.jpg" alt="Naturgy presenting a donation">
<figcaption>From left: Mymara Crespo Baiz, Naturgy director of communications; regional manager Javier Sánchez; and Tony Leung.</figcaption>
</figure>
<div class="logos"><img src="../img/naturgy-logo.jpg" alt="Naturgy logo"></div>
<figure class="figure">
<img src="../img/janson-family.jpg" alt="The Janson family with Foundation members">
<figcaption>From left: Zahida de Janson, Janeth Janson, Haydee and Carl Janson of Janson Coffee Farm, with Tony Leung, Laurie Lemmlie-Leung, and Linda Chang.</figcaption>
</figure>
<div class="logos"><img src="../img/janson-logo.png" alt="Janson Coffee Farm logo"></div>""",
    )

    pages["en/renovation-progress-2024.html"] = page(
        "en/renovation-progress-2024.html",
        "Renovation progress 2024 — San Benito Library",
        "Building improvements completed in 2024.",
        """<h1>Renovation progress 2024</h1>
<p class="meta">31 January 2025</p>
<p>Looking back on 2024, we are glad to share the progress we made together. Thanks to your generosity and that of our <a href="thank-you-to-our-corporate-donors.html">corporate donors</a>, we raised enough to begin much-needed renovations. These changes make a more welcoming, accessible, and useful space.</p>
<div class="gallery">
<img src="../img/reno-en-1.jpg" alt="Widened walkway around the building">
<img src="../img/reno-en-2.jpg" alt="Widened doorway between rooms">
<img src="../img/reno-en-3.jpg" alt="Roof repair">
<img src="../img/reno-en-4.jpg" alt="Electrical work">
<img src="../img/reno-en-5.jpg" alt="New ceiling">
<img src="../img/reno-en-6.jpg" alt="New glass entrance doors">
</div>""",
    )

    pages["en/annual-reports.html"] = page(
        "en/annual-reports.html",
        "Annual report 2024 — San Benito Library",
        "Fundraising, building work, books, and language classes in 2024.",
        """<h1>Annual report 2024</h1>
<p class="meta">9 January 2025</p>
<h2>Board of directors</h2>
<p>On 29 January 2023 the board elected:</p>
<ul>
<li>President: Tony Leung</li>
<li>Vice president: Linda Chang</li>
<li>Secretary: Laurie Lemmlie-Leung</li>
<li>Treasurer: Alan Baumbach</li>
<li>Fiscal: Cher Michel</li>
<li>Members: Stephanie, Gregorio Filis, Estela Ritter</li>
<li>Advisors: Ana Tribaldos, Miguel Samudio</li>
</ul>
<h2>Fundraising</h2>
<ul>
<li><strong>New Year’s Day food truck:</strong> Beth Harrison set up at Azel Ames’s community picnic. All proceeds went to the library.</li>
<li><strong>Community parties:</strong> Black and White Bash in August, Halloween in October, and an ugly-sweater Christmas party in December.</li>
<li><strong>“Be a Light” campaign:</strong> funded new lights in two days and inspired an anonymous monthly donor.</li>
<li><strong>Parada de las Flores:</strong> we showed the building work, rented the bathrooms, sold donated clothing, and gave out books.</li>
<li><strong>December bazaar:</strong> more than 30 vendors. Beth Harrison donated the food truck again; Lyn Bishop ran “BonBons for Books.” There was a classic-car display (Anyansi de Angel), a dog parade, storytime and crafts (Natalie Richie), face painting (Jenna Glasz), and balloon animals (Terry Newcombe).</li>
</ul>
<p>Thanks to Marianne Brown and The Quilt House for the quilt raffled in August, and to Alan Baumbach for the motorcycle raffled at the Christmas party.</p>
<p>We appreciate gifts from Moisés Vega (Grupo ENX), Javier Sánchez (Naturgy), and Haydee Janson (Janson Coffee Farm). The Janson family also donated a toilet and safety bars for the accessible bathroom. Linda Chang helped secure these contributions.</p>
<h2>Building improvements</h2>
<ul>
<li>Expanded the sidewalk around the building</li>
<li>Widened the doorway between the main rooms</li>
<li>Repaired the roof and installed new ceilings with lights and fans</li>
<li>Renovated both bathrooms; one is fully accessible thanks to the Janson family</li>
<li>New entrance with double glass doors, ready for the Christmas bazaar</li>
</ul>
<h2>Books</h2>
<p>Chris Thomas and volunteers catalogued more than 7,000 books for the opening.</p>
<h2>Language lessons</h2>
<p><strong>English.</strong> Natalie Richie relaunched classes in January for children (7–12), teens (13–18), and adults.</p>
<p><strong>Spanish.</strong> Low-cost classes with Arelis Mendoza grew from one mixed group into three levels.</p>
<p>This report summarizes the work of Fundación Arte y Cultura de Tierras Altas in 2024.</p>""",
    )

    for rel, html in pages.items():
        dest = docs / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        print("wrote", rel)

    (docs / "404.html").write_text(
        page(
            "index.html",
            "Página no encontrada — Biblioteca San Benito",
            "Página no encontrada.",
            """<h1>No encontramos esa página</h1>
<p>Vuelva al <a href="index.html">inicio</a> o al <a href="en.html">English home</a>.</p>""",
        ),
        encoding="utf-8",
    )
    print("wrote 404.html")

    (docs / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print("wrote robots.txt")

    (docs / "CNAME").write_text("bibliotecasanbenito.org\n", encoding="utf-8")
    print("wrote CNAME")


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    docs = root / "docs"
    write_pages(docs)
    print("done")

# Static page builder for the Wolf Den Electric concept. Run: python3 build.py
import json, os
BASE = 'https://wolf-den-electric-demo.vercel.app/'  # Vercel production URL
NEWDOMAIN = 'wolfdenelectricnc.com'  # PLACEHOLDER: unregistered when checked on 7 Oct 2026; Matt picks the real one
TEL, TEL_H = '+19195216412', '(919) 521&#8209;6412'
EMAIL = 'mjpapan@gmail.com'
TOWNS = ['Durham','Raleigh','Chapel Hill','Cary','Morrisville','Wake Forest','Apex','Hillsborough']
ORG = {"@context":"https://schema.org","@type":"Electrician","name":"Wolf Den Electric, LLC",
 "url":"https://"+NEWDOMAIN,"telephone":"+1-919-521-6412","email":EMAIL,
 "founder":{"@type":"Person","name":"Matthew Papanestor"},
 "address":{"@type":"PostalAddress","addressLocality":"Durham","addressRegion":"NC","postalCode":"27703","addressCountry":"US"},
 "openingHours":"Mo-Fr 09:00-17:00","areaServed":"Research Triangle, NC","foundingDate":"2021",
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"37"},
 "image":BASE+"img/matt-ladder-light.webp"}
FONTS = 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,500..800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap'
TRI = '<svg class="tri" viewBox="0 0 12 11" aria-hidden="true"><path d="M6 0 L12 11 H0 Z"/></svg>'
def K(t, cls=''): return f'<p class="kicker {cls}">{TRI}{t}</p>'
STARS = '<span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

def img(src, alt, sizes='100vw', eager=False, w=None, h=None, cls=''):
    small = src.replace('.webp','-800.webp')
    srcset = f' srcset="img/{small} 800w, img/{src} 1250w" sizes="{sizes}"' if os.path.exists('img/'+small) else ''
    dims = f' width="{w}" height="{h}"' if w else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="img/{src}"{srcset} alt="{alt}"{dims}{load}' + (f' class="{cls}"' if cls else '') + '>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Wolf Den Electric (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#19191b">
<link rel="preload" href="fonts/bricolage-grotesque-normal-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="fonts/literata-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="img/wolf-mark.webp" type="image/webp">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Wolf Den Electric site. Facts come from Google reviews, public records and Wolf Den&rsquo;s own archived site; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><img src="img/wolf-mark.webp" alt="" width="36" height="37"><span><b>Wolf Den</b><small>Electric, LLC</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--red" href="tel:{tel}"><span class="cl-full">Call {telh}</span><span class="cl-short">Call Matt</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot"><div class="wrap">
<div class="back">
 <div><p class="kicker kicker--red">{TRI}Back page</p><p class="bp-call">Call Matt.</p><a class="bp-num" href="tel:{TEL}">{TEL_H}</a><p class="bp-sub">Monday to Friday, 9am to 5pm. Durham, NC 27703. <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
 <ul class="bp-facts"><li>{TRI}<b>5.0</b> from 37 Google reviews</li><li>{TRI}NC electrical license <b>L.35950</b></li><li>{TRI}Veteran owned and operated</li><li>{TRI}Serving the Triangle since <b>2021</b></li></ul>
</div>
<div class="foot-grid">
 <div><h2>Inside</h2><ul><li><a href="services.html">Services</a></li><li><a href="services.html#porches">Porches and sunrooms</a></li><li><a href="reviews.html">Reviews</a></li><li><a href="about.html">About Matt</a></li><li><a href="contact.html">Get a quote</a></li></ul></div>
 <div class="foot-domain"><h2>About our web address</h2><p>Wolf Den no longer owns wolfdenelectric.com. The address now belongs to someone else (current registration July 2026), and links to it do not reach us. The new home is <b>{NEWDOMAIN}</b> <span class="ph-tag">placeholder</span>.</p></div>
</div>
<div class="foot-row"><span>Wolf Den Electric, LLC &middot; Durham, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('reviews.html','Reviews'),('about.html','About Matt'),('contact.html','Get a quote')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 62, (fn, len(t), t)
    assert 130 <= len(d) <= 165, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or ORG),fonts=FONTS,tel=TEL,telh=TEL_H) + body + FOOT)

EXA = 'https://exa.ai/library/place/1p9mtvs8q7t'
BZ = 'https://www.buildzoom.com/contractor/wolf-den-electric-llc'
# Google reviews as shown on the Exa place page (Google review data snapshot, Sep 2026). "..." = truncated at the source.
REV = [
 ('2025-11-12','Nov 2025','Google','If you are looking for a licensed electrician you can trust, you&rsquo;ve found it. Wolf Den provided very thorough electrical services while finding and correcting sloppy work left behind by the pervious electricians. It is a blessing to find someone who actually cares about providing safe electrical work done right the first time. The electrician was very knowledgeable about certain electrical codes that have changed over the years, and I was impressed by his ability and willingness to explain things. There was also no mess left behind...',None),
 ('2025-05-27','May 2025','Google','Matt is honest, strait forward, and prompt. He helped resolve our issue with minimal time and money requirements, and is a kind professional during the whole process. Highly recommend.',None),
 ('2025-03-21','Mar 2025','Google','I couldn&rsquo;t be happier with the service I received! Matt was professional, punctual, and extremely knowledgeable. He quickly diagnosed the issue, explained everything clearly, and completed the work efficiently with great attention to detail. The quality of work was top notch, and he left everything clean and tidy when he was done. If you&rsquo;re looking for a reliable electrician who gets the job done right the first time, I highly recommend Matt! Will definitely be using his services again in the future.',None),
 ('2025-01-14','Jan 2025','Google','Matt completed the electrical work in our sunroom which included multiple new interior outlets, a couple of indoor outlets and installation of exterior floodlights. Matt was professional, answered any questions we had and made sure we knew what work was being done. He was a pleasure to work with. I recommend Matt for your electrical needs.',None),
 ('2024-11-14','Nov 2024','Google','I highly recommend Matthew with Wolf Den Electric, LLC. He is very knowledgeable, professional and polite. Matthew completed a very thorough diagnostic to see why my doorbell wasn&rsquo;t ringing and my dishwasher wasn&rsquo;t working. We even visited with a neighbor to find out where the transformer powering the doorbell in my house is located. I am happy to report that Matthew completed the electrical repairs and the doorbell and dishwasher are both working.',None),
 ('2024-10-29','Oct 2024','BuildZoom','I strongly recommend Wolf Den Electrical for your electrical jobs. The owner, Matt Papanestor, always showed up on time and was courteous, respectful, and professional. He walked me through the process he would follow to complete the required job; explaining the alternative methods he could follow to complete each task and made recommendations on which method was the &ldquo;best&rdquo; and most cost effective. Once Matt started the job he kept me in loop every step of the way...','Charles S., Carolina Arbors'),
 ('2024-06-24','Jun 2024','Google','Matt was very responsive! He came out to give us a quote the day after I contacted him, and was here to do the work just a couple of days later. He ran lines to a new humidifier and sump pump in the crawl space and resolved a potentially hazardous situation on our scrern porch. He made sure everything was cleaned up before he left and was extremely courteous throughout. Would highly recommend him if you need any electrical work done!',None),
 ('2024-05-07','May 2024','Google','Matt was very responsive from my first inquiry and clearly communicated every step of each small project I had asked for. He answered all of my questions and prepared me for the complications that could crop up in each job, so it wasn&rsquo;t a surprise for me the day of his work. He and Vince were incredibly professional all day, cleaning up as they went, and even offered to help carry bags of potting soil...',None),
 ('2023-10-29','Oct 2023','Google','Matt fixed my electrical unit to the AC unit which had gone bad. And added outlets so he could hang my TV without any wires hanging down. He asked for the details of what I wanted to achieve and took numerous measurements to ensure he placed the outlets in the best location. Professional job, was on time and even cleaned up after himself by vacuuming the floor.',None),
]
def letter(i, cls=''):
    iso, d, src, q, who = REV[i]
    by = who or f'{src} review, 5 of 5'
    return f'<blockquote class="letter rv {cls}"><p>&ldquo;{q}&rdquo;</p><footer>{TRI}<span>{by}</span><time datetime="{iso}">{d}</time></footer></blockquote>'

SERV = [('Repairs and troubleshooting','Dead outlets, a doorbell that stopped ringing, a dishwasher with no power. One reviewer&rsquo;s doorbell and dishwasher both work again.'),
 ('Porch and sunroom electrical','Outlets, lighting and floodlights for screen porches closed in as three season rooms, glass rooms and new deck roofs. All on the permit record.'),
 ('Lighting and LED upgrades','New fixtures, recessed and LED lighting, indoor and outdoor.'),
 ('Wiring upgrades','Bring older wiring up to current code, and fix what the last electrician left behind.'),
 ('Backup generators','Generator hookups for homes and businesses so the power stays on in an outage.'),
 ('Ethernet for the home','Wired network runs for one room or the whole house.'),
 ('Insurance inspections','A licensed look at the electrical system when the insurer asks for one.'),
 ('Commercial and industrial','Energy efficient upgrades, maintenance and equipment installs for businesses and facilities.')]

# ---------- HOME ----------
page('index.html','Durham Electrician, Veteran Owned | Wolf Den Electric, LLC',
 'Wolf Den Electric is Matt Papanestor&#39;s licensed, veteran owned electrical shop in Durham. 5.0 from 37 Google reviews. Call (919) 521-6412 for a quote today.'.replace('&#39;',"'"), f'''
<section class="cover"><div class="wrap cover-grid">
 <p class="masthead" aria-hidden="true">Wolf Den</p>
 <div class="cover-copy">{K('Durham, NC &middot; Electrical contractor L.35950','kicker--red')}
  <h1>Durham&rsquo;s five star electrician is a guy named <span class="red">Matt.</span></h1>
  <p class="lede">Wolf Den Electric is Matthew Papanestor&rsquo;s licensed, veteran owned shop. Repairs, lighting, generators, home Ethernet, and the wiring for porch and sunroom builds across the Triangle since 2021.</p>
  <div class="cta"><a class="btn btn--red" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--ghost" href="contact.html">Get a quote <span aria-hidden="true">&rarr;</span></a></div></div>
 <figure class="cover-photo">{img('matt-ladder-light.webp','Matt Papanestor on a ladder, holding up a black barn light he is about to install',sizes='(max-width:900px) 100vw, 40vw',eager=True,w=1250,h=1562)}
  <ul class="coverlines"><li><b>5.0</b> 37 Google reviews</li><li><b>30</b> permitted jobs in 2025</li><li><b>Vet</b> owned and operated</li></ul></figure>
</div></section>

<aside class="notice" aria-labelledby="n-h"><div class="wrap notice-in"><p id="n-h" class="notice-h">{TRI}Heads up</p><p>Wolf Den no longer owns <b>wolfdenelectric.com</b>. If an old link sent you somewhere strange, that page is not us. This is the real Wolf Den, at <b>{NEWDOMAIN}</b> <span class="ph-tag">placeholder</span>.</p></div></aside>

<section class="contents" aria-labelledby="c-h"><div class="wrap contents-grid">
 <div class="rv">{K('In this issue')}<h2 id="c-h">Six jobs Matt takes on, <em>big and small.</em></h2></div>
 <ol class="toc">{''.join(f'<li class="rv"><a href="services.html#s{i+1}"><span class="toc-n">{i+1:02d}</span><span class="toc-t">{n}</span><span class="toc-d">{d}</span></a></li>' for i,(n,d) in enumerate(SERV[:6]))}</ol>
</div></section>

<section class="feature" id="porches" aria-labelledby="f-h"><div class="wrap feature-grid">
 <div class="feature-num rv"><span class="big">12</span><span>of 12</span><p>2025 jobs in BuildZoom&rsquo;s public permit sample were porch, deck roof or sunroom projects. Wolf Den is named on each.</p></div>
 <div class="feature-copy rv">{K('The feature','kicker--red')}<h2 id="f-h">Screen porch in March. <em>Three season room by summer.</em></h2>
 <p>Closing in a screen porch with glass is one of the most common jobs on Wolf Den&rsquo;s permit record. The permits read almost the same every time: &ldquo;enclose existing screen porch with glass and glass door to make 3 season room&hellip; and will install outlets to code.&rdquo; Wolf Den is named on these permits for the electrical work.</p>
 <p>One Google reviewer had the same job done: &ldquo;multiple new interior outlets&hellip; and installation of exterior floodlights.&rdquo;</p>
 <a class="btn btn--dark" href="services.html#porches">Porch and sunroom electrical</a></div>
</div></section>

<section class="letters" aria-labelledby="l-h"><div class="wrap">
 <div class="letters-head rv"><div>{K('Letters')}<h2 id="l-h">Thirty seven reviews. <em>A 5.0 average.</em></h2></div><a class="btn btn--dark" href="reviews.html">Read nine in full</a></div>
 <div class="letters-grid">{letter(0,'letter--lead')}{letter(1)}{letter(6)}</div>
</div></section>

<section class="profile" aria-labelledby="p-h"><div class="wrap profile-grid">
 <div class="rv">{K('Profile','kicker--red')}<h2 id="p-h">&ldquo;So you know you can sleep in your home safely.&rdquo;</h2>
 <p>That line is from Matt&rsquo;s own mission statement: &ldquo;To perform quality work at a fair price knowing that I have met all the standards that are required by the State of North Carolina so you know you can sleep in your home safely.&rdquo;</p>
 <a class="btn btn--ghost" href="about.html">About Matt</a></div>
 <dl class="stats rv"><div><dt>License</dt><dd>NC L.35950, active</dd></div><div><dt>Since</dt><dd>2021</dd></div><div><dt>Permitted projects</dt><dd>52, 2023 to 2026</dd></div><div><dt>Typical permit</dt><dd>about $22,500</dd></div></dl>
</div></section>''', ld=[ORG,bc(('Home',''))])

# ---------- SERVICES ----------
page('services.html','Electrical Services in Durham and Raleigh | Wolf Den Electric',
 'Repairs, porch and sunroom wiring, LED lighting, generators, home Ethernet and insurance inspections from Wolf Den Electric in Durham. Call Matt for a quote today.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Services</p>{K('Services','kicker--red')}<h1>Eight things Matt <em>gets called for.</em></h1>
<p class="lede">Taken from Wolf Den&rsquo;s own service list, plus the porch and sunroom work that fills the permit record.</p></div></section>
<div class="wrap svc">{''.join(f'<article id="s{i+1}" class="svc-item rv{" svc-item--wide" if i==1 else ""}"><span class="toc-n">{i+1:02d}</span><div><h2>{n}</h2><p>{d}</p></div></article>' for i,(n,d) in enumerate(SERV))}</div>
<section id="porches" class="wrap porch rv" aria-labelledby="po-h"><div class="porch-in">{K('Porches and sunrooms','kicker--red')}<h2 id="po-h">What the permits say.</h2>
<ul class="permits">{''.join(f'<li><span class="pd">{d}</span><span class="pw">{w}</span><span class="pv">{v}</span></li>' for d,w,v in [('Jul 2025','Durham 27703: glass room addition from an existing screen porch','$17,743'),('Apr 2025','North Raleigh 27612: screen porch closed in as a 3 season room, outlets to code','$45,062'),('Aug 2025','North Raleigh 27612: 12 by 13 sunroom, roof and deck addition','$22,526'),('Oct 2025','North Raleigh 27615: porch to 3 season room, deck rebuilt','$24,259'),('Aug 2025','North Raleigh 27613: porch to 3 season room, outlets to code','$34,980')])}</ul>
<p class="fine">Values are whole project permit valuations, not Wolf Den&rsquo;s share. Street addresses removed. Source: <a href="{BZ}" rel="noopener">BuildZoom</a>, from NC permit records.</p>
<p class="note"><strong>Placeholder:</strong> photos of two finished three season rooms, and the names of the sunroom builders Matt works with, if he wants them listed.</p></div></section>''', ld=[ORG,bc(('Home',''),('Services','services.html'))]+[{"@context":"https://schema.org","@type":"Service","name":n,"provider":{"@type":"Electrician","name":"Wolf Den Electric, LLC"},"areaServed":"Durham, NC"} for n,_ in SERV])

# ---------- REVIEWS ----------
page('reviews.html','5.0 Stars from 37 Google Reviews | Wolf Den Electric Durham',
 'Read what Triangle homeowners say about Matt Papanestor and Wolf Den Electric: 5.0 stars from 37 Google reviews, plus BuildZoom. Call (919) 521-6412 for a quote.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Reviews</p>{K('Letters','kicker--red')}<h1>Nine reviews. <em>Eight name Matt.</em></h1>
<p class="lede">Seven say Matt, one says Matthew, and one just says &ldquo;the electrician.&rdquo;</p></div></section>
<div class="wrap letters-wall">{''.join(letter(i) for i in range(len(REV)))}</div>
<section class="wrap sources rv"><h2>Where these come from</h2><p>Eight are Google reviews copied word for word from a September 2026 snapshot of Wolf Den&rsquo;s Google listing on the <a href="{EXA}" rel="noopener">Exa place page</a>, typos included. Three dots mark where the snapshot cuts a review short. Reviewer names were not in the snapshot. One is from Wolf Den&rsquo;s <a href="{BZ}" rel="noopener">BuildZoom profile</a>, signed by the reviewer.</p>
<p class="note"><strong>Not used:</strong> the three short testimonials on the old site (Jim S., Betty T., Traili Pub), because they can&rsquo;t be traced to a source. <strong>Placeholder:</strong> a live Google reviews feed once Matt approves it.</p></section>''', ld=[ORG,bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Matt Papanestor, Veteran Owned | Wolf Den Electric',
 'Meet Matthew Papanestor, owner of Wolf Den Electric: a veteran owned, licensed NC electrical contractor serving Durham and the Triangle since 2021. Call him today.', f'''
<section class="page-head page-head--dark"><div class="wrap about-head"><div class="rv"><p class="crumbs"><a href="index.html">Home</a> / About Matt</p>{K('Profile','kicker--red')}<h1>Licensed. Veteran owned. <em>Still the one on the ladder.</em></h1></div>
<figure class="about-photo rv">{img('matt-ladder-light.webp','Matt Papanestor installing a black barn light on a house in the Triangle',sizes='(max-width:900px) 100vw, 36vw',w=1250,h=1562)}<figcaption>Matt, from the old wolfdenelectric.com, via the Internet Archive</figcaption></figure></div></section>
<div class="wrap about">
<section class="about-copy rv"><p class="dropcap">Wolf Den Electric, LLC is Matthew Papanestor&rsquo;s electrical contracting company in Durham. It is veteran owned and operated, holds North Carolina electrical contractor license L.35950, and has served the Triangle since 2021.</p>
<p>Reviewers describe the same habits: Matt gives the quote quickly, explains the options and which one he&rsquo;d pick, and cleans up before he leaves. One reviewer mentions Vince on the crew.</p>
<blockquote class="mission"><p>&ldquo;To perform quality work at a fair price knowing that I have met all the standards that are required by the State of North Carolina so you know you can sleep in your home safely.&rdquo;</p><footer>{TRI}Wolf Den&rsquo;s mission statement</footer></blockquote>
<p class="note"><strong>Placeholder:</strong> Matt&rsquo;s branch of service, how he got into the trade, and why &ldquo;Wolf Den&rdquo;. None of that is on the public record, so none of it is invented here.</p></section>
<aside class="about-side rv"><h2>Why licensed matters</h2><p>Matt&rsquo;s old About page quoted the NC State Board of Examiners of Electrical Contractors: the average NC electrical contractor is 56, and of about 13,330 licensees, only 220 are 30 or younger.</p><p class="fine">TODO-VERIFY: figures as quoted on the old site in 2023; confirm with the Board before launch.</p>
<h2>Who Matt has worked for</h2><ul class="clients">{''.join(f'<li>{TRI}{c}</li>' for c in ['Fendol Farms','Trali Irish Pub','Block &amp; Associates Realty','iWatch Security','Norwood Gardens','Pool Professionals'])}</ul><p class="fine">Listed on the old wolfdenelectric.com in 2023 and 2024. Confirm each before launch.</p></aside>
</div>''', ld=[ORG,bc(('Home',''),('About Matt','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Get an Electrical Quote in Durham and Raleigh | Wolf Den',
 'Ask Matt Papanestor for an electrical quote in Durham, Raleigh, Chapel Hill or Cary. Call (919) 521-6412, Monday to Friday 9 to 5, or send the short form here.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Get a quote</p>{K('Get a quote','kicker--red')}<h1>Tell Matt <em>what&rsquo;s not working.</em></h1><p class="lede">Calling is fastest: {TEL_H}, Monday to Friday, 9am to 5pm.</p></div></section>
<div class="wrap est-grid">
<form id="qform" class="rv" novalidate>
<fieldset><legend>What kind of job?</legend><div class="chips-in">{''.join(f'<label><input type="checkbox" name="need" value="{k}"> {k}</label>' for k in ['Something stopped working','Porch or sunroom','Lighting','Generator','Ethernet','Insurance inspection','Business','Not sure'])}</div></fieldset>
<div class="two"><div class="field"><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div><div class="field"><label for="p">Phone</label><input id="p" name="tel" type="tel" autocomplete="tel" required></div></div>
<div class="two"><div class="field"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email"></div><div class="field"><label for="t">Town</label><select id="t" name="town">{''.join(f'<option>{t}</option>' for t in TOWNS)}<option>Somewhere else</option></select></div></div>
<div class="field"><label for="m">What&rsquo;s going on?</label><textarea id="m" name="msg" rows="5"></textarea></div>
<button class="btn btn--red" type="submit">Send to Matt <span aria-hidden="true">&rarr;</span></button>
<p class="note" id="qmsg" role="status">Demo form. Nothing is sent.</p></form>
<aside class="rv"><div class="card"><p class="kicker kicker--red">{TRI}Direct</p><a class="bp-num" href="tel:{TEL}">{TEL_H}</a><p>Mon to Fri, 9am to 5pm<br>Durham, NC 27703<br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="fine">Service area towns are a placeholder. The old site said &ldquo;the Triangle&rdquo;; permits show Durham, Raleigh and one job in Pikeville.</p></div></aside>
</div>''', ld=[ORG,bc(('Home',''),('Get a quote','contact.html'))])

page('404.html','Page Not Found | Wolf Den Electric, Durham North Carolina',
 'That page is not in the den. Head back to the Wolf Den Electric home page or call Matt Papanestor at (919) 521-6412 for a quote on your electrical work today.',
 f'<section class="wrap nf">{K("404","kicker--red")}<h1>Nothing in <em>this den.</em></h1><p style="margin-top:28px"><a class="btn btn--red" href="index.html">Back to the home page</a></p></section>')
print('built')

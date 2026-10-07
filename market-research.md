# Market research: electrician sites, for the Wolf Den Electric concept

## How this was done
- Researched 7 October 2026. This reuses the ten electrician sites studied for the Triple Crown concept (Mister Sparky, Mr. Electric and eight Triangle shops) and adds three that show up on "electrician Durham NC": Marsigli Electric, All Wired Up NC (its Durham page) and SKK Electric.
- Lighthouse 12, mobile, one run per page. Single runs are noisy, so treat the numbers as rough. No traffic numbers (Similarweb and Semrush need logins).
- Screenshots of the three Durham sites are in `research/`. The other ten are in the Triple Crown repo's `research/` folder.

## Lighthouse, mobile
| Site | Who | Perf | A11y | Best pr. | SEO | LCP | Weight |
|---|---|---|---|---|---|---|---|
| allwiredupnc.com/durham | Family owned, Wake Forest, has a Durham page | 70 | 95 | 75 | 92 | 4.8 s | 0.8 MB |
| marsiglielectric.com | Durham, license #36111 in the header | 68 | 93 | 100 | 100 | 6.8 s | 1.0 MB |
| skkelectric.com | Durham, 4.9 from 149 Google reviews | 58 | 91 | 93 | 100 | 10.1 s | 9.1 MB |
| bushcrowelectric.com | Raleigh, best of the full set | 81 | 100 | 93 | 100 | 3.8 s | 0.6 MB |
| powermasterelectric.com | Triangle, worst of the full set | 43 | 85 | 75 | 100 | 79.6 s | 23.7 MB |
| **wolfdenelectric.com** | **Client** | n/a | n/a | n/a | n/a | n/a | **Not Wolf Den's site any more** |

Wolf Den has no site to score. The domain on its Google listing now belongs to someone else (see below). Every Durham competitor above at least loads a real page.

## What happened to wolfdenelectric.com (checked without visiting it)
- **Registry record (RDAP, Verisign):** wolfdenelectric.com was registered on 2026-07-20 at Porkbun, expires 2027-07-20, Porkbun nameservers. DNS (via Google public DNS) points to 207.207.210.23, .36 and .50.
- **Internet Archive:** Wolf Den's own WordPress site (Astra and Elementor, "Powered by GoAxell.com") is archived from July 2023 to December 2024. By November 2025 the archive shows a different, much smaller page titled "Professional Electrical Service | Licensed & Insured". I did not open that page.
- **Job finder's check (saved, not repeated):** the domain answered with a "Checking your browser" gate and a 302 redirect to affiliate and spam pages (technicalaffiliate.com, electrician.yourhelper.org).
- **Google listing:** still links to https://wolfdenelectric.com/about-us/. Anyone who taps "Website" on Matt's Google profile ends up on someone else's affiliate page.
- **Possible new domains:** wolfdenelectricnc.com, wolfdenelectricllc.com, wolfdenelectrical.com, wolfdenelectricdurham.com and wolfdenelectric.net all returned "not found" from the registry on 7 Oct 2026, so they looked unregistered. Nothing was registered. The demo uses wolfdenelectricnc.com as a labeled placeholder.

## What the old site got wrong (from the archived copies)
- Template text never replaced: the About page says "located in [city, state], and serving [service area]"; the FAQ page shows a South Dakota address (36-B W 1st Ave, Miller, SD), "info@domain.com" and "+1-800-123-4567"; three home page cards still read "It elit tellus, luctus nec ullamcorper mattis" (lorem ipsum).
- The FAQ says "we offer emergency electrical services 24/7", while Google lists hours of Monday to Friday, 9 to 5. Do not repeat the 24/7 claim without Matt confirming it.
- The good parts worth keeping: the photo of Matt on a ladder with a barn light, "Veteran Owned and Operated", the license number, "Serving the Triangle since 2021", and a mission statement in Matt's own voice.

## Patterns from the strongest electrician sites (full set of 13)
1. **Phone first.** Tap to call in the header and the hero. Mobile users calling an electrician want the number, not a form.
2. **License number and review count with a source**, near the top. Marsigli opens with "LICENSED NORTH CAROLINA ELECTRICIAN, LICENSE #36111". ARC and Electric All Pro show their Google counts and license numbers in the hero.
3. **Owner in first person.** Electric All Pro's founder note and ARC's origin story do more than any "Why choose us" grid.
4. **A niche gets its own page.** All Wired Up NC has a "Home Addition and Room Addition Electrical Wiring" page and a "Shed and Workshop Wiring" page. PowerMaster built a whole site around generators.
5. **The look is converging** on dark navy or black with yellow or lime and a lightning bolt.

## Wolf Den's actual niche
BuildZoom's public sample of Wolf Den's 2025 permits lists 12 addresses, and all 12 are porch, deck roof or sunroom jobs, most of them "enclose existing screen porch with glass and glass door to make 3 season room unconditioned space and will install outlets to code". 19 of Wolf Den's 49 electrical projects are tagged as home additions. No Durham competitor in this set has a page for porch and sunroom electrical. That is the hook.

## What I built
| Pattern | In the concept |
|---|---|
| Phone first | "Call Matt" in the header on phones, the number on desktop, again in the hero and as the footer headline. |
| License and reviews with a source | L.35950 in the hero kicker; 5.0 from 37 Google reviews and 30 permitted jobs in 2025 as cover lines on the photo. |
| Owner in first person | The cover headline is about Matt; the profile section quotes his own mission statement. |
| A niche page | "Screen porch in March. Three season room by summer." on the home page, plus a permits table on the services page. |
| Different look | A magazine cover in Wolf Den's own red and charcoal, with Matt's real photo. No lightning bolts. |
| The domain problem | A red "Heads up" strip on the home page and a footer note telling visitors that wolfdenelectric.com is no longer Wolf Den's. |

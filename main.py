import yaml
import os

data = {}
content = {}

for i in os.listdir("_data/"):
    with open(f"_data/{i}", 'r', encoding="utf-8") as file:
        data[i] = yaml.safe_load(file)

for i in os.listdir("_includes/"):
    with open(f"_includes/{i}", "r", encoding="utf-8") as file:
        content[i] = file.read()

homed = data["homesection.yml"]
configd = data["_config.yml"]
sec1d = data["section1.yml"]
sec2d = data["section2.yml"]
sec3d = data["section3.yml"]
sec4d = data["section4.yml"]
sec5d = data["section5.yml"]
sec6d = data["section6.yml"]

home = content["lander.html"]
sec1 = content["section1.html"]
sec2 = content["section2.html"]
sec3 = content["section3.html"]
sec4 = content["section4.html"]
sec5 = content["section5.html"]
sec6 = content["section6.html"]
cont = content["contact.html"]


with open("_layout/home.html", "r") as file:
    index = file.read()


index = index.replace("{{title}}", configd["title"])
index = index.replace("{{favicon}}", configd["favicon"])

style = """
	<style>
		.social-icons li:not(:last-child) {margin-right: 1.5rem;}
		.social-icons li a {font-size: 21px;}
		{{colors}}
	</style>
"""
colors = ""
for i in homed["socialsites"]:
    a = "color: #{} !important;".format(i["color"])
    colors +=".social-icons li:nth-child({s1}) ".format(s1=i["position"]) + "a:hover{" + a + "}\n\t\t"

style = style.replace("{{colors}}", colors[:-3])
index = index.replace("{{socialsitesstyle}}", style)
with open("_includes/preloader.html", "r") as file:
    preloader = file.read()
index = index.replace("{{preloader.html}}", preloader)


home = home.replace("{{avatar_scale}}",str(homed["avatar_scale"]))
home = home.replace("{{avatar}}",homed["avatar"])
home = home.replace("{{name}}",configd["name"])
home = home.replace("{{whoami}}", ",".join(homed["whoami"]))

socialsites = ""
for i in homed["socialsites"]:
    socialsites += "<li class=\"list-inline-item\"><a href=\"" + i["link"] + "\">" + f"<i class=\"fab fa-"+ i["site"] + "\"></i></a></li>"

home = home.replace("{{socialsites}}", socialsites)

button = f"""<div class="mt-4">
                <a href="{homed["btn"]["link"]}" target="_blank" class="btn btn-default">{homed["btn"]["text"]}</a>
            </div>"""

home = home.replace("{{button}}", button)

parallax = """<div class="parallax" data-relative-input="true">
{{something}}
        </div>"""
something = ""
for i in homed["parallax"]:
    something += f"<img src=\"" + str(i["img"]) + "\" alt=\"mm\" width=\"" + str(i["scale"]) + "\" height=\"" + str(i["scale"]) + "\" data-depth= \"" + str(i["depth"]) + "\" class=\"layer p" + str(i["position"]) +"\">"

home = home.replace("{{parallax}}", parallax.replace("{{something}}", something))
index = index.replace("{{homesection.html}}", home)
maind = data["main.yml"]
sec1 = sec1.replace("{{main.section1.title}}", maind["section1"]["title"])
sec1 = sec1.replace("{{section1.Intro.avatar}}", sec1d["Intro"]["avatar"])
sec1 = sec1.replace("{{site.title}}", configd["title"])
sec1 = sec1.replace("{{section1.Intro.text}}", sec1d["Intro"]["text"])
sec1 = sec1.replace("{{section1.btn.text}}", sec1d["btn"]["text"])
sec1 = sec1.replace("{{section1.btn.link}}", sec1d["btn"]["link"])

skill = """
 <div class="skill-item">
                                <div class="skill-info clearfix">
                                    <h4 class="float-left mb-3 mt-0">{}</h4>
                                    <span class="float-right">{}</span>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar data-background" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow={} data-color=#{}>
                                    </div>
                                </div>
                                <div class="spacer" data-height="20"></div>
                            </div>
"""
skills = ""
for i in sec1d["skills"]:
    skills += skill.format(i["skill"], i["percentage"], i["percentage"], i["color"])

sec1 = sec1.replace("{{section1.skills}}", skills)

stat = """
<div class="col-md-3 col-sm-6">
                <!-- fact item -->
                <div class="fact-item">
                    <span style="color: #454360;" class="icon icon-{}"></span>
                    <div class="details">
                        <h3 class="mb-0 mt-0 number"><em class="count">{}</em></h3>
                        <p class="mb-0">{}</p>
                    </div>
                </div>
                <div class="spacer d-md-none d-lg-none" data-height="30"></div>
            </div>
"""
stats = ""

for i in sec1d["stats"]:
    stats += stat.format(i["icon"], i["count"], i["title"])
sec1 = sec1.replace("{{section1.stats}}", stats)

index = index.replace("{{section1.html}}", sec1)


skill = """
<div class="col-md-4" data-wow-delay="{}s">
                <!-- service box -->
                <div class="service-box rounded data-background padding-30 text-center shadow-yellow" data-color="#{}">
                    <img src="{}" alt="{}" />
                    <h3 style="color: #{};" class="mb-3 mt-0">{}</h3>
                    <p style="color: #{};" class="mb-0">{}</p>
                </div>
                <div class="spacer d-md-none d-lg-none" data-height="30"></div>
            </div>
"""

skills = ""
for i in sec2d["skills"]:
    skills += skill.format(i["time_delay"],i["tile_color"],i["img"],i["title"], i["title_color"], i["title"], i["text_color"], i["text"])

sec2 = sec2.replace("{{main.section2.title}}", maind["section2"]["title"])
sec2 = sec2.replace("{{section2.skills}}", skills)
sec2 = sec2.replace("{{section2.btn.link}}", sec2d["btn"]["link"])
sec2 = sec2.replace("{{section2.btn.linktext}}", sec2d["btn"]["linktext"])
sec2 = sec2.replace("{{section2.btn.text}}", sec2d["btn"]["text"])

index = index.replace("{{section2.html}}", sec2)

sec3 = sec3.replace("{{main.section3.title}}", maind["section3"]["title"])
edu = """
<div class="timeline-container wow fadeInUp" data-wow-delay="{}s">
                        <div class="content">
                            <span class="time">{}</span>
                            <h3 class="title">{}</h3>
                            <p>{}<br> <a href="{}">{}</a></p>
                        </div>
                    </div>
"""
edus = ""
for i in sec3d["Education"]:
    edus += edu.format(i["time_delay"], i["period"], i["title"], i["subject"], i["link"], i["college"])
sec3 = sec3.replace("{{section3.Education}}", edus)



work = """
<div class="timeline-container wow fadeInUp" data-wow-delay="{}s">
                        <div class="content">
                            <span class="time">{}</span>
                            <h3 class="title">{}</h3>
                            <p>{}</p>
                        </div>
                    </div>
"""

works = ""
for i in sec3d["Work"]:
    works += work.format(i["time_delay"], i["period"], i["title"], i["text"])

sec3 = sec3.replace("{{section3.Work}}", works)

index = index.replace("{{section3.html}}", sec3)


sec4 = sec4.replace("{{main.section4.title}}", maind["section4"]["title"])

cat = """<li class="list-inline-item" data-filter=".{}">{}</li>"""

cats = ""

for i in sec4d["categories"]:
    cats += cat.format(i, i)

sec4 = sec4.replace("{{section4.categories}}", cats)

work = """
<div class="col-md-4 col-sm-6 grid-item {{category}}">
                <a href="{}" target="_blank">
                    <div class="portfolio-item rounded shadow-dark">
                        <div class="details">
                            <span class="term">{{category}}</span>
                            <h4 class="title">{}</h4>
                            <span class="more-button"><i class="icon-link"></i></span>
                        </div>
                        <div class="thumb">
                            <img src="{}" alt="Portfolio-title" />
                            <div class="mask"></div>
                        </div>
                    </div>
                </a>
            </div>"""
works = ""
for i in sec4d["work"]:
    works += work.replace("{{category}}", ",".join(i["category"])).format(i["link"],i["title"], i["img"] )

sec4 = sec4.replace("{{section4.work}}", works)
index = index.replace("{{section4.html}}", sec4)

sec5 = sec5.replace("{{main.section5.title}}", maind["section5"]["title"])

review = """
<div class="testimonial-item text-center mx-auto">
                <div class="thumb mb-3 mx-auto">
                    <img src="{}" alt="customer-name" class="boximg" />
                </div>
                <h4 class="mt-3 mb-0">{}</h4>
                <span class="subtitle">{}</span>
                <div class="bg-white padding-30 shadow-dark rounded triangle-top position-relative mt-4">
                    <p class="mb-0">{}</p>
                </div>
            </div>
"""

reviews = ""

for i in sec5d["Reviews"]:
    reviews += review.format(i["img"], i["name"], i["designation"], i["text"])

sec5 = sec5.replace("{{section5.Reviews}}", reviews)

icon = """
<div class="col-md-3 col-6">
                <!-- client item -->
                <div class="client-item">
                    <div class="inner">
                        <img src="{}" width="100em" height="100em" alt="" />
                    </div>
                </div>
            </div>
"""

icons = ""
for i in sec5d["Icons"]:
    icons+=icon.format(i)
sec5 = sec5.replace("{{section5.Icons}}", icons)

index = index.replace("{{section5.html}}", sec5)

sec6 = sec6.replace("{{main.section6.title}}", maind["section6"]["title"])
post = """
<div class="col-md-4">
                <!-- blog item -->
                <div class="blog-item rounded bg-white shadow-dark wow fadeIn">
                    <div class="thumb">
                        <a href="{}">
                            <span class="category">{}</span>
                        </a>
                        <a href="{}">
                            <img src="{}" alt="blog-title"/>
                        </a>
                    </div>
                    <div class="details">
                        <h4 class="my-0 title"><a href="{}">{}</a></h4>
                        <ul class="list-inline meta mb-0 mt-2">
                            <li class="list-inline-item">{}</li>
                            <li class="list-inline-item">{}</li>
                        </ul>
                    </div>
                </div>
            </div>
"""

posts = ""
for i in sec6d["posts"]:
    posts += post.format(i["link"], i["type"], i["link"], i["img"], i["link"], i["title"], i["date"], i["author"])
sec6 = sec6.replace("{{section6.posts}}", posts)

index = index.replace("{{section6.html}}", sec6)


cont = cont.replace("{{main.contact.title}}", maind["contact"]["title"])
cont = cont.replace("{{main.contact.subtitle}}", maind["contact"]["subtitle"])

index = index.replace("{{contact.html}}", cont)
with open("index.html", "w", encoding="utf-8") as file:
    file.write(index)

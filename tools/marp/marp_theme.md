---
theme: gaia
_class: lead
paginate: false
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')


```json
{
    "folders": [
        {
            "path": "."
        }
    ],
    "settings": {
        "markdown.marp.themes": [
            "./style/socrates.css"
            "./style/plato.css"
            "./style/leibniz.css"
            "./style/kant.css"
            "./style/hegel.css"
            "./style/freud.css"
            "./style/heidegger.css"
            "./style/jobs.css"
            "./style/schema.css"
            "./style/structure.css"
        ]
    }
}
```

## You might as well use my themes directly from github using the url, just like depicted below:

```json
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"markdown.marp.themes": [
			"https://cunhapaulo.github.io/style/freud.css"
			"https://cunhapaulo.github.io/style/hegel.css"
			"https://cunhapaulo.github.io/style/heidegger.css"
			"https://cunhapaulo.github.io/style/kant.css"
			"https://cunhapaulo.github.io/style/leibniz.css"
			"https://cunhapaulo.github.io/style/plato.css"
			"https://cunhapaulo.github.io/style/schema.css"
			"https://cunhapaulo.github.io/style/simple.css"
			"https://cunhapaulo.github.io/style/socrates.css"
			"https://cunhapaulo.github.io/style/structure.css"
		]
	}
}
```
<style>

   .cite-author {
      text-align        : right;
   }
   .cite-author:after {
      color             : orangered;
      font-size         : 125%;
      /* font-style        : italic; */
      font-weight       : bold;
      font-family       : Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
      padding-right     : 130px;
   }
   .cite-author[data-text]:after {
      content           : " - "attr(data-text) " - ";      
   }

   .cite-author p {
      padding-bottom : 40px
   }

</style>


---

![bg left:40% 80%](https://marp.app/assets/marp.svg)

# **Marp**

Markdown Presentation Ecosystem

https://marp.app/

---

# How to write slides

Split pages by horizontal ruler (`---`). It's very simple! :satisfied:

```markdown

# Slide 1

foobar

---

# Slide 2

foobar
```

---

# How to insert plantuml file into Markdown

## For Gitlab
!includeurl https://plantuml:SecretPassword@git.example.com/gitlab/project/-/raw/master/File_to_import.puml

## For Github
![alternative text](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/plantuml/plantuml-server/master/src/main/webapp/resource/test2diagrams.txt)

THe marp export pdf does not show the above image. 

Alternatively, have a on-save automation for plantuml to save an .svg file. Then always reference the .svg file.

This way, the marp export to PDF will also work.

# Adding header and footer



---
theme: gaia
_class: lead
paginate: false
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
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

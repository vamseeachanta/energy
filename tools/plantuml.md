## Introduction
The ability to draw ascii drawings and help project participants. Drawings and diagrams can benefit developers, architects, project sponsors etc. PlantUML is a component that allows to quickly write and generate drawings and diagrams using basic ascii code. 

This document describes the following:
- A method to prepare drawings to steamline project work and development etc.
- How to write source in asciidoc + PlantUML; 
- How to get rendered in HTML + PNG on github markdown pages.

## Summary

The advantages to ascii code based drawings or diagrams such as plantuml are:
- Ability to quickly generate drawings from ground up
- Ability to quickly edit to update/correct drawings to keep sync with code
- Integrate drawings in markdown files using general CI/CD practices

Best practices:
- Always save each plantuml drawing as individual files
  - helps in easy CI-CD
  - facilitates easy use of templates
  - facilitates easy use existing flowcharts for new flowchart



[https://blog.anoff.io/2018-07-31-diagrams-with-plantuml/](https://blog.anoff.io/2018-07-31-diagrams-with-plantuml/)
[https://stackoverflow.com/questions/32203610/how-to-integrate-uml-diagrams-into-gitlab-or-github/32771815#32771815](https://stackoverflow.com/questions/32203610/how-to-integrate-uml-diagrams-into-gitlab-or-github/32771815#32771815)

Good starting examples (and reference links) are given below:

[https://real-world-plantuml.com/](https://real-world-plantuml.com/)

[https://paircoders.com/2019/06/05/create-sequence-diagrams-with-plantuml/](https://paircoders.com/2019/06/05/create-sequence-diagrams-with-plantuml/)

[https://forum.plantuml.net/9735/participant-text-overflows-from-the-right-of-its-box](https://forum.plantuml.net/9735/participant-text-overflows-from-the-right-of-its-box)

## Installation

Install plantuml using the below command:
  - choco install plantuml
  - troubleshooting:
    - ensure chocolatey is installed on the computer. 
    - https://chocolatey.org/install

## Rendering in an IDE

An plantuml extension or utility can be used to render in an IDE. Instructions for IDE(s) is given in this section.
### VS Code

- Install the extension 'PlantUML' in VS code
  - [https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
- Set up custom location to save files

- Exporting images to other formats using plantuml extension
  - <img src="https://github.com/vamseeachanta/energy/blob/master/tools/puml/export_diagram.png" width="200" height="300" />
  - [ ![](<img src="https://github.com/vamseeachanta/energy/blob/master/tools/puml/export_diagram.png" width="200" height="300" />) ]("tools/puml/export_diagram.png")
  - Click option to 'Export Workspace Diagrams' 
  - choose the format to save diagrams


Typical errors and how to resolve them:
- Error: Diagram unnamed. Try "@startuml name"
  - Resolution: 

## Github Integration

Github integration will greatly help streamline implementation. A method to implement a stand-alone file inline with a markdown file is given in this section.

- Create an individual plantuml file. An example plantuml file saved in location [https://github.com/vamseeachanta/energy/blob/master/tools/puml/wbs.puml](https://github.com/vamseeachanta/energy/blob/master/tools/puml/wbs.puml) with below code:

<pre><code>
'''
@startwbs
* Project Organization
** Procure project work
*** Perosn 1
*** Perosn 2
** US Resources
*** Technical Project Manager
*** Doc Controller/BA
** Project Resources
*** Project manager (scrum master/planning/release train)
*** 2 Fullstack developers
*** 1 Devops/Automation
*** 1 PowerBI + SQL
*** 1 Scrum master + release train
@endwbs
'''
</code></pre>

- The below format is defined in markdown (.md) file:
  - http://www.plantuml.com/plantuml/proxy?cache=no&src=(raw github plantuml link)
- Key things to note are:
  - raw github file link can be obtained from actual githublink file link
  - cache=no will allow to seamlessly update image along with code
- Example format is below of a file in repo is below
  - http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/vamseeachanta/energy/master/tools/puml/wbs.puml

- Exact code used in markdown is:
<pre><code>
![example UML](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/vamseeachanta/energy/master/tools/puml/wbs.puml)
</code></pre>

- The rendering of the example file in github is:

![example UML](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/vamseeachanta/energy/master/tools/puml/wbs.puml)


### Other IDEs

For developers, getting it to work in in other IDEs may be difficult.


## References

- [https://plantuml.com/](https://plantuml.com/)

- [https://plantuml.com/sitemap-language-specification](https://plantuml.com/sitemap-language-specification)

- [https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

- [https://www.reddit.com/r/git/comments/j6zaji/plant_uml_alternative_is_there_a_good_tool_for/](https://www.reddit.com/r/git/comments/j6zaji/plant_uml_alternative_is_there_a_good_tool_for/)

- [https://www.codeproject.com/Articles/1278703/UML-Made-Easy-with-PlantUML-VS-Code](https://www.codeproject.com/Articles/1278703/UML-Made-Easy-with-PlantUML-VS-Code)

- [https://www.linux-magazine.com/Issues/2020/235/PlantUML-Diagrams/(offset)/3](https://www.linux-magazine.com/Issues/2020/235/PlantUML-Diagrams/(offset)/3)

- [https://github.github.com/gfm/](https://github.github.com/gfm/)
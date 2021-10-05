## Introduction
PlantUML is top priority. The ability to draw ascii drawings and help project participants (from Developers to architects to project sponsors alike) immensly. 

This document describes the following:
- How to prepare drawings to steamline project work and development etc.
- How to write source in asciidoc + PlantUML; How to get rendered in HTML + SVG/PNG nicely.

## Summary

Best practices:
- Always save each plantuml drawing as individual files
  - helps in easy CI-CD
  - facilitates easy use of templates
  - facilitates easy reuse of existing flowcharts

- If included with code practice are following:

- If indivdual files are required for quick integration:
 

'''plantuml
@startuml component
actor client
node app
database db

db -> app
app -> client
@enduml
'''

[https://blog.anoff.io/2018-07-31-diagrams-with-plantuml/](https://blog.anoff.io/2018-07-31-diagrams-with-plantuml/)
[https://stackoverflow.com/questions/32203610/how-to-integrate-uml-diagrams-into-gitlab-or-github/32771815#32771815](https://stackoverflow.com/questions/32203610/how-to-integrate-uml-diagrams-into-gitlab-or-github/32771815#32771815)

## Rendering in an IDE

### VS Code

- Install the extension 'PlantUML' in VS code
  - [https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
- Set up custom location to save files

- Exporting images to other formats using plantuml extension
  - ![Right click on individual plantuml file](tools/puml/export_diagram.png)
  - Click option to 'Export Workspace Diagrams' 
  - choose the format to save diagrams


### Other IDEs

Difficult to get it working in other IDEs


## References

- [https://plantuml.com/](https://plantuml.com/)

- [https://plantuml.com/sitemap-language-specification](https://plantuml.com/sitemap-language-specification)

- [https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

- [https://www.reddit.com/r/git/comments/j6zaji/plant_uml_alternative_is_there_a_good_tool_for/](https://www.reddit.com/r/git/comments/j6zaji/plant_uml_alternative_is_there_a_good_tool_for/)
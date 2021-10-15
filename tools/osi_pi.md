## Introduction

OSIsoft makes the PI System, the market-leading data management platform for industrial operations, that helps you move from complexity to simplicity.

https://techsupport.osisoft.com/Products/Layered%20Products/PI-AF/Overview


## Summary


### PI AF
PI Asset Framework (PI AF) is a single repository for asset-centric models, hierarchies, objects, and equipment. It integrates, contextualizes, refines, references, and further analyzes data from multiple sources, including one or more PI Data Archives and non-PI sources such as external relational databases. Together, these metadata and time series data provide a detailed description of equipment or assets.

PI AF can expose this rich data to PI System components, such as PI VIsion, PI DataLink, or PI ProcessBook, where it can be used to build displays, run calculations, deliver important information, and more. PI Asset Framework can also expose these data to non-PI systems via a rich set of data access products. PI AF also includes a number of basic and advanced search capabilities to help users sift through static and real time information. The following comparison table lists the capabilities of current and earlier versions of PI AF.

### PI System components

- PI VIsion
- PI DataLink
- PI ProcessBook

### PI System components

- PI AF SDK is the foundational .NET-based software development kit for interacting with asset metadata and time series data stored in the PI Asset Framework. It is available from PI Developers Club* (formerly known as vCampus). For more information, refer to PI AF SDK Homepage.
- PI Server 2018 introduces a single setup kit that includes PI Data Archive, PI Asset Framework with Asset Analytics and Notifications, PI Web API, PI System Directory, and all dependent components. Users can choose the desired components to install in a new installation.

### PI System Explorer

https://livelibrary.osisoft.com/LiveLibrary/content/en/server-v9/GUID-21B52B10-20E6-4039-B358-E0159ECA76C2


## Developer/Test Servers

### Sandbox


### Dockers


https://pisquare.osisoft.com/s/question/0D51I00004UHlTwSAL/installing-pi-applications-on-docker


Old version may have docker support. However, explore if new version has docker support?

https://pisquare.osisoft.com/s/Blog-Detail/a8r1I000000GvHEQA0/spin-up-pi-web-api-container-af-server-included

https://pisquare.osisoft.com/s/Blog-Detail/a8r1I000000GvQdQAK/compose-pi-system-container-architecture

https://pisquare.osisoft.com/s/question/0D51I00004UHk7sSAD/is-there-a-way-to-create-an-afsdk-docker-container

https://resources.osisoft.com/presentations/how-to-put-your-af-server-into-a-container/

### Resources

PI DevClub subscriptions
https://customers.osisoft.com/

### Hyperlinks


### Code snippets

?


### Collapsible sections

#### Direct text

<details><summary>Small block of code (Click me)</summary>
<p>

#### yes, even hidden code blocks!

```python
print("hello world!")
```

</p>
</details>


<details><summary>Big block of code (Click me)</summary>
<p>
import { constants } from 'os'
import { createWriteStream, createReadStream } from 'fs'

// ... click to expand/collapse
;(async () => {
  const result = await new Promise((r, j) => {
    const input = process.env['INPUT'] || __filename
    const output = process.env['OUTPUT']
    const rs = createReadStream(input)
    const ws = output ? createWriteStream(output) : process.stdout
    rs.pipe(ws)
    rs.on('error', (err) => {
      if (err.errno === -constants.errno.ENOENT) {
        return j(`Cannot find file ${input}`)
      }
      return j(err)
    })
    rs.on('close', () => {
      r({ input, 'output': output })
    })
  })
  const res = {
    version: process.version,
    ...result,
  }
  console.log(res)
})()

</p>
</details>


https://gist.github.com/joyrexus/16041f2426450e73f5df9391f7f7ae5f

#### Code from external file

?

### References



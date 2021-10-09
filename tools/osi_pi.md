## Introduction

OSIsoft makes the PI System, the market-leading data management platform for industrial operations, that helps you move from complexity to simplicity.

## Summary

The recommended best practices are:


## Components

### Images

- Direct image, original size:
 - tba

- Image, custom size:
 - tba

- Image, custom size:
 - tba

### Tables

??

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



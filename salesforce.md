## Introduction

Salesforce platform

## Summary

- See "First Steps" section below

- Course work:
    - preferred:
        - https://www.udemy.com/course/salesforce-development/
    - further courses under review are below:
        - https://www.udemy.com/courses/search/?q=salesforce+developer&src=sac&kw=salesforce

- Podcasts:
    - https://developer.salesforce.com/podcast


### First Steps (Week 3)

- Start the course work given in summary
- listen to all the podcasts to get good idea of what is possible using the technology

- Create account in below website
    - https://developer.salesforce.com/

- Pick 5 projects from below link
    - https://developer.salesforce.com/code-samples-and-sdks
    - for each project:
        - document the project in md file
            - exlain the architecture
            - learn about plantuml using document: [tools\plantuml.md](tools\plantuml.md)
            - draw project flowchart(s) in plantuml
        - Run the projects in playgrounds

- Learn Test Driven Development (TDD) principles

### Course work (Weeks 3, 4, 5, 6, 7)

Key things to note:
- Start the course work given in summary
- document all the learnings in the repository
- save all code as programming files
- along with coursework, on developer.salesforce.com, after registering, do the following:
    - Follow all the trailhead basics : [https://trailhead.salesforce.com/en/content/learn/modules/trailhead_basics](https://trailhead.salesforce.com/en/content/learn/modules/trailhead_basics)
        - learn to create playgrounds
        - learn to install packages (using GUI or using URL)
        - 
    - run 5 chosen projects in playgrounds
- work to get the following salesforce certifiations:
    - ?
    - ?


### General working

### IDE: VS Code 

For general working in VS code:
[https://code.visualstudio.com/docs/languages/typescript](https://code.visualstudio.com/docs/languages/typescript)


### Omni channel 

![Omni-Channel](https://github.com/vamseeachanta/energy/blob/master/salesforce/Omni-Channel.png)

Queue based on routing
![https://github.com/vamseeachanta/energy/blob/master/salesforce/Omni-Channel.png](https://github.com/vamseeachanta/energy/blob/master/salesforce/Omni-Channel.png)

Skill based on routing
![https://github.com/vamseeachanta/energy/blob/master/salesforce/Queue-based-omni-channel-routing.jpg](https://github.com/vamseeachanta/energy/blob/master/salesforce/Queue-based-omni-channel-routing.jpg)

Queue based vs. Skill based

![https://github.com/vamseeachanta/energy/blob/master/salesforce/Queue-based-omni-channel-routing.jpg](https://github.com/vamseeachanta/energy/blob/master/salesforce/Omnichannel_what_is_possible.png)

### Omni channel queue architecture

Insert (new) case:
- Case is created
- Assigned to queue (Omni)

- Multiple agents. 
    - Based on status, availability, capacity based workload etc. on the Omnichannel. Based on configuration, case is assigned to a single agent

- If case update (i.e existing case ) scenario:
    - Status updated to need additional information
    - Route to special information group
    - owner should be changed to different queue. This will be another omnichannel queue
    - repeat architecture.


[https://youtu.be/RFz6tfmAXyA](https://youtu.be/RFz6tfmAXyA)

[https://www.mstsolutions.com/technical/salesforce-omni-channel](https://www.mstsolutions.com/technical/salesforce-omni-channel)
[https://ledgeviewpartners.com/blog/whats-possible-with-omni-channel-in-salesforce-for-customer-service/](https://ledgeviewpartners.com/blog/whats-possible-with-omni-channel-in-salesforce-for-customer-service/)


### References


## Introduction

Salesforce platform

## Summary

- See "First Steps" section below

- Course work (Still to be determined):
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

developer.salesforce.com training:
    - document all the learnings in training repository. 
    - save all code as programming files
    - as you train, learn any unknown topics and document them. Some go-by websites
        - https://www.salesforcetutorial.com/sfdc-tutorial/
        - trailhead.salesforce.com/developer/training
        - google search topics
    - Based on quality of your documentation, we will reuse in this repo for future trainings of developers.
    - train on developer.salesforce.com, after registering, do the following:
        - Follow all the trailhead basics : [https://trailhead.salesforce.com/en/content/learn/modules/trailhead_basics](https://trailhead.salesforce.com/en/content/learn/modules/trailhead_basics)
            - learn to create playgrounds
            - learn to install packages (using GUI or using URL)
        - complete the below chosen trailhead modules in following areas:
            - basics area
                - ?
                - ?
            - apex area
                - ?
                - ?
            - lightening area
                - ?
                - ?
            - lightening web components (LWC) area
                - ?
                - ?

        - run 5 chosen projects in playgrounds
    - work towards getting the following salesforce certifiations:
        - ?
        - ?

udemty course
- Start the udemy course  given in summary

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


## Introduction

OSIsoft makes the PI System, the market-leading data management platform for industrial operations, that helps you move from complexity to simplicity.
https://techsupport.osisoft.com/Products/Layered%20Products/PI-AF/Overview

There are different roles for various experts using the OSI soft PI system:
- Installation and setup
- Controller Network to PI System interface (Connect the instrumentation to PI system - typ. process engineers, industrial control experts etc.)
- PI System administration (AssetFramework i.e. AF, assets, Tags, attibutes etc.)
- Full stack development (C# or Python) with PI System interface (Programmer jobs)

## Summary

In summary, like any other data systen, OSI PI and associated systems are data software system. 
OSI PI and associated systems have APIs and SDK (PIAFSDK) developers can interface and work with.
Both .NET/C# (Not sure of differences here) and Python have SDKs. No official support for Python.

### PI AF

PI Asset Framework (PI AF) is a single repository for asset-centric models, hierarchies, objects, and equipment. It integrates, contextualizes, refines, references, and further analyzes data from multiple sources, including one or more PI Data Archives and non-PI sources such as external relational databases. Together, these metadata and time series data provide a detailed description of equipment or assets.

PI AF can expose this rich data to PI System components, such as PI VIsion, PI DataLink, or PI ProcessBook, where it can be used to build displays, run calculations, deliver important information, and more. PI Asset Framework can also expose these data to non-PI systems via a rich set of data access products. PI AF also includes a number of basic and advanced search capabilities to help users sift through static and real time information. The following comparison table lists the capabilities of current and earlier versions of PI AF.

### PI System components

- Basic
    - PI System Explorer
    - PI SDK Utility
- Advanced
    - PI ProcessBook
    - PI SQL Commander
    - PI Interface Configuration Utility
    - PI OLEDB
    - PI VIsion (Visualize data, raw, analytics, predictive analytics etc.)
    - PI DataLink

### PI AF SDK

- PI AF SDK is the foundational .NET-based software development kit for interacting with asset metadata and time series data stored in the PI Asset Framework. It is available from PI Developers Club* (formerly known as vCampus). For more information, refer to PI AF SDK Homepage.
- PI Server 2018 introduces a single setup kit that includes PI Data Archive, PI Asset Framework with Asset Analytics and Notifications, PI Web API, PI System Directory, and all dependent components. Users can choose the desired components to install in a new installation.

Example Data:
| Parameter |   Physical Quantity |  Value |  Unit |   Additional comments |
|---|---|---|---|---|
| Pore Pressure | Pressure  | 200 | psi | n/a | 
| Pore Pressure | Pressure  | 200 | psi | n/a | 
| Pore Pressure | Pressure  | 200 | psi | n/a | 

### PI System Explorer

https://livelibrary.osisoft.com/LiveLibrary/content/en/server-v9/GUID-21B52B10-20E6-4039-B358-E0159ECA76C2


# Typical Tasks of OSISoft PI Developer

The typical steps of setting up and onboarding a developer are:
- The OSI PI administrator will add the active directory (AD) of the developer to relevant PI servers for development.
    - Usually only sandbox/development and staging environments access are provided
    - The production environments are linked to live equipment and thus can disrupt equipment operation and shut-down equipment such as pumps, rigs etc.
    - Alternatively, a default username will also be provided to configure the PI SDK utility to connect to PI resources
    - Users may have server access but may still need further read and write access (In-house PI experts can help with this)

- The developer will install PI System to get access to PI System Explorer and other tools
- Setup .NET/C# or Python development setup per preference (and approval by the IT systems)
- Use exploratory codes to understand the project

Example OSISoft PI usecases for developers are given below. One of more can be part of the work.

Reading Data:
- Reading data needs permissions
- Data can be read from a PI Point (or PI tag). Typical data:
    - current value
    - historical or recorded values
    - future values (if recorded and exist for querying)

Performing Analysis:
- Simple statistics of recorded values. 
    - Note that statistical methods used may not contain repeat recorded values to minimize data storage. Therefore, handling such statistics accurately needs data principle knowledge 
- Advanced analysis using python scripts etc.

Writing Data:
- Data can written to pi tag:
    - Supply input or configuration values
- Future predicted data from algorithm to keep in state of readiness for comparison against actual values
- etc.

Visualizing Data:
- PI Vision can help:
    - Visualize data (current, recorded and future values)
    - Measured vs. predited data
- Alternatively, any other plotting programs/libraries can be used

Real-time analysis or ML Models:
- Based on historical data and current data (e.g. pore pressure, mud pump pressure), using various geophysical properties can be used in a model (algorithm) to predict the next expected data (pressure)
- This prediction can be plotted against expected data
- A ML model can further be used to calibrate the model (algorithm)

## Code Examples

For python examples, see py/osi_py.md
.NET/C# examples will be analogous to python. Will be added.

## Developer/Test Servers

### Sandbox


### Dockers - As Sandbox?

https://pisquare.osisoft.com/s/question/0D51I00004UHlTwSAL/installing-pi-applications-on-docker

Old version may have docker support. However, explore if new version has docker support?

https://pisquare.osisoft.com/s/Blog-Detail/a8r1I000000GvHEQA0/spin-up-pi-web-api-container-af-server-included

https://pisquare.osisoft.com/s/Blog-Detail/a8r1I000000GvQdQAK/compose-pi-system-container-architecture

https://pisquare.osisoft.com/s/question/0D51I00004UHk7sSAD/is-there-a-way-to-create-an-afsdk-docker-container

https://resources.osisoft.com/presentations/how-to-put-your-af-server-into-a-container/

### Resources

PI DevClub subscriptions
https://customers.osisoft.com/

### References

https://www.youtube.com/user/OSIsoftLearning

https://www.youtube.com/watch?v=zj2EoTkpz1k A good overview
https://www.youtube.com/watch?v=Ab-1wMFj3DA&list=PLMcG1Hs2JbcsGGJ84BtG2fClp7SF7K9jU PI System Basics

https://www.youtube.com/watch?v=_n3yLpjMhew    OSIsoft: PI Basics- Connect to and Search a PI System

https://www.youtube.com/watch?v=qqD07Vl6RZQ Running PI Edge in Containers


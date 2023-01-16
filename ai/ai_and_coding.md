## Introduction




## Summary


### ChatGPT

ChatGPT has changed software development!

However, 68.1% of Software Engineers still don't use it.
As a CTO, I'm telling my teams to use 
#ChatGPT
 in their daily work to increase both velocity and quality.

1/ Generate boilerplate code

To build a new project from scratch, I ask ChatGPT to create a skeleton of the app I need, using the technologies, frameworks, and versions I choose.
I can even make it part of my team's documentation. It saves at least an hour or so each time

2/ Research and compare

Many times there are different ways to implement something. So my usual approach is to build a rough PoC of two competing approaches and compare them.
ChatGPT can do it for me:
- React vs Vue
- Algorithm A or B
- etc
This saves the half day of work, easily.

3/ Explain the code

How many times our work is simply to understand a code base that wasn't built by us? Spaghetti code, with no comments. We did a little bit line by line.
Now we can ask ChatGPT to explain what the code does, and we save a bunch of time.

4/ Comment code

We can extend point 3 above by adding line-by-line comments to that code base we didn't build.
But we can also make our own code properly commented before shipping, by asking ChatGPT to add comments.
No more uncommented code in PRs.

5/ Write test cases

Ask ChatGPT to generate test cases for a list of scenarios. Even tell which framework, version, etc you want to be used. Boom, it will do it for you.
No more untested PRs.

6/ Write documentation

You can ask ChatGPT to write documentation on things like:
- How to spin up a certain code base,
- The packages required for it to run
- What the code does,
- What are the know limitations.
- Etc.

It might not be perfect, but the 80/20 rule applies.

7/ Generate regexes

Regexes are one of those specific syntaxes we don't use from time to time. We need to Google, look up syntax, and spend significant time every time we need one.
Not anymore, we can just ask ChatGPT to generate it.

8/ Rewrite code using the correct style

I just wrote down some code conventions from one of my teams and added them to the prompt, along with some spaghetti code.
Very useful when merging code from different repos/teams, which would need to be refactored before merging.

9/ Find bugs in your code

When you know what you want, but the code doesn't do what you want. Instead of adding a console. logs all over the place, you can ask ChatGPT to spot the bug for you.
This works best on function-level bugs, not repo levels. Still, a massive improvement.

10/ Leetcode type algorithms

If you need a specific isolated function, to run on optimal complexity. ChatGPT can get you a very fast start.
An obvious use case for this is coding interviews. But sometimes it's useful in day-to-day work too.

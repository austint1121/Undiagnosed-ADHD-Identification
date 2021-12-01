# Undiagnosed-ADHD-Identification

Proposal [here](https://github.com/austint1121/Capstone_Proposal)

[Project progress](https://github.com/users/austint1121/projects/1)

# Summary

# Introduction

ADHD is a developmental disorder associated with an ongoing pattern of inattention, hyperactivity, and/or impulsivity.
The symptoms of ADHD can interfere significantly with an individual’s daily activities and relationships. ADHD symptoms
begin in
childhood [and worsen in the teen years and adulthood](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know#part_6209)
.

People with ADHD experience an ongoing pattern of the following types of symptoms:

- Inattention–having difficulty paying attention
- Hyperactivity–having too much energy or moving and talking too much
- Impulsivity–acting without thinking or having difficulty with self-control

Some people with ADHD mainly have symptoms of inattention. Others mostly have symptoms of hyperactivity-impulsivity.
Some people have both types of symptoms.

ADHD comes in many forms and severities, and teenagers and adults who are undiagnosed often don't even consider they may
have ADHD if their symptoms don't perfectly match stereotypes of ADHD in the media.

## Problem

As established above, Undiagnosed ADHD can be difficult for those with it. But why is
it [so common](https://www.singlecare.com/blog/news/adhd-statistics/#adult-adhd-statistics) for ADHD to go undiagnosed?

Personally, I think this is a multi-pronged issue:

**ADHD is not well understood.**
ADHD is still a [subject of heavy research](https://www.cdc.gov/ncbddd/adhd/research.html) in the science/medical field.
Currently, we do not know what causes ADHD, but we know there is some genetic component involved. There is no blood test
or any kind of empirical way to test for ADHD; it can only be diagnosed through observation of its symptoms.

**The way ADHD is Diagnosed.**
To be diagnosed with ADHD, you would have to specifically bring it up with your doctor; this means that if you don't
suspect you have it, you may never bring it up to your doctor on your own. ADHD is diagnosed by a
doctor [asking a series of questions](https://www.cdc.gov/ncbddd/adhd/diagnosis.html) relating to long-term behavioral
patterns at home, so it would be difficult for a doctor to notice ADHD symptoms during a regular visit.

**The way ADHD is portrayed**
People with ADHD are typically portrayed as young kids, who are extremely hyper-active and disobedient. However,
hyperactivity is only one component of ADHD, and it expresses itself in various ways. Especially as kids grow older,
hyperactivity can [look very different](https://www.nytimes.com/2010/12/14/health/14klass.html) from what is portrayed
in media/pop culture. This results in individuals rejecting the idea that they, or someone they know, has ADHD because
their symptoms don't look like stereotypical ADHD symptoms.

So, is there a solution that can be reliably used that **doesn't require a deep understanding of ADHD**, and could help
spread awareness that a person may have ADHD regardless of any **personal** or **societal** bias towards what ADHD looks
like?

Such a solution would greatly benefit individuals with undiagnosed ADHD, and help push people towards getting a
diagnoses. There are lots of "ADHD self-tests" on the internet, but they are questionable at best, and misleading at
worst. If our hypothetical solution also used **real data** from those diagnosed with ADHD, it would definitely give it
more weight as a solution.

Where human perception fails, a machine can excel. Machine learning is the perfect solution for this kind of problem. An
AI **doesn't need a deep understanding** of a subject to recognize underlying patterns, and **it doesn't care** about
any personal bias, or what ADHD "should" look like according to society. The nature of machine learning also means it
would **need to use real data**, But does a data source like that even exist?

## Data

The [NSCH](https://www.census.gov/programs-surveys/nsch/data/datasets.html) is a household survey that produces national
and state-level data on the physical and emotional health of children 0 - 17 years old in the United States. Since 2016,
the NSCH has been an annual survey. The survey supports national estimates every year and state-level estimates by
combining 2 or 3 years of data. In this project I would primarily look at the 2020 data.

The survey collects information related to the health and well-being of children, including access to and use of health
care, family interactions, parental health, school and after-school experiences, and neighborhood characteristics. A
parent or other adult caregiver with knowledge of the sampled child’s health and health care filled out the topical
questionnaire.

Survey topics include:

- Child and family characteristics
- **Physical and mental health status, including current conditions and functional difficulties**
- Health insurance status, type, and adequacy
- Access and use of health care services
- Medical, dental, and specialty care needed and received
- Family health and activities
- Impact of child’s health on family
- Neighborhood characteristics

## Goal

In the NSCH data is a question that asks:

- Has a doctor or other health care provider EVER told you that this child has… Attention Deficit Disorder or
  Attention-Deficit/Hyperactivity Disorder, that is, ADD or ADHD?

For this project, I'm going create a tool that can give the probability that a child from the survey has ADHD, **but is
undiagnosed**.

One distinction I'd like to make: **This project is not about diagnosing kids with ADHD**. Only a trained medical
professional can diagnose someone with ADHD. This project and it's results are about spreading awareness.

# Data Cleaning

# Modeling

# Conclusion
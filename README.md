# Undiagnosed-ADHD-Identification

by [Matthew Turner](https://www.linkedin.com/in/matthew-turner-a5649a21b/)

# Summary

# Introduction

ADHD is a developmental disorder associated with an ongoing pattern of inattention, hyperactivity, and/or impulsivity.
The symptoms of ADHD can interfere significantly with an individual’s daily activities and relationships. ADHD symptoms
begin in
childhood [and worsen in the teen years and adulthood](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know#part_6209)

ADHD comes in many forms and severities, and teenagers and adults who are undiagnosed often don't even consider they may
have ADHD if their symptoms don't perfectly match stereotypes of ADHD in the media.

## Problem

As established above, Undiagnosed ADHD can be difficult for those with it. But why is
it [so common](https://www.singlecare.com/blog/news/adhd-statistics/#adult-adhd-statistics) for ADHD to go undiagnosed?

Personally, I think this is a multi-pronged issue:

**ADHD is not well understood.**
ADHD is still a [subject of heavy research](https://www.cdc.gov/ncbddd/adhd/research.html) in the science/medical field.

**The way ADHD is Diagnosed.**
To be diagnosed with ADHD, you would have to specifically bring it up with your doctor; this means that if you don't
suspect you have it, you may never bring it up to your doctor on your own.

**The way ADHD is portrayed**
People with ADHD are typically portrayed as young kids, who are extremely hyper-active and disobedient. However,
hyperactivity is only one component of ADHD, and it expresses itself in various ways. Especially as kids grow older,
hyperactivity can [look very different](https://www.nytimes.com/2010/12/14/health/14klass.html) from what is portrayed
in media/pop culture.

So, is there a solution that can be reliably used that **doesn't require a deep understanding of ADHD**, and could help
spread awareness that a person may have ADHD regardless of any **personal** or **societal** bias towards what ADHD looks
like? If our hypothetical solution also used **real data** from those diagnosed with ADHD, it would definitely give it
more weight as a solution.

But does a data source like that even exist?

## Data

The [NSCH](https://www.census.gov/programs-surveys/nsch/data/datasets.html) is a household survey that produces national
and state-level data on the physical and emotional health of children 0 - 17 years old in the United States. Since 2016,
the NSCH has been an annual survey.

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

# Data Understanding

As mentioned above, the [NSCH](https://www.census.gov/programs-surveys/nsch/data/datasets.html) is a household survey
that produces national and state-level data on the physical and emotional health of children 0 - 17 years old in the
United States. It is performed by the US Census Bureau, and an extremely
detailed [methodology report](https://www2.census.gov/programs-surveys/nsch/technical-documentation/methodology/2020-NSCH-Methodology-Report.pdf)
is included with the data.

As a Data scientist I need to ask myself:

**Is this data suitable for our goal, and what kind of limitations does it have?**

The most important thing about this data, is that it is representative of the population as a whole. Starting on page 8
of the methodology report, there is a detailed explanation of the collection methods used to gather this data. In
summary, modifications were made to this data to ensure it was representative of the overall population.

## Exploratory Data Analysis

In this [notebook](/Notebooks/EDA.ipynb) I investigate and visualize distributions and key points in my data relating to
kids diagnosed with ADHD.

The key points I found were:

- There are **4306 children** in this sample have been **diagnosed** with ADHD.
  <br>

- **10%** of kids in this sample have been **diagnosed** ADHD.
  <br>

- Of these kids, **69% are male**, and **31% are female**
  <br>

- of the kids diagnosed with ADHD,

    - **61%** are between the ages of **12-17**
    - **36%** are between the ages of **6-11**
    - **3%** are between the ages of **0-5**

- The Racial/Ethnic distribution of children with ADHD is:

| Race        | Percentage  |
| ----------- | ----------- |
| White       | 80%         |
| Black       | 8%          |
| Asian       | 2%          |
| Mixed       | 8%          |
| Native Am.  | 0.009%      |
| Hawaiian    | 0.006%      |

<br>

# Data Cleaning

The Data file can specifically be found [here](https://www.census.gov/programs-surveys/nsch/data/datasets.html)

To prepare the data for cleaning I:

- Removed columns related to ADHD
- Ensured all NaN values present in the dataset were addressed
- Performed a train-test split on the data and created a holdout set.
- Saved transformed/cleaned data as CSV files.

The full data cleaning notebook can be found [here](/Notebooks/Data_Cleaning.ipynb)

# Modeling

I created 3 different types of models: [Sklearn decision tree](Notebooks/Modeling-Decision_Tree.ipynb)
, [Catboost](Notebooks/Modeling-Catboost.ipynb), and a [Keras neural network](Notebooks/Modeling-Keras.ipynb).
My [final model](Notebooks/Modeling-Catboost-Tuning.ipynb) is a Catboost model.

For each model type, created a first simple model, and iterated from it, attempting to optimize the Recall and AUC scores.

- **Recall** because I don’t want the model to be missing kids that may have, potentially, already been passed over/ignored by doctors.
- AUC as a more general overview to how my model is doing

I decided to ignore the accuracy score of this model, since I had a significant class imbalance in my target.

# Results
For my final model, I attempted to address the class imbalance issue first, using the random oversampling technique, I then used
the [Optuna](https://optuna.readthedocs.io/en/stable/index.html) library to perform hyper parameter tuning on the model.



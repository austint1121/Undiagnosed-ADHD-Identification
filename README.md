# Undiagnosed-ADHD-Identification
Proposal [here](https://github.com/austint1121/Capstone_Proposal)

[Project progress](https://github.com/users/austint1121/projects/1)

## Data Understanding

## Goal
In the NSCH data is a question that asks:
- Has a doctor or other health care provider EVER told you that this child has…
  Attention Deficit Disorder or Attention-Deficit/Hyperactivity Disorder, that is, ADD or ADHD?

For this project I would like to
Create a model that can return the probability that a child from the survey has ADHD, **but is undiagnosed**.

To achieve this, I would train the model on kids from the survey who **have** been diagnosed with ADHD. Then I would have
the model predict the probability that a child has ADHD on kids from the survey who **have not** been diagnosed with ADHD.

The idea here being, that if the model finds many similarities between a child who **has not** been diagnosed, and the
children who **have been** diagnosed, then that child may have undiagnosed ADHD.

The target audience here would be the creators/sponsors of the survey, and this would be a binary classification problem.

# Data Cleaning

# Modeling

# Conclusion
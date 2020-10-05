# Mech Car


## Purpose of this analysis
In the past, Jeremy and I analysed some data and the management was happy.

 Now, Jeremy is approached by upper management about a special project. AutosRUs’ newest prototype, the MechaCar, is suffering from production troubles that are blocking the manufacturing team’s progress. AutosRUs’ upper management has called on Jeremy and the data analytics team to review the production data for insights that may help the manufacturing team.

## Resources
* Software: `Visual Studio Code` (v1.49.2), `RStudio` (v1.3.1093), `R` x64 3.6.3
* Data
    * MechaCar Data: click ![here](Resources/MechaCar_mpg.csv)
    * Suspension Coil Data: click ![here](Resources/Suspension_Coil.csv)

## Deliverable 1: Linear Regression to Predict MPG

### Imgage 1: Output of Deliverable 1

![](Resources/Deliverable1.png)

### Answers to the 3 questions

* Which variables/coefficients provided a non-random amount of variance to the mpg values in the dataset?

    **Answer**: There were two variables/coefficients that provide a non-randon amount of varience to the mpg values in the dataset - `vehicle_length` & `ground_clearance`

* Is the slope of the linear model considered to be zero? Why or why not?

    **Answer**: No the slope is not Zero, since the `R-squared value is around .7149` which shows a strong co-relation.

* Does this linear model predict mpg of MechaCar prototypes effectively? Why or why not?
    
    **Answer**: Yes, the linear model predicts mpg of MechaCar Prototypes effectively because the `p-value is < 0.05`.

## Deliverable 2: Summary Statistics on Suspension Coils

### Imgage 2: Output of Deliverable 2
![](Resources/Deliverable2.png)

### Answer to the question

* The design specifications for the MechaCar suspension coils dictate that the variance of the suspension coils must not exceed 100 pounds per square inch. Does the current manufacturing data meet this design specification for all manufacturing lots in total and each lot individually? Why or why not?

    **Answer**: The current manufacturing data 
    1) **Does meet** the design specification for all manufacturing lots in total - since the variance of all the lots combined is 76.23, which is less than 100
    2) **Does not meet** the design specification for all manufacturing lots individually - it meets for lot 1 and lot 2, but not for lot 3, where the varience is 220 which is more than 100.

## Deliverable 3: T-Tests on Suspension Coils

Written Summary
In your README, create a subheading ## T-Tests on Suspension Coils, then briefly summarize your interpretation and findings for the t-test results. Include screenshots of the t-test to support your summary.

***Deliverable 3 Requirements***
You will earn a perfect score for Deliverable 3 by completing all requirements below:

* An RScript is written for t-test that compares all manufacturing lots against mean PSI of the population (5 pt)
* An RScript is written for three t-tests that compare each manufacturing lot against mean PSI of the population (10 pt)
* There is a summary of the t-test results across all manufacturing lots and for each lot (5 pt)


## Deliverable 4: Study Design: MechaCar vs Competition

Using your knowledge of R, design a statistical study to compare performance of the MechaCar vehicles against performance of vehicles from other manufacturers.

Follow the instructions below to complete Deliverable 4.

* In your README, create a subheading ## Study Design: MechaCar vs Competition.
* Write a short description of a statistical study that can quantify how the MechaCar performs against the competition. In your study design, think critically about what metrics would be of interest to a consumer: for a few examples, cost, city or highway fuel efficiency, horse power, maintenance cost, or safety rating.
* In your description, address the following questions:
    * What metric or metrics are you going to test?
    * What is the null hypothesis or alternative hypothesis?
    * What statistical test would you use to test the hypothesis? And why?
    * What data is needed to run the statistical test?*


***Deliverable 4 Requirements***
You will earn a perfect score for Deliverable 4 by completing all requirements below:

The statistical study design has the following:
* A metric to be tested is mentioned (5 pt)
* A null hypothesis or an alternative hypothesis is described (5 pt)
* A statistical test is described to test the hypothesis (5 pt)
* The data for the statistical test is described (5 pt)
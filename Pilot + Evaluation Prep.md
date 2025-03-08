# Core assignment: Pilot + Evaluation Prep [+4.5] Group

Pilot [+1]

[+0.5] Present the pilot user with a brief statement of the scenario and task. Ask the pilot user to complete the task. Note: You might feel (very) nervous that something will break. That is OK. It's ok for the pilot user to break things as they test out your system. Be prepared to restart/recover your system when things break. Note what happened step by step. Include 0.5-1p of notes on one pilot user. Additionally, summarize in a few sentences: What happened? Why? What changes do you need to make to your system before the next pilot?

> The pilot testing revealed that users found the UI elegant and straightforward, with all testers agreeing that the results were good. However, several areas for improvement were identified. Key enhancements include ensuring that important information remains easily accessible by adding a disclaimer and info page, increasing spacing between elements for better readability, and implementing hover comments for additional explanations. Additionally, improvements in download separation and better demo figures for colorblindness support were suggested to enhance accessibility. The next steps involve refining these aspects, conducting another pilot experiment to validate the changes, and fully implementing the system based on user feedback.

[+0.5] Involve another pilot user outside the course. Include 0.5-1p of notes on this second pilot user. Summarize in a few sentences: What happened? Why? What changes do you need to make to your system before the next pilot?

> We conducted another pilot study with a TA from the CS department who has mild red-green color blindness. After introducing the background of our project, we asked him to use our web app. He tested our example figures and found the results to be effective. However, he expressed confusion regarding our simulation results.
Currently, our system only displays the simulated version of the original figure, as we initially thought that also including simulations of the processed figure  would overcrowd the interface (that would be 3 colorblindness $\times$ 2 = 6 figures). Additionally, we positioned the simulation button next to the processed figure, assuming that all outputs should be grouped on the same side. This led to confusion — the TA mistakenly believed the simulated results corresponded to the processed figure rather than the original.
To address this issue, we plan to simplify the simulation display. Instead of simulating all three conditions, we will generate only two figures: one showing the simulated red-green color blindness effect on the original image and one on the processed image. Since red-green color blindness is the most common type, this approach will provide clearer and more meaningful simulation results while reducing visual clutter.









Before conducting an evaluation [+3]

1. [+0.5] Articulate1-2 questions motivating the evaluation. In other words, what are the 1-2 things you want to prioritize learning through the evaluation?
> 1. How long does it take users to complete a full task (from uploading image to getting their result)?
> 2. How often do users encounter errors or need clarification while using the system?

1. [+0.5] What metrics will you use to answer the above research questions? Why are these metrics appropriate? What are the benefits and drawbacks of using these metrics?
Requirements: You are required to conduct a mixed-methods study where you collect qualitative and quantitative data. In your response to this question, describe what kind of data (e.g., open-ended survey, interview, time, clicks, etc.) will be useful for answering your motivating questions.
> The key quantitative metrics include task completion time, how often users gets confused/frustrated, number of clicks and usability ratings (1 to 5). 
> We may also ask users to use it multiple times and see if they get better at it, which would be a good indicator of learnability.
> These will measure efficiency, clarity, and navigation ease by identifying bottlenecks in user interactions. Additionally, qualitative feedback will be collected through open-ended surveys and short interviews to understand why users face difficulties or succeed. By analyzing how long tasks take, how many clicks are needed, and how often errors occur, we can pinpoint usability issues. Combining objective metrics with user insights ensures targeted improvements before the next pilot test.

1. [+1] Specify a plan for recruiting participants.
How will you contact participants (e.g., mailing lists, in-person, etc.)?
What are your inclusion/exclusion criteria for participants? 
Will you include participants you interviewed for user research? Why or why not?
Where will you perform the evaluation?
What data will you collect from participants? How will you inform them of this and obtain informed consent?
> ### **Participant Recruitment Plan**
> We will recruit **TAs and students** by reaching out in person, leveraging classroom settings, office hours, and lab spaces to invite participation. This ensures that we engage individuals who are familiar with academic tools and likely to use such a system.
> #### **Inclusion/Exclusion Criteria**  
> - **Inclusion:** Participants must be TAs or visual impaired students with some experience in programming, to ensure they can meaningfully interact with the system.  
> - **Exclusion:** Participants who lack programming experience, or are unavailable for an in-person session will be excluded.
> #### **Previously Interviewed Participants**  
> We will include participants from prior user research, even though they have not seen the prototype yet. Their previous insights on usability challenges will help us assess whether the system meets the needs and expectations they initially expressed.  
> #### **Evaluation Location**  
> The evaluation will be conducted in person in an office setting, ensuring controlled conditions, direct observation, and the ability to address any technical issues immediately.
> #### **Data Collection & Consent**  
> We will collect:  
> - **Quantitative data**: Task completion time, error frequency, number of clicks, usability ratings, and interaction behaviors.  
> - **Qualitative data**: Open-ended survey responses and brief interviews about usability.
> Participants will be informed of data collection beforehand and asked for consent, ensuring they understand the study's purpose, data usage, and their right to withdraw at any time.

1. [+1] Write out a step-by-step protocol for conducting each user evaluation. Getting on the same page is important for more easily conducting studies and analyzing data across participants. Your protocol should include: (1) a script of what you will say to each participant; (2) what behaviors/responses you expect from participants and how that may change the flow of the study, if at all; and (3) how you will transition between phases of the study (e.g., from a task to an interview). 

> The step-by-step protocol:
> 1. "Thank you for participating in our study. We have developed a system aimed at improving accessibility in academic materials, particularly for color-blind students. This tool evaluates whether an academic figure is colorblind-friendly. If not, it automatically adjusts the figure by modifying colors and adding patterns or hatches. Currently, our tool supports various types of bar plots and also includes features such as color blindness simulation and external resources for further learning.
> In this study, we’d like you to imagine that you are a teaching assistant who has created several bar plots for a discussion section. However, some of these figures are not accessible to certain types of color-blind students. You will use our tool to generate more accessible versions of these figures. We have prepared five sample figures with different characteristics, such as resolution, color palette, and aspect ratio. You are free to explore the tool’s functions and ask for clarification at any time.
> During the process, we will record how long you take to generate each figure, the number of clicks and interactions you make, and any difficulties you encounter. Afterward, we will ask you to complete a short survey about your experience. Your participation is completely voluntary, and if at any point you feel uncomfortable or do not wish to continue, please let us know.
> Do you have any questions before we begin? If not, we can start.""
> 2. If the participant follows the UI smoothly, which is most likely to happen during from our experience in the pilot study as our UI is very self-explainary), we would proceed without intervention.$\quad$
If they seem to struggle to understand a feature, we would first leave them some time to figure it our, and then prompt them with, "Would you like an explanation of this function?" $\quad$
Repeat this process for all five sample figures.
> 3. After the use have finished all the required tasks, we will transist from the task to the survey.
> We would guide the user through the survey and note any additional feedback they provide. We would ask them to provide rating and feedback (if any) on the overall experience, quality of results, usability, etc.
If necessary, ask follow-up questions based on their responses to clarify any insights.

[+0.5] Name your system!

> *ColorSense*

[+0.5] DEPTH: Design a logo for your system. Include a PNG in your repo. Add it to the README. 
> ![ColorSense Logo](logo.jpg)

Did you use a generative AI tool for this assignment? If so, which tool(s) and how?
> Yes, we used ChatGPT to grammar check our responses and rephrase.

How much time did you spend on this assignment
- as a group?
About 2 hours
- individually?
About 45 minutes each

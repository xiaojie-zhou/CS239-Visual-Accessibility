### \# Core assignment: Evaluation \[+10\] Group

**Phase**: Evaluation  
**Due date**: Friday, March 14 at 11:59pm PT  
**The goal** of this stage of the project is to evaluate your high-fidelity prototype with potential users.   
**Course learning objectives** this assignment facilitates: (1) Create an interactive system grounded in user research, iterative prototyping, and evaluation; (2) Explore and express complex problems, design choices; and (3) Reflect on what you know, don’t know, and how to learn what you don’t know.   
**Grading**: This is a group assignment. All members of the group are expected to participate fully. Each group will receive one grade. / Every member will receive the same number of points.  
**What to submit**: Add a .MD file in your GitHub repo with the responses to the following questions. **Submit the github repo link to BruinLearn. Only one person needs to submit for the group.**

#### Conducting user evaluation \[+5\]

Your goal is to assess the usability of your system. 

1. \[+5\] Evaluate your system with at least 10 participants. Write and submit 0.5-1p of notes for each participant.   
> ##### Participant 1
> Participant 1 is a TA with color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 5 and it helps them to make their teaching material more accessible. The participant thinks the notification (alert) pop-up when the file is uploaded successfully is unnecessary, so we removed it to reduce redundant user interaction. The participant is very likely to recommend ColorSense to others and is very satisfied with the performance of the tool. Among all the features, the participant finds color mapping and adding patterns (hatches) to bar plots most useful. The participant suggests that the tool can also provide rationale about how the accessibility score of the user’s upload is calculated, so that the user can better understand the weakness of their original diagram. By reusing the tool, the participant observes a decrease in the time it takes to convert the diagram, indicating that the interaction flow is learnable and easy to use.


> ##### Participant 2
> Participant 2 is a student without color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 5 and it helps them to make their course material more accessible. The participant does not find any feature confusing or unnecessary, and is very likely to recommend ColorSense to others.  Moderately satisfied with the performance of ColorSense, the participant finds accessibility score and color adjustment most useful. Similar to Participant 1, this participant also finds themselves spending less time on each diagram as they reuse the tool.


> ##### Participant 3
> Participant 3 is a TA without color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 5 and it helps them to make their teaching material more accessible. The participant does not find any feature confusing or unnecessary, and is likely to recommend ColorSense to others. The participant is very satisfied with the performance of the tool. Among all features, the participant finds color mapping and adding patterns (hatches) to bar plots most useful. Similar to Participant 1, this participant also thinks the pop-up of file upload success is unnecessary and good to remove. In addition to the existing features, the participant suggests enabling batch processing to accelerate the process.


> ##### Participant 4
> Participant 4 is a TA without color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 4 and it helps them to make their teaching material more accessible. The participant does not find any feature confusing or unnecessary, and is very likely to recommend ColorSense to others. The participant is moderately satisfied with the performance of the tool and finds the simulation feature most useful because it helps them understand what the diagram looks like for students with color blindness.


> ##### Participant 5
> Participant 5 is a TA without color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 5 and it helps them to make their teaching material more accessible. During the interaction flow, the participant finds the scoring UI a little confusing because it is unclear whether the score is for the original or converted diagram. They suggest that the wording of the scoring explanation can be formulated as “The original diagram was …” to avoid the potential confusion. According to the participant, they are very likely to recommend ColorSense to others and are moderately satisfied with the performance of the system. Among all features, the participant finds color mapping and adding patterns (hatches) to bar plots most useful.


> ##### Participant 6
> Participant 6 is a TA without color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 4 and it can maybe help them to make their teaching material more accessible. Similar to Participant 1 and 3, they think the file upload message is unnecessary and can be removed. According to the participant, they are very likely to recommend ColorSense to others and are very satisfied with the performance of the system. However, they agree with Participant 3 that batch operations would be very helpful because it can greatly reduce the time and effort required when there are multiple diagrams to process. The features they find most useful are color blindness simulation, adding patterns (hatches), and color mapping.


> ##### Participant 7
> Participant 7 is a TA without color vision deficiency. On a scale of 1 to 5, the participant thinks ColorSense is easy to use at level 4 and it can help them to make their teaching material more accessible. The user thinks the main flow is easy to interact with and does not find any features confusing or necessary. According to the participant, they are very likely to recommend ColorSense to others and are moderately satisfied with the performance of the system. The features they find most useful are color blindness simulation, accessibility scoring, and color mapping. To improve the system, they suggest that it would be beneficial to show the users how the accessibility scores are calculated and increase the size of the output picture.


> ##### Participant 8
> Participant 8 is a student with color vision deficiency who found ColorSense easy to use (4/5) and helpful in improving accessibility. They did not find any features confusing or unnecessary and rated their satisfaction with the system’s performance as 5/5, stating they are very likely to recommend it to others. The most useful feature for them was Color Adjustment, and they suggested adding mobile support to enhance usability on smaller screens. This feedback highlights the tool’s effectiveness while emphasizing the need for improved accessibility on mobile devices.


> ##### Participant 9
> Participant 9 is a student with color vision deficiency who found ColorSense very easy to use (5/5) and effective in achieving their accessibility goals. They did not report any confusing or unnecessary features and rated their satisfaction with performance as 4/5, indicating they are very likely to recommend it to others. The most useful features for them were Adding Pattern and Color Adjustment. As an improvement, they suggested displaying the accessibility score after conversion or providing a simulation of the generated graph to ensure accessibility. This feedback highlights the need for clearer feedback on accessibility outcomes.


> ##### Participant 10
> Participant 10 is a TA with color vision deficiency who found ColorSense very easy to use (5/5) and effective in achieving their accessibility goals. They did not find any features confusing or unnecessary and rated their satisfaction with performance as 4/5, stating they are very likely to recommend it to others. The most useful features for them were Adding Pattern and Color Adjustment. As an improvement, they suggested supporting multiple images at once to enhance usability. This feedback highlights the potential benefit of batch processing for greater efficiency.

#### After your evaluation \[+4\]

1. \[+4\] Analyze your data and write up your key findings. The findings should be about 0.5-1p for each motivating question and any other interesting findings.    
- For any qualitative data where you cannot easily remember the details of the results, a thematic analysis is required. When you conduct a thematic analysis, include your codebook.  
- For any quantitative data, submit a script for analysis \+ your data. Recommendation: Create a notebook for your analysis. Someone should be able to run your notebook to reproduce your results. 

> Since it is hard to quantify the evaluation process for our system, we primarily collected qualitative data.  We tracked the time participants took to complete the workflow and observed an improvement with repeated use, indicating that the tool is easy to learn. However, since it can only process one image at a time, its efficiency is limited. We also recorded the number of clicks, but due to differences in user habits, the results varied. With a limited sample size, the noise in the data made it difficult to interpret clear patterns, so we decided not to collect after 3 participants.

> Codebook:
> 
| Code | Definition | Example excerpt |
| :---- | :---- | :---- |
| Effectiveness | Whether the performance of the system aligns with the expectation of users that it improves the accessibility of the course material | The participant is *moderately satisfied* with the performance of the tool |
| Learnability | Easiness to follow and learn the interaction flow  | By reusing the tool, the participant observes a decrease in the time it takes to convert the diagram, indicating that the interaction flow is learnable and easy to use. |
| Generalizability | How likely it will help other people | The participant is *very likely* to recommend ColorSense to others |
| Redundancy | Unnecessary user interaction with the flow | Similar to Participant 1, this participant also thinks the pop-up of file upload success is unnecessary and good to remove. |
| Confusion | Content hard for users to interpret | During the interaction flow, the participant finds the scoring UI a little confusing because it is unclear whether the score is for the original or converted diagram. They suggest that the wording of the scoring explanation can be formulated as “The original diagram was …” to avoid the potential confusion. |
| Highlight features | The features participants personally find most helpful | The participant is *moderately satisfied* with the performance of the tool and finds the simulation feature most useful because it helps them understand what the diagram looks like for students with color blindness. |
| Nice-to-have features | The features can be added to improve the system | In addition to the existing features, the participant suggests enabling batch processing to accelerate the process. |

> Takeaway:

> - According to the feedback the usability and effectiveness of ColorSense achieves our expectation. The majority of participants consider it “easy to use” and are very satisfied with the performance of the tool. Except for a few nits, the main flow of user experience is considered straightforward and concise, effectively guiding the users through the process.  
> - In addition to the generally positive feedback, there are a couple improvements we made according to the participants’ suggestions:  
>   - We removed the alert pop-up for file upload success, which was considered as redundant by three participants. The user will only see such an alert message when the file upload is failed.   
>   - We modified the scoring UI to clarify the object of the score. Some participants are slightly confused by the score and are unsure if it refers to the original diagram or the converted one.  
>   - We modified the scoring UI to explain how the score is calculated. This increases interpretability of the component.  
> - We also collected some suggestions on nice-to-have features in the future. Due to the limitation of time, we are unable to add the features to our system for now. A couple participants mentioned that they would love to see support of batch processing and mobile web.

#### Group Reflection \[+1\]

1. What is one thing that went well in your evaluation? 
> One key success of our evaluation was the consistently high user satisfaction and recommendation scores. All participants rated their likelihood to recommend ColorSense as 5/5, demonstrating that the tool effectively addresses a real need. Additionally, the learnability of the tool was evident, as multiple users reported spending less time on each diagram upon reuse.
2. What is one thing that you wish you could have done differently?   
> One thing that could have been improved is getting feedback from a broader range of students and instructors with different levels of experience in accessibility. While our evaluation focused on TAs and students—our main target users—it would have been helpful to include more participants who actively create visual materials for accessibility. For example, instructors who frequently design complex diagrams or lecture slides might have given more insight into how well ColorSense fits into their workflow. Also, testing with more users who have severe color vision impairments would help confirm how effective the tool is for different accessibility needs.
3. How, if at all, did your participants represent the personas you intended to design for? 
> Our participants largely matched our intended target personas, particularly students and educators with and without color vision deficiencies. Since ColorSense is designed to help make educational materials more accessible, having TAs and students as primary testers was relevant. However, we had fewer participants with severe color vision impairments, so the tool’s effectiveness for a broader range of accessibility needs might need further validation.
4. How do you think this impacted your results? 
> Since our participants were mostly TAs and students, the feedback focused on educational materials like lecture slides and diagrams rather than broader applications in other fields. This means ColorSense was evaluated in a way that aligns well with its intended use in academic settings, which is a positive outcome. However, because most participants had mild or no color vision deficiencies, we may not have captured all the challenges faced by users with more severe impairments. Their feedback could provide deeper insights into how well the tool truly improves accessibility for those who rely on it the most.
5. Based on the above, what does this say about the potential applicability of your system?
> The feedback shows that ColorSense works well in academic settings, where TAs and students need to make their materials more accessible. Participants found the tool easy to use and helpful for improving accessibility, making it a good fit for educators creating lecture slides, course materials, and diagrams. However, some users requested batch processing and clearer accessibility score explanations, which suggests that ColorSense could also help people who work with large sets of images. Testing outside of academia could help see if the tool is useful in areas like web accessibility, graphic design, or publishing.
6. What new questions do you have based on your evaluation?
> - How well does ColorSense support users with severe color vision impairments? Most participants either had mild deficiencies or no deficiencies, so further testing could help confirm if the tool meets the needs of those who rely on it the most.
> - Would more transparency in accessibility scoring improve user confidence? Since multiple participants wanted a clearer explanation of how scores are calculated, refining this feature could make the tool more valuable.
> - How important is mobile support for users? One participant mentioned the need for a mobile-friendly version—would adding this make ColorSense more accessible for students and instructors on the go?

Did you use a generative AI tool for this assignment? If so, which tool(s) and how? 
> Yes, we used GPT to refine our interview questions and rephrase our responses to make them more professional and concise.

How much time did you spend on this assignment as a group? individually?
> About 1.5 hours for group discussion and 2 hours for interview and data analysis per person.
# Gaming Noise Monitor

## Requirements Outline

### Functional Requirements
+ Alerts if you’re being too loud
+ Has different settings for noise detection; baby, parents, casual
+ Baby has red LED; 60dB
+ Parents has yellow LED; 70dB
+ Casual has green LED; 80dB


### Non-Functional Requirements
+ Detection of people nearby
+ Have an ultrasonic detector with a laser next to it so people can see where it points


## Planning

### Flowchart

![flowchart](/images/flowChart.png)

### Pseudocode

#### Functions for different noise levels

- BEGIN baby()
    - WHILE true
        - READ volume
        - IF volume > 60 THEN
            - OUTPUT buzzer.on() 
        - ENDIF
- END baby()
        
- BEGIN parents()
    - WHILE true
        - READ volume
        - IF volume > 70 THEN
            - OUTPUT buzzer.on() 
        - ENDIF
- END parents()

- BEGIN casual()
    - WHILE true
        - READ volume
        - IF volume > 80 THEN
            - OUTPUT buzzer.on() 
        - ENDIF
- END casual()

#### Main Program

- BEGIN
    - WHILE true
        - READ potentiometer
        - IF potentiometer < 21845 THEN
            - baby()
        - ELIF potentiometer > 21845 AND < 43690  THEN
            - parents()
        - ELIF potentiometer > 43690 THEN
            - casual()
        - ENDIF
    ENDWHILE
END


## Evaluation

### My Evaluation

My project effectively meets the functional and non functional requirements, it has three different modes each with different levels of how loud before it goes off. If you are too loud the lights change colour and the buzzer starts buzzing. I did not complete the nearby people detection as I was more focused on getting the sound detection working and making the wiring efficent.

### Peer Evaluation

#### PMI 1

Positive: I like how the modes in the code are lined up to represent different volume sensing rates.
The mode selection system is well made, with a logical method for selections.

Negative: Modes are not explained well enough, Buzzer can of obviously trigger the original microphone detector over and over again.

Implication: The unique modes, and intuitive mode selection on this system, makes it have a wide use case in detecting noise at different volumes.
The modes could be explained a little better, and the buzzer and microphone loop could cause issues.


#### PMI 2

Positive: The device completesthe required task, and effectively alerts the usere

Negative: Selecting the mode is extremely bothersome and could be improved

Implication: The project fulfills its purposebut cou;d ave beem designed to be more user friendly


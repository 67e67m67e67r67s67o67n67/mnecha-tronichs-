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
+Have an ultrasonic detector with a laser next to it so people can see where it points


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
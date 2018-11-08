# Hybrid Visual Fixation Experiment

The hybrid visual fixation or habituation (`hvf`) can be used to investigate
aspects of attentional behaviour, currently used with infants. It involves 
protocolled scoring of looking behaviour, using a video feed of the child. 

This experiment has been requested by
[Maartje de Klerk](http://www.uu.nl/staff/MdeKlerk/0) and has been programmed by
[Chris van Run](http://www.uu.nl/staff/CPAvanRun) and -- later on --
[Jacco van Elst](https://www.uu.nl/staff/JCvanElst).

# Parts & Phases
There are two main parts.
- Attention testing : assesses the current attention span of the participant.  
- Fixation testing : assesses the amount of fixation on certain auditive
tokens.  

These are presented in four phases:  
- Pre-test phase (attention testing)  
- Habituation phase (fixation testing)  
- Test phase (fixation testing)  
- Post-test phase (attention testing)  

# Specific definitions (for the linguistics-naive programmer)    

It's easy to get confused by the use of the words 'token', 'trial', 'type'
etc. in the context of, eg. linguistics vs. programming, and maybe even more
so by the HVF paradigm. Recommended quick reading:

[wikipedia article on type-token disctinction](https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction)

- **Type** : a sound type, eg. a Dutch native non-word 'feep', phonetically
/fe:p/
- **Token** : a 'version' of a specific (sound) type, which could in practice
mean ('feep' as example):
	- Tokens are recorded versions of the type 'feep' as pronounced by
	**one speaker** (one speaker verbalized a few instances of /fe:p/, these
	recordings are all different tokens of the same type).
	- Tokens are recorded versions of the type 'feep', as pronounced by
	**different speakers**, i.e.**multiple speakers** verbalized the type
	'feep', /fe:p/
	- Two tokens in a trial could thus be different 'versions' based upon
	either/or/both aspects: in this case; speaker and recorded 'take'.
	- Even if two clearly different types are in a tokentuple (/fe:p/ by
	speaker one, /fa:p/ by speaker two), people tend to refer to them **both**
	as tokens (and they would be right). This tends to be confusing.

- **Token sequence**: any 'row' of tokens that defines a unique unit of a
 trial. Currently, only within the habituation phase, a token sequence input 
 csv file can contain exactly 12 tokens per row. They can be multiple instances 
 of the same type, pronounced by one speaker, or multiple speaker's versions of 
 a single type. Or, in fact, they could be any sequence of 12 audio stimulus 
 files the researcher may want to present in a habituation trial.

- **Tokenpair** : a special instance of a tokensequence, that is, a pair (2!) of 
sounds that defines a unique sub trial unit, currently only within a 'real' test (post 
habituation phase) trial.

- **Trial**: in the HVF experiment, a trial's start and end is defined by 
button presses of the experimenter. He/she repsonds as quickly to the estimated 
attentional (gaze) state of the observed child. Total time and total looking 
time are being monitored. The following rules define a trial flow:
	- As soon as the child does *not* attend to the trial's stimulus for 
a (configurable) period (default is two seconds), a new trial is started.
	- As soon as tokens in a trial's token sequence have been repeated a 
	(configurable) maximum amount, the trial ends. In the habituation phase,
	this means each sequence of 12 can be played a maximum of three times. In 
	the testing phase (tokenpairs), this means that eacht pair can be repeated 
	a maximum of 18 times. 

During a trial, a single image (visual) is always accompanied by an amount of 
speech sounds. In the multiple speaker vesion, this means that one image is 
being viewed, while clearly different voices are being played. 

# Input
The `stimuli` directory contains are csv files which are used for the fixation
testing. Other stimuli are defined in the `stimuli.zm` module in `./modules`,
`./test` and `./attention_test` directories. The other input is gathered from
the `global_defs.zm` and `defs.zm` modules. The name of the input-csv files are
expected to be build from the three determinators that are present in the
participant data:

* contrast (native/nonnative)
* first alteration (alt/nalt)
* group (one or two)

Only for habituation, this option is relevant:

* speaker (single or mutiple)

Determined by a *combination of contrast and group* as filled out in the
participant GUI, a certain csv file with tokens is selected (A1/A2/B1/B2).
If the contrast is **native**, a **type A csv file** is selected, and if
nonnative, a **type B csv file**. Which one of the two versions is habituated
-- and after that -- tested with alternations, depends on the value of
**group** (`group_one_two`) as given in the participant info.



The following participant info is relevant for the study:

Name                       | Description                              | Valid choices           | Comments
---------------------------|------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------
participant ID             | Some name or code                        | Baby1, B017, etc.       |
created                    | ISO time stamp                           | 2023-03-14 03:14:59     | Automatically filled
gender_m_f                 | Gender                                   | "m" or "f"              |
age_months                 | Age in months                            | All integers above 0    | Careful with this value
type_risk_control          | Whether subject is 'special'              | "risk" or "control"     | E.g. dyslexia in family
contrast_native_nonnative  | Are both sounds native?                 | "native" or "nonnative" | If native, select 'type A' csv, otherwise type B!
first_alternation_alt_nalt | Whether the first trial alternates or not | "alt" or "nalt"         | If "nalt", the first trial does not alternate, but the second does. And vice versa.
group_one_two              | Determines which token is trained/tested | "one" or "two"          | I.e.: train on "faap" and contrast with "feep", or vice versa. (native example, given Dutch language).
training_train_ntrain      | Wether or not the child has recieved special training | "train" or "ntrain" | Just for adminsitration purposes
speaker_mutiple_single     | Wether mutiple speakers or one single speaker is 'reading' the type from a tuken sequence. | "multiple" or "single" | Only used in the habituation phase.


# CSV file names and contents in relation to the current experiment goal

Each file name needs to be in the form of a "test" or a "hab" format (prefix: 'hab_'
or 'test_'). Examples are: `test_native_alt_A1.csv` or 
`hab_native_nalt_B2_sspeaker.csv`. *Test type* csv files contain two sounds 
that are contrasted, *habituation type* files contain a sequence of 12 tokens. 
In our current operationalization, the "not on first token alternating" only 
determines whether **the first pair of tokens** is a real contrast or not. 
So, for testing, an "alt" .csv in the current operationalization implies 
contrasts on ID 1, 5, 8 and 12, whereas "nalt" implies contrasts on ID 2, 5, 8 
and 12.

# Tokens, speakers and trials (specific)

A naming convention has been introduced in order to work towards a more generic 
way of using and reusing this type of experiment.

The format for naming stimuli becomes:

Speaker*speakerID*\_*type*\_*token*

eg.

	'Speaker1_faap_1.wav' -------> The first token by speaker 1 for type 'faap'
	'SpeakerJ_sEn_23.wav' -------> The 23d token by speaker J for type 'sEn'


This way, sounds and coding of sounds is better identifiable at a human **and** 
computer science level.



# Multiple or single speaker options during habituation phase

For brevity, let's truncate the following options for stimulus names, first 
considering a habituation phase in which 12 recordings of the same type have 
been made by a single speaker:

Speaker1_feep_1.wav  
Speaker1_feep_2.wav  
...  
Speaker1_feep_12.wav  

and coded in table from as:

s1-t1
s1-t2
...
s1-s12

As for headers, s1 means "Sound 1" , etc...

The input file for a single speaker habituation would then have the follwing 
structure:

id |   s1    |  s2     | s3     |  s4    |  s5    |  s6    |   s7    |  s8   |  s9   |  s10   |   s11  |  s12
---|---------|---------|--------|--------|--------|--------|---------|-------|-------|--------|--------|---------
1  | *s1-t1* | s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
2  | *s1-t2* | *s1-t1* | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
3  | *s1-t3* | s1-t2   | *s1-t1*| s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
4  | *s1-t4* | s1-t2   | s1-t3  | *s1-t1*| s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
5  | *s1-t5* | s1-t2   | s1-t3  | s1-t4  | *s1-t1*| s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
6  | *s1-t6* | s1-t2   | s1-t3  | s1-t4  | s1-t5  | *s1-t1*| s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
7  | *s1-t7* | s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | *s1-t1* | s1-t8 | s1-t9 | s1-t10 | s1-t11 | s1-t12
8  | *s1-t8* | s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   |*s1-t1*| s1-t9 | s1-t10 | s1-t11 | s1-t12
9  | *s1-t9* | s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 |*s1-t1*| s1-t10 | s1-t11 | s1-t12
10 | *s1-t10*| s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | *s1-t1*| s1-t11 | s1-t12
11 | *s1-t11*| s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | *s1-t1*| s1-t12
12 | *s1-t12*| s1-t2   | s1-t3  | s1-t4  | s1-t5  | s1-t6  | s1-t7   | s1-t8 | s1-t9 | s1-t10 | s1-t1  |*s1-t1*

For the multiple speaker habituation, the structure would be:

Speaker1_feep_1.wav  
Speaker2_feep_1.wav  
...  
Speaker12_feep_1.wav  

and coded in table from as:

s1-t1  
s2-t1  
...  
s12-s1  


The input file for a multiple speaker habituation would then have the following 
structure:

id |   s1    |  s2     | s3     |  s4    |  s5    |  s6    |   s7    |  s8   |  s9   |  s10   |   s11  |  s12
---|---------|---------|--------|--------|--------|--------|---------|-------|-------|--------|--------|---------
1  | *s1-t1* | s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
2  | *s2-t1* | *s1-t1* | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
3  | *s3-t1* | s2-t1   | *s1-t1*| s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
4  | *s4-t1* | s2-t1   | s3-t1  | *s1-t1*| s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
5  | *s5-t1* | s2-t1   | s3-t1  | s4-t1  | *s1-t1*| s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
6  | *s6-t1* | s2-t1   | s3-t1  | s4-t1  | s5-t1  | *s1-t1*| s7-t1   | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
7  | *s7-t1* | s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | *s1-t1* | s8-t1 | s9-t1 | s10-t1 | s11-t1 | s12-t1
8  | *s8-t1* | s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   |*s1-t1*| s9-t1 | s10-t1 | s11-t1 | s12-t1
9  | *s9-t1* | s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 |*s1-t1*| s10-t1 | s11-t1 | s12-t1
10 | *s10-t1*| s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | *s1-t1*| s11-t1 | s12-t1
11 | *s11-t1*| s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | *s1-t1*| s12-t1
12 | *s12-t1*| s2-t1   | s3-t1  | s4-t1  | s5-t1  | s6-t1  | s7-t1   | s8-t1 | s9-t1 | s10-t1 | s1-t1  |*s1-t1*

The idea behind this file stucture is: the first stimulus in a trial is fixed. 
The program automatically randomized the other 11 options. For file creation, 
the diagonal from top left to bottom right and the first column of sounds are 
the only values where one would have to change things, considering they were 
first copies of the first row.

# Example of test phase (token sequences of two, aka tokentuples)


#### Testing contrasts for type "feep" (contrast with "faap").
In the testing phase, a different flow starts. Let's say this is a "nalt"
version. Here, *token (version) 2* is *new* to the participant (so the contrast is on **type only**), with the newest type always presented first in the token-tuple.

id | sound 1    			      | sound 2   			      | extra (not in .csv)
---|------------------------|-----------------------|----------------------------------------
1  | Speaker1\_feep**\_2**  | Speaker1\_feep**\_2**  | Note the 'feep' token (version) 2 has not been heard before (token 1 was used in habituation)
2  | Speaker1\_**faap**\_2  | Speaker1_feep_2       |  the first actual contrast in terms of types
3  | Speaker1_feep_2        | Speaker1_feep_2       |
4  | Speaker1_feep_2        | Speaker1_feep_2       |
5  | Speaker1\_**faap**\_2  | Speaker1_feep_2       | alternation (type  contrast) on 5
6  | Speaker1_feep_2        | Speaker1_feep_2       |
7  | Speaker1_feep_2        | Speaker1_feep_2       |
8  | Speaker1\_**faap**\_2  | Speaker1_feep_2       | alternation on 8
9  | Speaker1_feep_2        | Speaker1_feep_2       |
10 | Speaker1_feep_2        | Speaker1_feep_2       |
11 | Speaker1_feep_2        | Speaker1_feep_2       |
12 | Speaker1\_**faap**\_2  | Speaker1_feep_2       | alternation on 12

# Output
One can get output by running `zepdbextract` in the experiment directory.
This generates the following tables.

*Regular output* (data useful for regular 'bulk' analysis within the paradigmn, info summised per trial)
hvf-01-pre_output-1.csv
hvf-01-hab_output-3.csv
hvf-01-test_output-5.csv
hvf-01-post_output-7.csv

*Stimulus based output* (if you want to check what stimulus was administered, etc.) 
hvf-01-pre_stim-2.csv
hvf-01-hab_stim-4.csv
hvf-01-test_stim-6.csv
hvf-01-post_stim-8.csv


# Requirements
- Zep installed. (From [here](http://beexy.org/zep/wiki/doku.php?id=download)
for instance)
- This experiment unarchived.
- A camera to record participant.
- A method to overlay the camera stream with the control window.
- A BeexyBox response box or for less accurate look-time measurements: a
keyboard.

# Running the experiment
- Navigate via the CLI/CMD to the folder or run `linux-terminal.sh` /
`windows-terminal.bat`.
- Run the command `zep hvf.zp`.
- Create a participant and enter participant data via the control window.
- Press `start`.
- Use the response box to continue and mark looking time onset/offset.
(Note: keyboard alternatives are `t` for looking time and `spacebar` for
continue)

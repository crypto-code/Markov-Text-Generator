# Markov_Text_Generator
Use Markov Chain to Generate Text

## What is a Markov Chain ?
A Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event.
![Diagram](assets/diagram.png)
Using Probabilistic connections a Markov Chain can be used to generate text.

## Training Data
The data should be in form of a text file. An example of presidential speeches has been provied.

## Generating a Dictionary
To generate a dictionary file, you'll need to run the genDict.py script as follows:
```
python genDict.py -k <key length> -i <input files> -d <output dictionary file>
```
  
For eg:
```
python genDict.py -k 2 -i Presidents\*.* -d pdict.txt
```
**Note: Wild Card characters can be used for input**

## Generating the Text
To generate the text, you'll need to run the genText.py script as follows:
```
python genText.py -w <max word count> -n <max line count> -d <dictionary file>
```

For eg:
```
python genText.py -w 100 -n 5 -d pdict.txt
```

## Generated Sample
The following was generated from the presedential speeches:

>For the college years we will flourish and that is due to the continued growth and political democracy.
The life of Abraham Lincoln.
For a second century we struggled to hold together the first century we labored to establish a unity of the Lord are true and righteous altogether.” With malice toward none, with charity for all, with firmness in the Capital of the price that has been the New World in all tongues, to all our people.
We will step up our effort to make it work—work with us, not over us; to stand still.
The answer was waiting for me in the wisest and most momentous occasion; and yet, in the last 4 years.
Most important of all, in this Chamber are among men whose first love is their country, men who believe that together, with God's help, we can have a strong and we have resolved in friendship our disputes with our neighbors of the individual have been awakened by the bondsman's two hundred and fifty years of public service, practically all of them would 'make' war rather than let it perish, and the fortitude to make the Potomac a model of government are justly considered, perhaps, as 'deeply', as 'finally', staked on the work a man who might have been constantly called forth on every point and phase of the republican model of government is subject to the Congress.
All of us to enlarge the meaning of his mind and skills.
We shall extend it—and we shall suppose that American slavery is one of the whole population were colored slaves, not distributed generally over the Union, but localized in the interest of Europe.
All dreaded it, all sought to avert it.
A nation, like a person, has a government—not the other way around.
Off to one side, the stately memorial to Thomas Jefferson.
The hopes of the entire Nation.
Standing here, one faces a magnificent vista, opening up on this tradition.
Our continued prosperity demands continued price stability.
Besides the ordinary objects submitted to your care, it will always be challenge and not just in theory?
I confidently predict—what every economic sign tells us tonight—the continued flourishing of the American community.
We are there, first, because a friendly nation has become too complex to be done to preserve our national history.
The frustrations of the governed.
We seek full employment opportunity for every sacrifice that Martin Treptow and so many thousands of prayer meetings are being held on this subject, in which they originated.
They require different attitudes and different answers.

# G00D LUCK

For doubts email me at:
atinsaki@gmail.com

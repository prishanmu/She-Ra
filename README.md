# She-Ra and the Princesses of Power
Text analysis of scripts from the recent reboot of She-Ra and the Princesses of Power

![She-Ra Header](https://66.media.tumblr.com/9b9f55574ad52fb049f922538d821f3e/591b7a4c7a6cb38a-df/s2048x3072/04187ca7d64acd1b132f8e0d489a7fe9c828afbb.jpg)

**Background Information**

She-Ra and the Princesses of Power is a Netflix reboot of the 80's cartoon, She-Ra: Princess of Power. Over the past few years, 52 episodes have come out and the series' stories have concluded. The series is known for its variety of representation, both causual and central to the story, and themes of friendship, abandonment, colonialism, and queer relationships. As a fan of the show and data scientist, I wanted to look deeper into the dailogue of the show.

**Data Source**

I gathered transcripts from a She-Ra fan-made wiki page. Since this source is dependent solely on fan contributions, there may be some mistakes and many episodes do not have complete scripts. I will be updating this repo and my data analysis as more scripts become available to me. For now, we can consider the results a reflection of mainly season 1 & 2. 

Link to Transcripts:https://she-raandtheprincessesofpower.fandom.com/wiki/Category:Transcripts

Below is a list of episodes for which I did not obtain a completed script: 

* Season 1: Episode 10
* Season 2: Episode 1, 3, 6, 7
* Season 3: Episode 1-4, 6
* Season 4: Episode 2-5, 9, 10, 12, 13
* Season 5: Episode 1-4, 7-12


**Research Questions**: 

*   Who are the main or most active characters of this show? Does this change by season? 
*   What are the most common words used by characters in this show?
* What are the most "important" words spoken by certain characters on this show? 
* What are some relationships among words on this show? 
* Sentiment Analysis by Character and Season
* Data Modeling: Can we predict which lines were spoken by Adora? or Catra? 

**Files in this Repo**:

* README.md: Markdown file discussing details of this project. 
* txt_scripts/: path to txt files of the show's scripts.
* img_files/: path to image files I used.
* tv_script_to_csv.py: Python file used to convert the txt files into one csv file.
* she_ra_dialogue.csv: CSV file with each line of dialogue and who said it during which episode. 
* She_Ra_Project.ipynb: Jupyter Notebook holding my text analysis work and completmentary data visualization. 
* Entrapta_Wordclouds.ipynb: Jupyter Notebook containing code to create some wordclouds using the character Entrapta's lines. Kept separate from the She_Ra notebooks as I used this work for a fan competition and not for the purpose of answering my research questions.  

While I will be uploading updates to my Jupyter Notebook on GitHub, the latest version will be on [Google Colab](https://colab.research.google.com/drive/1kkazlx1-L0pf5uvlMYmBeFjFPrXZ7wg-?usp=sharing).

**References**

* https://www.kaggle.com/ambarish/fun-in-text-mining-with-simpsons/report
* https://medium.com/data-slice/the-words-of-witches-wizards-7a1a96672ebf
* https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-bigrams/
* https://towardsdatascience.com/a-complete-exploratory-data-analysis-and-visualization-for-text-data-29fb1b96fb6a
* https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial#Gensim-Word2Vec%C2%A0Tutorial

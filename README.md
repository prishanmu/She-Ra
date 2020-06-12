# She-Ra and the Princesses of Power
Text Analysis of Scripts from the recent Reboot of She-Ra and the Princesses of Power

**Background Information**

She-Ra and the Princesses of Power is a Netflix reboot of the 80's cartoon, She-Ra: Princess of Power. Over the past few years, 52 episodes have come out and the series' stories have concluded. The series is known for its variety of representation, both causual and central to the story, and themes of friendship, abandonment, colonialism, and queer relationships. As a fan of the show and data scientist, I wanted to look deeper into the dailogue of the show.

**Data Source**

I gathered transcripts from a She-Ra fan-made wiki page. Since this source is dependent solely on fan contributions, there may be some mistakes and many episodes do not have complete scripts. I will be updating this repo and my data analysis as more scripts become available to me. For now, we can consider the results a reflection of mainly season 1 & 2. 

Link to Transcripts:https://she-raandtheprincessesofpower.fandom.com/wiki/Category:Transcripts

Below is a list of episodes for which I did not obtain a completed script: 

* Season 1: Episode 5, 7, 9
* Season 2: Episode 1, 3, 6, 7
* Season 3: Episode 1-4, 6, 7
* Season 4: Episode 2-5, 9, 10, 12, 13
* Season 5: Episode 1-4, 7-12

**References**

Other projects I was inspired by: 
* https://www.kaggle.com/ambarish/fun-in-text-mining-with-simpsons/report
* https://medium.com/data-slice/the-words-of-witches-wizards-7a1a96672ebf

**Research Questions**: 

*   Who are the main or most active characters of this show? Does this change by season? 
*   What are the most common words used by characters in this show?
* What are the most "important" words spoken by certain characters on this show? 
* What are some relationships among words on this show? 
* Sentiment Analysis by Character and Season
* Data Modeling: Can we predict which lines were spoken by Adora? or Catra? 

**Files in this Repo**:

* README.md: Markdown file discussing details of this project. 
* txt_scripts/: path to txt files of the show's scripts
* tv_script_to_csv.py: Python file used to convert the txt files into one csv file
* she_ra_dialogue.csv: CSV file with each line of dialogue and who said it during which episode. 
* She_Ra_Project.ipynb: Jupyter Notebook holding my text analysis work and completmentary data visualization. 

While I will be uploading updates to my Jupyter Notebook on GitHub, the latest version will be on [Google Colab](https://colab.research.google.com/drive/1kkazlx1-L0pf5uvlMYmBeFjFPrXZ7wg-?usp=sharing).

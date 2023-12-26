# Today_arxiv

This is a repo presenting a simple python script for arxiv crawling.
If you want to catch up the latest papers in your research areas, this project will help!

## Setup
```
git clone https://github.com/PaperRepos/Today_arxiv.git && cd Today_arxiv
pip install -r requirements.txt
```

## Run
```
python arxiv.py
cat today_arxiv.txt
```
### Demo GIF
<img src="https://github.com/PaperRepos/Today_arxiv/blob/main/fig/today.gif?raw=true">

## Tweak for your purpose
<img src="https://github.com/PaperRepos/Today_arxiv/blob/main/fig/today.png?raw=true">

### arXiv categories
In the script, you can add/remove the arxiv category to crawl. As shown above, you can edit `arxiv.py` to get what you want. There is `categories`, the categories to fetch; the arxiv categories can be found [here](https://arxiv.org/category_taxonomy).

### Number of papers in each category
Another knob is the number of papers to fetch in each category. By default, it is set as 100. You can also adjust this by your convenience.

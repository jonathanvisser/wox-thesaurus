## Description
A plugin that allows you to look-up any word from "Big Huge Thesaurus" (http://words.bighugelabs.com). This is great if you do a lot of writing - allowing you to stay in flow whilst spicing up your language with Wox's heads-up display.

![img](https://github.com/jonathanvisser/wox-thesaurus/raw/master/docs/wox-thesaurus.gif)

## First things
Please sign-up here for your own free API key: http://words.bighugelabs.com/api.php and edit the "main.py" file entering your API key value against the "API_KEY" constant.

## Usage
* Simply enter the letter "t" followed by the word you're searching for.
* The results are ordered by word class, and grouped by relationship type, such as "synonyms", "antonyms", and "similar terms".
* The search only begins for words with 3 or more characters.
* When words return many results, these are wrapped across multiple lines.

## Notes
This is a Python plug-in and requires that [Python](https://www.python.org/downloads/) is installed and in your "Path" variable. Although Wox states that it comes with a Python environment, on Windows, none of the Python plug-ins worked for me. So I installed Python and manually set the path variable, as shown [here](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/).

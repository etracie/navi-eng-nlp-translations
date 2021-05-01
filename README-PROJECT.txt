README:

1. web-scraper can be found in the zip file - it gathers the Navi and English posts and saves them in separate files
    A. credit to Kyle Tracy
2. stanza-train contains the bulk of the project
    A. credit to Stanford NLP Stanza
    B. to run:
        1. >> cd ./stanza-train
        2. >> pip install -r ./requirements.txt
            // if there's an error, you may need to manually install torch (pip install torch)
        3. >> cd stanza
        4. >> python aligining_nav_en.py
3. stanza contains additional information such as the data files and the tagging capabilities
    A. english_216lines.txt contains 216 lines of English translations
    B. navi-216lines.txt contains 216 of accompanying Navi translations

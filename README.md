# Values_Extractor-Python-Library
This repository was created to share with you my work and then make possible some pull requests to improve and turn wider the library.

To use the library, you need to clone the file in your computer, and then paste it in the following folder.

---------------------------------------------------------------------------
C:\Users\*Your user*\AppData\Local\Programs\Python\*Your Python folder*\Lib
---------------------------------------------------------------------------

After paste the library file there, now you are able to import the library in your code editor.
The code will return the values with the measurements units converted according to the S.I.

    Arguments
    ---------
    text_to_extract is the text that you want to extract the values.
    classification_type can be 'time', 'distance', 'speed' and it defines what type of results you want.
    all_printed=True is to print all results that the algorithm found.

    Examples
    --------
    Input:
    text = I have only 1 minute
    a = Values_Extractor(text, classification_time='time', all_printed=True)
    x = extractor()

    Output:
    x will be equal one list of lists with the values 

    In your terminal will be printed 60 sec too

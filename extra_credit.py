# -*- coding: utf-8 -*-
import csv

LINKS = 0
SPAM = 1
LENGTH = 2
SYMBOLS = 3
WORDNUMS = 4
LABEL = 5



def make_prediction(doesHaveLinks, doesHaveSpammyWords, lengthOfText, numberOfSymbols,
                    numberOfWordsContainingNumbersAndLetters):
    class_label_prediction = 'ham'
    lengthOfText = float(lengthOfText)
    numberOfSymbols = float(numberOfSymbols)
    numberOfWordsContainingNumbersAndLetters = float(numberOfWordsContainingNumbersAndLetters)
    if doesHaveSpammyWords == 'False' and numberOfWordsContainingNumbersAndLetters <= 0 and lengthOfText <= 98:
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'False' and numberOfWordsContainingNumbersAndLetters <= 0 and lengthOfText > 98 and doesHaveLinks == 'False':
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'False' and numberOfWordsContainingNumbersAndLetters <= 0 and lengthOfText > 98 and doesHaveLinks == 'True':
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'False' and 0 < numberOfWordsContainingNumbersAndLetters <= 2 and lengthOfText <= 133:
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'False' and lengthOfText <= 133 and numberOfWordsContainingNumbersAndLetters > 2:
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'False' and 0 < numberOfWordsContainingNumbersAndLetters <= 1 and 133 < lengthOfText <= 168:
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'False' and 133 < lengthOfText <= 168 and 1 < numberOfWordsContainingNumbersAndLetters <= 5 and numberOfSymbols <= 12:
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'False' and 133 < lengthOfText <= 168 and 1 < numberOfWordsContainingNumbersAndLetters <= 5 and numberOfSymbols > 12:
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'False' and 133 < lengthOfText <= 168 and numberOfWordsContainingNumbersAndLetters > 5:
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'False' and numberOfWordsContainingNumbersAndLetters > 0 and lengthOfText > 168:
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'True' and lengthOfText <= 114 and numberOfWordsContainingNumbersAndLetters <= 0 and doesHaveLinks == 'False':
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'True' and lengthOfText <= 114 and numberOfWordsContainingNumbersAndLetters <= 0 and doesHaveLinks == 'True':
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'True' and lengthOfText <= 114 and numberOfWordsContainingNumbersAndLetters > 0:
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'True' and lengthOfText > 114 and numberOfSymbols <= 11:
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'True' and lengthOfText > 114 and 11 < numberOfSymbols <= 14:
        class_label_prediction = 'spam'
    elif doesHaveSpammyWords == 'True' and lengthOfText > 114 and numberOfSymbols > 14 and numberOfWordsContainingNumbersAndLetters <= 1:
        class_label_prediction = 'ham'
    elif doesHaveSpammyWords == 'True' and lengthOfText > 114 and numberOfSymbols > 14 and numberOfWordsContainingNumbersAndLetters > 1:
        class_label_prediction = 'spam'

    return class_label_prediction


def determine_accuracy(actual, predicted):
    if actual == predicted:
        return True
    else:
        return False


def writeHeader():
    with open('extra_credit_predictions.csv', 'a', encoding="ISO-8859-1") as in_file:
        addingHeader = csv.writer(in_file, delimiter=',', quotechar='"')

        headers = ['doesHaveLinks', 'doesHaveSpammyWords', 'lengthOfText', 'numberOfSymbols', 'numberOfWordsContainingLettersAndNumbers', 'actual_class_label',
                   'predicted_class_label']
        addingHeader.writerow(headers)


# appends the features of each text to predictions.csv
def appendToNewCSV(row1, row2, row3, row4, row5, row6, row7):
    with open('extra_credit_predictions.csv', 'a', encoding="ISO-8859-1") as in_file:
        append = csv.writer(in_file, delimiter=',', quotechar='"')

        predictions = [row1, row2, row3, row4, row5, row6, row7]
        append.writerow(predictions)


def main():
    accuracies = 0
    inaccuracies = 0
    writeHeader()
    with open('extra_credit_testing_data.csv', 'r', encoding="ISO-8859-1") as in_file:
        reader = csv.reader(in_file, delimiter=',')

        # skips to the text message column
        header_row = next(reader)

        for row in reader:
            prediction = make_prediction(row[LINKS], row[SPAM], row[LENGTH], row[SYMBOLS], row[WORDNUMS])
            appendToNewCSV(row[LINKS], row[SPAM], row[LENGTH], row[SYMBOLS], row[WORDNUMS], row[LABEL], prediction)
            outcome = determine_accuracy(row[LABEL], prediction)
            if outcome:
                accuracies += 1
            else:
                inaccuracies += 1
    accuracy = (accuracies / (accuracies + inaccuracies)) * 100
    print("The accuracy is " + str(accuracy) + "%.")


main()

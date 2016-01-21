import pygame

## @package Utilities
#  Documentation for the Utilities module.
#
#  The Utilities module is a set of functions that have no specific class.
#  These functions can be used when needed and are best separate for reusability.

## A function to test for if two rectangles intersect.
#  @param rect1Pos The position of the first rectangle.
#  @param rect1Dim The dimensions of the first rectangle.
#  @param rect2Pos The position of the second rectangle.
#  @param rect2Dim The position of the second rectangle.
#  @returns A True/False value for if the two rectangles intersect.
def rectRectIntersection(rect1Pos, rect1Dim, rect2Pos, rect2Dim):
    #Check to see if the two rectangles are NOT intersecting.
    if rect1Pos.x > (rect2Pos.x + rect2Dim.x) or (rect1Pos.x + rect1Dim.x) < rect2Pos.x \
            or rect1Pos.y > (rect2Pos.y + rect2Dim.y) or (rect1Pos.y + rect1Dim.y) < rect2Pos.y:
        #There is no intersection.
        return False
    #Otherwise there is an intersection.
    return True

## A function load in the scores from scores.txt.
#  @returns An int array of the scores
def loadScores():
    # Opens scores.txt and loads each line in to a new element in the loadedScores array
    scoresFile = open('scores.txt', 'r')
    loadedScores = scoresFile.readlines()
    # Closes the file
    scoresFile.close()

    # Remove the /n from the end of each line
    for i in range(0, len(loadedScores)):
        loadedScores[i] = loadedScores[i].replace("\n", "")

    # Convert to a int array
    scores = []
    for i in range(0, len(loadedScores)):
        scores.append(int(loadedScores[i]))

    # Return the array of scores
    return scores

## A function write the scores to scores.txt.
#  @param scores The int array of the scores
def saveScores(scores):
    # Opens the file for writing to
    scoresFile = open("scores.txt", "w")

    # Writes the scores to the file
    for i in range(0, len(scores)):
        scoresFile.write("%d\n" % scores[i])

    # Closes the file
    scoresFile.close()

## A function sorts the scores and the latest score into the correct order and removes the lowest score.
#  @param latestScore The latest score
#  @param scores The int array of the scores
#  @returns The sorted array of the scores
def sortScores(latestScore, scores):
    # Add the latest score to the array of scores
    scores.append(latestScore)

    # Sort the array in descending order
    scores = sorted(scores, reverse=True)

    # Remove the last element in the array
    scores.pop()

    # Return the new array of scores
    return scores
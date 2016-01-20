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
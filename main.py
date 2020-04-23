
from PIL import Image
import copy
import numpy as np
import pandas as pd
from itertools import islice
from env import path

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def main():
    dataFrameManager = DataFrameManager()
    print(path)
    # path = 

    # sort data train,
    # if character new, create new ObjectDeterminant
    # qualify character new, if zero space or sizing is different.
    # marginalize data for likely.
    # after train set, move to more text.
    # filter through analysis, update FQ

    listCharacterPixels = dataFrameManager.calculateBlackBackgroundFeatureSetIdentificationObjectComposite(path)

    listModifiedKnownFeatureSetIdentificationObject = []
    listCharacterPixels = dataFrameManager.seperateCharactersByZeroSpaceColumnsReturnListCharacterPixelsLight(path)
    # listCharacterPixels = dataFrameManager.seperateCharactersByZeroSpaceColumnsReturnListCharacterPixelsDark(path)
    print("len")
    print(len(listCharacterPixels))
    indexCharacterPixel = 0
    for characterPixels in listCharacterPixels:

        knownFeatureSetIdentificationObjectComposite = FeatureSetIdentificationObjectComposite()

        # print("len(listCharacterPixels)")
        # print(len(listCharacterPixels[5]))
        if len(characterPixels) == 0:
            continue
        # knownFeatureSetIdentificationObject = dataFrameManager.calculateFeatureSetIdentificationObjectComposite1(listCharacterPixels[9])
        knownFeatureSetIdentificationObject = dataFrameManager.calculateFeatureSetIdentificationObjectComposite1(characterPixels)
        modifiedKnownFeatureSetIdentificationObject = dataFrameManager.calculateAllZeroSpaceInFeatureSetIdentificationObject(knownFeatureSetIdentificationObject)

        #Now have all zeriozed in lim zeroSpace objects.
        #now calculate continuity.

        modifiedKnownFeatureSetIdentificationObject = dataFrameManager.calculateZeroSpaceContinuity(modifiedKnownFeatureSetIdentificationObject)
        #Need hook featureSetIdentificationObject continuity.
        

        # print("len(calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject)")
        # print(len(modifiedKnownFeatureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject))
        # for zeroSpaceObject in modifiedKnownFeatureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
        #     print("SPACER")
        #     for listValue in zeroSpaceObject.listResults:
        #         for pixelObject in listValue:
        #             print("pixelObject.xValue")
        #             print(pixelObject.xValue)
        #             print(pixelObject.yValue)

        # print("len(modifiedKnownFeatureSetIdentificationObject.pixelObjectComposite.listPixelObjects)")
        # print(len(modifiedKnownFeatureSetIdentificationObject.pixelObjectComposite.listPixelObjects))
        if len(modifiedKnownFeatureSetIdentificationObject.pixelObjectComposite.listPixelObjects) == 1:
            modifiedKnownFeatureSetIdentificationObject.numberClassified = "."
            listModifiedKnownFeatureSetIdentificationObject.append(modifiedKnownFeatureSetIdentificationObject)
            indexCharacterPixel += 1
            continue

        dataFrameManager.calculateZeroSpacePercentageOccupy(modifiedKnownFeatureSetIdentificationObject)

        
        dataFrameManager.calculateZeroSpaceBorderConnectivity(modifiedKnownFeatureSetIdentificationObject)

        # modifiedKnownFeatureSetIdentificationObject.numberClassified = dataFrameManager.classifyNumber(modifiedKnownFeatureSetIdentificationObject)
        # print("modifiedKnownFeatureSetIdentificationObject.numberClassified")
        # print(modifiedKnownFeatureSetIdentificationObject.numberClassified)


        listModifiedKnownFeatureSetIdentificationObject.append(modifiedKnownFeatureSetIdentificationObject)
        # if indexCharacterPixel == 2:
        #     break
        indexCharacterPixel += 1


    # print("modifiedKnownFeatureSetIdentificationObject.numberClassified")
    # for modifiedKnownFeatureSetIdentificationObject in listModifiedKnownFeatureSetIdentificationObject:
    #     print(modifiedKnownFeatureSetIdentificationObject.numberClassified)

    # # given where percentage occupy is above a given percentile, match percentile meaningful and borders of native set.
    # # calculateMatch


    # xList = []
    # yList = []
    # pixelObjectComposite = knownFeatureSetIdentificationObject.pixelObjectComposite
    # for pixel in pixelObjectComposite.listZeroizedPixelObjects:
    #     xList.append(pixel.xValue)
    #     yList.append(pixel.yValue)
    # d = {'x':xList,'y':yList}
    # df = pd.DataFrame(d)
    # xLim =  pixelObjectComposite.xLim
    # yLim =  pixelObjectComposite.yLim
    # df.plot(kind='scatter',x='x',y='y',color='red', ylim=(0,yLim),xlim=(0,xLim))
    # plt.show()
# def calculateIsZeroSpaceAboveMedianThreshold():
#     continue
# def calculateFromDataSetCompositeRelevantFeaturesForCharacter():
#     continue
# def calculateRelevantTests():
#     #test 1
#     continue

#single out qualifiers.
#intake data, 


#update featureQualifiers
#calculate determinate feature qualifiers.
#attatch to tests
#support making tests, finding most relevant qualifies
#sorting incoming data for fq determination



def calculateQuadBorder(testingFeatureSetIdentificationObject, listCalculateFeatureSetIdentificationObject):
    # if isQuadBorderCondition:
    possibleMatches = listCalculateFeatureSetIdentificationObject
    
    # differentiate between 8 and 0 
    # if no gap between top and bottom segment
    # then case is zero
    continueOperationQuadBorderCondition = False
    listWhiteSpaceContinuityCalculationComposite = calculateIsWhiteSpaceContinuityFromMinLimToMaxLim(testingFeatureSetIdentificationObject, False, True, True)
    isAnyWhiteSpacePresent = calculateIsAnyWhiteSpacePresent(listWhiteSpaceContinuityCalculationComposite)


    if isAnyWhiteSpacePresent:
        print("inside any white")
        # possibleMatches = [knownFeatureSetIdentificationObjectComposite.listFeatureSetIdentificationObject[0]]
        characterIdentifier = 5
        possibleMatches = removeFeatureSetIdentificationObjectFromListByCharacterIdentifier(characterIdentifier, possibleMatches)
        characterIdentifier = 8
        possibleMatches = removeFeatureSetIdentificationObjectFromListByCharacterIdentifier(characterIdentifier, possibleMatches)
        


    if isAnyWhiteSpacePresent == False:
        print("inside any False")
        characterIdentifier = 0
        possibleMatches = removeFeatureSetIdentificationObjectFromListByCharacterIdentifier(characterIdentifier, possibleMatches)
        continueOperationQuadBorderCondition = True
        
    if continueOperationQuadBorderCondition:
        print("continuing")
        #calculate difference 8 and 5 
        listWhiteSpaceContinuityCalculationComposite = calculateIsWhiteSpaceContinuityFromMinLimToMaxLim(testingFeatureSetIdentificationObject, True, True, False)
        isAnyWhiteSpacePresent = calculateIsAnyWhiteSpacePresent(listWhiteSpaceContinuityCalculationComposite)
        print("isAnyWhiteSpacePresent")
        print(isAnyWhiteSpacePresent)
        if isAnyWhiteSpacePresent:
            characterIdentifier = 8
            possibleMatches = removeFeatureSetIdentificationObjectFromListByCharacterIdentifier(characterIdentifier, possibleMatches)
        
        if isAnyWhiteSpacePresent == False:
            characterIdentifier = 5
            possibleMatches = removeFeatureSetIdentificationObjectFromListByCharacterIdentifier(characterIdentifier, possibleMatches)
        
        # print("possibleMatches")
        # print("len(possibleMatches)")
        # print(len(possibleMatches))
        # print(possibleMatches[0].characterIdentifier)
    
    return possibleMatches

def calculateClosestSegmentToMedian(isXAxis, featureSetIdentificationObject):
    if isXAxis:
        for segment in featureSetIdentificationObject.listSegmentXDelimiter:
            #calculate closest to median
            #handle on median
            print("featureSetIdentificationObject.medianXValue")
            print(featureSetIdentificationObject.medianXValue)

    if isXAxis == False:
        lowestDistanceFromMedian = 0
        lowestDistanceIndex = 0
        indexSegment = 0
        
        for segment in featureSetIdentificationObject.listSegmentYDelimiter:
            #calculate closest to median
            #handle on median
            # calculate distance from medyan

            currentDistanceFromMedian = featureSetIdentificationObject.medianXValue - segment.pixelList[0].yValue
            #correct for negative values.
            if currentDistanceFromMedian < 0:
                # print("negative")
                currentDistanceFromMedian = currentDistanceFromMedian / -1
            # print("print(currentDistanceFromMedian)")
            # print(currentDistanceFromMedian)

            if indexSegment == 0:
                lowestDistanceFromMedian = currentDistanceFromMedian
                indexSegment += 1
                continue
           
            if currentDistanceFromMedian < lowestDistanceFromMedian:
                lowestDistanceFromMedian = currentDistanceFromMedian
                lowestDistanceIndex = indexSegment
            indexSegment += 1
            
    print("lowestDistanceFromMedian")
    print(lowestDistanceFromMedian)
    print("lowestDistanceIndex")
    print(lowestDistanceIndex)
    return lowestDistanceIndex
        


    


def calculateIsAnyWhiteSpacePresent(listWhiteSpaceContinuityCalculationComposite):
    isAnyWhiteSpacePresent = False

    for whiteSpaceContinuityCalculationComposite in listWhiteSpaceContinuityCalculationComposite:
        # print("break")
        for whiteSpaceContinuityCalculation in whiteSpaceContinuityCalculationComposite.listWhiteSpaceContinuityCalculation:
            print(whiteSpaceContinuityCalculation.isWhiteSpaceContinuity)
            if whiteSpaceContinuityCalculation.isWhiteSpaceContinuity:
                isAnyWhiteSpacePresent = True 
                break

    print("isAnyWhiteSpacePresent")
    print(isAnyWhiteSpacePresent)
    return isAnyWhiteSpacePresent


def removeFeatureSetIdentificationObjectFromListByCharacterIdentifier(characterIdentifier, listFeatureSetIdentificationObject):
    modifiedListFeatureSetIdentificationObject = listFeatureSetIdentificationObject
    #remove at index 
    #find at index
    #identifer for known will be the number they represent

    indexToRemove = 0
    indexFeatureSetIdentificationObject = 0
    for featureSetIdentificationObject in listFeatureSetIdentificationObject:
        if featureSetIdentificationObject.characterIdentifier == characterIdentifier:
            indexToRemove = indexFeatureSetIdentificationObject
        indexFeatureSetIdentificationObject += 1

    del modifiedListFeatureSetIdentificationObject[indexToRemove:indexToRemove+1]

    return modifiedListFeatureSetIdentificationObject

def calculateIsWhiteSpaceContinuityFromMinLimToMaxLim(featureSetIdentificationObject, isXAxis, isNegativeDirection, isBorder):
    
    listWhiteSpaceContinuityCalculationComposite = []
    if isXAxis:
        print("xaxi")
        for segment in featureSetIdentificationObject.borderSegmentCalculationX.listPixelSegmentMatchingLim:
            whiteSpaceContinuityCalculationComposite = WhiteSpaceContinuityCalculationComposite()
            for pixel in segment.pixelList:
                whiteSpaceContinuityCalculation = WhiteSpaceContinuityCalculation()
                # isNegativeDirection = True
                pixelX = pixel

                # print("pixel.xValue")
                # print(pixelX.xValue)
                # print(pixelX.yValue)
                
                originPixelXSeeking = pixelX.xValue
                originPixelYSeeking = pixelX.yValue
                # #handle while iterable 
                xLim =  featureSetIdentificationObject.pixelObjectComposite.xLim
                if isBorder:
                    xLim = xLim - 1

                pixelXSeeking = originPixelXSeeking
                pixelYSeeking = originPixelYSeeking

                previousXValue = originPixelXSeeking
                # handle where one pixel out of pixel list, iterate to lim min see there is no black markation
                
                isMarkationPresent = False
                indexOperation = 0 
                while indexOperation < xLim:
                    if isNegativeDirection:
                        pixelXSeeking = previousXValue - 1
                        previousXValue = pixelXSeeking

                    # print("pixelXSeeking")
                    # print(pixelXSeeking)
                    # print("pixelYSeeking")
                    # print(pixelYSeeking)
                    indexSegmentSeeking = 0
                    for pixelY in featureSetIdentificationObject.pixelObjectComposite.listZeroizedPixelObjects:
                        if pixelXSeeking == pixelY.xValue:
                            if pixelYSeeking == pixelY.yValue:
                                isMarkationPresent = True
                                
                                print("hitx")
                                break
                        indexSegmentSeeking += 1
                    indexOperation += 1

                if isMarkationPresent == False:
                    whiteSpaceContinuityCalculation.isWhiteSpaceContinuity = True

                whiteSpaceContinuityCalculationComposite.listWhiteSpaceContinuityCalculation.append(whiteSpaceContinuityCalculation)
            listWhiteSpaceContinuityCalculationComposite.append(whiteSpaceContinuityCalculationComposite)

    if isXAxis == False:
        print("y axis")
        for segment in featureSetIdentificationObject.borderSegmentCalculationY.listPixelSegmentMatchingLim:
            whiteSpaceContinuityCalculationComposite = WhiteSpaceContinuityCalculationComposite()
            for pixel in segment.pixelList:
                # print("pixel.xValue")
                # print(pixel.xValue)
                # print(pixel.yValue)
                whiteSpaceContinuityCalculation = WhiteSpaceContinuityCalculation()
                # isNegativeDirection = True
                pixelY = pixel
                
                originPixelXSeeking = pixelY.xValue
                originPixelYSeeking = pixelY.yValue
                # #handle while iterable 
                yLim =  featureSetIdentificationObject.pixelObjectComposite.yLim #listZeroizedPixelObjects[featureSetIdentificationObject.pixelObjectComposite.xLim].xValue

                pixelXSeeking = originPixelXSeeking
                pixelYSeeking = originPixelYSeeking

                previousYValue = originPixelYSeeking
                # handle where one pixel out of pixel list, iterate to lim min see there is no black markation
                

                if isBorder:
                    yLim = yLim - 1

                isMarkationPresent = False
                indexOperation = 0 
                while indexOperation < yLim:
                    if isNegativeDirection:
                        pixelYSeeking = previousYValue - 1
                        previousYValue = pixelYSeeking

                    # print("pixelXSeeking")
                    # print(pixelXSeeking)
                    # print("pixelYSeeking")
                    # print(pixelYSeeking)

                    indexSegmentSeeking = 0
                    for pixelX in featureSetIdentificationObject.pixelObjectComposite.listZeroizedPixelObjects:
                        if pixelYSeeking == pixelX.yValue:
                            if pixelXSeeking == pixelX.xValue:
                                isMarkationPresent = True
                                print("hit")
                                break
                        indexSegmentSeeking += 1
                    indexOperation += 1

                if isMarkationPresent == False:
                    whiteSpaceContinuityCalculation.isWhiteSpaceContinuity = True

                whiteSpaceContinuityCalculationComposite.listWhiteSpaceContinuityCalculation.append(whiteSpaceContinuityCalculation)
            listWhiteSpaceContinuityCalculationComposite.append(whiteSpaceContinuityCalculationComposite)

    return listWhiteSpaceContinuityCalculationComposite


def calculateIsWhiteSpaceContinuityFromSegmentToLim(segment, featureSetIdentificationObject, isXAxis, isPositiveDirection, isBorder):
    listWhiteSpaceContinuityCalculationComposite = []
    if isXAxis:
        for segment in featureSetIdentificationObject.borderSegmentCalculationX.listPixelSegmentMatchingLim:
            whiteSpaceContinuityCalculationComposite = WhiteSpaceContinuityCalculationComposite()
            for pixel in segment.pixelList:
                whiteSpaceContinuityCalculation = WhiteSpaceContinuityCalculation()
                isNegativeDirection = True
                pixelX = pixel
                
                originPixelXSeeking = pixelX.xValue
                originPixelYSeeking = pixelX.yValue
                # #handle while iterable 
                xLim =  featureSetIdentificationObject.pixelObjectComposite.listZeroizedPixelObjects[featureSetIdentificationObject.pixelObjectComposite.xLim].xValue

                if isBorder:
                    xLim = xLim - 1

                pixelXSeeking = originPixelXSeeking
                pixelYSeeking = originPixelYSeeking

                previousXValue = originPixelXSeeking
                # handle where one pixel out of pixel list, iterate to lim min see there is no black markation
                
                isMarkationPresent = False
                indexOperation = 0 
                while indexOperation < xLim:
                    if isNegativeDirection:
                        pixelXSeeking = previousXValue - 1
                        previousXValue = pixelXSeeking

                    indexSegmentSeeking = 0
                    for pixelY in featureSetIdentificationObject.pixelObjectComposite.listZeroizedPixelObjects:
                        if pixelXSeeking == pixelY.xValue:
                            if pixelYSeeking == pixelY.yValue:
                                isMarkationPresent = True
                                break
                        indexSegmentSeeking += 1
                    indexOperation += 1

                if isMarkationPresent == False:
                    whiteSpaceContinuityCalculation.isWhiteSpaceContinuity = True

                whiteSpaceContinuityCalculationComposite.listWhiteSpaceContinuityCalculation.append(whiteSpaceContinuityCalculation)
            listWhiteSpaceContinuityCalculationComposite.append(whiteSpaceContinuityCalculationComposite)

    if isXAxis == False:
        print("y axis")
        for segment in featureSetIdentificationObject.borderSegmentCalculationY.listPixelSegmentMatchingLim:
            whiteSpaceContinuityCalculationComposite = WhiteSpaceContinuityCalculationComposite()
            for pixel in segment.pixelList:
                whiteSpaceContinuityCalculation = WhiteSpaceContinuityCalculation()
                isNegativeDirection = True
                pixelY = pixel
                
                originPixelXSeeking = pixelY.xValue
                originPixelYSeeking = pixelY.yValue
                # #handle while iterable 
                yLim =  featureSetIdentificationObject.pixelObjectComposite.yLim #listZeroizedPixelObjects[featureSetIdentificationObject.pixelObjectComposite.xLim].xValue

                pixelXSeeking = originPixelXSeeking
                pixelYSeeking = originPixelYSeeking

                previousYValue = originPixelYSeeking
                # handle where one pixel out of pixel list, iterate to lim min see there is no black markation
                

                if isBorder:
                    yLim = yLim - 1

                isMarkationPresent = False
                indexOperation = 0 
                while indexOperation < yLim:
                    if isNegativeDirection:
                        pixelYSeeking = previousYValue - 1
                        previousYValue = pixelYSeeking

                    indexSegmentSeeking = 0
                    for pixelX in featureSetIdentificationObject.pixelObjectComposite.listZeroizedPixelObjects:
                        if pixelYSeeking == pixelX.yValue:
                            if pixelXSeeking == pixelX.xValue:
                                isMarkationPresent = True
                                break
                        indexSegmentSeeking += 1
                    indexOperation += 1

                if isMarkationPresent == False:
                    whiteSpaceContinuityCalculation.isWhiteSpaceContinuity = True

                whiteSpaceContinuityCalculationComposite.listWhiteSpaceContinuityCalculation.append(whiteSpaceContinuityCalculation)
            listWhiteSpaceContinuityCalculationComposite.append(whiteSpaceContinuityCalculationComposite)

    return listWhiteSpaceContinuityCalculationComposite

def calculateBorderSegmentX(featureSetIdentificationObject):
    borderSegmentCalculation = BorderSegmentCalculation()
    xLim =  featureSetIdentificationObject.pixelObjectComposite.xLim

    pixelMatchingLim = PixelObject()
    for segment in featureSetIdentificationObject.listSegmentXDelimiter:
        for pixel in segment.pixelList:
            if pixel.xValue == 0:
                borderSegmentCalculation.isSegmentNegativeBoundary = True
                break
            if pixel.xValue == 1:
                borderSegmentCalculation.isSegmentNegativeBoundary = True
                break

        for pixel in segment.pixelList:
            if pixel.xValue == xLim:
                borderSegmentCalculation.isSegmentPositiveBoundary = True
                borderSegmentCalculation.listPixelSegmentMatchingLim.append(segment)
                break
            if pixel.xValue == xLim - 1:
                borderSegmentCalculation.isSegmentPositiveBoundary = True
                borderSegmentCalculation.listPixelSegmentMatchingLim.append(segment)
                break

                
    return borderSegmentCalculation

def calculateBorderSegmentY(featureSetIdentificationObject):
    borderSegmentCalculation = BorderSegmentCalculation()
    yLim = featureSetIdentificationObject.pixelObjectComposite.yLim

    for segment in featureSetIdentificationObject.listSegmentYDelimiter:
        for pixel in segment.pixelList:
            if pixel.yValue == 0:
                borderSegmentCalculation.isSegmentNegativeBoundary = True
                break
            if pixel.yValue == 1:
                borderSegmentCalculation.isSegmentNegativeBoundary = True
                break
        for pixel in segment.pixelList:
            if pixel.yValue == yLim:
                borderSegmentCalculation.isSegmentPositiveBoundary = True
                borderSegmentCalculation.listPixelSegmentMatchingLim.append(segment)
                break
            if pixel.yValue == yLim - 1:
                borderSegmentCalculation.isSegmentPositiveBoundary = True
                borderSegmentCalculation.listPixelSegmentMatchingLim.append(segment)
                break
    return borderSegmentCalculation

class ColumnScan:
    def __init__(self):
        self.listBlackAreaReadingColumn = []
        # self.fullRangeSet = None
        # self.markationSet = None
        # self.name = "henry"

    def getListBlackAreaReadingColumn(self):
        return self.listBlackAreaReadingColumn

    def insertBlackAreaReadingColumnIntoList(self, value):
        self.listBlackAreaReadingColumn.append(value)

class BlackAreaReadingColumn:
    def __init__(self):
        self.rowStartPoint = None
        self.rowEndPoint = None
        self.distanceBetween = "distance 10"

    def getDistanceBetween(self):
        return self.distanceBetween

class DataFrameManager:
    def __init__(self):
        cortexicalThought = []
    def classifyNumber(self, featureSetIdentificationObject):
        indexZeroSpaceObject = 0
        meaningfulZeroSpaceList = []
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
 
            # if zeroSpaceObject.percentageOccupy > .1:
            print("zeroSpaceObject.percentageOccupy")
            print(zeroSpaceObject.percentageOccupy)
            print(zeroSpaceObject.isMinLimXBorder)
            print(zeroSpaceObject.isMaxLimXBorder)
            print(zeroSpaceObject.isMinLimYBorder)
            print(zeroSpaceObject.isMaxLimYBorder)
            # print("indexZeroSpaceObject")
            # print(indexZeroSpaceObject)
            meaningfulZeroSpaceList.append(zeroSpaceObject)

            # indexZeroSpaceObject += 1
        

        highestZeroSpaceObjectPercentageOccupy = ZeroSpaceObject()
        result = -1
        #0 case
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .416:
                if zeroSpaceObject.percentageOccupy < .5:
                    if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                        result = "0"

        #1 case
        isOneCaseCondition1 = False
        isOneCaseCondition2 = True

        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .416:
                if zeroSpaceObject.percentageOccupy < .417:
                    if zeroSpaceObject.isMinLimXBorder and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder:
                        isOneCaseCondition1 = True
                        continue
            if zeroSpaceObject.percentageOccupy >= .5:
                if zeroSpaceObject.percentageOccupy < .51:
                    isOneCaseCondition2 = False
                            # if zeroSpaceObject.isMinLimXBorder and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder:
                            #     result = 1
        
        if isOneCaseCondition1 and isOneCaseCondition2:
            result = "1"

        #2 case
        isTwoCaseCondition1 = False
        isTwoCaseCondition2 = False
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .33:
                if zeroSpaceObject.percentageOccupy < .35:
                    if zeroSpaceObject.isMinLimXBorder and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                        isTwoCaseCondition1 = True
                        continue
            # if zeroSpaceObject.percentageOccupy >= .29:
            #     if zeroSpaceObject.percentageOccupy < .30:
            #     # if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
            #         # print("one")
            #         isTwoCaseCondition2 = True

        
        # for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
        #     if zeroSpaceObject.percentageOccupy == .29:
        #         if zeroSpaceObject.percentageOccupy < .30:
        #             # if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
        #                 # print("one")
        #             isTwoCaseCondition2 = True
        
        if isTwoCaseCondition1: #and isTwoCaseCondition2:
            result = "2"

        #3 case
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .416:
                if zeroSpaceObject.percentageOccupy < .5:
                    if zeroSpaceObject.isMinLimXBorder and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                        result = "3"
  

        #4 case
        isFourCaseCondition1 = False
        isFourCaseCondition2 = False
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .20:
                if zeroSpaceObject.percentageOccupy < .21:
                    isFourCaseCondition1 = True
                    continue
                if zeroSpaceObject.percentageOccupy > .20:
                    if zeroSpaceObject.percentageOccupy < .21:
                        isFourCaseCondition2 = True

        # for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
        #     if zeroSpaceObject.percentageOccupy > .20:
        #         if zeroSpaceObject.percentageOccupy < .21:
        #             isFourCaseCondition2 = True
        
        if isFourCaseCondition1 and isFourCaseCondition2:
            result = "4"

        #5 case
        isFiveCaseCondition1 = False
        isFiveCaseCondition2 = True
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .29:
                if zeroSpaceObject.percentageOccupy < .35:
                    if zeroSpaceObject.isMinLimXBorder and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                        isFiveCaseCondition1 = True
                        continue

        # for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .29:
                if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                     
                # if zeroSpaceObject.percentageOccupy < .26:
                    isFiveCaseCondition2 = False
        
        if isFiveCaseCondition1 and isFiveCaseCondition2:
            result = "5"

        

        #6 case
        isSixCaseCondition1 = False
        isSixCaseCondition2 = False
        # isSixCaseCondition3 = False
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy >= .25:
                if zeroSpaceObject.percentageOccupy < .26:
                    isSixCaseCondition1 = True
                    continue
            
            if zeroSpaceObject.percentageOccupy >= .20:
                if zeroSpaceObject.percentageOccupy < .21:
                # if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                    # print("one")
                    isSixCaseCondition2 = True
        
        if isSixCaseCondition1 and isSixCaseCondition2:
            result = "6"

        # for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
        #     if zeroSpaceObject.percentageOccupy > .16:
        #         if zeroSpaceObject.percentageOccupy < .17:
        #             isSixCaseCondition2 = True
        
        # for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
        #     if zeroSpaceObject.percentageOccupy > .0416:
        #         if zeroSpaceObject.percentageOccupy < .0417:
        #             if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder:
        #                 isSixCaseCondition3 = True
        # if isSixCaseCondition1 and isSixCaseCondition2 and isSixCaseCondition3:
        #     print("six")

        #7 case
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy >= .5:
                if zeroSpaceObject.percentageOccupy < .51:
                    result = "7"
        
        #8 case
        isEightCaseCondition1 = False
        isEightCaseCondition2 = False
        listCopyCaseMatch = []
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy >= .08:
                if zeroSpaceObject.percentageOccupy < .085:
                    isEightCaseCondition1 = True
                    listCopyCaseMatch.append(0)
            # if zeroSpaceObject.percentageOccupy >= .08:
            #     if zeroSpaceObject.percentageOccupy < .085:
            #         isEightCaseCondition2 = True
                    
        
        if len(listCopyCaseMatch) == 2:
            isEightCaseCondition2 = True
        if isEightCaseCondition1 and isEightCaseCondition2:
            result = "8"

        #9 case
        isNineCaseCondition1 = False
        isNineCaseCondition2 = False
        isNineCaseCondition3 = False
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy >= .12:
                if zeroSpaceObject.percentageOccupy < .126:
                    isNineCaseCondition1 = True

        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .16:
                if zeroSpaceObject.percentageOccupy < .17:
                    isNineCaseCondition2 = True
        
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            if zeroSpaceObject.percentageOccupy > .0416:
                if zeroSpaceObject.percentageOccupy < .0417:
                    if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
                        isNineCaseCondition3 = True

        if isNineCaseCondition1 and isNineCaseCondition2 and isNineCaseCondition3:
            result = "9"

        return result



        # if len(meaningfulZeroSpaceList) <= 2:
        #     highestZeroSpaceObjectPercentageOccupy = ZeroSpaceObject()
        #     indexCalculation = 0
        #     for zeroSpaceObject in meaningfulZeroSpaceList:
        #         if indexCalculation == 0:
        #             highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #             indexCalculation += 1
        #             continue
        #         if zeroSpaceObject.percentageOccupy > highestZeroSpaceObjectPercentageOccupy.percentageOccupy:
        #             highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #         indexCalculation += 1
        #     zeroSpaceObject = highestZeroSpaceObjectPercentageOccupy
        #     # print('zeroSpaceObject.percentageOccupy')
        #     # print(zeroSpaceObject.percentageOccupy)
        #     if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
        #         print("zero")

        # #1 case
        # if len(meaningfulZeroSpaceList) <= 2:
        #     highestZeroSpaceObjectPercentageOccupy = ZeroSpaceObject()
        #     indexCalculation = 0
        #     for zeroSpaceObject in meaningfulZeroSpaceList:
        #         if indexCalculation == 0:
        #             highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #             indexCalculation += 1
        #             continue
        #         if zeroSpaceObject.percentageOccupy > highestZeroSpaceObjectPercentageOccupy.percentageOccupy:
        #             highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #         indexCalculation += 1
        #     zeroSpaceObject = highestZeroSpaceObjectPercentageOccupy
        #     if zeroSpaceObject.isMinLimXBorder and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder:
        #         print("one")
        # #2 case
        # if len(meaningfulZeroSpaceList) == 2:
        #     # highestZeroSpaceObjectPercentageOccupy = ZeroSpaceObject()
        #     # indexCalculation = 0
        #     # for zeroSpaceObject in meaningfulZeroSpaceList:
        #     #     if indexCalculation == 0:
        #     #         highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #     #         indexCalculation += 1
        #     #         continue
        #     #     if zeroSpaceObject.percentageOccupy > highestZeroSpaceObjectPercentageOccupy.percentageOccupy:
        #     #         highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #     #     indexCalculation += 1
        #     # zeroSpaceObject = highestZeroSpaceObjectPercentageOccupy
        #     if meaningfulZeroSpaceList[0].isMinLimXBorder and meaningfulZeroSpaceList[0].isMaxLimXBorder == False and meaningfulZeroSpaceList[0].isMinLimYBorder == False and meaningfulZeroSpaceList[0].isMaxLimYBorder == False:
        #         if meaningfulZeroSpaceList[1].isMinLimXBorder == False and meaningfulZeroSpaceList[1].isMaxLimXBorder and meaningfulZeroSpaceList[1].isMinLimYBorder == False and meaningfulZeroSpaceList[1].isMaxLimYBorder == False:
        #             print("two")
        # #3 case
        # if len(meaningfulZeroSpaceList) <= 3:
        #     highestZeroSpaceObjectPercentageOccupy = ZeroSpaceObject()
        #     indexCalculation = 0
        #     for zeroSpaceObject in meaningfulZeroSpaceList:
        #         if indexCalculation == 0:
        #             highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #             indexCalculation += 1
        #             continue
        #         if zeroSpaceObject.percentageOccupy > highestZeroSpaceObjectPercentageOccupy.percentageOccupy:
        #             highestZeroSpaceObjectPercentageOccupy = zeroSpaceObject
        #         indexCalculation += 1
        #     zeroSpaceObject = highestZeroSpaceObjectPercentageOccupy
        #     # print('zeroSpaceObject.percentageOccupy')
        #     # print(zeroSpaceObject.percentageOccupy)
        #     if zeroSpaceObject.isMinLimXBorder == False and zeroSpaceObject.isMaxLimXBorder == False and zeroSpaceObject.isMinLimYBorder == False and zeroSpaceObject.isMaxLimYBorder == False:
        #         print("zero")

        #8
        # iterate through all, zerospace, if at least contain amount, if percentage match with false conditions.

    def calculateZeroSpaceBorderConnectivity(self, featureSetIdentificationObject):
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            isMinLimXBorder = False
            isMaxLimXBorder = False
            isMinLimYBorder = False
            isMaxLimYBorder = False
            #x min
            if zeroSpaceObject.listResults[0][0].xValue == 0:
                isMinLimXBorder = True

            #x max
            indexEmptyListIteration = 1
            searchingIndex = 0
            # handle get latest index where not empty
            # reverse index
            isCalculating = True
            while isCalculating:
                searchingIndex = len(zeroSpaceObject.listResults) - indexEmptyListIteration
                if len(zeroSpaceObject.listResults[searchingIndex]) != 0:
                    isCalculating = False
                indexEmptyListIteration += 1
            # print("searchingIndex")
            # print(searchingIndex)
            # print("len(zeroSpaceObject.listResults)")
            # print(len(zeroSpaceObject.listResults))
            # print("zeroSpaceObject.listResults")
            # print(zeroSpaceObject.listResults)
            
            if zeroSpaceObject.listResults[searchingIndex][0].xValue == featureSetIdentificationObject.pixelObjectComposite.xLim:
                isMaxLimXBorder = True 
            #y min
            for pixelObjectList in zeroSpaceObject.listResults:
                for pixelObject in pixelObjectList:
                    if pixelObject.yValue == 0:
                        isMinLimYBorder = True 
                        break
                if isMinLimYBorder:
                    break
            #y max
            for pixelObjectList in zeroSpaceObject.listResults:
                for pixelObject in pixelObjectList:
                    if pixelObject.yValue == featureSetIdentificationObject.pixelObjectComposite.yLim:
                        isMaxLimYBorder = True 
                        break
                if isMaxLimYBorder:
                    break
            
            # for pixelObject in zeroSpaceObject.listResults:
            #     if pixelObject.yValue == 0:
            #         isMinLimYBorder = True 
            #         break
            # for pixelObject in zeroSpaceObject.listResults:
            #     if pixelObject.yValue == featureSetIdentificationObject.pixelObjectComposite.yLim:
            #         isMaxLimYBorder = True 
            #         break
            zeroSpaceObject.isMinLimXBorder = isMinLimXBorder
            zeroSpaceObject.isMaxLimXBorder = isMaxLimXBorder
            zeroSpaceObject.isMinLimYBorder = isMinLimYBorder
            zeroSpaceObject.isMaxLimYBorder = isMaxLimYBorder
        
            
            


    def calculateZeroSpacePercentageOccupy(self, featureSetIdentificationObject):
        #given x lim + y lim calculate amount of pixels.
        # print("featureSetIdentificationObject.pixelObjectComposite.xLim")
        # print(featureSetIdentificationObject.pixelObjectComposite.xLim)
        
        # print("featureSetIdentificationObject.pixelObjectComposite.yLim")
        # print(featureSetIdentificationObject.pixelObjectComposite.yLim)
        totalAmountOfPixels = featureSetIdentificationObject.pixelObjectComposite.xLim * featureSetIdentificationObject.pixelObjectComposite.yLim
        # print("totalAmountOfPixels")
        # print(totalAmountOfPixels)
        # print("len(featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject)")
        # print(len(featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject))
        indexZeroSpaceObject = 0
        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            # print(zeroSpaceObject)
            totalPixelLength = 0
            for pixelObjectList in zeroSpaceObject.listResults:
                totalPixelLength += len(pixelObjectList)
            # print("totalPixelLength")
            # print(totalPixelLength)
            pecentageOccupy = totalPixelLength / totalAmountOfPixels
            # print("pecentageOccupy")
            # print(pecentageOccupy)
            featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject[indexZeroSpaceObject].percentageOccupy = pecentageOccupy
            indexZeroSpaceObject += 1
        #calculate total pixels
        
        # for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
        #     print("percentageOccupy")
        #     print(zeroSpaceObject.percentageOccupy)


    def calculateFeatureSetMatches(self, featureSetIdentificationObjectComposite, featureSetIdentificationObjectComposite1):
        # print("len(featureSetIdentificationObjectComposite.listFeatureSetIdentificationObject)")
        # print(len(featureSetIdentificationObjectComposite.listFeatureSetIdentificationObject))

        # dataFrameManager.calculateFeatureSetMatches(featureSetIdentificationObjectComposite, featureSetIdentificationObjectComposite1)
        # featureSetIdentificationObjectComposite.listFeatureSetIdentificationObject[0].pixelSegmentProximityAnalysis.listIsAboveYDelimiter1ProximityResults
        # print("len(featureSetIdentificationObjectComposite1.listFeatureSetIdentificationObject)")
        # print(len(featureSetIdentificationObjectComposite1.listFeatureSetIdentificationObject))
        listFeatureSetComparison = []
        #for checking characters
        indexTestingFeatureSet = 0
        for testingFeatureSetIdentificationObject in featureSetIdentificationObjectComposite1.listFeatureSetIdentificationObject:
            # isNoMatchFound = True
            listResults = []
            print("indexTestingFeatureSet")
            print(indexTestingFeatureSet)


            # print("len(testingFeatureSetIdentificationObject.listSegmentXDelimiter)")
            # print(len(testingFeatureSetIdentificationObject.listSegmentXDelimiter))

            # print("len(testingFeatureSetIdentificationObject.listSegmentYDelimiter)")
            # print(len(testingFeatureSetIdentificationObject.listSegmentYDelimiter))


            print("len(testingFeatureSetIdentificationObject.pixelSegmentProximityAnalysis.listIsAboveXDelimiter1ProximityResults)")
            print(len(testingFeatureSetIdentificationObject.pixelSegmentProximityAnalysis.listIsAboveXDelimiter1ProximityResults))
        
            # print("len(testingFeatureSetIdentificationObject.pixelSegmentProximityAnalysis.listIsAboveYDelimiter1ProximityResults)")
            # print(len(testingFeatureSetIdentificationObject.pixelSegmentProximityAnalysis.listIsAboveYDelimiter1ProximityResults))

            featureSetComparison = FeatureSetComparison()
            # #for characters possibility known
            indexKnown = 0
            for knownFeatureSetIdentificationObject in featureSetIdentificationObjectComposite.listFeatureSetIdentificationObject:
                #compare amount matching segment and proximity values
                #
                # proximity character for identification.
                #segments
                
                if len(testingFeatureSetIdentificationObject.listSegmentXDelimiter) == len(knownFeatureSetIdentificationObject.listSegmentXDelimiter):
                    # result = True
                    print("len(knownFeatureSetIdentificationObject.listSegmentXDelimiter)")
                    print(len(knownFeatureSetIdentificationObject.listSegmentXDelimiter))
                    featureSetComparison.isSegmentXMatching = True
                    featureSetComparison.indexKnown = indexKnown
                    # print("true at index ")
                    # print(indexTestingFeatureSet)
                    print("testing hit!!!!")
                    # break
                indexKnown += 1

            
            listFeatureSetComparison.append(featureSetComparison)
            indexTestingFeatureSet += 1

        print("listFeatureSetComparison")
        print(len(listFeatureSetComparison))
        indexResults = 0
        for val in listFeatureSetComparison:
            print("indexResults")
            print(indexResults)
            print("featureSetComparison.isSegmentXMatching")
            print(featureSetComparison.isSegmentXMatching)
            print("featureSetComparison.indexKnown")
            print(featureSetComparison.indexKnown)

            # if val:
            #     print("true at index")
            #     print(indexResults)
            indexResults += 1

        

    def calculateFeatureSetIdentificationObjectComposite(self, path):
        featureSetIdentificationObjectComposite = FeatureSetIdentificationObjectComposite()
        
        overallIndex = 0
        im = Image.open(path) # Can be many different formats.
        pix = im.load()
        # print(im.size) # Get the width and hight of the image for iterating over

        xLim = im.size[0]
        yLim = im.size[1]

        intXLim = int(xLim)
        intYLim = int(yLim)

        indexX = 0 
        indexY = 0

        listXY = []
        listCharacterPixels = [[]]
        isInitialBlackAreaReached = False
        isBlackAreaReached = False
        while indexX < intXLim:
            indexY = 0
            isBlackAreaReached = False
            while indexY < intYLim:
                if pix[indexX,indexY][0] < 100:
                    # print("hit")
                    isInitialBlackAreaReached = True
                    isBlackAreaReached = True

                    pixelObject = PixelObject()
                    pixelObject.redValue = pix[indexX,indexY][0]
                    # self.listXY = [[indexX,indexY]]

                    pixelObject.xValue = indexX
                    pixelObject.yValue = indexY
                    listXY.append(pixelObject)

                    #for each 
                    listCharacterPixels[len(listCharacterPixels)-1].append(pixelObject)
                    # continue
                indexY += 1
            if isInitialBlackAreaReached:
                if isBlackAreaReached == False:
                    if len(listCharacterPixels[len(listCharacterPixels)-1]) != 0:
                        listCharacterPixels.append([])
            indexX += 1

        xList = []
        yList = []

        listPixelObjectComposite = []
        # overallIndex = 0
        # print("listCharacterPixels")
        # print(len(listCharacterPixels))
        return listCharacterPixels


    def calculateBlackBackgroundFeatureSetIdentificationObjectComposite(self, path):
        featureSetIdentificationObjectComposite = FeatureSetIdentificationObjectComposite()
        # print("hit")
        overallIndex = 0
        im = Image.open(path) # Can be many different formats.
        # print("hit1")
        pix = im.load()
        # print(im.size) # Get the width and hight of the image for iterating over
        # print("hit2")
        xLim = im.size[0]
        yLim = im.size[1]

        intXLim = int(xLim)
        intYLim = int(yLim)

        indexX = 0 
        indexY = 0

        listPixelPreviousToAppend = []
        listCharacterPixels = [[]]
        isInitialWhiteAreaReached = False
        isWhiteAreaReached = False
        while indexX < intXLim:
            indexY = 0
            isWhiteAreaReached = False
            isIndexYWhiteSegmentDelimter = True
            while indexY < intYLim:

                if pix[indexX,indexY][0] > 150:
                
                    isInitialWhiteAreaReached = True
                    isWhiteAreaReached = True

                    pixelObject = PixelObject()

                    # pixelObject.setRedValue(pix[indexX,indexY][0])
                    # pixelObject.insertIntoListXY([indexX,indexY])

                    pixelObject.redValue = pix[indexX,indexY][0]
                    # self.listXY = [[indexX,indexY]]

                    pixelObject.xValue = indexX
                    pixelObject.yValue = indexY
                    
                    listCharacterPixels[len(listCharacterPixels)-1].append(pixelObject)
                    isIndexYWhiteSegmentDelimter = False
                #handle only one pixel in x column
                # if indexY == intYLim -1:
                #     if len(listCharacterPixels[len(listCharacterPixels)-1]) == 1:
                #         print("hit inside")
                #         pixelObject = listCharacterPixels[len(listCharacterPixels)-1][0]
                #         listCharacterPixels.append([])
                #         listCharacterPixels[len(listCharacterPixels)-1].append(pixelObject)
                indexY += 1

            if isInitialWhiteAreaReached:
                if isWhiteAreaReached == False:
                    if len(listCharacterPixels[len(listCharacterPixels)-1]) != 0:
                        listCharacterPixels.append([])

            indexX += 1

        return listCharacterPixels

    # def calculateAllZeroSpace(self):
    #     #Find all predominate markation coloration 
    #     #quantity of pixels above markation...
    #     #meh given context no need for averages needed.


    def seperateCharactersByZeroSpaceColumnsReturnListCharacterPixelsDark(self, path):
        featureSetIdentificationObjectComposite = FeatureSetIdentificationObjectComposite()
        overallIndex = 0
        im = Image.open(path)
        pix = im.load()
        xLim = im.size[0]
        yLim = im.size[1]

        intXLim = int(xLim)
        intYLim = int(yLim)

        indexX = 0 
        indexY = 0

        listPixelPreviousToAppend = []
        listCharacterPixels = [[]]
        isInitialZeroAreaReached = False
        isZeroAreaReached = False
        while indexX < intXLim:
            indexY = 0
            isZeroAreaReached = False
            isIndexYWhiteSegmentDelimter = True
            while indexY < intYLim:

                if pix[indexX,indexY][0] > 100:
                    isInitialZeroAreaReached = True
                    isZeroAreaReached = True
                    pixelObject = PixelObject()

                    pixelObject.redValue = pix[indexX,indexY][0]

                    pixelObject.xValue = indexX
                    pixelObject.yValue = indexY
                    
                    listCharacterPixels[len(listCharacterPixels)-1].append(pixelObject)
                    isIndexYWhiteSegmentDelimter = False
                    indexY += 1
                    continue

                indexY += 1

            if isInitialZeroAreaReached:
                if isZeroAreaReached == False:
                    if len(listCharacterPixels[len(listCharacterPixels)-1]) != 0:
                        listCharacterPixels.append([])

            indexX += 1
        return listCharacterPixels

    def seperateCharactersByZeroSpaceColumnsReturnListCharacterPixelsLight(self, path):
        # if len(listCharacterPixels) <= 1:
        featureSetIdentificationObjectComposite = FeatureSetIdentificationObjectComposite()
        overallIndex = 0
        im = Image.open(path)
        pix = im.load()
        xLim = im.size[0]
        yLim = im.size[1]

        intXLim = int(xLim)
        intYLim = int(yLim)

        indexX = 0 
        indexY = 0

        listPixelPreviousToAppend = []
        listCharacterPixels = [[]]
        isInitialZeroAreaReached = False
        isZeroAreaReached = False
        while indexX < intXLim:
            indexY = 0
            isZeroAreaReached = False
            isIndexYWhiteSegmentDelimter = True
            while indexY < intYLim:

                if pix[indexX,indexY][0] < 150:
                    isInitialZeroAreaReached = True
                    isZeroAreaReached = True
                    pixelObject = PixelObject()
                    pixelObject.redValue = pix[indexX,indexY][0]

                    pixelObject.xValue = indexX
                    pixelObject.yValue = indexY
                    
                    listCharacterPixels[len(listCharacterPixels)-1].append(pixelObject)
                    isIndexYWhiteSegmentDelimter = False
                    indexY += 1
                    continue

                indexY += 1

            if isInitialZeroAreaReached:
                if isZeroAreaReached == False:
                    if len(listCharacterPixels[len(listCharacterPixels)-1]) != 0:
                        listCharacterPixels.append([])

            indexX += 1
        return listCharacterPixels

    def calculateFeatureSetIdentificationObjectComposite1(self, characterPixel):
        #for each pixel object do all needed caclulations
        # for pixelObjectList in listCharacterPixels:
        # overallIndex += 1
        # if overallIndex == 11:
            # break
        # if overallIndex == len(listCharacterPixels):
        #     break
        # create composite object
        pixelObjectComposite = PixelObjectComposite()
        pixelObjectComposite.listPixelObjects =  characterPixel

        # featureSetIdentificationObject = FeatureSetIdentificationObject()
        # featureSetIdentificationObject.pixelObjectComposite = pixelObjectComposite
        # create zeroized            
        zeroizedXIndex = 0
        isInitialZeroize = True
        previousXIndex = 0
        zeroizedIterationIndex = 0
        # modifiedPixelList = []
        
        
        for pixel in pixelObjectComposite.listPixelObjects:
            if pixel.isZeroSpace == True:
                continue
            modifiedPixed = pixel
            if isInitialZeroize:
                isInitialZeroize = False
                previousXIndex = pixel.xValue
                modifiedPixed.xValue = zeroizedXIndex
                pixelObjectComposite.listZeroizedPixelObjects.append(modifiedPixed)
                zeroizedIterationIndex += 1
                continue
            if pixel.xValue != previousXIndex:
                previousXIndex = pixel.xValue
                zeroizedXIndex += 1
                modifiedPixed.xValue = zeroizedXIndex
                pixelObjectComposite.listZeroizedPixelObjects.append(modifiedPixed)
                zeroizedIterationIndex += 1
                continue
            modifiedPixed.xValue = zeroizedXIndex
            pixelObjectComposite.listZeroizedPixelObjects.append(modifiedPixed)
            zeroizedIterationIndex += 1
    
        zeroizedXIndex = 0
        isInitialZeroize = True
        previousXIndex = 0
        zeroizedIterationIndex = 0

        # get low value y for zeroize     
        indexY = 0
        #find lowest y point 
        isInitialY = True
        lowestYValue = 0
        lowestYValueIndex = 0
        
        for pixel in pixelObjectComposite.listZeroizedPixelObjects:
            y = int(pixel.yValue)
            currentValue = y
            if isInitialY:
                lowestYValue = currentValue
                lowestYValueIndex = 0
                isInitialY = False
                indexY += 1
                continue
            if currentValue < lowestYValue:
                lowestYValue = currentValue
                lowestYValueIndex = indexY
            indexY += 1
        
        differenceFromLowestY = lowestYValue

        zeroizedYList = []

        indexPixelModifyYValue = 0
        # get high low values x,y zeroizedY 
        for pixel in pixelObjectComposite.listZeroizedPixelObjects:
            # for first value set previous,
            #append to list
            y = int(pixel.yValue)
            modifiedValue = y - differenceFromLowestY
            pixelObjectComposite.listZeroizedPixelObjects[indexPixelModifyYValue].yValue = modifiedValue
            
            indexPixelModifyYValue += 1

        # highestXValue zeroized
        highestXValue = 0
        highestXValueIndex = 0
        isInitialX = True
        indexXPixel = 0

        for pixel in pixelObjectComposite.listZeroizedPixelObjects:
            x = int(pixel.xValue)
            currentXValue = x

            if isInitialX:
                highestXValue = currentXValue
                highestXValueIndex = 0
                isInitialX = False
                indexXPixel += 1
                continue

            if currentXValue > highestXValue:
                highestXValue = currentXValue
                highestXValueIndex = indexXPixel
            indexXPixel += 1
        
        pixelObjectComposite.highestXValuePixelIndex = highestXValueIndex

        # lowestXValue zeroized
        lowestXValue = 0
        lowestXValueIndex = 0
        isInitialX = True
        indexXPixel = 0

        for pixel in pixelObjectComposite.listZeroizedPixelObjects:
            x = int(pixel.xValue)
            currentXValue = x

            if isInitialX:
                lowestXValue = currentXValue
                lowestXValueIndex = 0
                isInitialX = False
                indexXPixel += 1
                continue

            if currentXValue < lowestXValue:
                lowestXValue = currentXValue
                lowestXValueIndex = indexXPixel
            indexXPixel += 1
        
        pixelObjectComposite.lowestXValuePixelIndex = lowestXValueIndex

        # highestYValue zeroized
        highestYValue = 0
        highestYValueIndex = 0
        isInitialY = True
        indexYPixel = 0

        for pixel in pixelObjectComposite.listZeroizedPixelObjects:
            y = int(pixel.yValue)
            currentYValue = y

            if isInitialY:
                highestYValue = currentYValue
                highestYValueIndex = 0
                isInitialY = False
                indexYPixel += 1
                continue

            if currentYValue > highestYValue:
                highestYValue = currentYValue
                highestYValueIndex = indexYPixel
            indexYPixel += 1
        
        pixelObjectComposite.highestYValuePixelIndex = highestYValueIndex

        # lowestYValue zeroized
        lowestYValue = 0
        lowestYValueIndex = 0
        isInitialY = True
        indexYPixel = 0

        for pixel in pixelObjectComposite.listZeroizedPixelObjects:
            y = int(pixel.yValue)
            currentYValue = y

            if isInitialY:
                lowestYValue = currentYValue
                lowestYValueIndex = 0
                isInitialY = False
                indexYPixel += 1
                continue

            if currentYValue < lowestYValue:
                lowestYValue = currentYValue
                lowestYValueIndex = indexYPixel
            indexYPixel += 1
        
        pixelObjectComposite.lowestYValuePixelIndex = lowestYValueIndex

        # pixelObjectComposite yLim xLim
        pixelObjectComposite.xLim = pixelObjectComposite.listZeroizedPixelObjects[pixelObjectComposite.highestXValuePixelIndex].xValue
        pixelObjectComposite.yLim = pixelObjectComposite.listZeroizedPixelObjects[pixelObjectComposite.highestYValuePixelIndex].yValue

        indexX = 0
        listOrderedPixelsByXColomn = []

        while indexX <= pixelObjectComposite.xLim:
            listPixels = []
            for pixel in pixelObjectComposite.listZeroizedPixelObjects:
                xValue = int(pixel.xValue)
                if xValue == indexX:
                    listPixels.append(pixel)
            listOrderedPixelsByXColomn.append(listPixels)
            indexX += 1 
        pixelObjectComposite.listOrderedPixelsByXColomn = listOrderedPixelsByXColomn

        indexY = 0
        listOrderedPixelsByYColomn = []
        # print("ylim")
        # print(pixelObjectComposite.yLim)
        while indexY <= pixelObjectComposite.yLim:
            listPixels = []
            for pixel in pixelObjectComposite.listZeroizedPixelObjects:
                yValue = int(pixel.yValue)
                if yValue == indexY:
                    listPixels.append(pixel)
            listOrderedPixelsByYColomn.append(listPixels)
            indexY += 1 
        pixelObjectComposite.listOrderedPixelsByYColomn = listOrderedPixelsByYColomn
        # print("here")
        # print(len(pixelObjectComposite.listOrderedPixelsByYColomn))
        # print("len")
        #

        pixelSegment = PixelSegment()
        listPixelSegmentXDirection = []
        for listPixels in pixelObjectComposite.listOrderedPixelsByXColomn:
            # print(listPixels)
            # print(len(listPixels))
            modificationListPixels = listPixels

            while len(modificationListPixels) != 0:
                originPixel = modificationListPixels[0]
                originPixelXValue = originPixel.xValue
                originPixelYValue = originPixel.yValue
                pixelSegment.pixelList.append(originPixel)

                seekingPixelXValue = originPixelXValue 
                seekingPixelYValue = originPixelYValue + 1

                isSeekingPixelPresent = False

                isOperation = True 
                while isOperation:
                    isNoPixelFound = True
                    for pixel in modificationListPixels:
                        if pixel.xValue == seekingPixelXValue:
                            if pixel.yValue == seekingPixelYValue:
                                pixelSegment.pixelList.append(pixel)
                                isNoPixelFound = False
                                seekingPixelYValue += 1
                    if isNoPixelFound:
                            isOperation =  False 
                            break

                for pixel in pixelSegment.pixelList:
                    indexToRemove = 0 
                    for pixelModified in modificationListPixels:
                        if pixel.xValue == pixelModified.xValue:
                            if pixel.yValue == pixelModified.yValue:
                                # index to remove
                                break
                        indexToRemove += 1

                    del modificationListPixels[indexToRemove:(indexToRemove+1)]

                listPixelSegmentXDirection.append(pixelSegment)
                pixelSegment = PixelSegment()
        pixelObjectComposite.listPixelSegmentXDirection = listPixelSegmentXDirection


        # print("listOrderedPixelsByYColomn")
        # print(len(listOrderedPixelsByYColomn))
        
        # for list 

        # for listPixels in pixelObjectComposite.listOrderedPixelsByYColomn:
        #     print("inside")
        #     print(listPixels)
        #     print(len(listPixels))
        #     print("listPixels[0].yValue]")
        #     print(listPixels[0].yValue)

        pixelSegment = PixelSegment()
        listPixelSegmentYDirection = []
        for listPixels in pixelObjectComposite.listOrderedPixelsByYColomn:
            # print(listPixels)
            # print(len(listPixels))
            modificationListPixels = listPixels

            while len(modificationListPixels) != 0:
                originPixel = modificationListPixels[0]
                originPixelXValue = originPixel.xValue
                originPixelYValue = originPixel.yValue
                pixelSegment.pixelList.append(originPixel)

                seekingPixelXValue = originPixelXValue + 1
                seekingPixelYValue = originPixelYValue

                isSeekingPixelPresent = False

                isOperation = True 
                while isOperation:
                    isNoPixelFound = True
                    for pixel in modificationListPixels:
                        if pixel.xValue == seekingPixelXValue:
                            if pixel.yValue == seekingPixelYValue:
                                pixelSegment.pixelList.append(pixel)
                                isNoPixelFound = False
                                seekingPixelXValue += 1
                    if isNoPixelFound:
                            isOperation =  False 
                            break


                for pixel in pixelSegment.pixelList:
                    indexToRemove = 0 
                    for pixelModified in modificationListPixels:
                        if pixel.xValue == pixelModified.xValue:
                            if pixel.yValue == pixelModified.yValue:
                                # index to remove
                                break
                        indexToRemove += 1

                    del modificationListPixels[indexToRemove:(indexToRemove+1)]

                listPixelSegmentYDirection.append(pixelSegment)
                pixelSegment = PixelSegment()
        pixelObjectComposite.listPixelSegmentYDirection = listPixelSegmentYDirection

        segmentXDelimiterList= []
        segmentYDelimiterList = []
        #trollys
        for pixelSegment in pixelObjectComposite.listPixelSegmentXDirection:
            # print("pecX")
            # print(len(pixelEdgeCase.pixelList))
            if len(pixelSegment.pixelList) >= 2:
                segmentXDelimiterList.append(pixelSegment)


        # print("pixelObjectComposite.listPixelSegmentYDirection")
        # print(pixelObjectComposite.listPixelSegmentYDirection)
        for pixelSegment in pixelObjectComposite.listPixelSegmentYDirection:
            # print("pecY")
            if len(pixelSegment.pixelList) >= 2:
                segmentYDelimiterList.append(pixelSegment)

        xList = []
        yList = []
        for pixelSegment in segmentXDelimiterList:
            for pixel in pixelSegment.pixelList:
                xList.append(pixel.xValue)
                yList.append(pixel.yValue)
        for pixelSegment in segmentYDelimiterList:
            for pixel in pixelSegment.pixelList:
                xList.append(pixel.xValue)
                yList.append(pixel.yValue)

        #trolly
        featureSetIdentificationObject = FeatureSetIdentificationObject()
        featureSetIdentificationObject.pixelObjectComposite = pixelObjectComposite
        featureSetIdentificationObject.listSegmentXDelimiter = segmentXDelimiterList
        featureSetIdentificationObject.listSegmentYDelimiter = segmentYDelimiterList
    # PixelObjectComposite
        listFeatureSetIdentificationObject = []
        listFeatureSetIdentificationObject.append(featureSetIdentificationObject)

        # xLim =  pixelObjectComposite.listZeroizedPixelObjects[pixelObjectComposite.highestXValuePixelIndex].xValue
        # yLim =  pixelObjectComposite.listZeroizedPixelObjects[pixelObjectComposite.highestYValuePixelIndex].yValue
        
        xLim =  pixelObjectComposite.xLim
        yLim =  pixelObjectComposite.yLim
        
        # print("xLim")
        # print(xLim)
        # print(yLim)

        # determine median x value
        medianXValue = xLim / 2 
        # determine median y value
        medianYValue = yLim / 2 
        #

        # print("median")
        # print(medianXValue)
        # print(medianYValue)

        featureSetIdentificationObject.medianXValue = medianXValue
        featureSetIdentificationObject.medianYValue = medianYValue

        # print("len(featureSetIdentificationObject.listSegmentXDelimiter)")
        # print(len(featureSetIdentificationObject.listSegmentXDelimiter))

        # print("len(featureSetIdentificationObject.listSegmentYDelimiter)")
        # print(len(featureSetIdentificationObject.listSegmentYDelimiter))
        # # trolly

        pixelSegmentProximityAnalysis = PixelSegmentProximityAnalysis()
        for segmentDelimiter in featureSetIdentificationObject.listSegmentXDelimiter:
            isAboveMedian = False
            valueCheckCondition = segmentDelimiter.pixelList[0].xValue
            if valueCheckCondition > featureSetIdentificationObject.medianXValue:
                isAboveMedian = True
            proximitySegment = ProximitySegment()
            proximitySegment.segment = segmentDelimiter
            proximitySegment.isAboveDelimiter = isAboveMedian
            pixelSegmentProximityAnalysis.listProximitySegmentX.append(proximitySegment)

    
        for segmentDelimiter in featureSetIdentificationObject.listSegmentYDelimiter:
            isAboveMedian = False
            valueCheckCondition = segmentDelimiter.pixelList[0].yValue
            if valueCheckCondition > featureSetIdentificationObject.medianYValue:
                isAboveMedian = True
            proximitySegment = ProximitySegment()
            proximitySegment.segment = segmentDelimiter
            proximitySegment.isAboveDelimiter = isAboveMedian
            pixelSegmentProximityAnalysis.listProximitySegmentY.append(proximitySegment)

        featureSetIdentificationObject.pixelSegmentProximityAnalysis = pixelSegmentProximityAnalysis

        #calculate white space pixels within bounds of black markation xLim and yLim 

        #handle zeroized pixels zeroSpace
        # for pixel in pixelObjectComposite.listPixelObjects:
        #     if pixel.isZeroSpace == False:
        #         continue
        #     modifiedPixed = pixel
            
        #     if isInitialZeroize:
        #         isInitialZeroize = False
        #         previousXIndex = pixel.xValue
        #         modifiedPixed.xValue = zeroizedXIndex
        #         pixelObjectComposite.listZeroizedWhiteSpacePixelObjects.append(modifiedPixed)
        #         zeroizedIterationIndex += 1
        #         continue

        #     if pixel.xValue != previousXIndex:
        #         previousXIndex = pixel.xValue
        #         zeroizedXIndex += 1
        #         modifiedPixed.xValue = zeroizedXIndex
        #         pixelObjectComposite.listZeroizedWhiteSpacePixelObjects.append(modifiedPixed)
        #         zeroizedIterationIndex += 1
        #         continue
        #     modifiedPixed.xValue = zeroizedXIndex
        #     pixelObjectComposite.listZeroizedWhiteSpacePixelObjects.append(modifiedPixed)
        #     zeroizedIterationIndex += 1
        return featureSetIdentificationObject

     #support for retroactive revisit of zero space.
    def calculateAllZeroSpaceInFeatureSetIdentificationObject(self, featureSetIdentificationObject):
        modifiedFeatureSetIdentificationObject = featureSetIdentificationObject

        modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects.append([])
        indexX = 0  
        while indexX <= modifiedFeatureSetIdentificationObject.pixelObjectComposite.xLim:
            print("indexX value")
            print(indexX)

            indexY = 0
            while indexY <= modifiedFeatureSetIdentificationObject.pixelObjectComposite.yLim:
                isMarkationPresent = False
                for pixelObject in modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedPixelObjects:
                    if indexX == pixelObject.xValue:
                        if indexY == pixelObject.yValue:
                            isMarkationPresent = True
                            
                if isMarkationPresent == False:
                    pixelObject = PixelObject()
                    pixelObject.xValue = indexX
                    pixelObject.yValue = indexY
                    #append latest list
                    modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[len(modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects)-1].append(pixelObject)
                indexY += 1

            if indexX == modifiedFeatureSetIdentificationObject.pixelObjectComposite.xLim:
                indexX += 1
                break

            modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects.append([])
            indexX += 1
        # print("modifiedFeatureSetIdentificationObject")
        # print(modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects)
        return modifiedFeatureSetIdentificationObject

    def calculateZeroSpaceContinuityZeroIndex(self, featureSetIdentificationObject):
   
        # seekingList = calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[calculationContinuityObject.indexOperation][:]
        # seekingList = calculationContinuityObject.listMatchTotal[calculationContinuityObject.indexOperation]
        # calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[calculationContinuityObject.indexOperation]
        
        isLimCase = False
        #calculate seekingList until non-zero length sub-list found
        isCalculatingSeekingList = True
        while isCalculatingSeekingList:
            seekingList = featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation][:]
            if len(seekingList) != 0:
                break
            featureSetIdentificationObject.calculationContinuityObject.indexOperation += 1

        # print("calculationContinuityObject.indexOperation")
        # print(calculationContinuityObject.indexOperation)
        # print("calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved")
        # print(len(calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved))
        # print("calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[(calculationContinuityObject.indexOperation+1)][:]")
        # print(len(calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects))
        
        if featureSetIdentificationObject.calculationContinuityObject.indexOperation != len(featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved)-1:
            comparisonList = featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[(featureSetIdentificationObject.calculationContinuityObject.indexOperation+1)][:]
         # #handle zero case at lim
        if featureSetIdentificationObject.calculationContinuityObject.indexOperation == len(featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved)-1:
            isLimCase = True
            featureSetIdentificationObject.calculationContinuityObject.isLimCase = True

        if featureSetIdentificationObject.calculationContinuityObject.isLimCase:
            # calculateContinuous
            print("LIM CASE")
            print("len(seeking")
            print(len(seekingList))
            
            for pixelObject in seekingList:
                print("seekingList xValue")
                print(pixelObject.xValue)
                print(pixelObject.yValue)
            #for values, calculate if black markation, in y direction if 
            isBlackMarkation = False

            calculatingIndex = 0
            isCalculating = True
            while isCalculating:
                isCalculating = False
                # highPixelObject = PixelObject()

                # for pixelObject in seekingList:
                # indexHighCalculation = 0
                # for pixelObject in seekingList:
                    
                #     if indexHighCalculation == 0:
                #         highPixelObject = pixelObject
                #         indexHighCalculation += 1
                #         continue
                    
                #     if pixelObject.yValue >= highPixelObject.yValue:
                #         highPixelObject = pixelObject

                #     indexHighCalculation += 1
                if calculatingIndex == 0:
                    featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].append(seekingList[calculatingIndex])
                            
                    
                pixelObject = seekingList[calculatingIndex]
                seekingXValue = pixelObject.xValue
                seekingYValue = pixelObject.yValue + 1
                print("seekingXValue")
                print(seekingXValue)
                print(seekingXValue)
                for pixelObjectComparison in seekingList:
                    if seekingXValue == pixelObjectComparison.xValue:
                        if seekingYValue == pixelObjectComparison.yValue:
                            # isBlackMarkation = False
                            print("hit inside")
                            isCalculating = True
                            featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].append(pixelObjectComparison)
                            break
             
                calculatingIndex += 1
            
            #remove at delimiter
            for pixelObject in featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]:   
                
                indexToRemove = 0
                for pixelObjectComparison in featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation]:
                    if pixelObject.xValue == pixelObjectComparison.xValue:
                        if pixelObject.yValue == pixelObjectComparison.yValue:
                            break
                    indexToRemove += 1
                
                del featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation][indexToRemove:indexToRemove+1]
                

        



        if featureSetIdentificationObject.calculationContinuityObject.isLimCase == False:
            listIndexMatchComparisonList = []
            listIndexAdditionalPixelObjects = []

            isBlackMarkationFound = False
            indexSearch = 0
            print("SCOURGE")
            for pixelObject in seekingList:
                print("Xvalue")
                print(pixelObject.xValue)
                print(pixelObject.yValue)
            for pixelObject in seekingList:
                # print(pixelObject)
                # seekingXValue = pixelObject.xValue + 1
                # seekingYValue = pixelObject.yValue
                listIndexMatchComparisonList.append(indexSearch)
                seekingXValue = pixelObject.xValue
                seekingYValue = pixelObject.yValue + 1

                isNoWhiteMarkationFound = True

                for pixelObjectComparison in seekingList:

                    if seekingXValue == pixelObjectComparison.xValue:
                        if seekingYValue == pixelObjectComparison.yValue:

                            print("hit seekingXValue")
                            print(seekingXValue)
                            print(seekingYValue)
                            if isBlackMarkationFound == False:
                                # listIndexMatchComparisonList.append(indexSearch)
                                isNoWhiteMarkationFound = False
                                isComparisonFound = True

                            # if isBlackMarkationFound: 
                            #     #append to other list
                            #     listIndexAdditionalPixelObjects.append(indexSearch)

                if isNoWhiteMarkationFound:
                    # if seekingYValue != 0:
                    isBlackMarkationFound = True
                    break

                indexSearch += 1
            



            
            print("len(listIndexMatchComparisonList)")
            print(len(listIndexMatchComparisonList))
            if len(listIndexMatchComparisonList) != 0:
                for index in listIndexMatchComparisonList:
                    print("hit")
                    print(index)
                    print("len(seekingList)")
                    print(len(seekingList))
                    pixelObject = seekingList[index]
                    print("index xValue")
                    print(pixelObject.xValue)
                    print(pixelObject.yValue)

                

                    featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].append(pixelObject)
                    #append to temp list for futher calculation.
                    featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal.append(pixelObject)
                    



                # calculate connecting zeroSpace of operating index.
                # highest direction 
                # highestCalculationContinuityIndex = 1
                isHighestCalculationContinuity = True
                while isHighestCalculationContinuity:
                    isHighestCalculationContinuity = False
                    nextPixelObjectIndex = len(featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal) + 1 

                    if nextPixelObjectIndex < len(featureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[featureSetIdentificationObject.calculationContinuityObject.indexOperation]):
                        #handle on top index pixelObject
                        print("cool")
                        topPixelObject = featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal)-1]
                        
                        seekingXValue = topPixelObject.xValue
                        seekingYValue = topPixelObject.yValue + 1

                        # seekingHighValue 
                        pixelObjectComparison = featureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[featureSetIdentificationObject.calculationContinuityObject.indexOperation][nextPixelObjectIndex]
                        
                        isNextZeroSpacePresent = False 
                        if pixelObjectComparison.xValue ==  seekingXValue:
                            if pixelObjectComparison.yValue ==  seekingYValue:
                                isHighestCalculationContinuity = True
                                print("yo")
                                # append to total calculation
                                featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal.append(pixelObjectComparison)
                                featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].append(pixelObjectComparison)
                            

                isLowestCalculationContinuity = True
                while isLowestCalculationContinuity:
                    isLowestCalculationContinuity = False
                    nextPixelObjectIndex = len(featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal) + 1 

                    lowPixelObject = featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal[0]
                    
                    seekingXValue = lowPixelObject.xValue
                    seekingYValue = lowPixelObject.yValue - 1

                    print("seekingYValue")
                    print(seekingYValue)
                    if seekingYValue != -1:
                    #how to find value in the 
                    # for each value in list
                    #if lower value found
                        for pixelObjectComparison in featureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[featureSetIdentificationObject.calculationContinuityObject.indexOperation]:
                            if pixelObjectComparison.xValue ==  seekingXValue:
                                if pixelObjectComparison.yValue ==  seekingYValue:
                                    isLowestCalculationContinuity = True
                                    print("low")
                                    # append to total calculation
                                    featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal.insert(0,pixelObjectComparison)
                                    featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].insert(0,pixelObjectComparison)
                                    break

                #Removal from copy for next iteration
                for pixelObject in featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]:   
                    
                    indexToRemove = 0
                    for pixelObjectComparison in featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation]:
                        if pixelObject.xValue == pixelObjectComparison.xValue:
                            if pixelObject.yValue == pixelObjectComparison.yValue:
                                break
                        indexToRemove += 1
                    
                    del featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation][indexToRemove:indexToRemove+1]
        # return featureSetIdentificationObject        
       
        # for pixelObject in calculationContinuityObject.listTempMatchTotal:
        #     print("second.xValue")
        #     print(pixelObject.xValue)
        #     print(pixelObject.yValue)

        # for pixelObject in calculationContinuityObject.listMatchTotal[len(calculationContinuityObject.listMatchTotal)-1]:
        #     print("test.xValue")
        #     print(pixelObject.xValue)
        #     print(pixelObject.yValue)
                    

    def calculateZeroSpaceCalculationContinuityObject(self,featureSetIdentificationObject):
        # print("calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.xLim")
        # print(calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.xLim)
        # calculationContinuityObject = featureSetIdentificationObject.calculationContinuityObject
        while featureSetIdentificationObject.calculationContinuityObject.indexOperation < featureSetIdentificationObject.pixelObjectComposite.xLim:
            # break
            if featureSetIdentificationObject.calculationContinuityObject.indexOperation == 0:
                featureSetIdentificationObject.calculationContinuityObject.listMatchTotal.append([])
                # calculationContinuityObject.indexOperation = 0
                self.calculateZeroSpaceContinuityZeroIndex(featureSetIdentificationObject)


            
            if featureSetIdentificationObject.calculationContinuityObject.isLimCase:
                break
            #seekingList from listIndexAdditionalPixelObjects
            # if listMatchTotal
            #deep copy of, removed at index
            # print("calculationContinuityObject.indexOperation")
            # print(calculationContinuityObject.indexOperation)
            # seekingList = calculationContinuityObject.listMatchTotal[calculationContinuityObject.indexOperation][:]
            # seekingList = calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved
            seekingList = featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1][:]
            featureSetIdentificationObject.calculationContinuityObject.listMatchTotal.append([])

            # seekingList = calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[calculationContinuityObject.indexOperation]
            # comparisonList = calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[(calculationContinuityObject.indexOperation+1)][:]
            comparisonList = featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[(featureSetIdentificationObject.calculationContinuityObject.indexOperation+1)][:]

            listIndexMatchComparisonList = []
            featureSetIdentificationObject.calculationContinuityObject.listIndexAdditionalPixelObjects = []

            isBlackMarkationFound = True
            isAlternateStore = False
            isInitialMatchFound = False
            for pixelObject in seekingList:
                indexSearch = 0
                seekingXValue = pixelObject.xValue + 1
                seekingYValue = pixelObject.yValue

                isNoWhiteMarkationFound = True
                for pixelObjectComparison in comparisonList:
                    if seekingXValue == pixelObjectComparison.xValue:
                        if seekingYValue == pixelObjectComparison.yValue:
                            isInitialMatchFound = True
                            isBlackMarkationFound = False

                            if isAlternateStore == False:
                                listIndexMatchComparisonList.append(indexSearch)
                            if isAlternateStore:
                                featureSetIdentificationObject.calculationContinuityObject.listIndexAdditionalPixelObjects.append(indexSearch)
                            break

                    if isInitialMatchFound:
                        if isBlackMarkationFound:
                            isAlternateStore = True

                    indexSearch += 1
                    
            print("len(listIndexMatchComparisonList)")
            print(len(listIndexMatchComparisonList))
            for index in listIndexMatchComparisonList:
                print("hit")
                pixelObject = comparisonList[index]
                # print("pixelObject.xValue")
                # print(pixelObject.xValue)
                # print(pixelObject.yValue)

                featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].append(pixelObject)
                #append to temp list for futher calculation.
                featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal.append(pixelObject)

     
            # calculate connecting zeroSpace of operating index.
            # highest direction 
            # highestCalculationContinuityIndex = 1
            # isHighestCalculationContinuity = True
            # while isHighestCalculationContinuity:
            #     isHighestCalculationContinuity = False
            #     nextPixelObjectIndex = len(calculationContinuityObject.listTempMatchTotal) + 1 

            #     if nextPixelObjectIndex < len(calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[calculationContinuityObject.indexOperation]):
            #         #handle on top index pixelObject
            #         print("cool")
            #         topPixelObject = calculationContinuityObject.listTempMatchTotal[len(calculationContinuityObject.listTempMatchTotal)-1]
                    
            #         seekingXValue = topPixelObject.xValue
            #         seekingYValue = topPixelObject.yValue + 1

            #         # seekingHighValue 
            #         pixelObjectComparison = calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[calculationContinuityObject.indexOperation][nextPixelObjectIndex]
                    
            #         isNextZeroSpacePresent = False 
            #         if pixelObjectComparison.xValue ==  seekingXValue:
            #             if pixelObjectComparison.yValue ==  seekingYValue:
            #                 isHighestCalculationContinuity = True
            #                 print("yo")
            #                 # append to total calculation
            #                 calculationContinuityObject.listTempMatchTotal.append(pixelObjectComparison)
            #                 calculationContinuityObject.listMatchTotal[len(calculationContinuityObject.listMatchTotal)-1].append(pixelObjectComparison)
            
            if len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]) != 0:
                
                highPixelObject = PixelObject()
                isHighestCalculationContinuity = True
                while isHighestCalculationContinuity:
                    isHighestCalculationContinuity = False

                    # find highest y value
                    # highPixelObject = calculationContinuityObject.listTempMatchTotal[0]
                    print("len pixel obeject list total")
                    print(len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]))
                    indexHighCalculation = 0
                    for pixelObject in featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]:
                        
                        if indexHighCalculation == 0:
                            highPixelObject = pixelObject
                            indexHighCalculation += 1
                            continue
                        
                        if pixelObject.yValue >= highPixelObject.yValue:
                            highPixelObject = pixelObject

                        indexHighCalculation += 1
                    
                    # for pixelObject 
                    print("high pixel object")
                    print(highPixelObject.xValue)
                    print(highPixelObject.yValue)

                    seekingXValue = highPixelObject.xValue
                    seekingYValue = highPixelObject.yValue + 1
        
                    print("high seekingXValue")
                    print(seekingXValue)
                    print(seekingYValue)
                    print("featureSetIdentificationObject.calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.yLim")
                    print(featureSetIdentificationObject.pixelObjectComposite.yLim)
                    for val in comparisonList:
                        print("seeking val")
                        print(val.xValue)
                        print(val.yValue)
                    if seekingYValue <= featureSetIdentificationObject.pixelObjectComposite.yLim:
                        for pixelObjectComparison in comparisonList:
                            if pixelObjectComparison.xValue ==  seekingXValue:
                                if pixelObjectComparison.yValue ==  seekingYValue:
                                    isHighestCalculationContinuity = True
                                    print("high")
                                    print(pixelObjectComparison.xValue)
                                    print(pixelObjectComparison.yValue)
                                    print("match")
                                    # append to total calculation
                                    # calculationContinuityObject.listTempMatchTotal.insert(0,pixelObjectComparison)
                                    featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].append(pixelObjectComparison)
                                    break  
                    
                    


                isLowestCalculationContinuity = True
                while isLowestCalculationContinuity:
                    isLowestCalculationContinuity = False
                    # nextPixelObjectIndex = len(calculationContinuityObject.listTempMatchTotal) + 1 
                    # lowPixelObject = calculationContinuityObject.listTempMatchTotal[0]

                    # find lowest y value
                    lowPixelObject = featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal[0]
                    indexLowCalculation = 0
                    for pixelObject in featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]:
                        
                        if indexLowCalculation == 0:
                            lowPixelObject = pixelObject
                            indexLowCalculation += 1
                            continue
                        
                        if pixelObject.yValue < lowPixelObject.yValue:
                            lowPixelObject = pixelObject

                        indexLowCalculation += 1
                    # for pixelObject in calculationContinuityObject.listMatchTotal[len(calculationContinuityObject.listMatchTotal)-1]:
                    #     print("low seekingXValue")
                    #     print(pixelObject.xValue)
                    #     print(pixelObject.yValue)
                    
                    seekingXValue = lowPixelObject.xValue
                    seekingYValue = lowPixelObject.yValue - 1

                    print("low seekingXValue")
                    print(seekingXValue)
                    print(seekingYValue)
                    if seekingYValue != -1:
                    #how to find value in the 
                    # for each value in list
                    #if lower value found
                        for pixelObjectComparison in comparisonList:
                        # calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects[calculationContinuityObject.indexOperation]:
                            if pixelObjectComparison.xValue ==  seekingXValue:
                                if pixelObjectComparison.yValue ==  seekingYValue:
                                    isLowestCalculationContinuity = True
                                    print("low")
                                    # append to total calculation
                                    featureSetIdentificationObject.calculationContinuityObject.listTempMatchTotal.insert(0,pixelObjectComparison)
                                    featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1].insert(0,pixelObjectComparison)
                                    break


                #  #Removal from copy for next iteration
                for pixelObject in featureSetIdentificationObject.calculationContinuityObject.listMatchTotal[len(featureSetIdentificationObject.calculationContinuityObject.listMatchTotal)-1]:
                    indexToRemove = 0
                    print("removing")
                    print(pixelObject.xValue)
                    print(pixelObject.yValue)
                    
                    for pixelObjectComparison in featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation+1]:
                        

                        if pixelObject.xValue == pixelObjectComparison.xValue:
                            if pixelObject.yValue == pixelObjectComparison.yValue:
                                print("pixelObjectComparison")
                                print(pixelObjectComparison.xValue)
                                print(pixelObjectComparison.yValue)
                                break
                        indexToRemove += 1
                    # print()
                    del featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved[featureSetIdentificationObject.calculationContinuityObject.indexOperation+1][indexToRemove:indexToRemove+1]
                

            # if calculationContinuityObject.indexOperation == 0:
            #     break

            featureSetIdentificationObject.calculationContinuityObject.indexOperation += 1
            

        # for listValue in calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved:
        #     print("list iter")
        #     for pixelObject in listValue:
        #             print("pixelObject.xValue")
        #             print(pixelObject.xValue)
        #             print(pixelObject.yValue)

        zeroSpaceObject = ZeroSpaceObject()
        zeroSpaceObject.listResults = featureSetIdentificationObject.calculationContinuityObject.listMatchTotal
        featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject.append(zeroSpaceObject)

        for zeroSpaceObject in featureSetIdentificationObject.calculationContinuityObject.zeroSpaceObjectComposite.listZeroSpaceObject:
            print("SPACER")
            for listValue in zeroSpaceObject.listResults:
                for pixelObject in listValue:
                    print("pixelObject.xValue")
                    print(pixelObject.xValue)
                    print(pixelObject.yValue)       

        return featureSetIdentificationObject

#         class ZeroSpaceObjectComposite():
#     def __init__(self):
#         self.listZeroSpaceObject = []

# class ZeroSpaceObject():
#     def __init__(self):
#         self.listResults = []
#         self.percentageX = 0
#         self.percentageY = 0
#         self.isTouchingOpenLim = False
#         self.isXAxisPositiveTouching = False
#         self.isXAxisNegativeTouching = False
#         self.isYAxisPositiveTouching = False
#         self.isYAxisNegativeTouching = False

        

    def calculateZeroSpaceContinuity(self, featureSetIdentificationObject):
        calculationContinuityObject = CalculationContinuityObject()
        # calculationContinuityObject.modifiedFeatureSetIdentificationObject = featureSetIdentificationObject
       
        # calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved = copy.deepcopy(calculationContinuityObject.modifiedFeatureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects)
        calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved = copy.deepcopy(featureSetIdentificationObject.pixelObjectComposite.listZeroizedWhiteSpacePixelObjects)

        zeroSpaceObjectComposite = ZeroSpaceObjectComposite()
        featureSetIdentificationObject.calculationContinuityObject = calculationContinuityObject

        isContinueOperation = True
        indexCalculation = 0

        while isContinueOperation:
            calculationContinuityObject.indexOperation = 0
            calculationContinuityObject.listMatchTotal = []
            calculationContinuityObject.listTempMatchTotal = []
            calculationContinuityObject.listIndexAdditionalPixelObjectsTotal = []
            calculationContinuityObject.listIndexMatchComparisonList = []

            calculationContinuityObject.isLimCase = False

            #while there is whitespace,
            self.calculateZeroSpaceCalculationContinuityObject(featureSetIdentificationObject)
            isContinueOperation = False

            for listValues in featureSetIdentificationObject.calculationContinuityObject.copyZeroListWithCalculatedIndexRemoved:
                if len(listValues) != 0:
                    isContinueOperation = True

            indexCalculation += 1
        
        # featureSetIdentificationObject.calculationContinuityObject = calculationContinuityObject
        return featureSetIdentificationObject


    def createComparisonMatrixGrid(self):
        d = pd.DataFrame(np.zeros((50, 30), dtype = int))
        return d

    def calculateBlackWhiteLineBreaks(self, dataframe):
        columnScan = ColumnScan()
    
        instanceDataframe = dataframe
        returningString = ""
        listBlackIndexX = []
        listBlackIndexY = []

    
        for index, row in instanceDataframe.iterrows():
            intRowRed = int(row['red'])
            if intRowRed < 250:
                listBlackIndexX.append(int(row['x']))
                listBlackIndexY.append(int(row['y']))
              
        return listBlackIndexX, listBlackIndexY

    def calculateBlackAreaReadingColumn(self, dataFrame, indexOfValueThresholdReached):
        # print("black area index", indexOfValueThresholdReached)

        #handle where white space is continous or ending piece at index where white is markation to end.

        #from start point continue until edge piece found, return index,
        # isSearchingTrue = true 

        indexStart = indexOfValueThresholdReached + 1
        indexOfValueToContinueOperation = 0

        # don't want to start from 0 index, want to start from index obtained.
        # for this placing values in list would be optimum
        instanceDataframe = dataFrame

        for index, row in islice(instanceDataframe.iterrows(), indexStart, None):
        # for index, row in instanceDataframe.iloc[indexOfValueThresholdReached:].iterrows():
            print(str(row['x']))
            # do calculation for row values
            # do 
            # row
            intRowRed = int(row['red'])
            if intRowRed > 100:
                # self.calculateBlackAreaReadingColumn(instanceDataframe, index)
                break
            indexOfValueToContinueOperation += 1

        return indexOfValueToContinueOperation

    def changeGrid(self, grid, scanList):
        modifiedGrid = grid
        #for each value at location scanList index, update grid
        # print(scanList)
        print("len")
        print(len(scanList))
        for v in scanList:
            value1 = int(v[0])
            value2 = int(v[1])
            modifiedGrid.loc[value1][value2] = 55
        return modifiedGrid

class PixelObject:
    def __init__(self):
        self.listXY = []
        self.redValue = None
        self.xValue = 0
        self.yValue = 0
        self.isZeroSpace = False


class PixelObjectComposite:
    def __init__(self):
        self.listPixelObjects = []
        self.listZeroizedPixelObjects = []
        self.listZeroizedWhiteSpacePixelObjects = []
        
        self.highestXValuePixelIndex = 0
        self.lowestXValuePixelIndex = 0

        self.highestYValuePixelIndex = 0
        self.lowestYValuePixelIndex = 0

        self.listOrderedPixelsByXColomn= []
        self.listOrderedPixelsByYColomn= []

        self.listPixelSegmentXDirection = []
        self.listPixelSegmentYDirection = []

        self.listOrderedPixelsByYColomnXHighestPriority = []

    

class PixelSegment():
    def __init__(self):
        self.pixelList = []
        self.continuousDistance = 0

    def getStartPixelXY(self):
        return self.startPixelXY
    def setStartPixelXY(self, value):
        self.startPixelXY = value

    def getEndPixelXY(self):
        return self.endPixelXY
    def setEndPixelXY(self, value):
        self.endPixelXY = value

    def getContinuousDistance(self):
        return self.continuousDistance
    def setContinuousDistance(self, value):
        self.continuousDistance = value


class FeatureSetIdentificationObject():
    def __init__(self):
        self.pixelObjectComposite = PixelObjectComposite()
        self.listPixel = []
        self.continuousDistance = 0
        self.listSegmentXDelimiter = []
        self.listSegmentYDelimiter = []
        self.pixelSegmentProximityAnalysis = PixelSegmentProximityAnalysis()
        self.borderSegmentCalculationX = BorderSegmentCalculation()
        self.borderSegmentCalculationY = BorderSegmentCalculation()
        self.characterIdentifier = 0
        self.zeroSpaceObjectComposite = ZeroSpaceObjectComposite()
        self.calculationContinuityObject = CalculationContinuityObject()
        
class FeatureSetIdentificationObjectComposite():
    def __init__(self):
        self.listFeatureSetIdentificationObject = []
        
class FeatureSetComparison():
    def __init__(self):
        self.isSegmentXMatching = False
        self.indexKnown = 0

class PixelSegmentProximityAnalysis():
    def __init__(self):
        self.listProximitySegmentX = []
        self.listProximitySegmentY = []

class BorderSegmentCalculation():
    def __init__(self):
        self.isSegmentPositiveBoundary = False
        self.isSegmentNegativeBoundary = False
        self.listPixelSegmentMatchingLim = []



class AccuracyDeterminace():
    def __init__(self):
        self.startPixelXY = [] # location and value
        self.endPixelXY = [] # location and value
        self.continuousDistance = 0

class ProximitySegment():
    def __init__(self):
        self.isAboveDelimiter = False
        self.segment = PixelSegment()


class MatchingProximitySegmentComparisonComposite():
    def __init__(self):
        self.listMatchingProximitySegmentComparison = []
        self.intListKnownHighestProbabilityMatch = []

class MatchingProximitySegmentComparison():
    def __init__(self):
        self.boolListProximitySegmentMatch = []
        self.indexMatch = 0


class WhiteSpaceContinuityCalculationComposite():
    def __init__(self):
        self.listWhiteSpaceContinuityCalculation = []
        self.segment = PixelSegment()
        self.overallIsContinuityAtAnyPixelInSegment = False

class WhiteSpaceContinuityCalculation():
    def __init__(self):
        self.isWhiteSpaceContinuity = False
        self.pixelCalculated = PixelObject()

class ZeroSpaceObjectComposite():
    def __init__(self):
        self.listZeroSpaceObject = []

class ZeroSpaceObject():
    def __init__(self):
        self.listResults = []
        self.percentageX = 0
        self.percentageY = 0
        self.isTouchingOpenLim = False
        self.isMinLimXBorder = False
        self.isMaxLimXBorder = False
        self.isMinLimYBorder = False
        self.isMaxLimYBorder = False
        self.percentageOccupy = 0

class CalculationContinuityObject():
    def __init__(self):
        self.indexOperation = 0
        # self.modifiedFeatureSetIdentificationObject = FeatureSetIdentificationObject()
        self.zeroSpaceObjectComposite =  ZeroSpaceObjectComposite()
        self.listContinuity = [[]]
        self.listMatchTotal = []
        self.listTempMatchTotal = []

        self.listPixelObjectsInCalculation = []

        self.listIndexAdditionalPixelObjectsTotal = []
        self.listIndexMatchComparisonList = []
        self.listRemovedCalculatedZeroizedWhiteSpacePixelObjects = []
        self.copyZeroListWithCalculatedIndexRemoved = []
        self.isComparisonFound = False
        self.isCalculationFinished = True

if __name__== "__main__":
  main()

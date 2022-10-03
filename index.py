#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import os
import numpy as np


os.system('clear')
print("Первые ходят черные:")

arr =  np.array([ [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])



arrUserPoints = []
arrBotPoints = []

botMuted = False

def POINTS_COUNTER():
	
	x = 0
	y = 0

	for i in arr:
		string = ""		
		for j in i:
			string +=  "% s" % j + " "

			if j == 1: arrUserPoints.append([x, y])
			elif j == 2: arrBotPoints.append([x, y])
			y += 1
		x += 1
		y = 0
	
def ABLE_POINTS (Step):
	
	if(Step == 1): 
		PointBlack = 1
		PointWhite = 2
		SomePoints = arrUserPoints
	else:
		PointBlack = 2
		PointWhite = 1
		SomePoints = arrBotPoints


	arrAblePoints = []
	arrPathPoints = []


	
	for UserPoint in SomePoints:
		findPath = 0
		#ВВЕРХ
		TopLineEndFound = 0
		TopLineIndx = 1
		while TopLineEndFound == 0:
			if UserPoint[0] - TopLineIndx > 0:
				if arr[UserPoint[0] - TopLineIndx][UserPoint[1]] == PointWhite:
					TopLineIndx += 1
				elif arr[UserPoint[0] - TopLineIndx][UserPoint[1]] == PointBlack:
					TopLineEndFound = 1
					TopLineIndx = 1
				else: 
					TopLineEndFound = 1
			else: TopLineEndFound = 1
		if TopLineIndx != 1 and TopLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] - TopLineIndx , UserPoint[1]])
			#NEW
			TopArrPathPoints = []
			for z in range(TopLineIndx + 1):
				if z != 0: TopArrPathPoints.append([UserPoint[0] - z, UserPoint[1]])
			TopCoordName =  str(UserPoint[0] - z) + ", " +  str(UserPoint[1])
			arrPathPoints.append({ TopCoordName : TopArrPathPoints})


		#ВНИЗ + if
		BottomLineEndFound = 0
		BottomLineIndx = 1
		while BottomLineEndFound == 0:
			if UserPoint[0] + BottomLineIndx < 7:
				if arr[UserPoint[0] + BottomLineIndx][UserPoint[1]] == PointWhite:
					BottomLineIndx += 1
				elif arr[UserPoint[0] + BottomLineIndx][UserPoint[1]] == PointBlack:
					BottomLineEndFound = 1
					BottomLineIndx = 1
				else: 
					BottomLineEndFound = 1
			else: BottomLineEndFound = 1
		if BottomLineIndx != 1 and BottomLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] + BottomLineIndx , UserPoint[1]])

			#NEW
			BottomArrPathPoints = []
			for z in range(BottomLineIndx + 1):
				if z != 0: BottomArrPathPoints.append([UserPoint[0] + z, UserPoint[1]])
			BottomCoordName =  str(UserPoint[0] + z) + ", " +  str(UserPoint[1])
			arrPathPoints.append({ BottomCoordName : BottomArrPathPoints})

		

		#ВЛЕВО
		LeftLineEndFound = 0
		LeftLineIndx = 1
		while LeftLineEndFound == 0:
			if UserPoint[1] - LeftLineIndx > 0:
				if arr[UserPoint[0]][UserPoint[1] - LeftLineIndx] == PointWhite:
					LeftLineIndx += 1
				elif arr[UserPoint[0]][UserPoint[1] - LeftLineIndx] == PointBlack:
					LeftLineEndFound = 1
					LeftLineIndx = 1
				else: 
					LeftLineEndFound = 1
			else: LeftLineEndFound = 1
		if LeftLineIndx != 1 and LeftLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] , UserPoint[1] - LeftLineIndx])

			#NEW
			leftArrPathPoints = []
			for z in range(LeftLineIndx + 1):
				if z != 0: leftArrPathPoints.append([UserPoint[0] , UserPoint[1] - z])
			LeftCoordName =  str(UserPoint[0]) + ", " +  str(UserPoint[1] - z)
			arrPathPoints.append({ LeftCoordName : leftArrPathPoints})



		#ВПРАВО
		RightLineEndFound = 0
		RightLineIndx = 1
		while RightLineEndFound == 0:
			if UserPoint[1] + RightLineIndx < 7:
				if arr[UserPoint[0]][UserPoint[1] + RightLineIndx] == PointWhite:
					RightLineIndx += 1
				elif arr[UserPoint[0]][UserPoint[1] + RightLineIndx] == PointBlack:
					RightLineEndFound = 1
					RightLineIndx = 1
				else: 
					RightLineEndFound = 1
			else: RightLineEndFound = 1
		if RightLineIndx != 1 and RightLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] , UserPoint[1] + RightLineIndx])
			#NEW
			RightArrPathPoints = []
			for z in range(RightLineIndx + 1):
				if z != 0: RightArrPathPoints.append([UserPoint[0] , UserPoint[1] + z])
			RightCoordName =  str(UserPoint[0]) + ", " +  str(UserPoint[1] + z)
			arrPathPoints.append({ RightCoordName : RightArrPathPoints}) 
			
				


		#ВЛЕВОВЕРХ
		LeftTopLineEndFound = 0
		LeftTopLineIndx = 1
		while LeftTopLineEndFound == 0:
			if UserPoint[0] - LeftTopLineIndx > 0 and UserPoint[1] - LeftTopLineIndx > 0:
				if arr[UserPoint[0] - LeftTopLineIndx][UserPoint[1] - LeftTopLineIndx] == PointWhite:	
					LeftTopLineIndx += 1
				elif arr[UserPoint[0] - LeftTopLineIndx][UserPoint[1] - LeftTopLineIndx] == PointBlack:
					LeftTopLineEndFound = 1
					LeftTopLineIndx = 1
				else: 
					LeftTopLineEndFound = 1
			else: LeftTopLineEndFound = 1
		if LeftTopLineIndx != 1 and LeftTopLineEndFound != 0:
			arrAblePoints.append([ UserPoint[0] - LeftTopLineIndx, UserPoint[1] - LeftTopLineIndx])
			#NEW
			LeftTopArrPathPoints = []
			for z in range(LeftTopLineIndx + 1):
				if z != 0: LeftTopArrPathPoints.append([UserPoint[0] - z, UserPoint[1] - z])
			LeftTopCoordName =  str(UserPoint[0] - z) + ", " +  str(UserPoint[1] - z)
			arrPathPoints.append({ LeftTopCoordName : LeftTopArrPathPoints})


		#ВПРАВОВВЕРХ
		RightTopLineEndFound = 0
		RightTopLineIndx = 1
		while RightTopLineEndFound == 0:
			if UserPoint[0] - RightTopLineIndx > 0 and UserPoint[1] + RightTopLineIndx < 7:
				if arr[UserPoint[0] - RightTopLineIndx][UserPoint[1] + RightTopLineIndx] == PointWhite:
					RightTopLineIndx += 1
				elif arr[UserPoint[0] - RightTopLineIndx][UserPoint[1] + RightTopLineIndx] == PointBlack:
					RightTopLineEndFound = 1
					RightTopLineIndx = 1
				else: 
					RightTopLineEndFound = 1
			else: RightTopLineEndFound = 1
		if RightTopLineIndx != 1 and RightTopLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] - RightTopLineIndx, UserPoint[1] + RightTopLineIndx])
			#NEW
			RightTopArrPathPoints = []
			for z in range(RightTopLineIndx + 1):
				if z != 0: RightTopArrPathPoints.append([UserPoint[0] - z, UserPoint[1] + z])
			RightTopCoordName =  str(UserPoint[0] - z) + ", " +  str(UserPoint[1] + z)
			arrPathPoints.append({ RightTopCoordName : RightTopArrPathPoints})

		#ВЛЕВОВНИЗ
		LeftBottomLineEndFound = 0
		LeftBottomLineIndx = 1
		while LeftBottomLineEndFound == 0:
			if UserPoint[0] + LeftBottomLineIndx < 7 and UserPoint[1] - LeftBottomLineIndx > 0:
				if arr[UserPoint[0] + LeftBottomLineIndx][UserPoint[1] - LeftBottomLineIndx] == PointWhite:
					LeftBottomLineIndx += 1
				elif arr[UserPoint[0] + LeftBottomLineIndx][UserPoint[1] - LeftBottomLineIndx] == PointBlack:
					LeftBottomLineEndFound = 1
					LeftBottomLineIndx = 1
				else: 
					LeftBottomLineEndFound = 1
			else: 
				LeftBottomLineEndFound = 1
		if LeftBottomLineIndx != 1 and LeftBottomLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] + LeftBottomLineIndx, UserPoint[1] - LeftBottomLineIndx])
			#NEW
			LeftBottomArrPathPoints = []
			for z in range(LeftBottomLineIndx + 1):
				if z != 0: LeftBottomArrPathPoints.append([UserPoint[0] + z, UserPoint[1] - z])
			LeftBottomCoordName =  str(UserPoint[0] + z) + ", " +  str(UserPoint[1] - z)
			arrPathPoints.append({ LeftBottomCoordName : LeftBottomArrPathPoints})

		#ВПРАВОВНИЗ
		RightBottomLineEndFound = 0
		RightBottomLineIndx = 1
		while RightBottomLineEndFound == 0:
			if UserPoint[0] + RightBottomLineIndx < 7 and UserPoint[1] + RightBottomLineIndx < 7:
				if arr[UserPoint[0] + RightBottomLineIndx][UserPoint[1] + RightBottomLineIndx] == PointWhite:
					RightBottomLineIndx += 1
				elif arr[UserPoint[0] + RightBottomLineIndx][UserPoint[1] + RightBottomLineIndx] == PointBlack:
					RightBottomLineEndFound = 1
					RightBottomLineIndx = 1
				else: 
					RightBottomLineEndFound = 1
			else: 
				RightBottomLineEndFound = 1
		if RightBottomLineIndx != 1 and RightBottomLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] + RightBottomLineIndx, UserPoint[1] + RightBottomLineIndx])
			#NEW
			RightBottomArrPathPoints = []
			for z in range(RightBottomLineIndx + 1):
				if z != 0: RightBottomArrPathPoints.append([UserPoint[0] + z, UserPoint[1] + z])
			RightBottomCoordName =  str(UserPoint[0] + z) + ", " +  str(UserPoint[1] + z)
			arrPathPoints.append({ RightBottomCoordName : RightBottomArrPathPoints})



	indexesCrew = []
	indexesCrew1 = []
	for x in arrAblePoints:
		if arr[x[0]][x[1]] == 1 or arr[x[0]][x[1]] == 2:
			indexesCrew.append(x)
		 	for z in arrPathPoints:
				if z.keys()[0] == str(x[0]) + ', ' + str(x[1]):
					indexesCrew1.append(z)
	


	for x in indexesCrew:
		if(x in arrAblePoints): 
			arrAblePoints.remove(x)

	ablePoints = DELETE_DUBLE(arrAblePoints)
	return [ablePoints, arrPathPoints]

def TEST_ABLE_POINTS (Step, compute_arr, iteration):
	
	if(Step == 1): 
		PointBlack = 1
		PointWhite = 2
		SomePoints = arrUserPoints
	else:
		PointBlack = 2
		PointWhite = 1
		SomePoints = arrBotPoints


	arrAblePoints = []
	arrPathPoints = []

	for UserPoint in SomePoints:
		findPath = 0
		#ВВЕРХ
		TopLineEndFound = 0
		TopLineIndx = 1
		while TopLineEndFound == 0:
			if UserPoint[0] - TopLineIndx > 0:
				if compute_arr[UserPoint[0] - TopLineIndx][UserPoint[1]] == PointWhite:
					TopLineIndx += 1
				elif compute_arr[UserPoint[0] - TopLineIndx][UserPoint[1]] == PointBlack:
					TopLineEndFound = 1
					TopLineIndx = 1
				else: 
					TopLineEndFound = 1
			else: TopLineEndFound = 1
		if TopLineIndx != 1 and TopLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] - TopLineIndx , UserPoint[1]])
			#NEW
			TopArrPathPoints = []
			for z in range(TopLineIndx + 1):
				if z != 0: TopArrPathPoints.append([UserPoint[0] - z, UserPoint[1]])
			TopCoordName =  str(UserPoint[0] - z) + ", " +  str(UserPoint[1])
			arrPathPoints.append({ TopCoordName : TopArrPathPoints})


		#ВНИЗ + if
		BottomLineEndFound = 0
		BottomLineIndx = 1
		while BottomLineEndFound == 0:
			if UserPoint[0] + BottomLineIndx < 7:
				if compute_arr[UserPoint[0] + BottomLineIndx][UserPoint[1]] == PointWhite:
					BottomLineIndx += 1
				elif compute_arr[UserPoint[0] + BottomLineIndx][UserPoint[1]] == PointBlack:
					BottomLineEndFound = 1
					BottomLineIndx = 1
				else: 
					BottomLineEndFound = 1
			else: BottomLineEndFound = 1
		if BottomLineIndx != 1 and BottomLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] + BottomLineIndx , UserPoint[1]])

			#NEW
			BottomArrPathPoints = []
			for z in range(BottomLineIndx + 1):
				if z != 0: BottomArrPathPoints.append([UserPoint[0] + z, UserPoint[1]])
			BottomCoordName =  str(UserPoint[0] + z) + ", " +  str(UserPoint[1])
			arrPathPoints.append({ BottomCoordName : BottomArrPathPoints})

		

		#ВЛЕВО
		LeftLineEndFound = 0
		LeftLineIndx = 1
		while LeftLineEndFound == 0:
			if UserPoint[1] - LeftLineIndx > 0:
				if compute_arr[UserPoint[0]][UserPoint[1] - LeftLineIndx] == PointWhite:
					LeftLineIndx += 1
				elif compute_arr[UserPoint[0]][UserPoint[1] - LeftLineIndx] == PointBlack:
					LeftLineEndFound = 1
					LeftLineIndx = 1
				else: 
					LeftLineEndFound = 1
			else: LeftLineEndFound = 1
		if LeftLineIndx != 1 and LeftLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] , UserPoint[1] - LeftLineIndx])

			#NEW
			leftArrPathPoints = []
			for z in range(LeftLineIndx + 1):
				if z != 0: leftArrPathPoints.append([UserPoint[0] , UserPoint[1] - z])
			LeftCoordName =  str(UserPoint[0]) + ", " +  str(UserPoint[1] - z)
			arrPathPoints.append({ LeftCoordName : leftArrPathPoints})



		#ВПРАВО
		RightLineEndFound = 0
		RightLineIndx = 1
		while RightLineEndFound == 0:
			if UserPoint[1] + RightLineIndx < 7:
				if compute_arr[UserPoint[0]][UserPoint[1] + RightLineIndx] == PointWhite:
					RightLineIndx += 1
				elif compute_arr[UserPoint[0]][UserPoint[1] + RightLineIndx] == PointBlack:
					RightLineEndFound = 1
					RightLineIndx = 1
				else: 
					RightLineEndFound = 1
			else: RightLineEndFound = 1
		if RightLineIndx != 1 and RightLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] , UserPoint[1] + RightLineIndx])
			#NEW
			RightArrPathPoints = []
			for z in range(RightLineIndx + 1):
				if z != 0: RightArrPathPoints.append([UserPoint[0] , UserPoint[1] + z])
			RightCoordName =  str(UserPoint[0]) + ", " +  str(UserPoint[1] + z)
			arrPathPoints.append({ RightCoordName : RightArrPathPoints}) 
			
				


		#ВЛЕВОВЕРХ
		LeftTopLineEndFound = 0
		LeftTopLineIndx = 1
		while LeftTopLineEndFound == 0:
			if UserPoint[0] - LeftTopLineIndx > 0 and UserPoint[1] - LeftTopLineIndx > 0:
				if compute_arr[UserPoint[0] - LeftTopLineIndx][UserPoint[1] - LeftTopLineIndx] == PointWhite:	
					LeftTopLineIndx += 1
				elif compute_arr[UserPoint[0] - LeftTopLineIndx][UserPoint[1] - LeftTopLineIndx] == PointBlack:
					LeftTopLineEndFound = 1
					LeftTopLineIndx = 1
				else: 
					LeftTopLineEndFound = 1
			else: LeftTopLineEndFound = 1
		if LeftTopLineIndx != 1 and LeftTopLineEndFound != 0:
			arrAblePoints.append([ UserPoint[0] - LeftTopLineIndx, UserPoint[1] - LeftTopLineIndx])
			#NEW
			LeftTopArrPathPoints = []
			for z in range(LeftTopLineIndx + 1):
				if z != 0: LeftTopArrPathPoints.append([UserPoint[0] - z, UserPoint[1] - z])
			LeftTopCoordName =  str(UserPoint[0] - z) + ", " +  str(UserPoint[1] - z)
			arrPathPoints.append({ LeftTopCoordName : LeftTopArrPathPoints})


		#ВПРАВОВВЕРХ
		RightTopLineEndFound = 0
		RightTopLineIndx = 1
		while RightTopLineEndFound == 0:
			if UserPoint[0] - RightTopLineIndx > 0 and UserPoint[1] + RightTopLineIndx < 7:
				if compute_arr[UserPoint[0] - RightTopLineIndx][UserPoint[1] + RightTopLineIndx] == PointWhite:
					RightTopLineIndx += 1
				elif compute_arr[UserPoint[0] - RightTopLineIndx][UserPoint[1] + RightTopLineIndx] == PointBlack:
					RightTopLineEndFound = 1
					RightTopLineIndx = 1
				else: 
					RightTopLineEndFound = 1
			else: RightTopLineEndFound = 1
		if RightTopLineIndx != 1 and RightTopLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] - RightTopLineIndx, UserPoint[1] + RightTopLineIndx])
			#NEW
			RightTopArrPathPoints = []
			for z in range(RightTopLineIndx + 1):
				if z != 0: RightTopArrPathPoints.append([UserPoint[0] - z, UserPoint[1] + z])
			RightTopCoordName =  str(UserPoint[0] - z) + ", " +  str(UserPoint[1] + z)
			arrPathPoints.append({ RightTopCoordName : RightTopArrPathPoints})

		#ВЛЕВОВНИЗ
		LeftBottomLineEndFound = 0
		LeftBottomLineIndx = 1
		while LeftBottomLineEndFound == 0:
			if UserPoint[0] + LeftBottomLineIndx < 7 and UserPoint[1] - LeftBottomLineIndx > 0:
				if compute_arr[UserPoint[0] + LeftBottomLineIndx][UserPoint[1] - LeftBottomLineIndx] == PointWhite:
					LeftBottomLineIndx += 1
				elif compute_arr[UserPoint[0] + LeftBottomLineIndx][UserPoint[1] - LeftBottomLineIndx] == PointBlack:
					LeftBottomLineEndFound = 1
					LeftBottomLineIndx = 1
				else: 
					LeftBottomLineEndFound = 1
			else: 
				LeftBottomLineEndFound = 1
		if LeftBottomLineIndx != 1 and LeftBottomLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] + LeftBottomLineIndx, UserPoint[1] - LeftBottomLineIndx])
			#NEW
			LeftBottomArrPathPoints = []
			for z in range(LeftBottomLineIndx + 1):
				if z != 0: LeftBottomArrPathPoints.append([UserPoint[0] + z, UserPoint[1] - z])
			LeftBottomCoordName =  str(UserPoint[0] + z) + ", " +  str(UserPoint[1] - z)
			arrPathPoints.append({ LeftBottomCoordName : LeftBottomArrPathPoints})

		#ВПРАВОВНИЗ
		RightBottomLineEndFound = 0
		RightBottomLineIndx = 1
		while RightBottomLineEndFound == 0:
			if UserPoint[0] + RightBottomLineIndx < 7 and UserPoint[1] + RightBottomLineIndx < 7:
				if compute_arr[UserPoint[0] + RightBottomLineIndx][UserPoint[1] + RightBottomLineIndx] == PointWhite:
					RightBottomLineIndx += 1
				elif compute_arr[UserPoint[0] + RightBottomLineIndx][UserPoint[1] + RightBottomLineIndx] == PointBlack:
					RightBottomLineEndFound = 1
					RightBottomLineIndx = 1
				else: 
					RightBottomLineEndFound = 1
			else: 
				RightBottomLineEndFound = 1
		if RightBottomLineIndx != 1 and RightBottomLineEndFound != 0:
			arrAblePoints.append([UserPoint[0] + RightBottomLineIndx, UserPoint[1] + RightBottomLineIndx])
			#NEW
			RightBottomArrPathPoints = []
			for z in range(RightBottomLineIndx + 1):
				if z != 0: RightBottomArrPathPoints.append([UserPoint[0] + z, UserPoint[1] + z])
			RightBottomCoordName =  str(UserPoint[0] + z) + ", " +  str(UserPoint[1] + z)
			arrPathPoints.append({ RightBottomCoordName : RightBottomArrPathPoints})


	indexesCrew = []
	indexesCrew1 = []
	for x in arrAblePoints:
		if compute_arr[x[0]][x[1]] == 1 or compute_arr[x[0]][x[1]] == 2:
			indexesCrew.append(x)
		 	for z in arrPathPoints:
				if z.keys()[0] == str(x[0]) + ', ' + str(x[1]):
					indexesCrew1.append(z)
	
	for x in indexesCrew:
		if(x in arrAblePoints): 
			arrAblePoints.remove(x)

	ablePoints = DELETE_DUBLE(arrAblePoints)
	return [ablePoints, arrPathPoints]

def DELETE_DUBLE(old_array):
	
	li = []
	li = [i for n, i in enumerate(old_array) if i not in old_array[:n]]

	return li


def COMPUTE_TREE(resultTreeArr, PathName):
	GetArr = ABLE_POINTS(2)
	arrAblePoints = GetArr[0]
	arrPathPoints = GetArr[1]

	compute_arr = []
	iteration = 0

	man_obj = []
	iterationObj = 0
	


	TestGetArr = TEST_ABLE_POINTS(2, resultTreeArr.copy(), iteration)
	testAblePoints = TestGetArr[0]
	testPathPoints = TestGetArr[1]

	if len(testAblePoints) > 0:
	
		for x in testAblePoints:
			compute_arr.append(resultTreeArr.copy())
			

			TestGetArr = TEST_ABLE_POINTS(2, resultTreeArr.copy(), iteration)
			testAblePoints = TestGetArr[0]
			testPathPoints = TestGetArr[1]

			if len(testAblePoints) > 0:
				ComInp1 = x[0]
				ComInp2 =  x[1]
				testPathPointsResult = []
				for y in testPathPoints:
					keyn = str(ComInp1) + ', ' + str(ComInp2)
					if(y.keys()[0] == keyn):
						testPathPointsResult.append(y[str(keyn)])
				for i in testPathPointsResult:
					for k in i:
						compute_arr[iteration][k[0]][k[1]] = 2


			TestGetArr1 = TEST_ABLE_POINTS(1, compute_arr[iteration], iteration)
			testAblePoints1 = TestGetArr1[0]
			testPathPoints1 = TestGetArr1[1]

			if len(testAblePoints1) > 0:
				man_arr = []
				iteration1 = 0
				

				for x1 in testAblePoints1:
					man_arr.append([])
					man_arr[iteration1] = compute_arr[iteration].copy()
					ComInp3 = x1[0]
					ComInp4 =  x1[1]
					testPathPointsResult1 = []
					for y in testPathPoints1:
						keyn = str(ComInp3) + ', ' + str(ComInp4)
						if(y.keys()[0] == keyn):
							testPathPointsResult1.append(y[str(keyn)])

				 	for i in testPathPointsResult1:
					 	for k in i:
							man_arr[iteration1][k[0]][k[1]] = 1
					
					man_obj.append({str(iteration) + str(iteration1): man_arr[iteration1]})

					iteration1 += 1
					iterationObj += 1


			
			iteration += 1
	
	return ([compute_arr, man_obj])


def WeightCounter (arr):
	manPointsCounter = 0
	computerPointsCounter = 0

	for x in arr:
		for y in x:
			
			if y == 1:
				manPointsCounter += 1
			elif y == 2:
				computerPointsCounter += 1

	return [manPointsCounter, computerPointsCounter] 


def HeuristicCost(arr):
	return arr[1] - arr[0]

def findMax (obj):
	arr = []
	for x in obj:
		arr.append(x[x.keys()[0]])
	return [max(arr), arr.index(max(arr))]

def setArr(NewArr):
	global arr
	arr = NewArr
	

def COMPUTE_INPUT ():

	CountStop = 4
	
	iteration = 0
	
	startTreeArr = arr.copy()

	worstManAnswer = []

	PathName = '' + str(iteration)

	ourMatrix = COMPUTE_TREE(arr.copy(), PathName)

	computeAbleMatrix = ourMatrix[0]
	userAbleMatrix = ourMatrix[1]
	
	if(len(userAbleMatrix) > 0):

		HeuristicCoster = 0
		for x in userAbleMatrix:
			HeuristicCoster = HeuristicCost(WeightCounter(x[x.keys()[0]]))
			worstManAnswer.append({x.keys()[0]: HeuristicCoster})
	
	if len(worstManAnswer) > 0:
		bestComputerAnswer =  worstManAnswer[findMax(worstManAnswer)[1]].keys()[0]
		
		setArr(np.array(computeAbleMatrix[int(bestComputerAnswer[0])]))
	else:
		if len(computeAbleMatrix) > 0:
			setArr(computeAbleMatrix[0])
		

def USER_INPUT():
	GetArr = ABLE_POINTS(1)
	arrAblePoints = GetArr[0]
	arrPathPoints = GetArr[1]



	print("Возможные варианты: ")
	resAblePoints = []
	for i in arrAblePoints:			
		aP = "" + "% s" % (i[0] + 1) + "% s" % (i[1] + 1)
		if aP not in resAblePoints:
			resAblePoints.append(aP)

	print(resAblePoints)
	


	userInp = input("Ваш ход?: ")

	userInp1 = int(str(abs(userInp))[0]) - 1
	userInp2 = userInp % 10 - 1

	checkUserInp = 0

	while checkUserInp == 0:
		checkUserInp1 = 0
		for i in arrAblePoints:
			if(userInp1 == i[0] and userInp2 == i[1]):		
				checkUserInp1 = 1
		if checkUserInp1 == 0:
			userInp = input("Выберите правильную ячейку! Повторите попытку. Ваш ход?: ")
			userInp1 = int(str(abs(userInp))[0]) - 1
			userInp2 = userInp % 10 - 1
		else:
			checkUserInp = 1

	checkUserInp = 0
	while checkUserInp == 0:
		if(arr[userInp1][userInp2] != 0): 
			userInp = input("Поле занято! Повторите попытку. Ваш ход?: ")
			userInp1 = int(str(abs(userInp))[0]) - 1
			userInp2 = userInp % 10 - 1
		else: checkUserInp = 1

	arrPathPointsResult = []

	for x in arrPathPoints:
		keyn = str(userInp1) + ', ' + str(userInp2)
		if(x.keys()[0] == keyn):
			arrPathPointsResult.append(x[str(keyn)])
			
	for x in arrPathPointsResult:
		for y in x:
			arr[y[0]][y[1]] = 1
	


def PRINT_GAME():
	print("   |  B1 B2 B3 B4 B5 B6 B7 B8 |")
	print("___|__________________________|")
	
	k = 1
	while k < 9:
		strA = "A" + "% s" % k + " |  " 
		for j in arr[k - 1]:
			if j == 0 :
				strA += "-  "
			elif j == 1 :
				strA += "1  "
			elif j == 2 :
				strA += "2  "

		strA += "|"
		print(strA)
		k += 1

	
	print("   |__________________________|")
	
	
	POINTS_COUNTER()
	
	print("Количество ваших фишек: " + "% s" % len(arrUserPoints))
	print("Количество фишек бота: " + "% s" % len(arrBotPoints))

i = 0

WINs = False

while WINs == False:

	GetArr = ABLE_POINTS(1)
	arrAblePoints = GetArr[0]
	GetArr2 = ABLE_POINTS(2)
	arrAblePoints2 = GetArr[0]

	if(len(arrAblePoints) != 0 and len(arrAblePoints2) != 0):
		if(WeightCounter(arr)[0] > WeightCounter(arr)[1]):
			print("Вы выйграли!")
		else:
			print("Вы проиграли!")
		WINs = True

	elif(WeightCounter(arr)[0] + WeightCounter(arr)[1] != 64):

		
		PRINT_GAME()
		USER_INPUT()
		arrUserPoints = []
		arrBotPoints = []

		PRINT_GAME()
		COMPUTE_INPUT()
		arrUserPoints = []
		arrBotPoints = []
	
		os.system('clear')
	else:
		if(WeightCounter(arr)[0] > WeightCounter(arr)[1]):
			print("Вы выйграли!")
		else:
			print("Вы проиграли!")
		WINs = True

	i += 1
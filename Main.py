from PIL import Image;
import numpy as np;
import matplotlib.pyplot as plt;
import time;
from collections import Counter;


def createExamples():
	numerArrayExamples = open("numArEx.txt","a");
	numbersWeHave = range(0,10);
	versionsWeHave = range(1,10);
	for eachNum in numbersWeHave:
		for eachVer in versionsWeHave:
			FileName = str(eachNum)+"."+str(eachVer);
			imageFilePath = "./tutorialimages/images/numbers/"+FileName+".png";
			ei = Image.open(imageFilePath);
			eiar = np.array(ei);
			eiar1 = str(eiar.tolist());

			lineToWrite = str(eachNum) + "::" +eiar1+"\n";
			numerArrayExamples.write(lineToWrite);



def threshold(imageArray):
	balanceAr = [];
	newAr = imageArray.copy();
	for eachRow in imageArray:
		for eachPix in eachRow:
			avgNum = reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]);
			balanceAr.append(avgNum);
	balanceAr = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr);
	for eachRow in newAr:
		for eachPix in eachRow:
			if reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) >= balanceAr:
				eachPix[0] = 255;
				eachPix[1] = 255;
				eachPix[2] = 255;
				eachPix[3] = 255;
			else:
				eachPix[0] = 0;
				eachPix[1] = 0;
				eachPix[2] = 0;
				eachPix[3] = 255;
	return newAr;



def whatNumIsThis(filePath):
	matchedAr = [];
	loadExamps = open("numArEx.txt","r").read();
	loadExamps = loadExamps.split("\n");

	i = Image.open(filePath);
	iar = np.array(i);
	iarl = iar.tolist();

	inQuestion = str(iarl);

	for eachExample in loadExamps:
		if(len(eachExample) > 3):
			splitEx = eachExample.split("::");
			currentNum = splitEx[0];
			currentAr = splitEx[1];

			eachPixEx = currentAr.split("],");
			eachPixInQ = inQuestion.split("],");

			x = 0;
			while(x<len(eachPixEx)):
				if (eachPixEx[x] == eachPixInQ[x]):
					matchedAr.append(int(currentNum));
				x += 1;

	x = Counter(matchedAr);
	print x;




whatNumIsThis("./tutorialimages/images/blank.png");

# createExamples();

# i = Image.open("./tutorialimages/images/numbers/y0.5.png");
# iar = np.asarray(i);
# plt.imshow(iar);
# plt.show();

# raw_input("..");

# iar = threshold(iar);

# plt.imshow(iar);
# plt.show();


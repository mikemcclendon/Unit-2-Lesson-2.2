import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

plt.figure()
loansData.boxplot(column='Amount.Funded.By.Investors') 
AFboxFig = plt.gcf()
AFboxFig.savefig('AmountFundedBoxPlot.png')

loansData.hist(column='Amount.Funded.By.Investors')
AFfig = plt.gcf()
AFfig.savefig('AmountFundedHist.png')

plt.figure()
stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
AFprobplot = plt.gcf()
AFprobplot.savefig("Amount_Funded_QQ.png")

plt.figure()
loansData.boxplot(column='Amount.Requested') 
ARboxFig = plt.gcf()
ARboxFig.savefig('AmountReqBoxPlot.png')

loansData.hist(column='Amount.Requested')
ARhistfig = plt.gcf()
AFfig.savefig('AmountReqHist.png')

plt.figure()
stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
ARprobplot = plt.gcf()
ARprobplot.savefig("Amount_Req_QQ.png")

plt.show()

#Both amounts maintain relatively similar central tendency around $10,000, however 'Amounted Funded'
#tends to skew slightly lower than 'Amount requested'. It seems many requests outside the 5k to 10k
#range are possibly granted within that level given there are more funded at that level than requested



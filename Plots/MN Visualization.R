library(corrplot)
library(ggplot2)

MN = read.csv("MN with additional features.csv")
MN = data.frame(MN)

#Regular histogram
br = 3150
hs = 10000000
hist(MN$AssessTot,xlim = c(0,hs), breaks = br * max(MN$AssessTot) / hs / 150, col='grey', main=" ", xlab = 'Asset Total Value')

#log transformation
MN$AssessTot = log(MN$AssessTot)
hist(MN$AssessTot,  xlab ="log Assess Total", main = " ", col="green")
curve(dnorm(x, mean=mean(MN$AssessTot), sd=sd(MN$AssessTot)), add=TRUE, col= 'darkblue', lwd=2)

MN_total = MN[,c("AssessTot","NumBldgs","UnitsTotal","LotArea","BldgArea","LotFront","BldgFront",
                "YearBuilt","ResidFAR","CommFAR","FacilFAR","Population","PopDensity","MedIncome","AvgIncome",
                "PerCapitaIncome","HighIncomeHouse","NumofHouses","NumofCondos",
                "EduRate","UnemployedRate","MarriedRate","DivorcedRate")]
M_total = cor(MN_total)
corrplot(M_total, method = "square")

MN_original = MN[,c("AssessTot","NumBldgs","UnitsTotal","LotArea","BldgArea","LotFront","BldgFront",
                    "YearBuilt","ResidFAR","CommFAR","FacilFAR")]
M = cor(MN_original)
corrplot(M, method = "square")

MN_addition = MN[,c("AssessTot","Population","PopDensity","MedIncome","AvgIncome",
                    "PerCapitaIncome","HighIncomeHouse","NumofHouses","NumofCondos",
                    "EduRate","UnemployedRate","MarriedRate","DivorcedRate")]
MN_addition_cor = cor(MN_addition)
corrplot(MN_addition_cor, method = "square")

Box1 = ggplot(MN, aes(x = factor(LandUseStr), y = AssessTot)) + geom_boxplot() + theme(text = element_text(size = 8)) + labs(x="Type of Land Use", y="Total Assessed Value")
Box1

Box2 = ggplot(MN, aes(x = factor(Zone), y = AssessTot)) + geom_boxplot() + theme(text = element_text(size = 8)) + labs(x="Zone in Manhattan", y="Total Assessed Value")
Box2

Box3 = ggplot(MN, aes(x = factor(OwnerType), y = AssessTot)) + geom_boxplot() + theme(text = element_text(size = 8)) + labs(x="Owner Type", y="Total Assessed Value")
Box3

log_build_area = log(MN$BldgArea)
Box4 = ggplot(MN, aes(x = factor(Zone), y = log_build_area)) + geom_boxplot() + theme(text = element_text(size = 8)) + labs(x="Zone in Manhattan", y="Building Area")
Box4
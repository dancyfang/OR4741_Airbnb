library(corrplot)
library(ggplot2)

MN = read.csv("MN with additional features.csv")
MN = data.frame(MN)
MN$AssessTot = log(MN$AssessTot) 
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
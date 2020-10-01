x <- 3

4 -> y
x <- 5
numlist <- c(0,1,2,3,4,5,6,7,8,9,10)
numlist <- c(0,1,2,3,4,5,6,7,8,9)
demo_table <- read.csv(file='demo.csv',check.names=F,stringsAsFactors = F)
demo_table2 <- fromJSON(txt='demo.json')
demo_table3 <- read.csv('demo2.csv', check.names = F, stringsAsFactors = F)
demo_table7 <- read.xlsx('Vehicle_Data.xlsx', check.names = F, stringsAsFactors = F)
demo_table7 <- read.csv('Vehicle_Data.xlsx', check.names = F, stringsAsFactors = F)
long_table <- gather(demo_table3,key="Metric",value="Score",buying_price:popularity)
long_table <- demo_table3 %>% gather(key="Metric",value="Score",buying_price:popularity)

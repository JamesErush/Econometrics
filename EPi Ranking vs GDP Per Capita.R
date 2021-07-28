epi<-epi2020results20200604_Copy$EPI.new
GDP<-epi2020results20200604_Copy$`GDP Per Capita`
plot(GDP,epi)
model <- lm(epi~log(GDP))
summary(model)

plot(GDP,epi)
x=seq(from=1,to=180,length.out = 1000)
y=predict(model,newdata=list(x=seq(from=1,to=180,length.out = 1000)),interval = "confidence")
matlines(x,y, lwd=2)

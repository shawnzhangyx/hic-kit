tart = commandArgs(trailing=T)[1]
end = commandArgs(trailing=T)[2]
name = commandArgs(trailing=T)[3]

names1 = list.files(pattern="pos1.txt")
la = list()
for(i in 1:12){
  name =names1[i]
  a = readLines(name)
  la[[i]] = as.numeric(a)

#  plot(density(a))
}

names2 = list.files(pattern="pos2.txt")
lb = list()
for(i in 1:12){
  name = names2[i]
  a = readLines(name)
  lb[[i]] = as.numeric(a)
}

#pdf("interaction_freq_myh6.pdf")
png(paste("interaction_freq_",name,".png",sep=''),height=960,width=960)
par(mfrow=c(6,2))

xrange=c(start,end)

for (i in c(1,2,5:10,3,4,11,12)){

t1 = table(floor(la[[i]]/5e3)*5)
p1 = as.numeric(names(t1))
t2 = table(floor(lb[[i]]/5e3)*5)
#t2 = t2[which(t2>20)]
p2 = as.numeric(names(t2))
#xrange = range(c(p1,p2))

plot(p2,t2,xlim=xrange,type='h',main=names1[i])
points(p1,t1,type='h',col='red')
}

dev.off()


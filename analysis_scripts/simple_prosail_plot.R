import os
import sys

filename_in = sys.argv[1]
if os.path.exists(filename_in):
    print os.path.basename(filename_in)

prosail <- read.table(filename_in, header=F)

# create plot
png("PROSAIL_D_Output.png",width=4000, height=3200, res=240)
par(mfrow=c(1,1), mar=c(4.6,5.2,1.0,0.7), oma=c(0.1,0.1,0.1,0.1))
plot(prosail[,1], prosail[,2], type="l", lwd=3)
dev.off()

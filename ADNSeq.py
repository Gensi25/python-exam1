class ADNseq:
    def __init__(self, adnSeq):
        self.adnSeq = adnSeq


    def percentatgeGC(self):
        counter = 0
        for base in self.adnSeq:
            if x == "G" or x == "C":
                counter +=1

        percentatge = round(counter / len(adn),4)
        return percentatge

    def transcripcioARN(self):
        seqARN = "" 
        seqARN = self.adnSeq.replace("T", "U")
        return seqARN
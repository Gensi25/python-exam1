class ADNSeq:
    def __init__(self, adnSeq):
        self.adnSeq = adnSeq


    def percentatgeGC(self):
        counter = 0
        for base in self.adnSeq:
            if x == "G" or x == "C":
                counter +=1

        percentatge = round(counter / len(self.adnSeq), 4)
        return percentatge

    def transcripcioARN(self):
        seqARN = "" 
        seqARN = self.adnSeq.replace("T", "U")
        return seqARN
    
    def test(self)
        seq1 = "ACGGTCATGCAA"
        seq2 = "CCGGCGCGCG"

        assert self.percentatgeGC(seq2) == 100.0
        assert self.transcripcioARN(seq1) == "ACGGUCAUGCAA"



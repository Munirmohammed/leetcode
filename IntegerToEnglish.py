class Solution:
    def numberToWords(self, num: int) -> str:
        powers=['Thousand','Million','Billion']
        digitword=[]
        for i in range(3,0,-1):
            sendee=num// 10**(3*i)
            digit=self.threedigit(sendee)
            if digit!="Zero":
                digitword.append(digit)
                digitword.append(powers[i-1])
            num=num% 10**(3*i)
        digit=self.threedigit(num)
        if digit=="Zero":
            if len(digitword)==0:
                digitword.append(digit)
        else:
            digitword.append(digit)
            
        print(digitword)
        return " ".join(digitword)
    
    def threedigit(self,num):
        tens=['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        ones=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        teens=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        digitword=[]
        if num==0:
            return "Zero"
        if num//100!=0:
            digitword.append(ones[num//100-1])
            digitword.append("Hundred")
        if num%100<20 and num%100>=10:
            digitword.append(teens[num%10])
            return " ".join(digitword)
        if (num%100)//10!=0:
            digitword.append(tens[(num%100)//10-2])
        if num%10!=0 :
             digitword.append(ones[num%10-1])
        return " ".join(digitword)

import math
import random
import numpy as np
import copy


first_tailx = 12.1
first_initialx = -3.0

precision = 4

len = first_tailx - first_initialx

bigger_len = 10 ** precision

end_len = len * bigger_len

ans1 = math.ceil(math.log2(end_len))

print(ans1)

second_tailx = 5.8
second_initialx = 4.1

sec_len = second_tailx - second_initialx

second_bigger_len = 10 ** precision

sec_end_len = sec_len * second_bigger_len

ans2 = math.ceil(math.log2(sec_end_len))

print(ans2)

add_bits = ans1 + ans2

print(add_bits)

chrom1 = []
chrom1_stringtype = []

TotalFitnessFunction = 0

for i in range(20):
    chrom1string = ""

    chrom1.append([])

    for j in range(ans1 + ans2):
        rand1 = random.randint(0,1)
        chrom1[i].append(rand1)

    for j in range(ans1):
        chrom1string += str(chrom1[i][j])

    ToDecimal_A = int(chrom1string,2)
    cal_A =  ToDecimal_A *(first_tailx-first_initialx)/(2 ** ans1 -1) + first_initialx

    chrom1[i].append(cal_A)
    
    chrom1string = ""

    for j in range(ans2):
        chrom1string += str(chrom1[i][18+j])

    ToDecimal_B = int(chrom1string,2)
    cal_B =  ToDecimal_B *(second_tailx-second_initialx)/(2 ** ans2 -1) + second_initialx

    chrom1[i].append(cal_B)

    for j in range(20):
        fu1 = 21.5 + cal_A * math.sin(4*math.pi*cal_A) + cal_B*math.sin(20*math.pi*cal_B)
    chrom1[i].append(fu1)
    
    TotalFitnessFunction += chrom1[i][35]
    
for z in range(1000):
#             sutato
    chrom2=copy.deepcopy(chrom1)
    chopool=[[0]*36 for i in range(40)] 
    #產生初始族群在輪盤上被選擇的機率與累積機率

    ProbChart = []
    TotalProb = 0
    Prob = 0


    for i in range(20):
        Prob = chrom2[i][35] / TotalFitnessFunction
        Prob = float(format(Prob, '.6f'))
        TotalProb += Prob
        TotalProb = float(format(TotalProb,'.6f'))
        ProbChart.append([])
        ProbChart[i].append(Prob)
        ProbChart[i].append(TotalProb)


    #比較累積機率的數值
    #輪盤法

    circle = []

    for i in range(20):

        circle.append([])
        count = 0
        #random  number between 0 and 1, and the    precision number is 6
        RandomToComp = float(format(random.uniform(0,1), '.6f'))
        
        
        for j in range(20):
            if(ProbChart[j][1] < RandomToComp ):
                count+=1
            elif(ProbChart[j][1] > RandomToComp):
                circle[i].append(i)
                circle[i].append(count+1)
                break
    # print(circle)

    #輪盤法above
    ############################################################

    #交叉crossover

    crossover_array = []

    for i in range(20):
        RandomToComp = float(format(random.uniform(0,1), '.6f'))
        if(RandomToComp < 0.25):
            crossover_array.append(1)
        else:
            crossover_array.append(0)

    # print(crossover_array)
    # print('---')

    crossover_array1 = []
    for i in range(20):
        if(crossover_array[i]==1):
            crossover_array1.append(i)
            
    #print(crossover_array1)

    counter1 = 0

    for nunbers in crossover_array1:
        counter1 += 1

    if(counter1 % 2 == 1):
        counter1  -= 1

    counter1 = int(counter1 / 2 )

    cross_number = random.randint(0,32)

    cross_number1 = random.randint(0,32)

    counter2=0

    for i in range(counter1):
        for j in range(32-cross_number):
            TmpNumber = chrom1[crossover_array1[counter2]][32-j]
            chrom2[crossover_array1[counter2]][32-j] = chrom2[crossover_array1[counter2+1]][32-j]
            chrom2[crossover_array1[counter2+1]][32-j] = TmpNumber
        counter2 += 2

    for i in range(20):
        for j in range(32):
            mixNumber = float(format(random.uniform(0,1), '.6f'))
            if(mixNumber < 0.1):
                if(chrom2[i][j] == 0):
                    chrom2[i][j] = 1
                else:
                    chrom2[i][j] = 0

    for i in range(20):
        chrom1string = ""
        
        for j in range(ans1):
            chrom1string += str(chrom2[i][j])
        
        ToDecimal_A = int(chrom1string,2)
        cal_A =  ToDecimal_A *(first_tailx-first_initialx)/(2 ** ans1 -1) + first_initialx

        chrom2[i][33] = cal_A
        
        chrom1string = ""

        for j in range(ans2):
            chrom1string += str(chrom2[i][18+j])

        ToDecimal_B = int(chrom1string,2)
        cal_B =  ToDecimal_B *(second_tailx-second_initialx)/(2 ** ans2 -1) + second_initialx

        chrom2[i][34] = cal_B

        for j in range(20):
            fu1 = 21.5 + cal_A * math.sin(4*math.pi*cal_A) + cal_B*math.sin(20*math.pi*cal_B)
        chrom2[i][35] = fu1
    # for i in range(20):
    #     chopool[i]=chrom1[i]
    #     chopool[i+20]=chrom2[i]


    for i in range(20):
        chopool[i]=copy.deepcopy(chrom1[i])
        chopool[i+20]=copy.deepcopy(chrom2[i])
        chrom1[i][35]=0


    for i in range (20):
        for j in range(40):
            if(chrom1[i][35]<chopool[j][35]):
                for k in range(36):
                    chrom1[i][k],chopool[j][k]=chopool[j][k],chrom1[i][k]
    
    print (chrom1[0][35])

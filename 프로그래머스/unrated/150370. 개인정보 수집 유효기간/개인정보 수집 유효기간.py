def solution(today, terms, privacies):
    
    year, month, day= map(int, today.split('.'))
    todayValue= year*28*12 + month*28 + day

    answer = []
    
    for idx, privacy in enumerate(privacies):
        expiredValue= getExpiredValue(privacy, terms)
        if expiredValue <= todayValue:
            answer.append(idx+1)
    
    return answer

def getExpiredValue(privacy, terms):
    
    date, term= privacy.split()
    year, month, day= map(int, date.split('.'))
    
    for data in terms:
        termName, termPeriod= data.split()
        if termName == term: break            
    
    convertedValue= year*28*12 + month*28 + day + int(termPeriod)*28
    
    return convertedValue

    
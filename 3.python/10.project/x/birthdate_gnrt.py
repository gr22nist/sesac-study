import random
import datetime

class BirthdateGenerator:
  month = [1,2,3,4,5,6,7,8,9,10,11,12]
  
  def gnrt_birthdate(self):
    year = random.randint(1958,2005)
    month = random.randint(month)
    # if month == 2:
    #   day = (1,28)
    # elif month == 4 or month == 6 or month == 9 or month ==11:        
    #   day = random.randint(1,30)
    # else:
    #    day = random.randint(1,31)
    day = (1,28) if month == 2 else (1,30) \
          if month == 4 or month == 6 or month == 9 or month == 11 else (1,31)
    
    date = datetime.date.today()
    age = f"{date.year} - {year}"
    
    return f"{year}-{month:02d}-{day:02d}", age